import os
import time
from pathlib import Path

from flask import Flask, render_template, request, session

from src.boundary.ui import blank_positions, evaluate_submission
from src.entity.magic_square import generate_puzzle

ROOT = Path(__file__).resolve().parents[2]


def _grid_from_form(form, puzzle: list[list[int]], blanks: frozenset[tuple[int, int]]) -> list[list[int]]:
    grid: list[list[int]] = []
    for r in range(4):
        row: list[int] = []
        for c in range(4):
            if (r, c) in blanks:
                raw = form.get(f"cell_{r}_{c}", "").strip()
                row.append(int(raw) if raw else 0)
            else:
                row.append(puzzle[r][c])
        grid.append(row)
    return grid


def _safe_grid_from_form(form, puzzle: list[list[int]], blanks: frozenset[tuple[int, int]]) -> list[list[int]]:
    grid: list[list[int]] = []
    for r in range(4):
        row: list[int] = []
        for c in range(4):
            if (r, c) not in blanks:
                row.append(puzzle[r][c])
                continue
            raw = form.get(f"cell_{r}_{c}", "").strip()
            try:
                row.append(int(raw) if raw else 0)
            except ValueError:
                row.append(0)
        grid.append(row)
    return grid


def _render(**kwargs):
    defaults = {
        "phase": "idle",
        "puzzle": None,
        "grid": None,
        "blanks": (),
        "start_time_ms": None,
        "elapsed_ms": None,
        "success": False,
        "error": None,
        "stopped": False,
    }
    defaults.update(kwargs)
    return render_template("index.html", **defaults)


def create_app() -> Flask:
    app = Flask(__name__, template_folder=str(ROOT / "templates"))
    app.secret_key = os.environ.get("FLASK_SECRET_KEY", "magic-square-dev")

    @app.get("/")
    def index():
        phase = session.get("phase", "idle")
        if phase == "playing":
            puzzle = session.get("puzzle")
            if not puzzle:
                session.clear()
                return _render(phase="idle")
            blanks = blank_positions(puzzle)
            return _render(
                phase="playing",
                puzzle=puzzle,
                grid=puzzle,
                blanks=tuple(blanks),
                start_time_ms=int(session["start_time"] * 1000),
            )
        if phase == "solved":
            return _render(
                phase="solved",
                elapsed_ms=session.get("elapsed_ms"),
                success=True,
            )
        return _render(phase="idle")

    @app.post("/start")
    def start():
        puzzle = session.pop("next_puzzle", None) or generate_puzzle()
        session["puzzle"] = puzzle
        session["phase"] = "playing"
        session["start_time"] = time.time()
        session.pop("elapsed_ms", None)
        blanks = blank_positions(puzzle)
        return _render(
            phase="playing",
            puzzle=puzzle,
            grid=puzzle,
            blanks=tuple(blanks),
            start_time_ms=int(session["start_time"] * 1000),
        )

    @app.post("/solve")
    def solve():
        if session.get("phase") != "playing":
            return _render(phase="idle")

        puzzle = session.get("puzzle")
        if not puzzle:
            session.clear()
            return _render(phase="idle")

        blanks = blank_positions(puzzle)
        try:
            grid = _grid_from_form(request.form, puzzle, blanks)
            result = evaluate_submission(puzzle, grid)
        except (ValueError, TypeError, IndexError):
            grid = _safe_grid_from_form(request.form, puzzle, blanks)
            return _render(
                phase="playing",
                puzzle=puzzle,
                grid=grid,
                blanks=tuple(blanks),
                start_time_ms=int(session["start_time"] * 1000),
                error="틀렸습니다",
            )

        if result == "correct":
            elapsed_ms = int((time.time() - session["start_time"]) * 1000)
            session["next_puzzle"] = generate_puzzle()
            session["phase"] = "solved"
            session["elapsed_ms"] = elapsed_ms
            session.pop("puzzle", None)
            session.pop("start_time", None)
            return _render(phase="solved", elapsed_ms=elapsed_ms, success=True)

        return _render(
            phase="playing",
            puzzle=puzzle,
            grid=grid,
            blanks=tuple(blanks),
            start_time_ms=int(session["start_time"] * 1000),
            error="틀렸습니다",
        )

    @app.post("/stop")
    def stop_game():
        session.pop("puzzle", None)
        session.pop("start_time", None)
        session.pop("elapsed_ms", None)
        session.pop("next_puzzle", None)
        session["phase"] = "idle"
        return _render(phase="idle", stopped=True)

    return app

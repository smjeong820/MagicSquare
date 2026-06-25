"""MagicSquare 웹 앱 진입점.

실행:
    python run.py
    # 또는
    flask --app src.boundary.web:create_app run --debug
"""

from src.boundary.web import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

# /commit-push — Git commit + GitHub push

**이 커맨드가 실행된 경우에만** commit·push를 수행한다. 평소 작업 중 임의 commit·push 금지.
추가 확인 질문 없이 아래 절차를 끝까지 실행한다.

## 선택 입력 (없으면 변경 내용에서 자동 추론)

```
Phase: [red | green | refactor | docs | chore]
Layer: [entity | boundary | —]
Test ID: [D-MSQ-01 등]
계약 ID: [INV-1 등 — GREEN/REFACTOR 시]
```

## 사전점검 (하나라도 실패하면 commit·push 중단)

1. `pytest -q` 전체 통과 — FAIL이면 중단 (코드 변경 커밋 시 필수; `Report/`·`Prompting/`·`.cursor/`만 변경이면 생략 가능)
2. 아래를 **병렬** 실행:
   - `git status`
   - `git diff` (staged + unstaged)
   - `git log -5 --oneline` (메시지 스타일 참고)
3. 커밋할 변경 없음 → 중단 보고
4. `.env`, `credentials.json`, `*.pem`, `*.key` 등 시크릿 파일 staging **금지** — 발견 시 경고 후 제외

## 커밋 메시지 형식 (ARRR · Tidy First)

| Phase | 형식 | 예시 |
|-------|------|------|
| RED | `test(계층): {Test ID} RED [RED]` | `test(entity): D-MSQ-01 RED [RED]` |
| GREEN | `feat(계층): {Test ID} GREEN [{계약 ID}]` | `feat(entity): D-MSQ-01 GREEN [INV-1]` |
| REFACTOR | `refactor(계층): {요약} — {계약 ID} [REFACTOR]` | `refactor(entity): THRESHOLD 상수 SSOT 추출 — INV-2 [REFACTOR]` |
| docs | `docs: {요약}` | `docs: Report/04 세션 보고서 추가` |
| chore | `chore: {요약}` | `chore: commit-push 커맨드 추가` |

- **한 커밋 = 한 사이클**: 구조 변경(refactor)과 동작 변경(feat/test)을 섞지 않는다.
- 변경이 여러 사이클에 걸쳐 있으면 **가장 작은 단위로 분리 커밋** 후 순서대로 push (RED → feat → refactor).
- 메시지에 Test ID·계약 ID를 반드시 포함한다 (해당 시).

## 절차

1. 사전점검 통과 확인
2. 변경 파일 분석 → Phase·Layer·Test ID·계약 ID 추론 → 커밋 메시지 초안
3. `git add` — 관련 파일만 staging (시크릿 제외)
4. `git commit` — 메시지는 HEREDOC 또는 `-m`으로 전달
5. `git push` — 현재 브랜치를 remote에 push (`-u origin HEAD` — upstream 없을 때만)
6. `git status`로 push 완료 확인

## Git Safety (절대 준수)

- `git config` 변경 금지
- `--no-verify`, `--no-gpg-sign` 등 hook 우회 금지
- `git push --force` / `git reset --hard` 금지 (사용자 명시 요청 없이)
- `main`/`master`에 force push 시도 금지 — 경고 후 중단
- `git commit --amend` 금지, 단 **모두** 충족 시만:
  1. 사용자가 amend 명시 요청, **또는** pre-commit hook이 파일을 수정해 재커밋 필요
  2. HEAD 커밋이 이번 세션에서 생성된 것
  3. 아직 remote에 push되지 않음
- pre-commit hook **실패** 시 amend 금지 → 문제 수정 후 **새 커밋**
- 빈 커밋 금지

## 완료 보고 형식

| 항목 | 내용 |
|------|------|
| pytest | N passed (또는 docs/chore — 생략) |
| 커밋 | `{short-hash}` — `{메시지}` |
| push | `{branch}` → `{remote}/{branch}` |
| 변경 파일 | `path1`, `path2`, … |

## 금지

- 변경 없이 빈 커밋
- 테스트 FAIL 상태에서 코드 커밋
- 시크릿 파일 커밋
- 사용자 요청 없이 force push

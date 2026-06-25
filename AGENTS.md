# Repository instructions
 
[프로젝트명] — Python 3.12, pytest 기반 Dual-Track TDD (C2C 추적) 프로젝트.
이 파일은 백과사전이 아니라 "지도"다. 자세한 내용은 docs/PRD.md 참고.
 
## 구조 (ECB)
- src/entity/[domain].py : Entity (순수 로직·불변식). Boundary import 금지.
- src/boundary/[ui].py   : Boundary (UI/입력). Entity를 import해 재사용.
- tests/entity/          : Track B — 불변식(INV-*) 검증
- tests/boundary/        : Track A — 입력/UI 계약(E-*, UC-*) 검증
- tests/conftest.py      : SSOT 픽스처 (공유 격자·상수)
- tests/_approval.py     : Golden Master harness
- tests/golden/          : *.approved.txt 기준 파일
 
## 테스트 ID 명명 규칙
- Track B (entity):   D-[기능코드]-NN  예) D-LOC-01
- Track A (boundary): U-[기능코드]-NN  예) U-IN-01
- 통합/골든:           T1, T2, T3...
 
## MomTest
- 계약은 MomTest로 발견한 과거 사실에서만 추출한다.
- AC → Invariant / Error Contract / Out-of-Scope 순으로 분류.
- ID 없는 동작은 구현하지 않는다.
 
## 테스트 명령
- 전체         : pytest -q
- Entity만     : pytest tests/entity -q
- Boundary만   : pytest tests/boundary -q
- 단일 테스트  : pytest tests/entity/test_X.py::test_func -v
- 커버리지(HTML): pytest tests/ --cov=src --cov-report=html:htmlcov -v
- Golden 기준 생성: UPDATE_GOLDEN=1 pytest tests/entity/test_X.py -v
 
## 워크플로 — ARRR
- RED   : tests/ 만 수정. src/ 금지. Then은 pytest.fail("RED: ID — …") 한 줄.
- GREEN : 실패 로그를 Context로 줘 최소 구현. 구현 줄에 계약 ID 주석.
- REFACTOR: 전부 GREEN 후에만. 전후로 pytest -q 확인.
 
## Tidy First / 커밋
- 구조 변경과 동작 변경을 한 커밋에 섞지 않는다.
- test(RED) / feat(GREEN) / refactor(REFACTOR) — 메시지에 Test ID 포함.
 
## 금지 (Don't)
- assert True · pytest.skip · xfail · 예외 삼키기 우회 금지.
- 기존 테스트 수정·삭제·비활성화 금지.
- 요청하지 않은 기능 미리 구현 금지 (과잉 구현).
- 함수 시그니처 임의 변경 금지.
- entity에서 boundary/control import 금지.

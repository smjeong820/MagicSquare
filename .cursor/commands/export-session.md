# /export-session — ARRR 1사이클 완료 보고 + Export
**추가 입력 없이 즉시 실행.** 추가 질문·확인 요청 금지.
`/export`의 상위 버전 — repeat Phase 전용 구조화 보고 포함.
## 자동 추출
- 세션 주제: 이번 대화의 핵심 작업
- 산출물: 생성·수정된 파일 목록
- Transcript: User/Cursor 턴 전체
## 번호 규칙
Report/·Prompting/ 의 기존 NN.* 파일 확인 → 가장 큰 번호 + 1 (2자리).
## 생성 파일 (반드시 2개)
- Report/NN.REPORT.md
- Prompting/NN.Export-Transcript.md
## 보고서 필수 섹션 (repeat Phase)
### ARRR 1사이클 완료 보고
| 단계 | Test ID | 요약 |
|------|---------|------|
| RED | | FAIL 원인 한 줄 |
| GREEN | | PASS, 변경 src/ 파일 |
| REFACTOR | | 스멜 1개 + 변경 내용 (없으면 "없음") |
### pytest 결과
python -m pytest tests/ -v 기준 전체 결과 요약
### Golden Master (해당 시)
| 파일 | matched 여부 | diff |
### 다음 Ask(RED) 후보
PRD C2C 기준으로 Test ID 1~3개 제안
### 미완료 우선순위 표 (D-* / U-* 남아있는 경우)
| Test ID | 계약 | 우선순위 | 이유 |
## 금지
- 사용자에게 추가 질문
- 기존 번호 파일 덮어쓰기
- 보고서만 만들고 Transcript 생략 (또는 그 반대)
- 다음 RED 후보를 PRD 근거 없이 임의 제안

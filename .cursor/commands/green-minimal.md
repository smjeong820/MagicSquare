# /green-minimal — GREEN 최소 구현
 
**금지:** 시그니처 변경. 요청 외 기능 추가. 테스트 수정/우회.
 
## 사전점검 (실행 전 자동 확인)
1. RED 상태 (pytest FAIL) 확인
2. 테스트 픽스처·SSOT 존재 확인
3. src/ 에 구현 없음 확인
 
## 구현 규칙
- 실패 로그를 Context로 읽고 통과시키는 최소 코드만.
- 구현 줄 끝에 충족 계약 ID 주석: # INV-1
- Then 블록의 pytest.fail 제거 → 실제 assert로 교체.
 
## 완료 후
pytest [테스트파일] -v
보고: Test ID · PASS · 변경 파일(src/ + tests/ 분리)

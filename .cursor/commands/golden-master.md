# /golden-master — Golden Master(Approval Test) 구축
 
대상이 pytest PASS 상태인지 먼저 확인. PASS가 아니면 중단하고 보고.
 
## 절차
1. tests/_approval.py 없으면 생성
   - assert_matches_golden(actual, relative_path) 함수 포함
2. 테스트에 golden 경로 연결
   - tests/golden/[test_id]_[픽스처].approved.txt
3. 기준 파일 생성:
   UPDATE_GOLDEN=1 pytest [테스트파일]::[함수명] -v
4. 검증 (UPDATE_GOLDEN 없음) → matched 확인
 
**금지:** golden 파일 수동 편집으로 통과 우회.
 
보고: golden 파일 경로 · matched 여부 · diff 있으면 내용 요약

# /red-test-plan — RED 설계표 작성 (파일 생성 금지)
 
**금지:** tests/·src/ 파일 생성·수정. GREEN/REFACTOR 진입. skip/xfail.
 
다음 4블록을 표로 작성해.
 
## 1. C2C 추적
| 판단 문구 | Test ID | Given | When | Then |
 
## 2. Track 설계표
| Test ID | 대상 함수 | Given → Then | Expected RED Failure |
 
## 3. 테스트 플랜
| 파일 경로 | 함수명 | 픽스처 | pytest 명령 |
 
## 4. ECB·Mock 점검
| 계층 | Mock 허용? | 금지 사항 |
 
완료 후: /red-skeleton 으로 넘길 준비됐다고 한 줄로 알려줘.

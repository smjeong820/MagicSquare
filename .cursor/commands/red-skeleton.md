# /red-skeleton — RED 스켈레톤 작성
 
**금지:** src/ 수정. assert 본문. skip/xfail. 통과 더미.
 
앞에서 확정한 설계표 기준으로 tests/ 에만 스켈레톤 작성.
 
## 템플릿
def test_[test_id]_[설명](픽스처):
    # Given: [상태]
    # When:  [함수 호출]
    # Then:  [기대 결과]
    pytest.fail("RED: [Test ID] — 구현 없음, 의도적 실패")
 
## 완료 후 실행하고 보고
pytest [테스트파일]::[함수명] -v
보고: Test ID · FAIL 한 줄 · 변경 파일(tests/만)

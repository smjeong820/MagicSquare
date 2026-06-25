first commit

## 실행

### 테스트

```bash
pytest -q
```

### 웹 앱

```bash
pip install -r requirements.txt
python run.py
```

브라우저에서 http://127.0.0.1:5000 열기.

- **Start** → 문제 표시 + 타이머 시작
- 붉은 칸(빈 칸)만 입력 후 **확인**
- 정답 → `정답입니다` + 우측에 소요 시간 표시 + 다음 문제 자동 생성
- **Start** 로 다음 라운드 시작
- 오답 → `틀렸습니다` (타이머 계속)

# BOM 소요량 계산기 — EXE 빌더

ERP BOM 역전개 텍스트 파일을 품목계정별로 집계하여 엑셀로 출력하는 데스크탑 앱입니다.

---

## 📦 EXE 다운로드 (가장 쉬운 방법)

1. 이 저장소의 **Actions** 탭 클릭
2. 가장 최근 **Build EXE** 워크플로우 클릭
3. 하단 **Artifacts** 섹션에서 `BOM_소요량계산기_Windows` 다운로드
4. 압축 해제 후 `BOM_소요량계산기.exe` 더블클릭

> 태그(예: `v1.0.0`)를 푸시하면 **Releases** 탭에도 자동으로 올라옵니다.

---

## 🚀 GitHub에 올려서 자동 빌드하는 방법

### 1단계 — 저장소 생성

```bash
# GitHub에서 새 저장소(public 또는 private) 생성 후:
git init
git remote add origin https://github.com/YOUR_NAME/bom-calculator.git
```

### 2단계 — 파일 올리기

```bash
git add .
git commit -m "init: BOM 소요량 계산기"
git push -u origin main
```

### 3단계 — Actions 확인

- GitHub 저장소 → **Actions** 탭
- `Build EXE` 워크플로우가 자동 실행됨 (약 3~5분)
- 완료 후 **Artifacts**에서 EXE 다운로드

### 4단계 — Release로 배포 (선택)

```bash
git tag v1.0.0
git push origin v1.0.0
```

→ **Releases** 탭에 EXE 파일이 자동 첨부됩니다.

---

## 📁 파일 구조

```
bom-calculator/
├── .github/
│   └── workflows/
│       └── build.yml          # GitHub Actions 빌드 설정
├── app/
│   ├── main.py                # PyWebView 래퍼 (앱 진입점)
│   └── BOM_소요량계산기.html   # 실제 앱 (HTML/JS)
├── BOM_소요량계산기.spec       # PyInstaller 빌드 설정
├── requirements.txt
└── README.md
```

---

## 🖥️ 로컬에서 직접 빌드하는 방법

Python 3.8 이상 필요.

```bash
pip install -r requirements.txt
pyinstaller BOM_소요량계산기.spec
# → dist/BOM_소요량계산기.exe 생성
```

---

## 📋 앱 사용법

1. `BOM_소요량계산기.exe` 실행
2. ERP에서 내보낸 BOM 역전개 `.txt` / `.tsv` 파일 드래그 또는 클릭 선택
3. 집계 방식 / 단계·계정 필터 설정
4. **소요량 계산 실행** 클릭
5. 결과 확인 후 **엑셀 다운로드** 클릭

### 지원 파일 형식
- 탭 구분자 텍스트 파일 (`.txt`, `.tsv`)
- 인코딩: UTF-8, EUC-KR 자동 감지
- `단계` 컬럼이 있는 ERP BOM 역전개 형식

### 엑셀 출력 시트
| 시트 | 내용 |
|------|------|
| 품목별소요량 | 계정별 그룹 / 자품목기준수 ÷ 모품목기준수 = 소요량 / 소계·합계 |
| 계정별요약   | 부자재·반제품·제품별 품목 수 및 총 소요량 |
| 원본데이터   | 필터 적용된 전체 행 |

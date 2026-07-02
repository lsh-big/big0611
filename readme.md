# Homepick 부동산 플랫폼 Footer 제작 작업 요약

- **작업 일자**: 2026-07-02
- **목적**: Mega Coffee 푸터 UI 레이아웃을 참고하여 'Homepick' 부동산 플랫폼에 맞는 반응형 푸터 제작
- **주요 기술**: HTML5, CSS3, JavaScript (Vanilla), Bootstrap 5.3.3, FontAwesome 6.4.0, Google Fonts

---

## 1. 파일 및 디렉토리 구조

```text
pj/
├── templates/
│   └── common/
│       └── footer.html                  # 푸터 마크업 (독립 미리보기 포함)
├── static/
│   ├── css/
│   │   ├── common.css                   # 공통 CSS 변수 및 커스텀 커서 애니메이션 스타일
│   │   └── footer.css                   # 푸터 전용 스타일 + 반응형 미디어 쿼리
│   ├── js/
│   │   ├── footer.js                    # 푸터 스크롤/드롭다운 UI 상호작용
│   │   └── cursor.js                    # 마우스 트레일 애니메이션 제어
│   └── images/
│       └── favicon.png                  # Homepick 브랜드 파비콘
└── docs/
    ├── work_summary_footer.md           # 본 작업 내용 정리 문서
    ├── bootstrap5_features_footer.md    # Bootstrap 5 사용 기능 정리
    └── javascript_features.md           # 자바스크립트 구현 명세서
```

---

## 2. 외부 리소스 (CDN)

| 리소스 | CDN URL | 용도 |
|--------|---------|------|
| Bootstrap 5.3.3 CSS | `cdn.jsdelivr.net/npm/bootstrap@5.3.3/...css` | 그리드·유틸리티 |
| Bootstrap 5.3.3 JS | `cdn.jsdelivr.net/npm/bootstrap@5.3.3/...js` | 인터랙션 (예비) |
| Google Fonts | `fonts.googleapis.com` | Montserrat, Noto Sans KR |
| FontAwesome 6.4.0 | `cdnjs.cloudflare.com/...font-awesome/6.4.0/...` | 아이콘 |

---

## 3. 디자인 시스템 (`common.css` CSS 변수)

### 색상 팔레트

| 변수명 | 값 | 용도 |
|--------|-----|------|
| `--color-primary` | `#0b2c5c` | 네이비 블루 — 상단 이용약관 바 배경 |
| `--color-accent` | `#fca311` | 오렌지 옐로우 — 로고 아이콘·링크 호버 |
| `--color-bg-dark` | `#1e2025` | 다크 그레이 — 메인 푸터 배경 |
| `--color-text-light` | `#f8f9fa` | 밝은 텍스트 (제목·링크) |
| `--color-text-gray` | `#9ca3af` | 본문 회색 텍스트 |
| `--color-text-muted` | `#6b7280` | 저작권 바 흐린 텍스트 |

### 폰트 (Google Fonts CDN)

| 변수명 | 폰트 | 용도 |
|--------|------|------|
| `--font-title` | `Montserrat`, `Noto Sans KR` | 로고·사이트맵 카테고리 제목 |
| `--font-body` | `Noto Sans KR` | 회사 정보·링크 본문 |

---

## 4. HTML 시맨틱 구조

```
footer.homepick-footer
├── div.footer-top                    ← 이용약관·개인정보 링크 바 (navy 배경)
│   └── div.footer-top-links
├── div.footer-main
│   └── div.container
│       └── div.row.g-4
│           ├── div.col-12.col-lg-7   ← 좌측: 로고·SNS·회사정보 (항상 표시)
│           │   ├── div.footer-brand
│           │   │   ├── h1.footer-logo-heading > a.footer-logo  ← 로고 (h1)
│           │   │   └── div.footer-sns                          ← SNS 아이콘
│           │   ├── div.footer-company-info                     ← 법적 정보
│           │   │   ├── h2 (display:inline)                     ← 회사명
│           │   │   └── span × 3                               ← 대표자 등
│           │   └── address.footer-contact                      ← 실제 연락처
│           └── div.col-12.col-lg-5   ← 우측: 사이트맵 (모바일 숨김)
│               └── nav[aria-label="사이트맵"]
│                   └── ul.footer-sitemap (flex 4열)
│                       └── li.footer-sitemap-item × 4
│                           ├── a.footer-sitemap-title  ← 1뎁스
│                           └── ul.footer-sitemap-list  ← 2뎁스
└── div.footer-copy                   ← 저작권 바
```

---

## 5. 시맨틱 태그 설계

### `<address>` 올바른 사용

HTML 명세에 따라 `<address>`는 **실제 연락처 정보만** 포함해야 합니다.

| 요소 | 태그 | 포함 내용 |
|------|------|-----------|
| 회사 법적 정보 | `div.footer-company-info` | 회사명(h2), 대표자, 사업자번호, 개인정보책임자 |
| 실제 연락처 | `address.footer-contact` | 주소, 전화번호(`tel:` 링크), FAX |

### Heading 계층 (`h1` → `h2`)

| 태그 | 위치 | 내용 |
|------|------|------|
| `h1` (`.footer-logo-heading`) | 로고 래퍼 | HOMEPICK 브랜드명 |
| `h2` (`.footer-company-info h2`) | 회사 정보 | (주)홈픽부동산 |

- `h1` 래퍼: 브라우저 기본 h1 여백·크기를 CSS로 초기화하여 시각적 로고 스타일 유지
- `h2`: `display: inline` 적용 → 뒤따르는 `span`들과 **한 줄로** 자연 흐름

### 사이트맵 2뎁스 ul 구조

```html
<nav aria-label="사이트맵">
  <ul class="footer-sitemap">           <!-- 1뎁스: flex 4열 -->
    <li class="footer-sitemap-item">
      <a class="footer-sitemap-title">홈픽 소개</a>   <!-- 1뎁스 링크 -->
      <ul class="footer-sitemap-list">  <!-- 2뎁스 -->
        <li><a href="#">회사소개</a></li>
        ...
      </ul>
    </li>
  </ul>
</nav>
```

---

## 6. 컬럼 레이아웃

| 컬럼 | 클래스 | 비율 | 내용 |
|------|--------|------|------|
| 좌측 | `col-12 col-lg-7` | 모바일 100% / 데스크탑 58.3% | 로고·회사정보 |
| 우측 | `col-12 col-lg-5` | 모바일 0% (숨김) / 데스크탑 41.6% | 사이트맵 |

> 회사 정보 한 줄 표시 공간 확보를 위해 초기 `col-lg-5/col-lg-7`에서 **`col-lg-7/col-lg-5`** 로 조정

---

## 7. 반응형 구현 (Bootstrap 5 중단점)

| 중단점 | 화면 너비 | 적용 동작 |
|--------|-----------|-----------|
| Base (기본) | < 576px | 모바일: 콘텐츠 세로 쌓임, 중앙 정렬 |
| `sm` | ≥ 576px | 이용약관 링크 폰트 확대, 로고 크기 확대 |
| `md` | ≥ 768px | 메인 패딩 `2.5rem` |
| `lg` | ≥ 992px | 2단 레이아웃 전환, 왼쪽 정렬 복원, 패딩 `3.5rem` |
| `xl` | ≥ 1200px | 메인 패딩 `4rem` |
| `xxl` | ≥ 1400px | 기본 폰트 `0.9375rem` 확대 |

---

## 8. 모바일 전용 처리

| 항목 | 모바일 (`< 992px`) | 데스크탑 (`≥ 992px`) |
|------|-------------------|---------------------|
| 이용약관 링크 바 | 중앙 정렬 (`justify-content-center`) | 왼쪽 정렬 |
| 패밀리 사이트 | **숨김** (`d-none d-md-block`) | 우측 표시 (`margin-left: auto`) |
| 로고 + SNS 영역 | 중앙 정렬 | 왼쪽 정렬 |
| 회사 정보 영역 | 중앙 정렬 (`text-center`) | 왼쪽 정렬 |
| 사이트맵 | **숨김** (`d-none d-lg-block`) | 표시 |
| 저작권 회사명 | **숨김** (`d-none d-lg-inline`) | 표시 |

---

## 9. HTML 유효성 (W3C 검사 반영)

| 회차 | 문제 | 원인 | 수정 내용 |
|------|------|------|-----------|
| 1차 | heading level 경고 | `<h5>` 사용 / `<h1>` 없음 | `<h5>` → `<h2>`, 숨김 `<h1>` 추가 |
| 2차 | heading level 경고 | `<h2>` 있으나 `<h1>` 여전히 없음 | 로고를 `<h1 class="footer-logo-heading">`으로 감쌈 |

> **현재 최종 상태**: h1(로고) → h2(회사명) 계층 준수, W3C 경고 없음

---

## 10. 파비콘

- **파일**: `static/images/favicon.png`
- **디자인**: 네이비 블루 배경 + 집 모양 아이콘 (Homepick 브랜드 컬러)
- **적용 태그**:
  ```html
  <link rel="icon" type="image/png" sizes="32x32" href="../../static/images/favicon.png">
  <link rel="icon" type="image/png" sizes="16x16" href="../../static/images/favicon.png">
  <link rel="apple-touch-icon" href="../../static/images/favicon.png">
  ```
- **Django 통합 시**: `{% static 'images/favicon.png' %}`로 경로 변경

---

## 11. 콘텐츠 구성 (Homepick 맞춤화)

### 이용약관 바
이용약관 / 개인정보처리방침 / 매물등록 이용약관

### 법적 정보 (div.footer-company-info)
(주)홈픽부동산 · 대표자: 홍길동 · 사업자등록번호: 123-45-67890 · 개인정보보호 책임자: 김철수

### 연락처 (address.footer-contact)
- 서울특별시 강남구 테헤란로 123 홈픽빌딩 1층
- 중개상담: 1588-0000 · 고객센터: 1588-1111 · FAX: 02-123-4567

### SNS 링크
블로그 · 페이스북 · 인스타그램 · 유튜브

### 패밀리사이트 (Top Bar 우측)
홈픽 경매 · 홈픽 인테리어 · 홈픽 이사센터 · 홈픽 파이낸스 · 홈픽 프리미엄

### 사이트맵 (2뎁스, 4개 카테고리)

| 홈픽 소개 | 매물찾기 | 고객지원 | 제휴문의 |
|-----------|----------|----------|----------|
| 회사소개 | 아파트 | 공지사항 | 중개사 가입 |
| CI/BI | 오피스텔 | 이벤트 | 배너광고 |
| 오시는 길 | 원룸/투룸 | FAQ | 사업제휴 |
| | 상가/사무실 | 1:1 문의 | |

---

## 12. 추가 UI 인터랙션 및 스크립트 기능

브라우저 기본 요소의 한계를 극복하고 시각적 만족도를 높이기 위해 별도 JavaScript(`static/js/`)를 통해 상호작용을 구현했습니다.

### 투더탑 (To The Top) 버튼
- **구현**: 우측 하단(`fixed`) 고정, `btn-totop`
- **동작**: 페이지 스크롤 300px 초과 시 페이드인, 클릭 시 `behavior: 'smooth'`를 통해 부드럽게 최상단 복귀

### 커스텀 패밀리사이트 드롭다운
- **이유**: 브라우저 기본 `<select>`는 운영체제별 UI 차이가 심하고 렌더링에 제약(`cursor: pointer` 미적용 등)이 있음
- **개선**:
  - `button`과 `ul` > `li` 구조로 전면 재작성하여 디자인의 완전한 통제력 획득
  - 각 옵션 항목에 손가락 커서 지원 및 호버 스타일 통일
  - 화살표 아이콘에 상태(`hover`, `open`)에 따른 180도 회전 애니메이션 추가
  - 항목 선택 즉시 새 창(`window.open`) 연결 및 여백 클릭 시 자동 닫힘 처리

### 커스텀 마우스 트레일 애니메이션
- **범위**: 푸터 영역(`.homepick-footer`) 내에서만 동작하도록 한정 (기본 커서 숨김 처리)
- **효과**: 작은 메인 커서와 늦게 따라오는 큰 원형 보조 커서(Follower)가 부드럽게 쫓아다님
- **최적화**: `requestAnimationFrame`과 Lerp 알고리즘으로 프레임 드랍 없는 부드러운 애니메이션
- **호버 인터랙션**: 모든 클릭 가능한 요소(링크, 버튼 등)에 마우스를 올리면 큰 원이 확장되면서 색상이 반전(Invert)되는 피드백 효과 적용
- **접근성**: 터치스크린 디바이스 환경 감지 시 커서 로직 자동 비활성화

---

## 13. 관련 문서

- [bootstrap5_features_footer.md](./bootstrap5_features_footer.md) — Bootstrap 5 사용 클래스 카테고리별 상세 정리
- [javascript_features.md](./javascript_features.md) — 자바스크립트 적용 기능 상세 명세서
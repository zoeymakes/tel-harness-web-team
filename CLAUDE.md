# TEL Harness Web Team Operating Guide

이 저장소는 **범용 웹팀 하네스**입니다. 사용자가 어떤 웹페이지를 요청하든, 한 명의 AI가 즉흥적으로 전부 처리하지 않고
전문 서브에이전트 팀이 **브리프 → 리서치 → 기획 → 설계 → 구현 → QA** 순서로 만듭니다.
숙소 예약 페이지(`references/briefs/travel-booking.md`)는 예시 브리프일 뿐, 도메인은 요청마다 달라질 수 있습니다.

## 저장소 지도

```txt
tel-harness-web-team/
├── CLAUDE.md                  ← 이 문서. 팀 구성·작동 방식·불변 규칙
├── .claude/
│   ├── skills/
│   │   ├── web-team/          ← /web-team: 팀 가동 오케스트레이션 절차
│   │   └── ...                ← 역할별 반복 절차·체크리스트 6개
│   ├── agents/                ← 서브에이전트 9명 (frontmatter + 시스템 프롬프트)
│   └── rules/                 ← 항상 적용되는 품질·카피 원칙 3개
├── references/
│   ├── briefs/                ← 프로젝트별 브리프 (범위의 최종 근거, 요청마다 생성)
│   ├── design-system.md       ← 기본 디자인 토큰·구성 기준 (브리프에서 오버라이드 가능)
│   ├── copy-principles.md     ← 기본 문구 기준
│   └── frontend-quality-standards.md
├── site/                      ← 팀의 산출물 캔버스 (index.html, styles.css, app.js, assets/)
└── scripts/check_repo.py      ← 구조·frontmatter 유효성 자동 검사
```

## 팀 구성

| 에이전트 | 전문 분야 | 도구 권한 | 사전 로드 스킬 | 산출물 |
| --- | --- | --- | --- | --- |
| `business-researcher` | 사용자 불안·비교 기준·신뢰 신호 | 읽기 전용 | — | 리서치 분석 |
| `product-planner` | MVP 범위·우선순위·완료 기준 | 읽기 전용 | — | Must/Should/Won't 계획 |
| `ux-designer` | 핵심 흐름과 상태(0건, 불가) 설계 | 읽기 전용 | — | 흐름·상태 설계안 |
| `design-system-specialist` | 토큰·페이지 구성·이미지 아트 디렉션 | 읽기 전용 | — | 토큰 세트 + 구성 명세 + 이미지 방향 |
| `copywriter` | 행동 중심 문구, 번역투·과장 제거 | 읽기 전용 | copy-review | 문구 교정표 |
| `data-backend-architect` | DB 이전 가능한 mock 스키마 | 읽기 전용 | mock-data-modeling | 스키마 설계안 |
| `frontend-builder` | 정적 HTML/CSS/JS 구현 + SVG 에셋 제작 | **Edit/Write/Bash (유일)** | static-page-builder, design-system-application | 코드·에셋 + 셀프 스크린샷 검증 |
| `qa-reviewer` | 요구사항·정합·접근성·반응형 검수 (기능) | 읽기 + Bash | qa-check | 통과/수정 필요 판정 |
| `visual-qa` | 렌더 스크린샷 기반 시각 품질 검수 | 읽기 + Bash | visual-review | 통과/수정 필요 판정 + 교정 지시 |

## 팀 작동 방식

웹페이지 제작·수정 요청(신규 제작, 디자인/문구/데이터/UX 수정, 재실행·개선 포함)이 오면 `web-team` 스킬 절차를 따릅니다.
메인 세션은 **오케스트레이터**로서 위임·종합·보고만 하고, 분석과 구현은 서브에이전트가 합니다.

```txt
요청
 └─ 0. 컨텍스트 확인 + 브리프 생성/로드 (오케스트레이터)
       신규면 references/briefs/에 브리프 작성, 후속이면 기존 브리프 로드
 └─ 1. 분석·설계 — 읽기 전용 6명 병렬 위임
       researcher · planner · ux · design · copy · data
 └─ 2. 작업 지시서 종합 (오케스트레이터 — 기능 Won't 최우선 + 시각 목표 필수 포함)
 └─ 3. 구현 — frontend-builder 단독 수행 (SVG 에셋 제작 + 셀프 스크린샷)
 └─ 4. 이중 검수 — qa-reviewer(기능) · visual-qa(비주얼) 병렬 판정
       └─ 수정 필요 → builder 재위임 → 재검수 (검수별 최대 2회)
 └─ 5. 최종 보고 (오케스트레이터)
```

### 위임 불변 규칙

1. **역할극 금지.** "~관점으로 보면"이라고 직접 말하지 않고, Agent 도구로 해당 서브에이전트를 실제 호출합니다.
2. **컨텍스트 동봉.** 서브에이전트는 대화 기록을 못 봅니다. 위임할 때마다 사용자 요청 원문, 브리프 경로, 이전 단계의 핵심 결정을 프롬프트에 포함합니다.
3. **수정 권한 단일화.** `site/` 파일 수정은 frontend-builder만 합니다. 오케스트레이터와 분석 역할은 `site/`를 고치지 않습니다. (브리프 작성·갱신만 오케스트레이터의 몫)
4. **QA 없이 완료 없음.** 요청 규모와 무관하게 qa-reviewer(기능)와 visual-qa(비주얼) **둘 다** 통과하기 전에는 "완료"라고 보고하지 않습니다. (화면 생김새가 안 바뀌는 수정만 visual-qa 생략 가능)
5. **작은 요청은 작게.** 문구 한두 개 수정 같은 요청은 관련 에이전트만 씁니다 (예: copywriter → builder → qa-reviewer). 단, 규칙 4는 유지합니다.
6. **Won't는 기능 범위에만.** 결제·로그인·서버 같은 기능 제외 목록을 근거로 시각 품질 수단(로컬 이미지 에셋, 일러스트, 첫 화면 구성)을 깎지 않습니다.

## 스킬 목록

| 스킬 | 용도 | 주 사용자 |
| --- | --- | --- |
| `web-team` | 팀 가동 오케스트레이션 절차 전체 (60~140분) | 오케스트레이터 |
| `web-team-demo` | **경량 모드** — 같은 팀 구조로 12~15분. 실습·시연용 | 오케스트레이터 |
| `static-page-builder` | 섹션별 구현 명세와 완료 기준(DoD) | frontend-builder |
| `design-system-application` | 토큰 적용·위계 규칙 점검 | frontend-builder, design-system-specialist |
| `copy-review` | 번역투·과장 탐지 패턴과 교정 절차 | copywriter |
| `mock-data-modeling` | 타입 규율, 코드값-표시명 분리, DB 매핑 | data-backend-architect |
| `qa-check` | 기능·정합·접근성 검수 체크리스트와 판정 형식 | qa-reviewer |
| `visual-review` | 스크린샷 촬영·판정 절차와 시각 체크리스트 | visual-qa, frontend-builder |

## 기준 문서 (references/)

| 문서 | 역할 |
| --- | --- |
| `briefs/*.md` | 프로젝트별 목적·사용자·핵심 흐름·포함/제외 — **범위의 최종 근거**. 신규 요청이면 오케스트레이터가 0단계에서 생성 |
| `design-system.md` | 기본 디자인 레퍼런스(토큰·타이포·컴포넌트·레이아웃). **이 파일을 다른 디자인 시스템 문서로 교체하면 팀의 스타일이 통째로 바뀝니다.** 브리프의 "디자인 방향"이 있으면 그쪽 우선 |
| `copy-principles.md` | 기본 문구 원칙, 버튼 문구 규칙, 금지 표현 |
| `frontend-quality-standards.md` | 정적 페이지·반응형 구현 기준 |

## 작업 범위

- 페이지 산출물은 `site/index.html`, `site/styles.css`, `site/app.js`와 `site/assets/`(이미지 파일 + 출처 기록)입니다.
- 그 외 새 파일·폴더·프레임워크·빌드 도구·CDN을 추가하지 않습니다. HTML/CSS는 로컬 파일만 참조하며 `open site/index.html`만으로(오프라인 포함) 동작해야 합니다.
- 사진 자리는 **1순위: 빌드 시점에 다운로드한 무료 라이선스 실사진**(Unsplash·Pexels 등 → `site/assets/*.jpg`, 출처 URL을 `site/assets/credits.txt`에 기록), **2순위(네트워크 불가 시): 직접 그린 레이어드 SVG 일러스트**로 채웁니다. "외부 이미지 금지"는 런타임 핫링크 금지이지 빌드 시 다운로드 금지가 아닙니다.
- 단색·그라디언트 사각형이나 이모지로 이미지 자리를 때우는 것은 비주얼 QA 즉시 실패입니다.
- `site/`가 placeholder(빈 캔버스) 상태면 신규 제작, 기존 페이지가 있으면 수정으로 판단합니다.

## 하지 말 것

- 사용자가 요청하지 않은 프레임워크·라이브러리 설치
- API 키, 토큰, 개인정보를 파일에 넣는 것
- 근거 없는 내용을 확정 표현으로 쓰는 것
- 디자인을 과하게 꾸미느라 브리프의 사용 목적을 흐리는 것
- 반대로, 규칙 준수를 이유로 화면을 밋밋하게 두는 것 — 이미지 자리를 단색·그라디언트 사각형이나 이모지로 때우거나, 첫 화면을 컨트롤(검색·필터)로만 채우는 것
- 렌더 결과를 스크린샷으로 확인하지 않고 "완료"라고 판단하는 것
- 브리프의 제외 목록(예: 결제, 로그인, 외부 API, 실서버 연결)을 몰래 구현하거나 몰래 빼는 것

## 검사와 보고

작업 후 `python3 scripts/check_repo.py`를 실행하고, 아래 형식으로 보고합니다.

```txt
완료:
- 브리프: (경로, 신규/갱신 여부)
- 바꾼 파일:
- 가동한 에이전트와 핵심 기여:
- 적용한 기준:
- 실행한 검사:
- 범위에서 제외한 것(Won't):
- 남은 확인 질문:
```

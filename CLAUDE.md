# TEL Harness Web Team Operating Guide

이 저장소는 TEL AI/AX 워크샵에서 **하네스 웹팀**을 실습하기 위한 예제입니다.
한 명의 AI가 즉흥적으로 전부 처리하지 않고, 아래에 정의된 팀 구조·규칙·검수 흐름을 따라 일합니다.

## 저장소 지도

```txt
tel-harness-web-team/
├── CLAUDE.md                  ← 이 문서. 팀 구성·작동 방식·불변 규칙
├── .claude/
│   ├── commands/
│   │   └── web-team.md        ← /web-team: 팀 가동 오케스트레이션 절차
│   ├── agents/                ← 서브에이전트 8명 (frontmatter + 시스템 프롬프트)
│   ├── skills/                ← 역할별 반복 절차·체크리스트 5개
│   └── rules/                 ← 항상 적용되는 품질·카피 원칙 3개
├── references/                ← 제품 브리프, 디자인 토큰, 카피 기준, 품질 기준
├── starter/                   ← 실제 수정 대상 (index.html, styles.css, app.js)
└── scripts/check_repo.py      ← 구조·frontmatter 유효성 자동 검사
```

## 팀 구성

| 에이전트 | 전문 분야 | 도구 권한 | 사전 로드 스킬 | 산출물 |
| --- | --- | --- | --- | --- |
| `business-researcher` | 사용자 불안·비교 기준·신뢰 신호 | 읽기 전용 | — | 리서치 분석 |
| `product-planner` | MVP 범위·우선순위·완료 기준 | 읽기 전용 | — | Must/Should/Won't 계획 |
| `ux-designer` | 검색→필터→카드→CTA 흐름, 상태 설계 | 읽기 전용 | — | 흐름·상태 설계안 |
| `design-system-specialist` | 토큰 기반 색·여백·타이포·CTA 위계 | 읽기 전용 | — | 토큰 대조·교정값 |
| `copywriter` | 행동 중심 문구, 번역투·과장 제거 | 읽기 전용 | copy-review | 문구 교정표 |
| `data-backend-architect` | Supabase 이전 가능한 mock 스키마 | 읽기 전용 | mock-data-modeling | 스키마 설계안 |
| `frontend-builder` | 정적 HTML/CSS/JS 구현 | **Edit/Write/Bash (유일)** | travel-page-builder, design-system-application | 코드 수정 |
| `qa-reviewer` | 요구사항·접근성·반응형 검수 | 읽기 + Bash | qa-check | 통과/수정 필요 판정 |

## 팀 작동 방식

웹페이지 제작/수정 요청이 오면 `/web-team` 절차를 따릅니다. 메인 세션은 **오케스트레이터**로서 위임·종합·보고만 하고, 분석과 구현은 서브에이전트가 합니다.

```txt
요청
 └─ 0. 요청 정리 + 규모 판단 (오케스트레이터)
 └─ 1. 분석·설계 — 읽기 전용 6명 병렬 위임
       researcher · planner · ux · design · copy · data
 └─ 2. 작업 지시서 종합 (오케스트레이터, Won't 목록이 최우선 규칙)
 └─ 3. 구현 — frontend-builder 단독 수행
 └─ 4. 검수 — qa-reviewer 판정
       └─ 수정 필요 → builder 재위임 → 재검수 (최대 2회)
 └─ 5. 최종 보고 (오케스트레이터)
```

### 위임 불변 규칙

1. **역할극 금지.** "~관점으로 보면"이라고 직접 말하지 않고, Task 도구로 해당 서브에이전트를 실제 호출합니다.
2. **컨텍스트 동봉.** 서브에이전트는 대화 기록을 못 봅니다. 위임할 때마다 사용자 요청 원문과 이전 단계의 핵심 결정을 프롬프트에 포함합니다.
3. **수정 권한 단일화.** `starter/` 파일 수정은 frontend-builder만 합니다. 오케스트레이터와 분석 역할은 파일을 고치지 않습니다.
4. **QA 없이 완료 없음.** 요청 규모와 무관하게 qa-reviewer 통과 전에는 "완료"라고 보고하지 않습니다.
5. **작은 요청은 작게.** 문구 한두 개 수정 같은 요청은 관련 에이전트만 씁니다 (예: copywriter → builder → qa-reviewer). 단, 규칙 4는 유지합니다.

## 스킬 목록

| 스킬 | 용도 | 주 사용자 |
| --- | --- | --- |
| `travel-page-builder` | 섹션별 구현 명세와 완료 기준(DoD) | frontend-builder |
| `design-system-application` | 토큰 적용·위계 규칙 점검 | frontend-builder, design-system-specialist |
| `copy-review` | 번역투·과장 탐지 패턴과 교정 절차 | copywriter |
| `mock-data-modeling` | 타입 규율, 코드값-표시명 분리, Supabase 매핑 | data-backend-architect |
| `qa-check` | 검수 체크리스트와 판정 형식 | qa-reviewer |

## 기준 문서 (references/)

| 문서 | 역할 |
| --- | --- |
| `travel-booking-product-brief.md` | 제품 상황, 사용자 불안, MVP 포함/제외 목록 — **범위의 최종 근거** |
| `airbnb-style-design.DESIGN.md` | 디자인 토큰(색·radius·shadow·spacing)과 UI 원칙 |
| `toss-style-consumer-copy.md` | 문구 원칙, 버튼 문구 예시, 금지 표현 |
| `frontend-quality-standards.md` | 정적 페이지·반응형 구현 기준 |

## 작업 범위

- 수정 대상은 `starter/index.html`, `starter/styles.css`, `starter/app.js` 세 파일뿐입니다.
- 새 파일·폴더·프레임워크·빌드 도구·CDN을 추가하지 않습니다. `open starter/index.html`만으로 동작해야 합니다.
- Work Wiki 실습은 별도 저장소 `tel-work-wiki-example`에서 진행합니다.

## 하지 말 것

- 사용자가 요청하지 않은 프레임워크·라이브러리 설치
- API 키, 토큰, 개인정보를 파일에 넣는 것
- 근거 없는 내용을 확정 표현으로 쓰는 것
- 디자인을 과하게 꾸미느라 사용 목적(검색→비교→예약 결정)을 흐리는 것
- MVP 제외 목록(결제, 로그인, 지도 API, 실서버 연결)을 몰래 구현하거나 몰래 빼는 것

## 검사와 보고

작업 후 `python3 scripts/check_repo.py`를 실행하고, 아래 형식으로 보고합니다.

```txt
완료:
- 바꾼 파일:
- 가동한 에이전트와 핵심 기여:
- 적용한 기준:
- 실행한 검사:
- 범위에서 제외한 것(Won't):
- 남은 확인 질문:
```

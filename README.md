# TEL Harness Web Team

Claude Code에서 **범용 하네스 웹팀** 구조를 직접 실습해보는 예제 저장소입니다.

이 저장소는 완성된 서비스가 아니라, AI에게 웹페이지 제작을 맡길 때 역할·기준·검수 흐름을 프로젝트 안에 어떻게 넣는지 눈으로 보고 바꿔보기 위한 실습 키트입니다. 어떤 페이지를 요청하든 팀이 **브리프 작성 → 리서치 → 기획 → UX/디자인/카피/데이터 설계 → 구현 → QA** 순서로 처음부터 만들어냅니다. 숙소 예약 페이지는 그중 하나의 예시 브리프입니다.

## 1분 시작

```bash
git clone https://github.com/zoeymakes/tel-harness-web-team.git
cd tel-harness-web-team
claude
```

Claude Code가 열리면 아래처럼 입력합니다. (예시 — 다른 어떤 페이지를 요청해도 됩니다)

```txt
/web-team 숙소 검색/예약 여행 페이지를 만들어줘.
지역, 날짜, 인원 검색이 가능하고, 숙소 카드, 필터, 예약 가능 여부 확인 CTA가 있는 페이지로 만들어줘.
실제 백엔드 없이 mock data로 구현하되, 나중에 Supabase로 확장하기 쉬운 구조로 만들어줘.
```

팀은 먼저 `references/briefs/`에 브리프를 만들거나 로드한 뒤, `site/` 안의 정적 웹페이지 세 파일을 채웁니다. `site/`는 팀 가동 전에는 빈 캔버스입니다.

## 팀 구성

| 에이전트 | 전문 분야 | 산출물 |
| --- | --- | --- |
| `business-researcher` | 사용자 불안·비교 기준·신뢰 신호 | 리서치 분석 |
| `product-planner` | MVP 범위·우선순위·완료 기준 | Must/Should/Won't 계획 |
| `ux-designer` | 핵심 흐름·상태(0건, 불가) 설계 | 흐름·상태 설계안 |
| `design-system-specialist` | 토큰 기반 색·여백·타이포·CTA 위계 | 토큰 대조·교정값 |
| `copywriter` | 행동 중심 문구, 번역투·과장 제거 | 문구 교정표 |
| `data-backend-architect` | DB 이전 가능한 mock 스키마 | 스키마 설계안 |
| `frontend-builder` | 정적 HTML/CSS/JS 구현 (**유일한 수정 권한**) | 코드 |
| `qa-reviewer` | 요구사항·접근성·반응형 검수 | 통과/수정 필요 판정 |

## 폴더 구조

```txt
tel-harness-web-team/
  CLAUDE.md                ← 하네스 포인터 + 불변 규칙 + 변경 이력
  README.md

  .claude/
    agents/                ← 서브에이전트 8명 (frontmatter + 시스템 프롬프트)
    skills/
      web-team/            ← 오케스트레이션 절차 (/web-team으로 호출)
      static-page-builder/
      design-system-application/
      copy-review/
      qa-check/
      mock-data-modeling/
    rules/                 ← 항상 적용되는 품질·카피 원칙 3개

  references/
    briefs/
      travel-booking.md    ← 예시 브리프 (새 프로젝트마다 여기에 브리프가 추가됨)
    design-tokens.md       ← 기본 디자인 토큰 (브리프에서 오버라이드 가능)
    copy-principles.md     ← 기본 문구 기준
    frontend-quality-standards.md

  site/                    ← 팀의 산출물 캔버스 (index.html, styles.css, app.js)

  scripts/check_repo.py    ← 구조·frontmatter 유효성 자동 검사
```

## 화면 확인

빌드 도구가 없는 정적 페이지라 설치·빌드 없이 바로 열립니다.

```bash
open site/index.html
```

## 실습 포인트

- `CLAUDE.md`: 하네스 트리거와 불변 규칙(수정 권한 단일화, QA 필수 등)
- `.claude/skills/web-team/SKILL.md`: 서브에이전트들을 어떤 순서로 실제 호출(위임)할지 적은 오케스트레이션 절차
- `.claude/agents/*.md`: 리서치, 기획, UX, 디자인, 카피, 데이터, 구현, QA 서브에이전트. YAML frontmatter(`name`, `description`, `tools`)로 역할·위임 조건·도구 권한을 정의하고, 본문이 각 에이전트의 시스템 프롬프트가 됩니다
- `.claude/skills/*/SKILL.md`: 반복 절차와 검토 기준. 에이전트 frontmatter의 `skills:` 필드로 해당 역할에 미리 로드됩니다
- `references/briefs/*.md`: 프로젝트마다 팀이 만드는 범위의 최종 근거. 요청이 바뀌면 브리프부터 바뀝니다
- `site/*`: 팀이 처음부터 채우는 정적 웹페이지

## 피드백할 때 보면 좋은 것

1. `/web-team`이 실제로 여러 역할을 잘 따라가는지
2. 브리프가 요청을 잘 반영해 생성되는지
3. `site/` 결과물이 너무 과하거나 어려운지
4. 어떤 설명이 비개발자에게 막히는지

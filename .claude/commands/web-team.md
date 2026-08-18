# /web-team

숙소 검색/예약형 웹페이지를 만들거나 수정할 때 사용하는 팀 실행 명령입니다.

## 입력

사용자의 요청문을 그대로 받습니다. 요청이 짧으면 아래 항목을 먼저 정리합니다.

- 페이지 목적
- 주 사용자
- 반드시 필요한 기능
- 이번 범위에서 제외할 것
- 참고해야 할 디자인/카피 기준

## 실행 순서

1. `business-researcher` 관점으로 사용자 불안과 비교 기준을 정리합니다.
2. `product-planner` 관점으로 MVP 범위와 화면 우선순위를 정합니다.
3. `ux-designer` 관점으로 검색, 필터, 카드, CTA 흐름을 설계합니다.
4. `design-system-specialist` 관점으로 `references/airbnb-style-design.DESIGN.md`를 적용합니다.
5. `copywriter` 관점으로 `references/toss-style-consumer-copy.md`를 적용합니다.
6. `data-backend-architect` 관점으로 mock data 구조를 정리합니다.
7. `frontend-builder` 관점으로 `starter/` 파일을 수정합니다.
8. `qa-reviewer` 관점으로 `references/frontend-quality-standards.md`와 `.claude/skills/qa-check/SKILL.md`를 기준으로 검사합니다.

## 사용해야 하는 Skill

- `.claude/skills/travel-page-builder/SKILL.md`
- `.claude/skills/design-system-application/SKILL.md`
- `.claude/skills/copy-review/SKILL.md`
- `.claude/skills/qa-check/SKILL.md`

## 완료 기준

- `starter/index.html`을 브라우저에서 열었을 때 주요 흐름이 보입니다.
- 검색 영역, 숙소 카드, 필터, 예약 가능 여부 CTA가 있습니다.
- 문구가 어렵거나 번역투처럼 느껴지지 않습니다.
- 모바일에서도 핵심 정보가 무너지지 않습니다.
- `python3 scripts/check_repo.py`가 통과합니다.

## 보고 형식

```txt
완료:
- 바꾼 파일:
- 적용한 역할:
- 적용한 기준:
- 확인한 것:
- 다음에 피드백받을 지점:
```

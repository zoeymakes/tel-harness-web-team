# TEL Harness Web Team

Claude Code에서 **하네스 웹팀**과 **Work Wiki** 구조를 직접 실습해보는 예제 저장소입니다.

이 저장소는 완성된 서비스가 아니라, AI에게 일을 맡기는 구조를 눈으로 보고 바꿔보기 위한 실습 키트입니다.

## 1분 시작

```bash
git clone https://github.com/zoeymakes/tel-harness-web-team.git
cd tel-harness-web-team
claude
```

Claude Code가 열리면 아래처럼 입력합니다.

```txt
/web-team 숙소 검색/예약 여행 페이지를 만들어줘.
지역, 날짜, 인원 검색이 가능하고, 숙소 카드, 필터, 예약 가능 여부 확인 CTA가 있는 페이지로 만들어줘.
실제 백엔드 없이 mock data로 구현하되, 나중에 Supabase로 확장하기 쉬운 구조로 만들어줘.
```

결과 화면은 `starter/` 안의 정적 웹페이지를 기준으로 수정됩니다.

## 폴더 구조

```txt
tel-harness-web-team/
  CLAUDE.md
  README.md

  .claude/
    commands/
      web-team.md
    agents/
      business-researcher.md
      product-planner.md
      ux-designer.md
      design-system-specialist.md
      copywriter.md
      frontend-builder.md
      data-backend-architect.md
      qa-reviewer.md
    skills/
      travel-page-builder/SKILL.md
      design-system-application/SKILL.md
      copy-review/SKILL.md
      qa-check/SKILL.md
    rules/
      product-quality-bar.md
      frontend-quality-standards.md
      consumer-copy-principles.md

  references/
    airbnb-style-design.DESIGN.md
    toss-style-consumer-copy.md
    travel-booking-product-brief.md
    frontend-quality-standards.md

  starter/
    index.html
    styles.css
    app.js

  work-wiki/
    SCHEMA.md
    CLAUDE.md
    00_inbox/
    10_sources/
    20_concepts/
    30_entities/
    40_projects/
    50_playbooks/
    60_questions/
    70_briefings/
```

## 화면 확인

별도 설치 없이 브라우저에서 열 수 있습니다.

```bash
open starter/index.html
```

로컬 서버로 보고 싶으면:

```bash
python3 -m http.server 4173 -d starter
```

브라우저에서 `http://localhost:4173`을 엽니다.

## 실습 포인트

- `CLAUDE.md`: AI가 프로젝트를 시작할 때 읽는 기본 작업 설명서
- `.claude/commands/web-team.md`: 여러 역할을 어떤 순서로 호출할지 적은 명령
- `.claude/agents/*.md`: 리서치, 기획, UX, 디자인, 구현, QA 역할 분리
- `.claude/skills/*/SKILL.md`: 반복 절차와 검토 기준
- `references/*`: AI가 참고할 디자인/카피/품질 기준
- `work-wiki/*`: 작업 중 생긴 지식을 다시 꺼내 쓰기 위한 구조

## 피드백할 때 보면 좋은 것

1. `/web-team`이 실제로 여러 역할을 잘 따라가는지
2. Claude가 references와 skills를 충분히 읽는지
3. `starter/` 결과물이 너무 과하거나 어려운지
4. Work Wiki 구조가 실제 업무 메모를 넣기에 편한지
5. 어떤 설명이 비개발자에게 막히는지

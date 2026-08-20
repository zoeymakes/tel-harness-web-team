# Frontend Quality Standards

## Static page 기준

- `site/index.html`에서 CSS와 JS 경로가 맞아야 합니다.
- JS가 실패해도 기본 안내 문구는 보여야 합니다. (`<noscript>` 포함)
- 폼 요소에는 label이 있어야 합니다.
- 버튼은 클릭 가능한 요소(`<button>`)로 구현하고, 읽을 수 있는 텍스트를 가집니다.
- 반복 렌더링되는 데이터(카드, 목록)는 `site/app.js`의 배열로 관리합니다.

## Responsive 기준

- 720px 이하에서 가로로 나열된 입력 영역은 세로 배치로 바뀝니다.
- 카드·목록은 한 열로 쌓이고, 요소가 겹치지 않습니다.
- CTA 버튼은 손가락으로 누르기 쉬운 크기(최소 높이 44px)입니다.

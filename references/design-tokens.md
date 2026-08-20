# Design Tokens — 기본 프리셋

범용 웹팀 하네스의 **기본 디자인 토큰**입니다. 브리프에 별도 "디자인 방향"이 없으면 이 값을 그대로 사용하고,
브리프가 다른 톤(예: 딱딱한 B2B, 다크 테마)을 요구하면 **브리프 쪽 값이 우선**합니다.
토큰을 바꿀 때는 즉석에서 값을 흩뿌리지 말고, 이 파일과 같은 구조의 토큰 표를 브리프에 정의한 뒤 사용합니다.

## Visual tokens

```yaml
color:
  background: "#fffaf7"
  surface: "#ffffff"
  text: "#1f2933"
  muted: "#667085"
  primary: "#ff385c"
  primary_dark: "#d92d4a"
  border: "#eadfd8"
  warm: "#fff1e8"

radius:
  card: 24px
  input: 16px
  button: 999px

shadow:
  card: "0 18px 45px rgba(31,41,51,0.10)"

spacing:
  page_x: "24px"
  section_y: "56px"
```

## UI principles (도메인 무관)

- 첫 화면의 핵심 입력/행동 영역은 크고 단순하게 둡니다.
- 카드·목록 항목은 정보 순서가 모든 항목에서 동일해야 합니다.
- 사용자의 결정에 필요한 정보(가격, 상태, 조건)는 숨기지 않습니다.
- 항목의 상태(가능/불가, 품절, 마감 등)는 목록에서 바로 구분되어야 합니다.
- 색은 CTA와 상태 표시를 중심으로 제한합니다. 장식용 색을 늘리지 않습니다.

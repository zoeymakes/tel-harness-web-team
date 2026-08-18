# Airbnb-style Travel Design Reference

이 파일은 Airbnb를 그대로 베끼기 위한 문서가 아니라, 여행/숙소 예약 서비스에서 참고할 수 있는 화면 원칙을 정리한 문서입니다.

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

## UI principles

- 검색 영역은 크고 단순하게 둡니다.
- 숙소 카드는 이미지, 위치, 핵심 특징, 가격, CTA 순서로 읽힙니다.
- 가격은 숨기지 않습니다.
- 예약 가능 여부를 카드에서 바로 알 수 있게 합니다.
- 색은 CTA와 상태 표시를 중심으로 제한합니다.

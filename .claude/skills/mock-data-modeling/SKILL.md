---
name: mock-data-modeling
description: 정적 페이지의 mock 데이터를 나중에 Supabase 같은 DB로 옮기기 쉬운 구조로 설계할 때 사용. 필드 타입 규율, 코드값-표시명 분리, 테이블 매핑을 다룬다. "데이터 구조", "스키마", "mock data 정리", "Supabase 확장", "데이터 다시 설계" 요청에서 사용.
---

# Mock Data Modeling

`site/app.js`의 mock 데이터를 "이 배열을 그대로 SQL 테이블로 옮길 수 있는가" 기준으로 설계하는 절차입니다. 핵심 엔티티(숙소, 상품, 게시글 등)는 브리프가 정하고, 이 스킬은 타입·구조 규율을 정합니다.

## 타입 규율 (가장 흔한 위반부터)

| 규칙 | ❌ | ⭕ |
| --- | --- | --- |
| 가격·수치는 숫자 | `price: '1박 189,000원'` | `pricePerNight: 189000` |
| 평점은 숫자 + 근거 개수 분리 | `rating: '4.9'` | `rating: 4.9, reviewCount: 128` |
| 불리언은 불리언 | `available: '가능'` | `available: true` |
| 한 필드 한 값 | `meta: '바다까지 도보 4분 · 침실 2개'` | `distanceNote: '...', bedrooms: 2` |
| 안정적인 id | 배열 인덱스로 식별 | `id: 'stay-001'` |

표시 포맷("1박 189,000원", "평점 4.9 (128)")은 **렌더 함수에서** 만든다. 데이터에 표시용 문자열을 저장하지 않는다.

## 코드값과 표시명 분리

enum성 값(유형, 카테고리, 상태)은 코드값으로 저장하고 한국어 표시명은 매핑 객체로 분리한다.

```js
// 예시 — 엔티티와 코드값은 브리프에 맞게 정의한다
const STAY_TYPES = { house: '독채', hotel: '호텔', pension: '펜션' };
const AMENITIES = { parking: '주차 가능', kitchen: '취사 가능', breakfast: '조식 포함' };
```

- 필터·탭 버튼의 `data-*` 값은 이 코드값과 정확히 일치시킨다.
- 다중 값 필드(태그, 옵션)는 코드값 배열로: `amenities: ['parking', 'kitchen']`

## 표준 레코드 예시 (여행 브리프 기준 — 구조만 참고)

```js
// 이후 Supabase stays 테이블로 이전 (amenities는 조인 테이블로 분리 예정)
const stays = [
  {
    id: 'stay-001',
    name: '서귀포 오션 독채',
    region: '제주',
    type: 'house',
    emoji: '🌊',
    pricePerNight: 189000,
    rating: 4.9,
    reviewCount: 128,
    bedrooms: 2,
    distanceNote: '바다까지 도보 4분',
    amenities: ['parking', 'kitchen'],
    available: true,
  },
];
```

## Supabase 매핑 (camelCase ↔ snake_case)

핵심 엔티티당 테이블 하나를 만들고, 각 필드의 대응을 표로 남긴다.

| JS 필드 | 테이블.컬럼 | 타입 |
| --- | --- | --- |
| id | {entity}.id | uuid (지금은 text) |
| 텍스트 필드 | {entity}.{snake_case} | text |
| 금액·수량 | {entity}.{snake_case} | integer |
| 평점 | {entity}.rating | numeric(2,1) |
| 여부 | {entity}.{snake_case} | boolean |
| 다중 값(태그 등) | 조인 테이블 (이후 분리) | — |

## 파일 구조 규칙

- `app.js` 상단: 매핑 객체 → 데이터 배열, 하단: 렌더/이벤트 로직. 데이터와 렌더링을 섞지 않는다.
- 레코드는 3~6개. 필터 축(유형·가격·상태)이 서로 다른 조합으로 만들어 필터 데모가 되게 한다.
- 실제 DB 클라이언트, API 키, fetch 코드는 범위 밖 — 넣지 않는다.

## 완료 기준

- [ ] 모든 숫자 정보가 숫자 타입, 표시 포맷은 렌더에서
- [ ] 코드값-표시명 매핑 분리, 필터 `data-*`와 일치
- [ ] 각 필드의 Supabase 테이블.컬럼 대응을 말할 수 있다
- [ ] 데이터 선언과 렌더 로직이 분리되어 있다

const stays = [
  {
    name: '서귀포 오션 독채',
    region: '제주',
    type: 'house',
    emoji: '🌊',
    price: '1박 189,000원',
    rating: '4.9',
    meta: '바다까지 도보 4분 · 침실 2개',
    tags: ['독채', '주차 가능', '취사 가능'],
    available: true,
  },
  {
    name: '중문 가든 호텔',
    region: '제주',
    type: 'hotel',
    emoji: '🌿',
    price: '1박 142,000원',
    rating: '4.7',
    meta: '조식 포함 · 수영장 이용 가능',
    tags: ['호텔', '조식', '수영장'],
    available: true,
  },
  {
    name: '애월 노을 펜션',
    region: '제주',
    type: 'pension',
    emoji: '🌅',
    price: '1박 98,000원',
    rating: '4.6',
    meta: '노을 전망 · 반려동물 동반 문의',
    tags: ['펜션', '가성비', '노을 전망'],
    available: false,
  },
];

const grid = document.querySelector('#stayGrid');
const summary = document.querySelector('#summary');
const buttons = document.querySelectorAll('.filter');
const form = document.querySelector('#searchForm');

function render(type = 'all') {
  const filtered = type === 'all' ? stays : stays.filter((stay) => stay.type === type);
  summary.textContent = `제주 지역 mock 숙소 ${filtered.length}개를 보여드릴게요.`;
  grid.innerHTML = filtered.map((stay) => `
    <article class="stay-card">
      <div class="stay-image" aria-hidden="true">${stay.emoji}</div>
      <div class="stay-body">
        <h2>${stay.name}</h2>
        <p class="meta">${stay.meta} · 평점 ${stay.rating}</p>
        <div class="tags">${stay.tags.map((tag) => `<span class="tag">${tag}</span>`).join('')}</div>
        <div class="price-row">
          <span class="price">${stay.price}</span>
          <button class="card-cta" type="button">${stay.available ? '예약 가능' : '날짜 변경'}</button>
        </div>
      </div>
    </article>
  `).join('');
}

buttons.forEach((button) => {
  button.addEventListener('click', () => {
    buttons.forEach((item) => item.classList.remove('active'));
    button.classList.add('active');
    render(button.dataset.type);
  });
});

form.addEventListener('submit', (event) => {
  event.preventDefault();
  const data = new FormData(form);
  const region = data.get('region') || '선택한 지역';
  summary.textContent = `${region} 조건에 맞는 mock 숙소를 확인하고 있어요.`;
  render(document.querySelector('.filter.active').dataset.type);
});

render();

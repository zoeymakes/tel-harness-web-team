from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

AGENTS = [
    '.claude/agents/business-researcher.md',
    '.claude/agents/product-planner.md',
    '.claude/agents/ux-designer.md',
    '.claude/agents/design-system-specialist.md',
    '.claude/agents/copywriter.md',
    '.claude/agents/frontend-builder.md',
    '.claude/agents/data-backend-architect.md',
    '.claude/agents/qa-reviewer.md',
]

SKILLS = [
    '.claude/skills/web-team/SKILL.md',
    '.claude/skills/static-page-builder/SKILL.md',
    '.claude/skills/design-system-application/SKILL.md',
    '.claude/skills/copy-review/SKILL.md',
    '.claude/skills/qa-check/SKILL.md',
    '.claude/skills/mock-data-modeling/SKILL.md',
]

OTHER = [
    'CLAUDE.md',
    'references/design-tokens.md',
    'references/copy-principles.md',
    'references/frontend-quality-standards.md',
    'site/index.html',
    'site/styles.css',
    'site/app.js',
]

errors = []

# 1. 필수 파일 존재 확인
for p in AGENTS + SKILLS + OTHER:
    if not (ROOT / p).exists():
        errors.append(f'파일 없음: {p}')

# 2. 브리프 폴더 확인 (예시 브리프 최소 1개)
briefs_dir = ROOT / 'references/briefs'
if not briefs_dir.is_dir() or not list(briefs_dir.glob('*.md')):
    errors.append('references/briefs/ 에 브리프(.md)가 최소 1개 있어야 합니다 (예시: travel-booking.md)')


def parse_frontmatter(path):
    """SKILL.md / agent 파일 상단의 YAML frontmatter를 단순 파싱한다."""
    lines = path.read_text(encoding='utf-8').splitlines()
    if not lines or lines[0].strip() != '---':
        return None
    fields = {}
    for line in lines[1:]:
        if line.strip() == '---':
            return fields
        if ':' in line and not line.startswith((' ', '\t', '-')):
            key, _, value = line.partition(':')
            fields[key.strip()] = value.strip().strip('"').strip("'")
    return None  # 닫는 '---' 없음


# 3. 서브에이전트 frontmatter 확인 (name, description 필수)
for p in AGENTS:
    path = ROOT / p
    if not path.exists():
        continue
    fm = parse_frontmatter(path)
    if fm is None:
        errors.append(f'YAML frontmatter 없음 (서브에이전트로 등록되지 않음): {p}')
        continue
    for field in ('name', 'description'):
        if not fm.get(field):
            errors.append(f'frontmatter에 {field} 필드 없음: {p}')
    expected = path.stem
    if fm.get('name') and fm['name'] != expected:
        errors.append(f'name({fm["name"]})이 파일명({expected})과 다름: {p}')

# 4. 스킬 frontmatter 확인 (description 권장 → 이 실습에서는 필수로 검사)
for p in SKILLS:
    path = ROOT / p
    if not path.exists():
        continue
    fm = parse_frontmatter(path)
    if fm is None:
        errors.append(f'YAML frontmatter 없음: {p}')
        continue
    if not fm.get('description'):
        errors.append(f'frontmatter에 description 없음 (자동 로드 불가): {p}')

# 5. site 페이지 참조 확인
html_path = ROOT / 'site/index.html'
if html_path.exists():
    html = html_path.read_text(encoding='utf-8')
    for ref in ['./styles.css', './app.js']:
        if ref not in html:
            errors.append(f'index.html에 참조 없음: {ref}')

if errors:
    print('문제 발견:')
    for e in errors:
        print('-', e)
    sys.exit(1)

print('OK: 하네스 웹팀 저장소 구조와 에이전트/스킬 정의가 유효합니다.')

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
required = [
    'CLAUDE.md',
    '.claude/commands/web-team.md',
    '.claude/agents/business-researcher.md',
    '.claude/agents/product-planner.md',
    '.claude/agents/ux-designer.md',
    '.claude/agents/design-system-specialist.md',
    '.claude/agents/copywriter.md',
    '.claude/agents/frontend-builder.md',
    '.claude/agents/data-backend-architect.md',
    '.claude/agents/qa-reviewer.md',
    '.claude/skills/travel-page-builder/SKILL.md',
    '.claude/skills/design-system-application/SKILL.md',
    '.claude/skills/copy-review/SKILL.md',
    '.claude/skills/qa-check/SKILL.md',
    'references/airbnb-style-design.DESIGN.md',
    'references/toss-style-consumer-copy.md',
    'references/travel-booking-product-brief.md',
    'references/frontend-quality-standards.md',
    'starter/index.html',
    'starter/styles.css',
    'starter/app.js',
    'work-wiki/SCHEMA.md',
    'work-wiki/CLAUDE.md',
]
missing = [p for p in required if not (ROOT / p).exists()]
if missing:
    print('Missing files:')
    for p in missing:
        print('-', p)
    sys.exit(1)

html = (ROOT / 'starter/index.html').read_text(encoding='utf-8')
for ref in ['./styles.css', './app.js']:
    if ref not in html:
        print(f'missing asset reference in index.html: {ref}')
        sys.exit(1)

print('OK: TEL harness web team repo structure is ready.')

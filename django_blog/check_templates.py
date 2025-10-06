import os
from pathlib import Path

# Base directory of the project (where manage.py is)
BASE_DIR = Path(__file__).resolve().parent

# Path to blog templates folder
TEMPLATES_DIR = BASE_DIR / 'blog' / 'templates' / 'blog'

# Required templates for CRUD
required_templates = [
    'post_list.html',
    'post_detail.html',
    'post_form.html',
    'post_confirm_delete.html'
]

# Check which templates are missing
missing = [t for t in required_templates if not (TEMPLATES_DIR / t).exists()]

if missing:
    print("❌ Missing templates:")
    for t in missing:
        print(f"- {t}")
else:
    print("✅ All required templates exist!")

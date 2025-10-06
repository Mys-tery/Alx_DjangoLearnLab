import os

# Path to your blog templates directory
TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), 'blog', 'templates', 'blog')

# Required templates for CRUD operations
required_templates = [
    'post_list.html',
    'post_detail.html',
    'post_form.html',
    'post_confirm_delete.html'
]

missing = []

for template in required_templates:
    if not os.path.exists(os.path.join(TEMPLATES_DIR, template)):
        missing.append(template)

if missing:
    print("❌ Missing templates:")
    for t in missing:
        print(f"- {t}")
else:
    print("✅ All required templates exist!")

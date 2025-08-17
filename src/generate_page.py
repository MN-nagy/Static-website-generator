from mark_to_html import markdown_to_html_node
from get_h1 import extract_title
import os


def generate_page(
    from_path: str = os.path.abspath("content/index.md"),
    template_path: str = os.path.abspath("template.html"),
    dest_path: str = os.path.abspath("public/index.html"),
    basepath=None,
):

    print(f"Generating page from {from_path} -> {dest_path}, using {template_path}")

    src = os.path.abspath(from_path)
    if not os.path.exists(src):
        print(f"Source directory {src} does not exist. Nothing to copy.")
        return

    with open(from_path, "r") as f:
        md = f.read()

    with open(template_path, "r") as t:
        template = t.read()

    html_string = markdown_to_html_node(md)
    content = html_string.to_html()

    title = extract_title(md)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", content)
    if basepath:
        template = template.replace('href="/', f'href="{basepath}')
        template = template.replace('src="/', f'src="{basepath}')

    dst = os.path.abspath(dest_path)
    os.makedirs(os.path.dirname(dst), exist_ok=True)

    with open(dst, "w") as ds:
        ds.write(template)

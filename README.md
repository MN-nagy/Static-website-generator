# Static Website Generator

A small, dependency-light Python static site generator that converts Markdown into a static HTML site.
Built as a learning exercise — includes block + inline parsing, a tiny templating step, static asset copying, and utilities to build for local dev or GitHub Pages.

---

## Preview

See the demo [here](https://mn-nagy.github.io/Static-website-generator/)

---

## Features

* Convert Markdown (`.md`) into semantic HTML (headings, paragraphs, lists, blockquotes, code blocks).
* Inline formatting support: **bold**, *italic*, `code`.
* Markdown links `[text](url)` and images `![alt](url)`.
* Tiny template injection using `{{ Title }}` and `{{ Content }}` placeholders in `template.html`.
* Static asset copying from `static/` to output directory (`public/` by default; optionally `docs/` for GitHub Pages).
* Recursive generation of all Markdown files in `content/` into matching directory structure in the output.
* Configurable `basepath` parameter so absolute `href="/..."` and `src="/..."` values can be prefixed for subdirectory deployments (e.g. `/REPO_NAME/`).

---

## Quickstart

### Prerequisites

* Python 3.8+
* (Optional) virtualenv

### Clone & setup

```bash
git clone https://github.com/MN-nagy/Static-website-generator.git
cd Static-website-generator

# create & activate a venv
python -m venv venv
# macOS / Linux
source venv/bin/activate
# Windows (cmd)
venv\Scripts\activate
# Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# install requirements if present (repo is minimal and may not include requirements.txt)
pip install -r requirements.txt || true
```

> Note: the project is intentionally minimal and often relies on the Python standard library.

---

## Run locally (development)

Generate the site and start a simple static HTTP server from the generated `public/` directory:

```bash
# make main.sh executable (only needed once on Unix)
chmod +x main.sh

# run the dev script (copies static -> public, builds HTML, and starts a server)
./main.sh

# then open in your browser:
http://localhost:8888
```

Alternatively, run the Python builder directly:

```bash
# build into the default output directory (public/)
python3 src/main.py
```

---

## Build for production (GitHub Pages under a repo path)

To deploy under `https://USERNAME.github.io/REPO_NAME/`, supply a `basepath` when building so generated `href`/`src` references are prefixed:

```bash
# example: build with basepath set to the repo name
python3 src/main.py "/REPO_NAME/"
```

To publish using the `docs/` folder:

1. Generate the site into `docs/` instead of `public/` (adjust `main.py` or use `build.sh` to target `docs/`).
2. Commit the `docs/` folder to the `main` branch.
3. In your GitHub repository → Settings → Pages, set the source to `main` branch and `/docs` folder.
4. Your site will be available at `https://USERNAME.github.io/REPO_NAME/`.

---

## Commands / Scripts

* `./main.sh` — dev script: generate site into `public/` and launch a local dev server.
* `python3 src/main.py "/REPO_NAME/"` — build for deployment under `/REPO_NAME/`.
* `python3 src/main.py` — build with default basepath (no prefixing).
* `./test.sh` — run unit tests (if test scripts are present).

---

## Tests

Run tests from the project root:

```bash
./test.sh
# or
python3 -m unittest discover -s src
```

Add unit tests into `src/` (e.g. `test_mark_to_node.py`, `test_htmlnode.py`). The repo includes example tests for core parsing and HTML generation components.

---

## Project layout

```
Static-website-generator/
├── content/                    # Markdown content (source)
│   ├── index.md
│   └── blog/...
├── static/                     # static assets (images, css)
│   ├── images/
│   └── index.css
├── docs/                       # (optional) production output for GitHub Pages
├── public/                     # (dev) generated site for local server
├── src/
│   ├── main.py
│   ├── copy_func.py
│   ├── generate_page.py
│   ├── generate_pages_recursive.py
│   ├── mark_to_block.py
│   ├── mark_to_node.py
│   ├── mark_to_html.py
│   ├── textnode.py
│   ├── htmlnode.py
│   └── ...tests...
├── template.html
├── build.sh                    # production build script (optional)
├── main.sh                     # dev server + build script
└── README.md
```

(Actual repository contents may vary — check the repo for the current tree.)

---

# Design notes & implementation details

The generator uses a two-step parsing approach:

* **Block parsing** (`markdown_to_blocks`) — splits raw Markdown into paragraphs, headings, lists, blockquotes, and code blocks.
* **Inline parsing** (`text_to_textnodes` + `split_nodes_*`) — breaks inline Markdown into `TextNode`s (text, bold, italic, code, link, image), converts those to `LeafNode`/`ParentNode` structures, and finally renders to HTML via `mark_to_html`/`htmlnode`.

Static assets are copied recursively from `static/` to the chosen output directory using `copy_recursive()` (see `src/copy_func.py`).

A `basepath` parameter lets you prefix absolute paths (e.g. `href="/..."`, `src="/..."`) for deployment under a subpath such as GitHub Pages.

---

## Troubleshooting & tips

* **Indentation in triple-quoted test strings**
  Use `textwrap.dedent(...)` for multi-line triple-quoted strings in tests to avoid leading spaces that alter parsing (especially in fenced code blocks).

* **Unmatched delimiters**
  The parser expects matching `**` and backticks `` ` ``. Unmatched delimiters may produce incorrect parsing or errors. Check Markdown for balanced delimiters or use the scanning logic in `mark_to_node.py`.

* **Attributes glued to tags**
  If you see malformed output like `<ahref=...>` or `<imgsrc=...>`, ensure the HTML node renderer prefixes non-empty props with a leading space (see `HTMLNode.props_to_html()` in `src/htmlnode.py`).

* **Windows vs Unix permissions**
  `chmod +x main.sh` is only needed on Unix-like systems. On Windows, run the Python builder directly.

---

## Known limitations

* Minimal or no front-matter/YAML metadata support.
* Not intended as a full-featured SSG — purpose is educational and for small sites.
* No plugin system or advanced template engine — template injection is intentionally simple.

---

## Contributing

Contributions, bug reports, and improvements are welcome.

1. Fork the repository.
2. Create a branch:

   ```bash
   git checkout -b feature/my-change
   ```
3. Make your changes and add tests.
4. Commit and push:

   ```bash
   git add .
   git commit -m "Describe your change"
   git push origin feature/my-change
   ```
5. Open a Pull Request describing the change.


---

> Note: this project was done as part of [boot.div](https://www.boot.dev/dashboard) golang [back-end](https://www.boot.dev/tracks/backend-python-golang) learing path, to view course click [here](https://www.boot.dev/courses/build-static-site-generator-python)

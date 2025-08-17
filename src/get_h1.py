def extract_title(markdown: str) -> str:
    for line in markdown.split("\n"):
        striped = line.strip()
        if striped.startswith("# "):
            header = striped.split(" ", maxsplit=1)[1].strip()
            return header
    raise Exception("No header found")

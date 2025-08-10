from typing import List


def markdown_to_blocks(markdown: str) -> List[str]:
    lines = markdown.split("\n")
    blocks, bucket = [], []
    for line in lines:
        if line.strip() == "":
            if bucket:
                blocks.append("\n".join(bucket).strip())
                bucket = []
        else:
            bucket.append(line)
    if bucket:
        blocks.append("\n".join(bucket).strip())
    return blocks

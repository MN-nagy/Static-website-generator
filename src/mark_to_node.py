from textnode import TextNode, TextType
from typing import List, Callable
from extract_markdown import extract_markdown_images, extract_markdown_links


def split_nodes_delimiter(
    old_nodes: List[TextNode], delimiter: str, text_type: TextType
) -> List[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        if node.text.count(delimiter) % 2 != 0:
            raise Exception(f"Unmatched delimiter: {delimiter}")

        parts = node.text.split(delimiter)

        for i, part in enumerate(parts):
            if part:
                if i % 2 == 0:
                    new_nodes.append(TextNode(part, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(part, text_type))

    return new_nodes


def split_nodes_markdown(
    old_nodes: List[TextNode],
    extractor: Callable[[str], List[tuple[str, str]]],
    node_type: TextType,
    pattern_fmt: str,
) -> List[TextNode]:

    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text_remaining = node.text
        matches = extractor(text_remaining)

        if not matches:
            new_nodes.append(node)
            continue

        for alt, url in matches:
            pattern = pattern_fmt.format(alt=alt, url=url)
            before, _, after = text_remaining.partition(pattern)

            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(alt, node_type, url))

            text_remaining = after

        if text_remaining:
            new_nodes.append(TextNode(text_remaining, TextType.TEXT))

    return new_nodes


def split_nodes_image(old_nodes: List[TextNode]) -> List[TextNode]:
    return split_nodes_markdown(
        old_nodes,
        extractor=extract_markdown_images,
        node_type=TextType.IMAGE,
        pattern_fmt="![{alt}]({url})",
    )


def split_nodes_link(old_nodes: List[TextNode]) -> List[TextNode]:
    return split_nodes_markdown(
        old_nodes,
        extractor=extract_markdown_links,
        node_type=TextType.LINK,
        pattern_fmt="[{alt}]({url})",
    )

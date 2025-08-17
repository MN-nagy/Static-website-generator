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

        text = node.text
        start = 0
        while True:
            open_idx = text.find(delimiter, start)
            if open_idx == -1:
                new_nodes.append(TextNode(text[start:], TextType.TEXT))
                break
            close_idx = text.find(delimiter, open_idx + len(delimiter))
            if close_idx == -1:
                new_nodes.append(TextNode(text[start:], TextType.TEXT))
                break
            if open_idx > start:
                new_nodes.append(TextNode(text[start:open_idx], TextType.TEXT))
            new_nodes.append(
                TextNode(text[open_idx + len(delimiter) : close_idx], text_type)
            )
            start = close_idx + len(delimiter)

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


def text_to_textnodes(text: str) -> list[TextNode]:
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

from htmlnode import *
from typing import List
from mark_to_block import markdown_to_blocks
from block_fn import BlockType, block_to_block_type
from mark_to_node import *
from text_to_leaf import text_node_to_leaf_node


def markdown_to_html_node(markdown: str):
    blocks = markdown_to_blocks(markdown)
    parent_container = ParentNode("div", children=[])
    for block in blocks:
        block_type = block_to_block_type(block)

        match block_type:
            case BlockType.HEADING:
                level = len(block) - len(block.lstrip("#"))
                text = block.lstrip("#").strip()
                html_node = ParentNode(f"h{level}", text_to_children(text))
            case BlockType.PARAGRAPH:
                text = " ".join(line.strip() for line in block.split("\n"))
                html_node = ParentNode("p", text_to_children(text))
            case BlockType.QUOTE:
                text = "\n".join(
                    (
                        line[2:]
                        if line.startswith("> ")
                        else line[1:] if line.startswith(">") else line
                    )
                    for line in block.split("\n")
                )
                html_node = ParentNode("blockquote", text_to_children(text))
            case BlockType.UNORDERED_LIST:
                items = block.split("\n")
                li_nodes = [
                    ParentNode("li", text_to_children(item.lstrip("*- ").strip()))
                    for item in items
                ]
                html_node = ParentNode("ul", li_nodes)
            case BlockType.ORDERED_LIST:
                items = block.split("\n")
                li_nodes = [
                    ParentNode(
                        "li", text_to_children(item.lstrip("0123456789. ").strip())
                    )
                    for item in items
                ]
                html_node = ParentNode("ol", li_nodes)
            case BlockType.CODE:
                lines = block.split("\n")
                code_content = "\n".join(lines[1:-1]) + "\n"
                code_node = LeafNode("code", code_content)
                html_node = ParentNode("pre", [code_node])

        parent_container.children.append(html_node)
    return parent_container


def text_to_children(text: str) -> List[HTMLNode]:
    text_nodes = text_to_textnodes(text)
    return [text_node_to_leaf_node(txt_node) for txt_node in text_nodes]

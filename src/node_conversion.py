from textnode import TextNode, TextType
from htmlnode import LeafNode


def node_conversion(text_node: TextNode) -> LeafNode:
    nodes = {
        TextType.TEXT: LeafNode(None, text_node.text),
        TextType.BOLD: LeafNode("b", text_node.text),
        TextType.ITALIC: LeafNode("i", text_node.text),
        TextType.CODE: LeafNode("code", text_node.text),
        TextType.LINK: LeafNode("a", text_node.text, props={"href": text_node.url}),
        TextType.IMAGE: LeafNode(
            "img", "", props={"src": text_node.url, "alt": text_node.text}
        ),
    }

    result = nodes.get(text_node.text_type)

    if not result:
        raise Exception("Invalid text type")

    return result

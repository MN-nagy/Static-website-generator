import unittest
from textnode import TextNode, TextType
from mark_to_node import split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    def test_none_text_type(self):
        node = TextNode("This is text", TextType.BOLD)
        self.assertTrue(node in split_nodes_delimiter([node], "n", TextType.CODE))

    def test_odd_parts(self):
        node = TextNode("This `is text `foo `par", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.BOLD)

    def test_split_functionality(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
        )


if __name__ == "__main__":
    unittest.main()

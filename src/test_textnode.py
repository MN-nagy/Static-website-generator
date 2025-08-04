import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq(self):
        node1 = TextNode("Text A", TextType.BOLD)
        node2 = TextNode("Text B", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_diff_text_type(self):
        node1 = TextNode("Text A", TextType.BOLD)
        node2 = TextNode("Text A", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_diff_url(self):
        node1 = TextNode("Text A", TextType.LINK, "https://boot.dev")
        node2 = TextNode("Text A", TextType.LINK, "https://boot.div")
        self.assertNotEqual(node1, node2)

    def test_no_url(self):
        node1 = TextNode("Text A", TextType.LINK)
        node2 = TextNode("Text A", TextType.LINK, "https://boot.div")
        self.assertNotEqual(node1, node2)

    def test_None_url(self):
        node1 = TextNode("Text A", TextType.LINK)
        node2 = TextNode("Text A", TextType.LINK, None)
        self.assertEqual(node1, node2)


if __name__ == "__main__":
    unittest.main()

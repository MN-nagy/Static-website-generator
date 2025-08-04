import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"class": "test"})
        self.assertEqual(node.props_to_html(), 'class="test"')

    def test_props_to_html_multiple(self):
        node = HTMLNode(props={"href": "https://example.com", "target": "_blank"})
        self.assertEqual(
            node.props_to_html(), 'href="https://example.com" target="_blank"'
        )

    def test_repr(self):
        node = HTMLNode("<div>", "hhh", None, {"class": "test"})
        expected_repr = (
            "HTMLNode(tag=<div>, value=hhh, children=None, props={'class': 'test'})"
        )
        self.assertEqual(repr(node), expected_repr)


if __name__ == "__main__":
    unittest.main()

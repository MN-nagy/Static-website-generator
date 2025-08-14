import unittest
import textwrap
from mark_to_html import markdown_to_html_node


class TestTextNode(unittest.TestCase):
    def test_paragraphs(self):
        md = textwrap.dedent(
            """\
            This is **bolded** paragraph
            text in a p
            tag here

            This is another paragraph with _italic_ text and `code` here
        """
        )
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p>"
            "<p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = textwrap.dedent(
            """\
            ```
            This is text that _should_ remain
            the **same** even with inline stuff
            ```
        """
        )
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\n"
            "the **same** even with inline stuff\n</code></pre></div>",
        )

    def test_ordered_list(self):
        md = "1. First\n2. _Second_\n3. Third"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>First</li><li><i>Second</i></li><li>Third</li></ol></div>",
        )

    def test_codeblock_again(self):
        md = (
            "```\nThis is text that _should_ remain\n"
            "the **same** even with inline stuff\n```"
        )
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\n"
            "the **same** even with inline stuff\n</code></pre></div>",
        )


if __name__ == "__main__":
    unittest.main()

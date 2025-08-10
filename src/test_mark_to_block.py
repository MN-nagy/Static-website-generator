import unittest
from mark_to_block import markdown_to_blocks


class TestTextNode(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_leading_and_trailing_newlines(self):
        md = """

# Heading

Some text here

"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["# Heading", "Some text here"])

    def test_multiple_empty_lines(self):
        md = "First paragraph\n\n\n\nSecond paragraph"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["First paragraph", "Second paragraph"])

    def test_single_block_no_newlines(self):
        md = "Just a single block"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Just a single block"])

    def test_block_with_whitespace_lines(self):
        md = "First paragraph\n   \nSecond paragraph"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["First paragraph", "Second paragraph"])


if __name__ == "__main__":
    unittest.main()

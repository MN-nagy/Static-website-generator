import unittest
from block_fn import BlockType, block_to_block_type


class TestBlockToBlockType(unittest.TestCase):

    def test_heading(self):
        self.assertEqual(block_to_block_type("# Heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### Small heading"), BlockType.HEADING)
        self.assertNotEqual(block_to_block_type("####### Too many"), BlockType.HEADING)

    def test_code_block(self):
        code_block = "```\nprint('Hello')\n```"
        self.assertEqual(block_to_block_type(code_block), BlockType.CODE)

    def test_quote(self):
        quote_block = "> This is a quote\n> with two lines"
        self.assertEqual(block_to_block_type(quote_block), BlockType.QUOTE)

    def test_unordered_list(self):
        ul_block = "- item one\n- item two\n- item three"
        self.assertEqual(block_to_block_type(ul_block), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        ol_block = "1. First\n2. Second\n3. Third"
        self.assertEqual(block_to_block_type(ol_block), BlockType.ORDERED_LIST)

    def test_paragraph(self):
        paragraph = "This is a normal paragraph without special syntax."
        self.assertEqual(block_to_block_type(paragraph), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()

import unittest
import textwrap
from get_h1 import extract_title


class TestBlockToBlockType(unittest.TestCase):
    def test_simple_h1(self):
        self.assertEqual(extract_title("# Hello"), "Hello")

    def test_h1_with_extra_spaces(self):
        self.assertEqual(extract_title("   #   My Title   "), "My Title")

    def test_extract_title(self):
        md = textwrap.dedent(
            """\
            # Title
            ## another title

            something else
            """
        )
        self.assertEqual("Title", extract_title(md))


if __name__ == "__main__":
    unittest.main()

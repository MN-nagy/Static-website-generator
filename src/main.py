from textnode import TextNode
from copy_func import generate_public


def main():
    text_obj = TextNode("This is some anchor text", "link", "https://www.boot.dev")
    generate_public()
    print(text_obj)


if __name__ == "__main__":
    main()

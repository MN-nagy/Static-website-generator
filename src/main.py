from copy_func import generate_public
from generate_pages_recursive import generate_pages_recursive
import sys

basepath = sys.argv[1] if len(sys.argv) > 1 else None


def main():
    generate_public("docs")
    generate_pages_recursive(dest_dir_path="docs", basepath=basepath)


if __name__ == "__main__":
    main()

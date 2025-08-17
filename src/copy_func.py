import os
import shutil


def copy_recursive(src, dst):

    if not os.path.exists(dst):
        os.makedirs(dst)

    if not os.path.exists(src):
        print(f"Source directory {src} does not exist. Nothing to copy.")
        return

    for item in os.listdir(src):
        s_item = os.path.join(src, item)
        d_item = os.path.join(dst, item)

        if os.path.isdir(s_item):
            copy_recursive(s_item, d_item)
        else:
            print(f"Copying {s_item} -> {d_item}")
            shutil.copy(s_item, d_item)


def generate_public():
    public = os.path.abspath("public")
    static = os.path.abspath("static")

    if os.path.exists(public):
        shutil.rmtree(public)

    copy_recursive(static, public)

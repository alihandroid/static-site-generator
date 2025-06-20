import os
import shutil
import sys
from page import generate_page
from textnode import *

STATIC_PATH = "./static"
PUBLIC_PATH = "./docs"
CONTENT_PATH = "./content"
TEMPLATE_PATH = "template.html"


def main():
    basepath = "/" if len(sys.argv) < 2 else sys.argv[1]

    if os.path.exists(PUBLIC_PATH):
        shutil.rmtree(PUBLIC_PATH)
    shutil.copytree(STATIC_PATH, PUBLIC_PATH)

    for root, _, files in os.walk(CONTENT_PATH):
        for file in files:
            if not file.endswith(".md"):
                raise Exception("Unknown file type {path}")
            from_path = os.path.join(root, file)
            dest_path = from_path.replace(CONTENT_PATH, PUBLIC_PATH)[:-2] + "html"
            generate_page(from_path, TEMPLATE_PATH, dest_path, basepath)


if __name__ == "__main__":
    main()

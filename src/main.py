import os
import shutil
from page import generate_page
from textnode import *

STATIC_PATH = "./static"
PUBLIC_PATH = "./public"


def main():
    shutil.rmtree(PUBLIC_PATH)
    shutil.copytree(STATIC_PATH, PUBLIC_PATH)

    generate_page("content/index.md", "template.html", "public/index.html")


if __name__ == "__main__":
    main()

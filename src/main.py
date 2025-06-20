import os
import shutil
from textnode import *

STATIC_PATH = "./static"
PUBLIC_PATH = "./public"


def main():
    shutil.rmtree(PUBLIC_PATH)
    shutil.copytree(STATIC_PATH, PUBLIC_PATH)


if __name__ == "__main__":
    main()

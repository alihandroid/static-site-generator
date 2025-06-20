from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    return list(map(lambda x: x.strip(), markdown.split("\n\n")))


def block_to_block_type(block):
    if re.match(r"^#{1,6} \w", block):
        return BlockType.HEADING

    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    lines = block.split("\n")

    quote = True
    for line in lines:
        if not line.startswith(">"):
            quote = False
            break
    if quote:
        return BlockType.QUOTE

    unordered = True
    for line in lines:
        if not line.startswith("- "):
            unordered = False
            break
    if unordered:
        return BlockType.UNORDERED_LIST

    ordered = True
    index = 0
    for line in lines:
        index += 1
        if not line.startswith(f"{index}. "):
            ordered = False
            break
    if ordered:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH

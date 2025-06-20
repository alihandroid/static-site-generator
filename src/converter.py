from blocks import BlockType, block_to_block_type, markdown_to_blocks
from htmlnode import LeafNode, ParentNode, text_node_to_html_node
from splitnodes import text_to_textnodes
from textnode import TextNode, TextType


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(text_node) for text_node in text_nodes]


def text_to_list_items(text):
    child_nodes = []
    for line in text.split("\n"):
        for i in range(len(line)):
            if line[i] == " ":
                break
        inner = text_to_children(line[i:])
        child_nodes.append(ParentNode("li", inner))
    return child_nodes


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown.strip())
    nodes = []

    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                inner = text_to_children(block.replace("\n", " "))
                new_node = ParentNode(
                    "p",
                    inner,
                )
            case BlockType.HEADING:
                count = 0
                while block[count] == "#":
                    count += 1
                new_node = LeafNode(f"h{count}", block)
            case BlockType.CODE:
                text_node = TextNode(block[4:-3], TextType.TEXT)
                inner = text_node_to_html_node(text_node)
                code = ParentNode(
                    "code",
                    [inner],
                )
                new_node = ParentNode(
                    "pre",
                    [code],
                )
            case BlockType.QUOTE:
                inner = text_to_children(block.replace(">", ""))
                new_node = LeafNode("blockquote", inner)
            case BlockType.UNORDERED_LIST:
                child_nodes = text_to_list_items(block)
                new_node = ParentNode("ul", child_nodes)
            case BlockType.ORDERED_LIST:
                child_nodes = text_to_list_items(block)
                new_node = ParentNode("ol", child_nodes)
        nodes.append(new_node)
    return ParentNode("div", nodes)

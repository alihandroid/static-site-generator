from textnode import TextNode, TextType
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if node.text is not None:
            parts = node.text.split(delimiter)
            if len(parts) % 2 == 0:
                raise Exception(f"Unmatched delimiter {delimiter}")
            toggle = True
            for part in parts:
                toggle = not toggle
                new_node = None
                if not toggle:
                    new_node = TextNode(part, TextType.TEXT)
                else:
                    new_node = TextNode(part, text_type)

                new_nodes.append(new_node)
    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

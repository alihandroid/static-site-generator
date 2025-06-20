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


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if node.text is not None:
            images = extract_markdown_images(node.text)
            after = node.text
            for image in images:
                parts = after.split(f"![{image[0]}]({image[1]})", 1)
                before = parts[0]
                after = parts[1]
                new_nodes.append(TextNode(before, TextType.TEXT))
                if len(image[0]) > 0:
                    new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            if len(after) > 0:
                new_nodes.append(TextNode(after, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if node.text is not None:
            links = extract_markdown_links(node.text)
            after = node.text
            for link in links:
                parts = after.split(f"[{link[0]}]({link[1]})", 1)
                before = parts[0]
                after = parts[1]
                new_nodes.append(TextNode(before, TextType.TEXT))
                if len(link[0]) > 0:
                    new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            if len(after) > 0:
                new_nodes.append(TextNode(after, TextType.TEXT))
    return new_nodes


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

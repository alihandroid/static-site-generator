import unittest

from htmlnode import text_node_to_html_node
from splitnodes import (
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_delimiter,
)
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_different_text(self):
        node1 = TextNode("Text node", TextType.BOLD)
        node2 = TextNode("Text different", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_different_types(self):
        node1 = TextNode("Text node", TextType.BOLD)
        node2 = TextNode("Text node", TextType.CODE)
        self.assertNotEqual(node1, node2)

    def test_same_url(self):
        node1 = TextNode("Text", TextType.LINK, "test_url")
        node2 = TextNode("Text", TextType.LINK, "test_url")
        self.assertEqual(node1, node2)

    def test_different_url(self):
        node1 = TextNode("Text", TextType.LINK, "test_url1")
        node2 = TextNode("Text", TextType.LINK, "test_url2")
        self.assertNotEqual(node1, node2)

    def test_link_without_url(self):
        node1 = TextNode("Text", TextType.LINK)
        node2 = TextNode("Text", TextType.LINK, "test_url")
        self.assertNotEqual(node1, node2)


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)


class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)


class TestExtractMarkdownLinks(unittest.TestCase):
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("link", "https://i.imgur.com/zjjcJKZ.png")], matches)


if __name__ == "__main__":
    unittest.main()

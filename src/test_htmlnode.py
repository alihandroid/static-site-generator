import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_none_props(self):
        node = HTMLNode(props=None)
        self.assertEqual(node.props_to_html(), "")

    def test_no_props(self):
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), "")

    def test_single_prop(self):
        node = HTMLNode(
            props={
                "href": "https://www.google.com",
            }
        )
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

    def test_multiple_props(self):
        node = HTMLNode(
            props={
                "href": "https://www.google.com",
                "target": "_blank",
            }
        )
        self.assertEqual(
            node.props_to_html(), ' href="https://www.google.com" target="_blank"'
        )


if __name__ == "__main__":
    unittest.main()

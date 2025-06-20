import os
from blocks import BlockType, block_to_block_type
from converter import markdown_to_html_node


def extract_title(markdown):
    for block in markdown.split("\n\n"):
        if block_to_block_type(block) == BlockType.HEADING and block.startswith("# "):
            return block[2:]
    return False


def generate_page(from_path, template_path, dest_path):
    with open(from_path) as f:
        markdown = f.read()

    html_node = markdown_to_html_node(markdown)
    title = extract_title(markdown)

    with open(template_path) as f:
        template = f.read()

    output = template.replace("{{ Title }}", title).replace(
        "{{ Content }}", html_node.to_html()
    )

    os.makedirs(os.path.split(dest_path)[0], exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(output)

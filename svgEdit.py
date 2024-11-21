import xml.etree.ElementTree as ET

def update_svg_ids(svg_path, output_path):
    tree = ET.parse(svg_path)
    root = tree.getroot()

    namespaces = {
        "svg": "http://www.w3.org/2000/svg",
        "inkscape": "http://www.inkscape.org/namespaces/inkscape",
    }

    for g in root.findall(".//svg:g", namespaces):
        label = g.attrib.get(f"{{{namespaces['inkscape']}}}label")
        if label and label.startswith("lesson"):
            g.attrib["id"] = label

    tree.write(output_path, encoding="utf-8", xml_declaration=True)

input_svg = "map_143.svg"
output_svg = "map_143_id.svg"

update_svg_ids(input_svg, output_svg)
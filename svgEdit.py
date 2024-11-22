import re

input_svg = "map_143.svg"
output_svg = "map_143_id.svg"

def update_ids(svg_content):
    pattern = r'(<g[^>]*?inkscape:label="(lesson\d+)"[^>]*?id=")([^"]+)"'
    
    def replacer(match):
        prefix, label, current_id = match.groups()
        return f'{prefix}{label}"'
    
    updated_content = re.sub(pattern, replacer, svg_content)
    return updated_content

with open(input_svg, "r", encoding="utf-8") as file:
    svg_content = file.read()

updated_content = update_ids(svg_content)

with open(output_svg, "w", encoding="utf-8") as file:
    file.write(updated_content)

print(f"SVG IDs updated successfully. Output saved to '{output_svg}'.")



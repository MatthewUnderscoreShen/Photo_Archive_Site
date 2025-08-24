# python script to generate an html file for the gallery
import os
import sys

# start of the html file
html_head = """<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" type="text/css" href="gallery_style.css">
    <script src="toggleGroup.js"></script>
    <title>Photo Gallery</title>
</head>
<body>
    <h1>Photo Gallery</h1>
"""

# end of html file
html_tail = """</body>
</html>
"""

def generate_image_html():
    # generate buttons
    html_buttons = "\t<div class=\"buttons\">\n"
    for year in os.listdir("images"):
        html_buttons += f"\t\t<button id=\"btn-{year}\" onclick=\"toggleGroup('{year}', this)\">{year}</button>\n"
    html_buttons += "\t</div>\n"

    # create one grid element for every image. Currently not separated by year
    html_images = ""
    for year in os.listdir("images"):
        html_images += f"""\t<div id=\"{year}\" class=\"image-year\">
        <h2>{year}</h2>
        <div class="grid">\n"""
        for file in os.listdir(os.path.join("images", year)):
            image_path_tail = year + "/" + file # ex: 2023/DSC##.JPG
            if not os.path.isfile(os.path.join("images", year, file)):
                continue
            html_images += f"\t\t\t<a href=\"images/{image_path_tail}\"><img src=\"thumbnails/{image_path_tail}\" alt=\"picture\"></a>\n"
        html_images += "\t\t</div>\n\t</div>\n"

    html_full = html_head + html_buttons + html_images + html_tail
    with open("index_test.html", "w") as f:
        f.write(html_full)

if __name__ == "__main__":
    generate_image_html()
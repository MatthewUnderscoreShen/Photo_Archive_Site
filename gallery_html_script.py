# python script to generate an html file for the gallery
import os
import sys

file_desc = os.open("index_test.html", os.O_CREAT | os.O_TRUNC | os.O_WRONLY)

# start of the html file
html_head = """<!DOCTYPE html>
<html>
<head>
    <title>a carolina reaper</title>
    <style>
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 15px;
        }

        .grid a {
            display: block;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
            transition: transform 0.3s ease;
        }

        .grid a:hover {
            transform: scale(1.25);
        }

        .grid img {
            width: 100%;
            height: auto;
            display: block;
            object-fit: cover;
        }
    </style>
</head>
<body>
    <h1>dipped in</h1>
    <p>mama liz's chili oil</p>
    <div class="grid">
"""

# end of html file
html_tail = """</div>
</body>
</html>
"""

def generate_image_html():
    # create one grid element for every image. Currently not separated by year
    html_images = ""
    for year in os.listdir("images"):
        for file in os.listdir(os.path.join("images", year)):
            image_path_tail = year + "/" + file # ex: 2023/DSC##.JPG
            if not os.path.isfile(os.path.join("images", year, file)):
                continue
            html_images += f"\t\t<a href=\"images/{image_path_tail}\"><img src=\"thumbnails/{image_path_tail}\" alt=\"picture\"></a>\n"
    return html_images

if __name__ == "__main__":
    file_desc = os.open("index_test.html", os.O_CREAT | os.O_TRUNC | os.O_RDWR)
    print(html_head + generate_image_html() + html_tail)
    html_full = html_head + generate_image_html() + html_tail
    os.write(file_desc, html_full.encode("utf-8"))
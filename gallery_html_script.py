# python script to generate an html file for the gallery
import os
import sys

# start of the html file
html_head = """<!DOCTYPE html>
<html>
<head>
    <title>a carolina reaper</title>
    <style>
        .buttons button {
            color: black;
            background-color:  #e7e7e7;
            font-size: 24px;
            border-radius: 8px;
            transition: background 0.1s
        }
        .buttons button.active {
            color: white;
            background-color: #555555;
        }
        .image-year {
            display: none;
        }
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
"""

# end of html file
html_tail = """\t<script>
        function toggleGroup(id, button) {
            const group = document.getElementById(id);
            if (group.style.display === "none" || group.style.display === "") {
                group.style.display = "block";
                button.classList.add("active");
            } else {
                group.style.display = "none";
                button.classList.remove("active");
            }
        }
    </script>
</body>
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
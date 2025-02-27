import os

# Define the path to the nested directory with HTML files
folder_path = os.path.join("Indic-Trans-2-Hindi", "Indic-Trans-2-Hindi")
html_files = [f for f in os.listdir(folder_path) if f.endswith('.html')]
html_files.sort()  # Optional: sort files alphabetically

# Begin constructing the index.html content
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Indic Translations - Hindi</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 20px; }
    h1 { color: #333; }
    ul { list-style: none; padding: 0; }
    li { margin: 5px 0; }
    a { text-decoration: none; color: #0366d6; }
    a:hover { text-decoration: underline; }
  </style>
</head>
<body>
  <h1>Indic Translations - Hindi</h1>
  <ul>
"""

# Add a list item for each HTML file
for file in html_files:
    relative_path = os.path.join("Indic-Trans-2-Hindi", "Indic-Trans-2-Hindi", file)
    html_content += f'    <li><a href="{relative_path}">{file}</a></li>\n'

# Close the HTML tags
html_content += """  </ul>
</body>
</html>
"""

# Write the content to index.html at the repository root
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

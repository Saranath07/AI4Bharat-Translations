import os

# Define the paths for both directories
indic_trans_dir = os.path.join("Indic-Trans-2-Hindi", "Indic-Trans-2-Hindi")
llama_dir = os.path.join("indic-trans-2-llama-405-output")

# Retrieve all HTML files from both directories and sort them alphabetically
indic_trans_files = sorted([f for f in os.listdir(indic_trans_dir) if f.endswith('.html')])
llama_files = sorted([f for f in os.listdir(llama_dir) if f.endswith('.html')])

# Begin constructing the index.html content
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Indic Translations - Files Index</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 20px; }
    h1 { color: #333; }
    h2 { color: #555; }
    ul { list-style: none; padding: 0; }
    li { margin: 5px 0; }
    a { text-decoration: none; color: #0366d6; }
    a:hover { text-decoration: underline; }
  </style>
</head>
<body>
  <h1>Files Index</h1>
"""

# Section for Indic-Trans-2-Hindi files
html_content += "  <h2>Indic-Trans-2-Hindi - Translation 1</h2>\n  <ul>\n"
for file in indic_trans_files:
    relative_path = os.path.join("Indic-Trans-2-Hindi", "Indic-Trans-2-Hindi", file)
    html_content += f'    <li><a href="{relative_path}">{file}</a></li>\n'
html_content += "  </ul>\n"

# Section for indic-trans-2-llama-405-output files
html_content += "  <h2>indic-trans-2-llama-405-output - Translation 2</h2>\n  <ul>\n"
for file in llama_files:
    relative_path = os.path.join("indic-trans-2-llama-405-output", "indic-trans-2-llama-405-output", file)
    html_content += f'    <li><a href="{relative_path}">{file}</a></li>\n'
html_content += "  </ul>\n"

# Close HTML tags
html_content += """</body>
</html>
"""

# Write the content to index.html at the repository root
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("index.html has been created with links to all HTML files from both directories.")

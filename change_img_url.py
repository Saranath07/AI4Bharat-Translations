import os
from bs4 import BeautifulSoup

# Define the directory paths.
# These assume the script is run from the parent directory that contains both folders.
hindi_dir = os.path.join("Indic-Trans-2-Hindi", "Indic-Trans-2-Hindi")
llama_dir = os.path.join("indic-trans-2-llama-405-output", "indic-trans-llama-405-output")

# List all files in the llama output directory.
for filename in os.listdir(llama_dir):
    llama_file_path = os.path.join(llama_dir, filename)
    hindi_file_path = os.path.join(hindi_dir, filename)

    # Only process if the matching file exists in the Hindi folder.
    if os.path.exists(hindi_file_path):
        print(f"Processing file: {filename}")

        # Read the contents of both files.
        with open(llama_file_path, "r", encoding="utf-8") as f:
            llama_html = f.read()
        with open(hindi_file_path, "r", encoding="utf-8") as f:
            hindi_html = f.read()

        # Parse HTML content with BeautifulSoup.
        soup_llama = BeautifulSoup(llama_html, "html.parser")
        soup_hindi = BeautifulSoup(hindi_html, "html.parser")

        # Find all image tags in both files.
        imgs_llama = soup_llama.find_all("img")
        imgs_hindi = soup_hindi.find_all("img")

        # Check if the number of image tags is the same.
        if len(imgs_llama) == len(imgs_hindi):
            # For each image, replace the src attribute in the Hindi version.
            for img_llama, img_hindi in zip(imgs_llama, imgs_hindi):
                # Update the src attribute.
                new_src = img_llama.get("src")
                img_hindi["src"] = new_src
            # Write the updated Hindi HTML back to file.
            with open(hindi_file_path, "w", encoding="utf-8") as f:
                f.write(str(soup_hindi))
            print(f"Updated image URLs in: {filename}")
        else:
            print(f"Warning: The number of image tags in {filename} differs between directories. Skipping file.")
    else:
        print(f"File {filename} not found in {hindi_dir}. Skipping.")

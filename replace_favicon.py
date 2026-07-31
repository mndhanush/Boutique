import os
import glob

directory = r"d:\GrowwPark projects\Bloom"
html_files = glob.glob(os.path.join(directory, "*.html"))

# We also should handle cases where the old string might have slight variations (though they were identical in my grep search earlier)
old_string = '<link rel="icon" type="image/svg+xml" href="assets/favicon.svg">'
new_string = '<link rel="icon" type="image/jpeg" href="assets/images/favicon1.jpg">'

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if old_string in content:
        content = content.replace(old_string, new_string)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {os.path.basename(file_path)}")

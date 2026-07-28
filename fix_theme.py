import os
import glob
import re

def main():
    directory = r"d:\GrowwPark projects\Bloom"
    html_files = glob.glob(os.path.join(directory, "*.html"))
    
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Change primary to black and secondary to pink
        content = content.replace("primary: '#EC4899'", "primary: '#000000'")
        content = content.replace("secondary: '#FFFFFF'", "secondary: '#EC4899'")
        
        # Force Light Mode variables to match Dark Mode variables for a persistent pink/black theme
        # Also handle any trailing spaces just in case
        
        # Actually, let's just use replace to be safe. We know exactly how it is formatted in index.html.
        content = content.replace("--bg-color: #FFFFFF;", "--bg-color: #050505;")
        content = content.replace("--bg-alt: #F9F6F0;", "--bg-alt: #0A0A0A;")
        content = content.replace("--card-bg: #FFFFFF;", "--card-bg: #111111;")
        content = content.replace("--text-main: #333333;", "--text-main: #CCCCCC;")
        content = content.replace("--text-heading: #000000;", "--text-heading: #FFFFFF;")
        content = content.replace("--navbar-bg: #FFFFFF;", "--navbar-bg: #000000;")
        content = content.replace("--border-color: #E5E5E5;", "--border-color: #333333;")
        
        # Change gold gradient to pink gradient
        content = content.replace(
            "background: linear-gradient(to right, #BF953F, #FCF6BA, #B38728, #FBF5B7, #AA771C);",
            "background: linear-gradient(to right, #EC4899, #F9A8D4, #DB2777, #FBCFE8, #BE185D);"
        )

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
    print(f"Fixed theme in {len(html_files)} HTML files.")

if __name__ == '__main__':
    main()

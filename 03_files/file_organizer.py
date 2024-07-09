# Simple file organizer by extension
import os
import shutil

EXTENSION_MAP = {
    "images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "documents": [".pdf", ".docx", ".txt", ".md"],
    "videos": [".mp4", ".mov", ".avi"],
    "code": [".py", ".js", ".html", ".css"],
}

def organize(directory):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            ext = os.path.splitext(filename)[1].lower()
            for folder, exts in EXTENSION_MAP.items():
                if ext in exts:
                    dest = os.path.join(directory, folder)
                    os.makedirs(dest, exist_ok=True)
                    shutil.move(filepath, os.path.join(dest, filename))
                    print(f"Moved {filename} -> {folder}/")
                    break

if __name__ == "__main__":
    organize(".")

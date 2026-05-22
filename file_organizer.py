import os
import shutil

EXTENSION_MAP = {
    "Images": {"jpg", "jpeg", "png", "gif", "bmp", "tiff", "svg"},
    "PDFs": {"pdf"},
    "Videos": {"mp4", "mkv", "mov", "avi", "flv", "wmv"},
}


def organize_files(target_dir):
    if not os.path.isdir(target_dir):
        print("Directory not found.")
        return
    for entry in os.listdir(target_dir):
        source_path = os.path.join(target_dir, entry)
        if not os.path.isfile(source_path):
            continue
        extension = os.path.splitext(entry)[1].lower().lstrip(".")
        for folder, extensions in EXTENSION_MAP.items():
            if extension in extensions:
                destination_dir = os.path.join(target_dir, folder)
                os.makedirs(destination_dir, exist_ok=True)
                destination_path = os.path.join(destination_dir, entry)
                shutil.move(source_path, destination_path)
                break


def main():
    directory = input("Enter directory path to organize: ").strip()
    organize_files(directory)


if __name__ == "__main__":
    main()

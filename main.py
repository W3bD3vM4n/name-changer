import sys
from pathlib import Path

def get_nonempty_input(prompt: str) -> str:
    while True:
        string_fill = input(prompt).strip()
        if not string_fill:
            print("Please enter a non-empty string")
        else:
            return string_fill

path = Path(get_nonempty_input("Enter the path to the file/folder: "))
if not (path.exists() and path.is_dir()):
    print("Invalid folder path")
    sys.exit(1)
    
old_sub = get_nonempty_input("Text to replace: ")
new_sub = input("New text: ")

files = [f for f in path.iterdir() if f.is_file()]

renamed = []
for file in files:
    new_name = file.name.replace(old_sub, new_sub)
    if new_name == file.name:
        continue
    target = file.with_name(new_name)
    file.rename(target)
    renamed.append((file.name, new_name))

print(f"\nTotal files scanned: {len(files)}")
print(f"Files renamed: {len(renamed)}\n")

print("First five renames:")
for old, new in renamed[:5]:
    print(f" · {old} -> {new}")
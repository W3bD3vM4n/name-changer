from pathlib import Path
import sys

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

print("\nChoose rename operation:")
print(" 1) Replace text")
print(" 2) Prepend text")
print(" 3) Append text")
option = get_nonempty_input("Enter 1, 2, or 3: ")
if option not in ("1", "2", "3"):
    print("Invalid choice")
    sys.exit(1)
 
if option == "1":
    old_sub = get_nonempty_input("Text to replace: ")
    new_sub = input("New text: ")
else:
    text = get_nonempty_input("Text to add: ")

files = [f for f in path.iterdir() if f.is_file()]

renamed = []
for file in files:
    if option == "1":
        new_name = file.name.replace(old_sub, new_sub)
    elif option == "2":
        new_name = text + file.name
    else:
        new_name = f"{file.stem}{text}{file.suffix}"
    
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
from pathlib import Path

file_names = []
first_five = []
counter = 0

def get_nonempty_input(prompt: str) -> str:
    while True:
        string_fill = input(prompt).strip()
        if not string_fill:
            print("Please enter a non-empty string")
        else:
            return string_fill

path_string = get_nonempty_input("Enter the path to the file/folder: ")
path = Path(path_string)

if path.exists() and path.is_dir():
    for file in path.iterdir():
        if file.is_file():
            file_names.append(file.name)
            if counter < 5:
                first_five.append(file.name)
            counter += 1
    print(f"\nFiles found: {len(file_names)}")
    print(f"\nFirst five samples:")
    for file in first_five:
        print(file)
else:
    print("Invalid folder path")
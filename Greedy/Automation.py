import os

def create_py_files(directory, file_names):
    for name in file_names:
        # Create the full file path with .py extension
        file_path = os.path.join(directory, f"{name}.py")
        
        # Create the file
        with open(file_path, 'w') as file:
            file.write("# This is the file: " + name + "\n")  # Optionally add some content

# Example usage
if __name__ == "__main__":
    current_directory = os.getcwd()  # Get the current working directory
    print(current_directory)
    files_to_create = ["605. Can Place Flowers", "680. Valid Palindrome II", "860. Lemonade Change", "976. Largest Perimeter Triangle", "1005. Maximize Sum Of Array After K Negations", "1013. Partition Array Into Three Parts With Equal Sum", "1403. Minimum Subsequence in Non-Increasing Order"]  # List of file names (without .py extension)

    create_py_files(current_directory, files_to_create)
    print(f"Created files: {[f'{name}.py' for name in files_to_create]}")

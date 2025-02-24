import os
import shutil

def main():
    # Define the base directory where your images are stored
    base_dir = input('Enter path to your images:')
    # Define target directory where you want to create new directories
    target_dir = input('Enter path to target directory:')

    # List of directories to create
    directories = ['Adele', 'Alice', 'Bob', 'Messi', 'User']

    # Create target directories if they don't exist
    for directory in directories:
        os.makedirs(os.path.join(target_dir, directory), exist_ok=True)

    # Define the distribution pattern
    pattern = ['Adele', 'User', 'Alice', 'User', 'Bob', 'User', 'Messi', 'User']

    # Function to get the directory based on the image index
    def get_directory(index):
        return pattern[index % len(pattern)]

    # Move files according to the specified logic
    for i in range(100):
        file_name = f"{i:03}.jpg"
        src_path = os.path.join(base_dir, file_name)
        dest_path = os.path.join(target_dir, get_directory(i), file_name)
        shutil.move(src_path, dest_path)
        print(f"Moved {file_name} to {get_directory(i)}")

    print("Images have been organized successfully.")

if __name__ == "__main__":
    main()

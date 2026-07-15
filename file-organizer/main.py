import os

from organizer import organize


def main():
    print("=" * 40)
    print("      FILE ORGANIZER")
    print("=" * 40)

    folder_path = input("Enter the folder path to organize: ").strip()

    if not os.path.exists(folder_path):
        print("Error: Folder does not exist.")
        return

    if not os.path.isdir(folder_path):
        print("Error: The path is not a folder.")
        return

    organize(folder_path)

    print("\nOrganization complete!")


if __name__ == "__main__":
    main()
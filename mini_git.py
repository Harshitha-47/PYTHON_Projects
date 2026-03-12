# Mini Git Version Control System using Python
# This program simulates a simplified version of Git.
# It allows users to add files, create commits, and view commit history.
# Each commit stores a snapshot of the file content with a message.
# This project demonstrates file handling and version tracking concepts.
import os
import shutil
import time

repo_folder = "mini_repo"
commit_folder = os.path.join(repo_folder, "commits")

# --------------------------
# Initialize Repository
# --------------------------
def init_repo():
    if not os.path.exists(repo_folder):
        os.makedirs(commit_folder)
        print("Repository initialized.")
    else:
        print("Repository already exists.")


# --------------------------
# Add File
# --------------------------
def add_file():
    filename = input("Enter file name to add: ")

    if os.path.exists(filename):
        shutil.copy(filename, repo_folder)
        print("File added to repository.")
    else:
        print("File not found.")


# --------------------------
# Commit Changes
# --------------------------
def commit():
    message = input("Enter commit message: ")

    timestamp = str(int(time.time()))
    new_commit = os.path.join(commit_folder, timestamp)

    os.makedirs(new_commit)

    for file in os.listdir(repo_folder):
        path = os.path.join(repo_folder, file)

        if os.path.isfile(path):
            shutil.copy(path, new_commit)

    with open(os.path.join(new_commit, "message.txt"), "w") as f:
        f.write(message)

    print("Commit created.")


# --------------------------
# Show History
# --------------------------
def history():

    if not os.path.exists(commit_folder):
        print("No commits yet.")
        return

    commits = os.listdir(commit_folder)

    if not commits:
        print("No commits found.")
        return

    print("\nCommit History\n")

    for commit in commits:
        msg_file = os.path.join(commit_folder, commit, "message.txt")

        if os.path.exists(msg_file):
            with open(msg_file, "r") as f:
                message = f.read()

            print("Commit ID:", commit)
            print("Message:", message)
            print("-"*30)


# --------------------------
# Main Menu
# --------------------------
def main():

    while True:

        print("\n===== Mini Git Menu =====")
        print("1. Initialize Repository")
        print("2. Add File")
        print("3. Commit Changes")
        print("4. View History")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            init_repo()

        elif choice == "2":
            add_file()

        elif choice == "3":
            commit()

        elif choice == "4":
            history()

        elif choice == "5":
            print("Exiting Mini Git")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
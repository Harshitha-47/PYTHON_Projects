class File:
    def __init__(self, name, size=1, permission="rw"):
        self.name = name
        self.size = size
        self.permission = permission


class Directory:
    def __init__(self, name):
        self.name = name
        self.files = {}
        self.subdirs = {}
        self.parent = None


class FileSystem:
    def __init__(self, quota=100):
        self.root = Directory("root")
        self.current = self.root
        self.quota = quota
        self.used = 0

    def mkdir(self, name):
        if name in self.current.subdirs:
            print("Directory already exists")
            return
        new_dir = Directory(name)
        new_dir.parent = self.current
        self.current.subdirs[name] = new_dir
        print("Directory created")

    def touch(self, name, size=1):
        if self.used + size > self.quota:
            print("Disk quota exceeded")
            return

        if name in self.current.files:
            print("File already exists")
            return

        self.current.files[name] = File(name, size)
        self.used += size
        print("File created")

    def ls(self):
        for d in self.current.subdirs:
            print("[DIR]", d)
        for f in self.current.files:
            print("[FILE]", f)

    def cd(self, name):
        if name == "..":
            if self.current.parent:
                self.current = self.current.parent
        elif name in self.current.subdirs:
            self.current = self.current.subdirs[name]
        else:
            print("Directory not found")

    def rm(self, name):
        if name in self.current.files:
            file = self.current.files[name]
            if "w" not in file.permission:
                print("Permission denied")
                return
            self.used -= file.size
            del self.current.files[name]
            print("File removed")

        elif name in self.current.subdirs:
            del self.current.subdirs[name]
            print("Directory removed")
        else:
            print("File/Directory not found")


fs = FileSystem()

while True:
    command = input(">> ").split()

    if command[0] == "mkdir":
        fs.mkdir(command[1])

    elif command[0] == "touch":
        fs.touch(command[1])

    elif command[0] == "ls":
        fs.ls()

    elif command[0] == "cd":
        fs.cd(command[1])

    elif command[0] == "rm":
        fs.rm(command[1])

    elif command[0] == "exit":
        break

    else:
        print("Invalid command")
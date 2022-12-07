from src.common import Solution


def build_filesystem(input):
    root = Directory("/", None)
    cwd = root
    for cmd_and_output in [cmd.splitlines() for cmd in input.split('$ ') if cmd != '']:
        command, output = cmd_and_output[0], cmd_and_output[1:]
        if command == 'cd /':
            cwd = root
        elif command == 'cd ..':
            cwd = cwd.parent
        elif command.startswith('cd'):
            arg = command.split(' ')[1]
            cwd = cwd.mkdir(arg)
        else:
            for arg1, arg2 in [o.split(' ') for o in output]:
                if arg1 == "dir":
                    cwd.mkdir(arg2)
                else:
                    cwd.touch(arg2, int(arg1))
    return root


class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.directories = {}
        self.files = {}

    def mkdir(self, directory):
        self.directories[directory] = Directory(directory, self)
        return self.directories[directory]

    def touch(self, name, size):
        self.files[name] = size

    def recursive_directory_search(self):
        directories = list(self.directories.values())
        for d in self.directories.values():
            directories += d.recursive_directory_search()
        return directories

    def du(self):
        return sum(self.files.values()) + sum([d.du() for d in self.directories.values()])

    def __str__(self):
        return self.name


class Day07(Solution):

    def part1(self, input: str) -> int:
        filesystem = build_filesystem(input)
        return sum([
            size for size in
            [directory.du() for directory in filesystem.recursive_directory_search()]
            if size <= 100000
        ])

    def part2(self, input: str) -> int:
        filesystem = build_filesystem(input)
        unused_disk_space = 70000000 - filesystem.du()
        required_to_free = 30000000 - unused_disk_space
        return min([
            size for size in
            [directory.du() for directory in filesystem.recursive_directory_search()] if
            size >= required_to_free
        ])

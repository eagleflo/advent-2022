#!/usr/bin/env python3
from enum import Enum


class FileType(Enum):
    DIR = 1
    FILE = 2


class Node:
    def __init__(self, name: str, size: int, file_type: FileType, parent: "Node"):
        self.name = name
        self.size = size
        self.file_type = file_type
        self.parent = parent
        self.files = {}

    # This is a bit cheesy...
    def __getitem__(self, key):
        return self.files[key]

    def link(self, node: "Node"):
        self.files[node.name] = node

    def depth(self) -> int:
        if not self.parent:
            return 0
        else:
            return 1 + self.parent.depth()

    def total_size(self) -> int:
        if self.file_type == FileType.FILE:
            return self.size
        else:
            size = 0
            for file in self.files.values():
                size += file.total_size()
            return size

    def __str__(self) -> str:
        if self.file_type == FileType.FILE:
            return f"- {self.name} (file, size={self.size})\n"
        else:
            result = f"- {self.name} (dir)\n"
            for file in self.files.values():
                indent = 2 * file.depth()
                result += f"{' ' * indent}{file}"
            return result


root_node = Node("/", 0, FileType.DIR, None)
cwd = root_node

terminal_output = open("07.txt").readlines()
for line in terminal_output:
    line = line.strip()
    if line.startswith("$"):
        if line.startswith("$ cd"):
            dir = line.replace("$ cd ", "")
            match dir:
                case "/":
                    cwd = root_node
                case "..":
                    cwd = cwd.parent
                case _:
                    if dir in cwd.files:
                        cwd = cwd.files[dir]
    else:
        # File
        size_or_dir, name = line.split(" ")
        if size_or_dir == "dir":
            node = Node(name, 0, FileType.DIR, cwd)
        else:
            node = Node(name, int(size_or_dir), FileType.FILE, cwd)
        cwd.link(node)

# print(root_node)
# print(root_node["a"]["e"].total_size())
# print(root_node["a"].total_size())
# print(root_node["d"].total_size())
# print(root_node.total_size())


def find_dirs_under_100k(node, nodes):
    if node.total_size() <= 100_000 and node.file_type == FileType.DIR:
        nodes.append(node)
    for file in node.files.values():
        find_dirs_under_100k(file, nodes)


nodes = []
find_dirs_under_100k(root_node, nodes)
print(sum(n.total_size() for n in nodes))

disk_space = 70_000_000
target_space = 30_000_000
unused_space = disk_space - root_node.total_size()
target_to_free = target_space - unused_space


def find_smallest_dir_to_delete(node, nodes):
    if node.total_size() > target_to_free:
        nodes.append(node.total_size())
    for file in node.files.values():
        find_smallest_dir_to_delete(file, nodes)


nodes = []
find_smallest_dir_to_delete(root_node, nodes)
nodes.sort()
print(nodes[0])

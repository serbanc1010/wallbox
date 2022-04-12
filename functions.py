import os
from pwd import getpwuid, getpwnam

SIZE = 14680064 #given file size

def find_repeated_number(v1, v2):
    """A function that given 2 vectors of integers finds the first repeated number"""
    vector = v1 + v2
    vector_set = set()
    for val in vector:
        if val in vector_set:
            return val
        else:
            vector_set.add(val)

    return None

def find_file(path):
    """
    A function that given a path of the file system finds the first file that meets the following
    requirements:
      a. The file owner is admin
      b. The file is executable
      c. The file has a size lower than 14*2^20
    """
    if os.path.isdir(path):
        root, dirs, files = next(os.walk(path))
        for file in sorted(files, key =  lambda x: os.stat(os.path.join(path, x)).st_size): #get list of files in given path, sorted by size, lowest first
            full_path = os.path.join(path, file)
            if os.access(full_path, os.X_OK) and os.path.getsize(full_path) < SIZE and getpwuid(os.stat(full_path).st_uid).pw_name == 'admin':
                return full_path

    return None

def find_swaps(seq):
    """
    A function that given a sequence finds the minimum quantity of permutations
    so that the sequence ends interspersed
    """
    swap_cnt = 0
    i = 1

    while i < len(seq) - 1:
        if seq[i] == seq[i-1]:
            opposite = int(not seq[i])
            idx = seq.index(opposite, i+1)
            print(f"swap index {i} -> {idx}")
            seq[i], seq[idx] = seq[idx], seq[i]
            swap_cnt += 1
            print(seq)
            i += 1
        else:
            i += 1
            continue

    return swap_cnt
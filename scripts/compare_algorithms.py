#
#
#   Compare speed of multiple hash algorithms
#
#

import os
import hashlib
import argparse

import oshash

from pprint import pprint
from timeit import timeit

try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None

try:
    import seaborn  # noqa
    seaborn.set()
except ImportError:
    pass


BLOCK_SIZE = 65536  # 64K: 64 * 1024


def hash_file(file_path, hash_func):
    hasher = hash_func()

    with open(file_path, "rb") as f:
        block_bytes = f.read(BLOCK_SIZE)

        while len(block_bytes) > 0:
            hasher.update(block_bytes)
            block_bytes = f.read(BLOCK_SIZE)

    return hasher.hexdigest()


def main():
    parser = argparse.ArgumentParser(description="OpenSubtitles Hash tool")

    parser.add_argument("file_path", help="File path to test each algorithm")
    parser.add_argument("-n", "--number", type=int, help="How many times to execute each algorithm", default=1)

    args = parser.parse_args()

    file_path = os.path.expanduser(args.file_path)

    algorithm_times = {
        "oshash": timeit(lambda: oshash.oshash(file_path), number=args.number)
    }

    for algorithm_name in hashlib.algorithms_guaranteed:
        if algorithm_name.startswith('shake_'):
                continue

        hash_func = getattr(hashlib, algorithm_name, None)

        algorithm_times[algorithm_name] = timeit(lambda: hash_file(file_path, hash_func), number=args.number)

    pprint(algorithm_times)

    if plt is not None:
        names, times = zip(*sorted(algorithm_times.items(), key=lambda x: x[1]))

        barlist = plt.bar(names, times)

        barlist[names.index("oshash")].set_color("red")  # mark oshash bar

        file_size = os.path.getsize(file_path)
        plt.title("{} ({})".format(file_path, oshash.utils.human_size(file_size)))

        plt.show()


if __name__ == '__main__':
    main()

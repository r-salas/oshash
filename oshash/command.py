#
#
#
#
#

import os
import sys
import argparse

from .api import oshash


def main():
    parser = argparse.ArgumentParser(description="OpenSubtitles Hash tool")

    parser.add_argument("file_path")

    args = parser.parse_args()

    file_path = os.path.expanduser(args.file_path)

    try:
        file_hash = oshash(file_path)
    except (IOError, ValueError) as e:
        sys.exit(e)

    print("OSHash ({}) = {}".format(file_path, file_hash))


if __name__ == '__main__':
    main()

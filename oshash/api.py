#
#
#   API
#
#

import os
import struct

from .utils import human_size


CHUNK_SIZE = 65536  # 64K: 64 * 1024
CHUNK_BYTE_FORMAT = "<q"  # long long little-endian


def to_uint64(value):
    return value & 0xFFFFFFFFFFFFFFFF


def oshash(file_path: str):
    byte_size = struct.calcsize(CHUNK_BYTE_FORMAT)

    file_size = os.path.getsize(file_path)

    min_file_size = CHUNK_SIZE * 2  # head and tail

    if file_size < min_file_size:
        raise ValueError("File size must be at least {}".format(human_size(min_file_size)))

    with open(file_path, "rb") as f:
        file_hash = file_size

        num_chunk_iterations = CHUNK_SIZE // byte_size

        for _ in range(num_chunk_iterations):
            file_bytes = f.read(byte_size)
            [unpacked] = struct.unpack(CHUNK_BYTE_FORMAT, file_bytes)
            file_hash = to_uint64(file_hash + unpacked)  # make sure variable is int64

        f.seek(-CHUNK_SIZE, os.SEEK_END)  # go to tail

        for _ in range(num_chunk_iterations):
            file_bytes = f.read(byte_size)
            [unpacked] = struct.unpack(CHUNK_BYTE_FORMAT, file_bytes)
            file_hash = to_uint64(file_hash + unpacked)

        return format(file_hash, "016x")  # convert to hex and pad with zeros if needed

# oshash
OpenSubtitles Hash implementation.

This algorithm is focused on speed because unlike other algorithms, OSHash doesn't read the whole file.
This makes it a perfect algorithm for hashing large files.

## Installation
The latest stable release can be installed from PyPI:

```console
$ pip install oshash
```

## API usage
Simply import `oshash` and call `oshash` function with your file path.

```py
import oshash

file_hash = oshash.oshash("/path/to/file")
```

## Command usage
You can compute OSHash directly from the terminal.

```console
$ oshash <file_path>
```

For example:
```console
$ oshash /path/to/video.mp4
OSHash (/path/to/video.mp4) = d315edebf53a4af3
```

## How It Works?

In pseudo-code, the hash is computed in the following way:

```
file_buffer = open("/path/to/file/")

head_checksum = checksum(file_buffer.head(64 * 1024))  # 64KB
tail_checksum = checksum(file_buffer.tail(64 * 1024))  # 64KB

file_hash = file_buffer.size + head_checksum + tail_checksum
```

You can read more in [OpenSubtitles.org Wiki](https://trac.opensubtitles.org/projects/opensubtitles/wiki/HashSourceCodes)

## Acknowledgements

Thanks to the [OpenSubtitles.org](https://www.opensubtitles.org) team for this algorithm.

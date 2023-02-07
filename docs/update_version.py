import re
import sys
from pathlib import Path

DOCS_DIRECTORY = Path(__file__).parent / 'source'
VERSION_PATTERN = re.compile('[0-9]{4}\.[0-9]{2}\.[0-9]{2}')


def update_docs_release_version(version: str, directory: Path):
    if not isinstance(directory, Path):
        directory = Path(directory)

    for filename in directory.iterdir():
        if filename.suffix == '.rst':
            with open(filename) as docs_file:
                content = docs_file.read()
            matches = re.findall(VERSION_PATTERN, content)
            if len(matches) > 0:
                content = content.replace(matches[0], version)
                with open(filename, 'w') as docs_file:
                    docs_file.write(content)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        version = sys.argv[1]
    else:
        raise ValueError('missing argument VERSION')
    if len(sys.argv) > 2:
        directory = sys.argv[2]
    else:
        directory = DOCS_DIRECTORY
    update_docs_release_version(version=version, directory=directory)

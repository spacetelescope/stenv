import re
import sys
from pathlib import Path

DOCS_DIRECTORY = Path(__file__).parent / 'source'
VERSION_REGEX_PATTERN = re.compile('[0-9]{4}\.[0-9]{2}\.[0-9]{2}')
VERSION_DUNAMAI_PATTERN = "(?P<base>\d+\.\d+\.\d+)"


def update_docs_release_version(version: str, directory: Path):
    if not isinstance(directory, Path):
        directory = Path(directory)

    existing = set()
    for filename in directory.iterdir():
        if filename.suffix == '.rst':
            with open(filename) as docs_file:
                content = docs_file.read()
            matches = set(re.findall(VERSION_REGEX_PATTERN, content)) - {version}
            if len(matches) > 0:
                existing.update(matches)
                for match in matches:
                    content = content.replace(match, version)
                    with open(filename, 'w') as docs_file:
                        docs_file.write(content)

    if len(existing) > 0:
        print(f'updated version references to {version} (previously {", ".join(existing)})')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        version = sys.argv[1]
    else:
        try:
            from dunamai import Version
        except (ImportError, ModuleNotFoundError):
            raise EnvironmentError('either specify a version as an argument, or install the `dunamai` package to automatically parse a version tag from version control')

        version = Version.from_any_vcs(pattern=VERSION_DUNAMAI_PATTERN).base
        
    if len(sys.argv) > 2:
        directory = sys.argv[2]
    else:
        directory = DOCS_DIRECTORY
    update_docs_release_version(version=version, directory=directory)

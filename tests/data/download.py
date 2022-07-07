import shutil
from pathlib import Path

import pooch

REMOTE_URL = "https://data.science.stsci.edu/redirect/spacetelescope-env-distribution/tests/"
REMOTE_PATHS = [
    ...,
]
LOCAL_DIRECTORY = Path(__file__).parent


def download_data(overwrite: bool = False):
    for remote_path in REMOTE_PATHS:
        local_path = LOCAL_DIRECTORY / Path(remote_path).name
        if overwrite or not local_path.exists():
            print(f'downloading "{remote_path}"')
            filename = pooch.retrieve(REMOTE_URL + remote_path, known_hash=None)
            shutil.move(filename, local_path)

    print("Done downloading files")


if __name__ == "__main__":
    download_data()

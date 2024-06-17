import argparse
import yaml
from pathlib import Path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="mamba_export_pip",
        description="appends the output of `pip freeze` to the end of an existing Mamba YAML exported with `mamba env export`, in the corresponding `pip` section",
        epilog="this script replicates the functionality of https://github.com/mamba-org/mamba/pull/2104, and will be obsolete when it is merged",
    )

    parser.add_argument("mamba_export_filename")
    parser.add_argument("pip_freeze_filename")

    arguments = parser.parse_args()

    mamba_export_filename = Path(arguments.mamba_export_filename)
    pip_freeze_filename = Path(arguments.pip_freeze_filename)

    with open(mamba_export_filename) as mamba_export_file:
        mamba_export = yaml.safe_load(mamba_export_file)

    with open(pip_freeze_filename) as pip_freeze_file:
        pip_freeze = pip_freeze_file.readlines()

    pip_freeze = [
        requirement.strip()
        for requirement in pip_freeze
        if " @ file" not in requirement
    ]

    mamba_export["dependencies"].append({"pip": pip_freeze})

    print(yaml.dump(mamba_export))

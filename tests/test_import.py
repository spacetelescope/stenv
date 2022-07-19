import importlib.metadata
import re
import sys
import yaml
from packaging.version import Version
from pathlib import Path
from typing import Mapping, Dict, Tuple

DEPENDENCY_PATTERN = re.compile(r"([\w\d-]+)\s*((?:[<>=~]=?|\^)\s*[\d\w.]*)?")
MINIMUM_DEPENDENCY_PATTERN = re.compile(r".*>=?\s*([\d\w.]+).*")


def parse_dependency(
        dependency: str,
        dependencies: Dict[str, Tuple[str, str]],
        version_specification_pattern: re.Pattern = DEPENDENCY_PATTERN,
):
    match = re.match(version_specification_pattern, dependency)
    if match is not None:
        groups = match.groups()
        dependencies[groups[0]] = groups[1]


INSTALLED_PACKAGES = {
    distribution.metadata["name"].lower(): distribution.metadata["version"]
    for distribution in importlib.metadata.distributions()
}


def check_package(
        package_name: str, minimum_version: Version = None, verbose: bool = True
) -> bool:
    if package_name in INSTALLED_PACKAGES:
        installed_version = Version(INSTALLED_PACKAGES[package_name])
        if minimum_version is not None:
            if not isinstance(minimum_version, Version):
                minimum_version = Version(str(minimum_version))
            if installed_version < minimum_version:
                print(
                    f'"{package_name}" is installed ({installed_version}) but out of date ({minimum_version} required)',
                    file=sys.stderr,
                )
                return False
        if verbose:
            print(f'"{package_name}" is installed ({installed_version})')
    else:
        print(f'"{package_name}" is not installed', file=sys.stderr)
        return False
    return True


def test_import():
    with open(Path(__file__).parent / "spacetelescope-env-latest.yml") as environment_file:
        environment = yaml.safe_load(environment_file)

    dependencies = {}

    for dependency in environment["dependencies"]:
        if isinstance(dependency, str):
            if "python" not in dependency and dependency not in "pip":
                parse_dependency(dependency, dependencies)
        elif isinstance(dependency, Mapping):
            dependency = list(dependency.items())[0]
            if dependency[0] == "pip":
                [
                    parse_dependency(dependency=pip_dependency, dependencies=dependencies)
                    for pip_dependency in dependency[1]
                ]

    errors = []
    for package_name, specification in dependencies.items():
        if specification is not None:
            min_version = re.match(MINIMUM_DEPENDENCY_PATTERN, specification)
            if min_version is not None:
                min_version = Version(min_version.groups()[0])
        else:
            min_version = None
        if not check_package(package_name, minimum_version=min_version):
            errors.append(package_name)
    assert len(errors) == 0, f"You must resolve {sum(errors)} errors (above) before running the tutorials."

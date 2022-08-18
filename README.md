# `stenv` - Space Telescope Calibration Pipeline and Analysis Tools

[![build](https://github.com/spacetelescope/stenv/actions/workflows/build.yml/badge.svg)](https://github.com/spacetelescope/stenv/actions/workflows/build.yml)
[![release](https://img.shields.io/github/v/release/spacetelescope/stenv)](https://github.com/spacetelescope/stenv/releases)
[![calver](https://img.shields.io/badge/calver-YYYY.0M.0D-22bfda.svg)](https://calver.org)

This repository builds YAML files that define environments for a `conda` installation. The `stenv-stable.yml`
, `stenv-latest.yml`, and `stenv-dev.yml` files provide minimum definitions for building this environment with stable
pinned versions, latest released versions, and latest Git commits, respectively. Each [release](https://github.com/spacetelescope/stenv/releases) provides frozen environment files (specific version
definitions at a snapshot in time) that are built and tested on each supported platform and Python version using GitHub Actions.

## Tested Platforms

The following platforms have
been [tested with import, unit, and smoke tests](https://github.com/spacetelescope/stenv/actions/workflows/build.yml)
against the latest releases of comprising packages:

- operating systems
    - Linux (GitHub Actions' `ubuntu-latest` image)
    - Mac OS (GitHub Actions' `macos-latest` image)
- Python versions
    - `3.8`
    - `3.9`
    - `3.10`
- version constraints
    - `stable` (manually-pinned stable patch versions)
    - `latest` (latest releases)
    - `dev` (latest commits on main branch)

## Installation

1. Install Miniconda - https://docs.conda.io/en/latest/miniconda.html

2. Retrieve an environment definition file by choosing one of the following methods:
    1. Download one of the general (platform-agnostic) YAML files (`stenv-stable.yml`, `stenv-latest.yml`,
       or `stenv-dev.yml`) from the root of this repository.
       > :warning: `stenv-stable.yml`, `stenv-latest.yml`, and `stenv-dev.yml` define unfrozen environments that **have
       not been built or tested against specific platforms**. To use a frozen environment (with explicit versions) that
       was built and tested on supported platforms, download a file from a specific release (below). :warning:

    2. [Pick a release from the Releases page](https://github.com/spacetelescope/stenv/releases). These releases have
       YAML files in the Assets section for each supported platform and Python version:
       [![release example](docs/release_example.png)](https://github.com/spacetelescope/stenv/releases)

       > Building and testing environments on supported platforms may take several minutes; **if a release was just made
       recently, you may need to wait for
       its [associated workflow job](https://github.com/spacetelescope/stenv/actions/workflows/build.yml) to finish
       before environment files are available**.
       
       You can download a YAML file from the [release page](https://github.com/spacetelescope/stenv/releases), or use `curl`
       with a direct URL:
       ```shell
       curl https://github.com/spacetelescope/stenv/releases/download/2022.08.08/stenv-macOS-py3.9-2022.08.08-latest.yml -o stenv-macOS-py3.9-2022.08.08-latest.yml
       ```

       This example assumes Mac OSX (`macOS`) with Python 3.9 (`py3.9`) and release `2022.08.08` with the `latest`
       constraints.
       
3. Create the environment with `conda env create --file <filename> --name <environment-name>` (the `--name` argument is the
   name of the environment that you create, and the handle that you will use later to activate):
   ```shell
   conda env create --file stenv-macOS-py3.9-2022.08.08-latest.yml --name stenv-py3.9-2022.08.08-latest
   ```

   Alternatively, you can skip downloading the file by passing the url directly to the `--file` argument of `conda env create`:
   ```shell
   conda env create --file https://github.com/spacetelescope/stenv/releases/download/2022.08.08/stenv-macOS-py3.9-2022.08.08-latest.yml --name stenv-py3.9-2022.08.08-latest
   ```

4. Finally, activate the environment to have access to the Python installation:
   ```shell
   conda activate stenv-py3.9-2022.08.08-latest
   ```

## Help

If you have issues, please contact one of the following help desks:

**HST Help Desk:** https://stsci.service-now.com/hst

**JWST Help Desk:** https://stsci.service-now.com/jwst

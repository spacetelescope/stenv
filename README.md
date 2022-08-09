# `stenv` - Space Telescope Calibration Pipeline and Analysis Tools

[![build](https://github.com/spacetelescope/stenv/actions/workflows/build.yml/badge.svg)](https://github.com/spacetelescope/stenv/actions/workflows/build.yml)
[![release](https://img.shields.io/github/v/release/spacetelescope/stenv)](https://github.com/spacetelescope/stenv/releases)
[![calver](https://img.shields.io/badge/calver-YYYY.0M.0D-22bfda.svg)](https://calver.org)

This repository builds YAML files that define environments for a `conda` installation. The `stenv-stable.yml`
, `stenv-latest.yml`, and `stenv-dev.yml` files provide minimum definitions for building this environment with stable
pinned versions, latest released versions, and latest Git commits, respectively. Additionally,
each [release](https://github.com/spacetelescope/stenv/releases) provides frozen environment files (specific version
definitions at a snapshot in time) that are built and tested on each supported platform and Python version.

## Tested Platforms

- operating systems
    - Ubuntu Linux (GitHub Actions' `ubuntu-latest` image)
    - Mac OS (GitHub Actions' `ubuntu-latest` image)
- Python versions
    - `3.8`
    - `3.9`
    - `3.10`
- version contraints
    - `stable` (patch versions)
    - `latest` (latest releases)
    - `dev` (latest commits on main branch)

## Installation

1. Install Miniconda - https://docs.conda.io/en/latest/miniconda.html

2. [Pick a release from the Releases page](https://github.com/spacetelescope/stenv/releases). These releases have YAML
   files in the Assets section for each supported platform and Python version:
   [![release example](docs/release_example.png)](https://github.com/spacetelescope/stenv/releases)

   This example assumes Mac OSX (`macOS`) with Python 3.9 (`py3.9`) and release `2022.08.08` with the `latest`
   constraints. To use this example for another configuration, download the respective environment file.

   > :warning: **Creation of a new release will trigger a
   new [workflow job in GitHub Actions](https://github.com/spacetelescope/stenv/actions/workflows/build.yml) that builds
   and tests the environment on a range of platforms and Python versions. This process may take several minutes; if a
   release was just made recently, you may need to wait for its associated workflow job to finish before environment
   files are available.**

3. You can download a YAML file with your browser from
   the [release page](https://github.com/spacetelescope/stenv/releases), or use `curl` with a direct URL:
   ```shell
   curl https://github.com/spacetelescope/stenv/releases/download/2022.08.08/stenv-macOS-py3.9-2022.08.08-latest.yml
   ```

4. To create the environment, use `conda env create --file <filename> --name <environment-name>`. The `--name` is the
   name of the environment that you create, and the handle that you later use to activate it:
   ```shell
   conda env create --file stenv-macOS-py3.9-2022.08.08-latest.yml --name stenv-py3.9-2022.08.08-latest
   ```
   Alternatively, you can pass the url to the `--file` argument of `conda env create`:
   ```shell
   conda env create --file https://github.com/spacetelescope/stenv/releases/download/2022.08.08/stenv-macOS-py3.9-2022.08.08-latest.yml --name stenv-py3.9-2022.08.08-latest
   ```

5. Finally, activate the environment to have access to the Python installation:
   ```shell
   conda activate stenv-macOS-py3.9-2022.08.08-latest
   ```

## Help

If you have issues, please contact one of the following help desks:

**HST Help Desk:** https://stsci.service-now.com/hst

**JWST Help Desk:** https://stsci.service-now.com/jwst
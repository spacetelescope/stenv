# `stenv` - Space Telescope Calibration Pipeline and Analysis Tools

[![build](https://github.com/spacetelescope/stenv/actions/workflows/build.yml/badge.svg)](https://github.com/spacetelescope/stenv/actions/workflows/build.yml)
[![release](https://img.shields.io/github/v/release/spacetelescope/stenv)](https://github.com/spacetelescope/stenv/releases)
[![calver](https://img.shields.io/badge/calver-YYYY.0M.0D-22bfda.svg)](https://calver.org)

> :warning: **This distribution platform is still in testing and is not yet an official release.**

This repository builds YAML files that define frozen environments (sets of packages at specific versions) for an
Anaconda installation. The [Releases page](https://github.com/spacetelescope/stenv/releases) provides a YAML file for
each release.

## Installation

1. install Anaconda - https://docs.conda.io/en/latest/miniconda.html
2. pick a release from the [Releases page](https://github.com/spacetelescope/stenv/releases)
   and download the accompanying YAML file
3. create a new Anaconda environment from the YAML file
   ```shell
   conda env create --file stenv-2022.08.08-py3.9-macOS.yml -n stenv-2022.08.08-py3.9-macOS
   ```
4. activate the environment
   ```shell
   conda activate stenv-2022.08.08-py3.9-macOS
   ```
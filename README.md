# Space Telescope Calibration and Analysis Tools (STCAT)

[![build](https://github.com/spacetelescope/stcat/actions/workflows/build.yml/badge.svg)](https://github.com/spacetelescope/stcat/actions/workflows/build.yml)
[![release](https://img.shields.io/github/v/release/spacetelescope/stcat)](https://github.com/spacetelescope/stcat/releases)
[![calver](https://img.shields.io/badge/calver-YYYY.0M.0D-22bfda.svg)](https://calver.org)

> :warning: **This distribution platform is still in testing and is not yet an official release.**

This repository builds YAML files that define frozen environments (sets of packages at specific versions) for an
Anaconda installation. The [Releases page](https://github.com/spacetelescope/stcat/releases) provides a YAML file for
each release.

## Installation

1. install Anaconda - https://docs.conda.io/en/latest/miniconda.html
2. pick a release from the [Releases page](https://github.com/spacetelescope/stcat/releases)
   and download the accompanying YAML file
3. create a new Anaconda environment from the YAML file
   ```shell
   conda env create --file stcat-macOS-py3.9-2022.08.08.yml -n stcat-macOS-py3.9-2022.08.08
   ```
4. activate the environment
   ```shell
   conda activate stcat-macOS-py3.9-2022.08.08
   ```
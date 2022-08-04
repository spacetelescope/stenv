# `stenv` - Space Telescope Calibration Pipeline and Analysis Tools

[![build](https://github.com/spacetelescope/stenv/actions/workflows/build.yml/badge.svg)](https://github.com/spacetelescope/stenv/actions/workflows/build.yml)
[![release](https://img.shields.io/github/v/release/spacetelescope/stenv)](https://github.com/spacetelescope/stenv/releases)
[![calver](https://img.shields.io/badge/calver-YYYY.0M.0D-22bfda.svg)](https://calver.org)

> :warning: **This distribution platform is still in testing and is not yet an official release.**

This repository builds YAML files that define frozen environments (sets of packages at specific versions) for an
Anaconda installation. The [Releases page](https://github.com/spacetelescope/stenv/releases) provides a YAML file for
each release.

If you have issues, please contact one of the following help desks:

**HST Help Desk:** https://stsci.service-now.com/hst

**JWST Help Desk:** https://stsci.service-now.com/jwst

## Installation

1. install Anaconda - https://docs.conda.io/en/latest/miniconda.html
2. pick a release from the [Releases page](https://github.com/spacetelescope/stenv/releases)
   and download the accompanying YAML file
3. create a new Anaconda environment from the YAML file
   ```shell
   conda env create --file stenv-macOS-py3.9-2022.08.08.yml -n stenv-macOS-py3.9-2022.08.08
   ```
4. activate the environment
   ```shell
   conda activate stenv-macOS-py3.9-2022.08.08
   ```
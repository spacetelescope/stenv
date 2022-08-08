# `stenv` - Space Telescope Calibration Pipeline and Analysis Tools

[![build](https://github.com/spacetelescope/stenv/actions/workflows/build.yml/badge.svg)](https://github.com/spacetelescope/stenv/actions/workflows/build.yml)
[![release](https://img.shields.io/github/v/release/spacetelescope/stenv)](https://github.com/spacetelescope/stenv/releases)
[![calver](https://img.shields.io/badge/calver-YYYY.0M.0D-22bfda.svg)](https://calver.org)

This repository builds YAML files that define frozen environments (sets of packages at specific versions) for an
Anaconda installation. The [Releases page](https://github.com/spacetelescope/stenv/releases) provides a YAML file for
each release.

If you have issues, please contact one of the following help desks:

**HST Help Desk:** https://stsci.service-now.com/hst

**JWST Help Desk:** https://stsci.service-now.com/jwst

## Installation

1. Install Miniconda - https://docs.conda.io/en/latest/miniconda.html
2. Pick a release from the [Releases page](https://github.com/spacetelescope/stenv/releases)
   and download the accompanying YAML file.

> :warning: **Note: YAML files
are [generated upon release creation](https://github.com/spacetelescope/stenv/actions/workflows/build.yml), and may take
several minutes to be attached to the Release Assets section.**

3. Create a new conda environment from the YAML file:
   ```shell
   conda env create --file stenv-macOS-py3.9-2022.08.08.yml -n stenv-macOS-py3.9-2022.08.08
   ```
4. Activate the new environment:
   ```shell
   conda activate stenv-macOS-py3.9-2022.08.08
   ```

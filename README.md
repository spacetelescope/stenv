# Space Telescope Environment Distribution

This repository builds YAML files that define frozen environments (sets of packages at specific versions) for an
Anaconda installation. The [Releases page](https://github.com/spacetelescope/spacetelescope-env-distribution/releases)
provides a YAML file for each release.

## Installation

1. install Anaconda - https://docs.conda.io/en/latest/miniconda.html
2. pick a release from the [Releases page](https://github.com/spacetelescope/spacetelescope-env-distribution/releases)
   and download the accompanying YAML file
3. create a new Anaconda environment from the YAML file
   ```shell
   conda env create --file release_1.0.0.yml
   ```
4. activate the environment
   ```shell
   conda activate 
   ```
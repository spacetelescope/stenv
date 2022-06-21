# Space Telescope Environment Distribution

This repository stores YAML files that define frozen environments (sets of packages at specific versions) for an
Anaconda installation. The `releases/` folder contains YAML files for each release.

## Installation

1. install Anaconda - https://docs.conda.io/en/latest/miniconda.html
2. clone this repository with Git (or download the ZIP and extract)
```shell
git clone https://github.com/spacetelescope/spacetelescope-env-distribution
cd spacetelescope-env-distribution
```
3. pick a desired release from the `releases/` folder
4. create a new Anaconda environment from the YAML file for your desired release
```shell
conda env create --file releases/release_1.0.0.yml
```
5. activate the environment
```shell
conda activate 
```
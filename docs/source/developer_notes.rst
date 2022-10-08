Developer Notes
###############

``stenv`` consists of two parts:

#. several Conda environment definition files in YAML format, and
#. a GitHub Actions workflow that builds and tests a working environment from each YAML file

Environment Definition Files
============================

The main environment consists of three separate YAML files, which each provide minimum packages for building a working environment locally:

#. ``stenv-stable.yml`` - package are pinned to their most recent stable feature versions
#. ``stenv-latest.yml`` - packages resolve to the latest version available on PyPI
#. ``stenv-dev.yml`` - packages are built from the latest main branch of their source code

Automated Build and Testing
===========================

The GitHub Actions `workflow <https://github.com/spacetelescope/stenv/actions/workflows/build.yml>`_ builds, tests, and exports environments to YAML files for Linux and Mac OS (using GitHub Actions' ``ubuntu-latest`` and ``macos-latest``). These environment definition YAML files are attached to `every new release <https://github.com/spacetelescope/stenv/releases>`_.

.. image:: release_example.png
  :alt: example of a release page, showing output files

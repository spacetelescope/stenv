Frequently Asked Questions
##########################

.. _build_fails:

``stenv`` doesn't build on my system; what do I do?
===================================================

You can use the environment definition YAML file (:ref:`environment_yaml`) in the root of the repository:

.. code-block:: shell

    conda env create -n stenv -f https://raw.githubusercontent.com/spacetelescope/stenv/main/environment.yaml 

This environment is unpinned, meaning it may take some time to resolve dependency versions. 
Additionally, the resulting package versions may not have been tested for your platform.

.. note::
    ``stenv`` does not currently have automated infrastructure for Apple Silicon ARM64 processors (``M1``, ``M1 Max``, ``M1 Ultra``, ``M2``);
    environments for Apple ARM64 are currently built and tested manually for every release.
    If there is not an ARM64 build for your desired release, you can see `this issue <https://github.com/spacetelescope/stenv/issues/86#issuecomment-1444583090>`_  or resolve the environment yourself with :ref:`environment_yaml`
    
.. warning::

    ``stenv`` does not currently support a native Windows installation. To build ``stenv`` on Windows, see :doc:`windows`.

Why isn't _____ package in ``stenv``?
=====================================

Not all STScI packages are included in the base ``stenv`` environment;
some packages are not supported and / or deprecated, and some are deemed too niche (or dependent on too many extra packages) to be included for all users.

To install a package in your local environment, you can use ``pip install`` while the environment is activated:

.. code-block:: shell

    conda activate stenv
    pip install <package_name>

To request that a new package be added to ``stenv``'s base environment (:ref:`environment_yaml`) for all users, or to add a package yourself, see :ref:`adding_a_package_to_stenv`.

What about Astroconda?
======================

Astroconda, historically maintained by STScI as a Conda software channel, provides data analysis tools and pipelines via the Conda package management system.

.. warning::
    Astroconda is no longer supported as of **February 1st, 2023**.

``stenv`` supersedes Astroconda as a STScI software distribution; it supports most of the packages in Astroconda, works with all current versions of Python, and provides a common environment for both the Hubble Space Telescope (HST) and James Webb Space Telescope (JWST) pipelines.
Additionally, while Astroconda primarily uses Conda recipes to build and serve packages, which need to be updated separately from PyPI releases, ``stenv`` draws most of its packages directly from PyPI with ``pip`` (though it still requires use of a Conda environment for ``hstcal`` and ``fitsverify``, which are provided by ``conda-forge``).


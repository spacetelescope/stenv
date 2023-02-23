Frequently Asked Questions
##########################

What if my platform isn't listed in released YAML files, or a released YAML file doesn't build on my system?
============================================================================================================

If the YAML files built for a release (see :ref:`choose_release`) do not include your platform, you can use the environment definition YAML file (:ref:`environment_yaml`) in the root of the repository.
Note, however, that this environment has not been tested for all platforms.

Why isn't _____ package in ``stenv``?
=====================================

Not all STScI packages are included in the base ``stenv`` environment;
some packages are not supported and / or deprecated, and some are deemed too niche (or dependent on too many extra packages) to be included for all users.

To install a package in your local environment, you can use ``pip install`` while the environment is activated:

.. code-block::

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


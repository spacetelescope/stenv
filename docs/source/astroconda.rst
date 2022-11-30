``stenv`` and Astroconda
########################

Astroconda, historically maintained by STScI as a Conda software channel, provides data analysis tools and pipelines via the Conda package management system.

.. warning::

    Astroconda will be sunset on **February 1st, 2023**.

``stenv`` supersedes Astroconda as a STScI software distribution; it supports most of the packages in Astroconda, works with all current versions of Python, and provides a common environment for both the Hubble Space Telescope (HST) and James Webb Space Telescope (JWST) pipelines.
Additionally, while Astroconda primarily uses Conda recipes to build and serve packages, which need to be updated separately from PyPI releases, ``stenv`` draws most of its packages directly from PyPI with ``pip`` (though it still requires use of a Conda environment for ``hstcal`` and ``fitsverify``, which are provided by ``conda-forge``).

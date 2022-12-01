.. _environments:

Environment Definitions
#######################

The main environment consists of several YAML files, which each provide instructions for building a working environment locally.
If you don't know which environment definition to choose, use ``stenv-latest.yml``

.. _stenv_stable:

``stenv-stable.yml``
====================

Packages in ``stenv-stable.yml`` are pinned to their most recent stable feature versions.
These are ideally updated once per quarter.

.. literalinclude:: ../../stenv-stable.yml
   :language: yaml

.. _stenv_latest:

``stenv-latest.yml`` (**recommended**)
======================================

Packages in ``stenv-latest.yml`` resolve to the latest versions available on PyPI.
This is the environment that most users should use.

.. literalinclude:: ../../stenv-latest.yml
   :language: yaml

.. _stenv_dev:

``stenv-dev.yml``
=================

``stenv-dev.yml`` is built from the latest main branch of package source code.
This is the most unstable environment, as packages might break dependencies upon each other, or have conflicting shared requirements.

.. literalinclude:: ../../stenv-dev.yml
   :language: yaml

Environment Definitions
#######################

The main environment consists of several YAML files, which each provide instructions for building a working environment locally.

``stenv-latest``
================

Packages in ``stenv-latest.yml`` resolve to the latest versions available on PyPI.
This is the environment that most users should use.

.. literalinclude:: ../../stenv-latest.yml
   :language: yaml

``stenv-stable``
================

Packages in ``stenv-stable.yml`` are pinned to their most recent stable feature versions.
These are ideally updated once every three months.

.. literalinclude:: ../../stenv-stable.yml
   :language: yaml

``stenv-dev``
=============

``stenv-dev.yml`` is built from the latest main branch of package source code.
This is the most unstable environment, as packages might break dependencies upon each other, or have conflicting shared requirements.

.. literalinclude:: ../../stenv-dev.yml
   :language: yaml

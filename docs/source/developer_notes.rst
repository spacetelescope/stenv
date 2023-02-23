Developer Notes
###############

``stenv`` consists of several parts:

#. a mostly unconstrained Conda environment definition YAML file :ref:`environment_yaml`
#. a `GitHub Actions CI workflow <https://github.com/spacetelescope/stenv/actions/workflows/build.yaml>`_ that automatically builds and tests the environment on several platforms
#. `regular GitHub releases <https://github.com/spacetelescope/stenv/releases>`_ with attached constrained Conda environment definition YAML files for every tested platform

.. _environment_yaml:

``environment.yaml``
====================

.. literalinclude:: ../../environment.yaml
   :language: yaml

.. _adding_a_package_to_stenv:

Adding a package to ``stenv``
=============================

To request that a new package be added to ``stenv``, or to add a package yourself, please `create a new issue in the repository <https://github.com/spacetelescope/stenv/issues/new?assignees=&labels=add+package&template=package_addition_request.md&title=add+%60%3Cpackage%3E%60+to+environment>`_.

.. image:: ./add_package_issue_template.png
    :alt: issue template for adding a package
    :target: https://github.com/spacetelescope/stenv/issues/new?assignees=&labels=add+package&template=package_addition_request.md&title=add+%60%3Cpackage%3E%60+to+environment

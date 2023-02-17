Developer Notes
###############

``stenv`` consists of several parts:

#. a mostly unconstrained Conda environment definition YAML file ``environment.yml`` (see :ref:`environment_definition`)
#. a `GitHub Actions CI workflow <https://github.com/spacetelescope/stenv/actions/workflows/build.yml>`_ that automatically builds and tests the environment on several platforms
#. `regular GitHub releases <https://github.com/spacetelescope/stenv/releases>`_ with attached constrained Conda environment definition YAML files for every tested platform

.. _environment_definition:

Environment Definition
======================

.. literalinclude:: ../../environment.yml
   :language: yaml

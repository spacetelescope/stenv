Installation
############

#. Install a Conda client such as `Miniconda <https://docs.conda.io/en/latest/miniconda.html>`_ or `Mamba <https://mamba.readthedocs.io/en/latest/installation.html>`_.

#. Choose a release from the `Releases page <https://github.com/spacetelescope/stenv/releases>`_ and download the environment definition file from the Assets section that corresponds to your platform.

        .. image:: release_example.png
            :alt: example of a release page, showing output files

        .. note::
            You can download a YAML file from the `release page <https://github.com/spacetelescope/stenv/releases>`_ or alternatively directly download with ``curl``:

            .. code-block:: shell

                curl -L https://github.com/spacetelescope/stenv/releases/download/2022.08.08/stenv-macOS-py3.9-2022.08.08-latest.yml -o stenv-macOS-py3.9-2022.08.08-latest.yml

            Alternatively, you can skip this step entirely by passing the url directly to the ``--file`` argument of ``conda env create``:

            .. code-block:: shell

                conda env create --file https://github.com/spacetelescope/stenv/releases/download/2022.08.08/stenv-macOS-py3.9-2022.08.08-latest.yml --name stenv-py3.9-2022.08.08-latest

        .. warning::
            Building and testing environments on supported platforms may take several minutes; **if a release was just made recently, you may need to wait** for its `associated workflow job to finish <https://github.com/spacetelescope/stenv/actions/workflows/build.yml>`_ before environment files are available.

#. Build the environment with ``conda env create --file <filename> --name <environment-name>`` (the ``--name`` argument is the name of the environment that you create). This example assumes that you downloaded an environment file for Mac OSX (``macOS``) with Python 3.9 (``py3.9``) and release ``2022.08.08`` with the ``latest`` constraints.

    .. code-block:: shell

        conda env create --file stenv-macOS-py3.9-2022.08.08-latest.yml --name stenv

#. Finally, activate the environment to have access to the Python installation:

    .. code-block:: shell

        conda activate stenv
        python
        >>> import jwst

    .. note::
        You can show installed packages in a Conda environment with ``conda env export``.

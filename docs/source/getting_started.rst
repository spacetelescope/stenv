Getting Started
###############

Conda Basics
============

``stenv`` defines a Conda environment, which is a set of packages installed together at specific versions.
A Conda environment is designed to be isolated from system packages, and can be **activated** to switch the current context (PATH, environment variables, available binaries, Python installation, etc.) to an isolated instance that is separate from the system. (This is similar to using ``source bin/activate``, if you are familiar with Python virtualenvs.)
This has the advantage of allowing several separate installations of Python packages and other tools without cluttering the system installation, allowing switching between use cases or package contexts at will.

Installation
============

.. _install_conda:

Install Conda
-------------

A Conda distribution provides the ``conda`` command, which lets you create, manage, and activate new environments. Try running the ``conda`` command in your terminal. If you get ``conda: command not found`` (or similar), you will need to install a conda distribution. If you already have a ``conda`` command in your terminal, you can skip to the next step.

The easiest option is to install `Miniconda <https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html>`_, which is full-featured but installs a minimal set of default packages initially. We will install more packages later on.

Alternatives include `Miniforge <https://github.com/conda-forge/miniforge#miniforge3>`_, which includes the ``mamba`` command (a much faster replacement for ``conda`` with all the same functionality) and `Anaconda <https://www.anaconda.com/distribution/>`_ which provides a full-featured base environment as well as hundreds of useful tools, libraries, and utilities by default.

The below instructions will work for any of the distributions, though Miniforge users will notice a speedup if they substitute ``mamba`` for ``conda`` when it appears in commands.

.. _choose_release:

Choose an ``stenv`` release
---------------------------

Now that you have a Conda installation, you should choose a release of ``stenv`` from the
`Releases page <https://github.com/spacetelescope/stenv/releases>`_ and choose the environment definition file
from the ``Assets`` section that corresponds with your platform.

.. image:: ./images/release_example.png
    :alt: example of a release page, showing output files
    :target: https://github.com/spacetelescope/stenv/releases

Every release is available for several combinations of operating system and Python version. The name of the release file indicates which is which. For example, a release of stenv for Python 3.11 on Linux will be named something like ``stenv-Linux-X64-py3.11-YYYY.MM.DD.yaml`` where ``YYYY.MM.DD`` is the date of the release. Unless you have particular requirements, you should choose the highest-numbered Python version available. (Note that version numbers aren't real numbers, and a hypothetical Python 3.20 would be newer than Python 3.2.)

Having chosen which asset to download, right-click (or control-click on macOS) on the link name and choose "Copy Link" or "Copy Link Address". Now, open a terminal window.

.. note::
    Every conda environment has a name. If you include the version numbers in the name, it will be easy to keep track of which version of stenv you have. So, you may want to replace ``stenv`` in the following example with ``stenv-py3.11-2023.01.01`` (changed as needed to match the version you downloaded).

**Short version:** In the terminal you have opened, you can create a conda environment by typing the command ``conda env create --name stenv --file``, a space, and then pasting the URL you copied in the last step. Hit enter to execute, and be prepared to wait a little while.

**Detailed version:**

1. Download the file from the link in the Releases page
2. In a terminal, navigate to the folder where you saved the file
3. Run ``conda env create --name stenv --file stenv-XXXX`` where ``stenv-XXXX`` is replaced by the name of the file you downloaded
4. Wait for the command to finish

.. note::
    If the build does not succeed on your system, please refer to :ref:`build_fails`

.. warning::
    **Can't find the release you need?** Building and testing environments on supported platforms may take several minutes; for new releases, you may need to wait for the `associated workflow job to finish <https://github.com/spacetelescope/stenv/actions/workflows/build.yaml>`_ before environment files are available.

Activating an environment
=========================

Environments let you install packages while isolating them from the rest of your system, and even each other. Even though we just built an environment, we will not be able to import the new packages yet::

    $ python -c 'import jwst; print("ok")'
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
    ModuleNotFoundError: No module named 'jwst'

In order to access the packages in ``stenv``, you must activate the ``stenv`` environment: 

.. code-block:: shell

    conda activate stenv

(If you chose another name when creating the environment, use that here instead.)

Activating a Conda environment changes which Python interpreter and packages are in use for that session (i.e. terminal window). Now, if you try to ``import jwst``::

    (stenv) $ python -c 'import jwst; print("ok")'

Every time you open a new terminal window, you will need to activate the environment with ``conda activate <name>`` before you can use stenv software.

.. code-block:: shell

    conda activate stenv

.. note::
    You can show installed packages available within a Conda environment with ``conda list``.

To deactivate an environment and return your shell to normal, run ``conda deactivate``:

.. code-block:: shell

    conda deactivate

(You can also just close the terminal window.)

Deleting an environment
=======================

To delete an environment with all of its packages, run ``conda env remove -n <name>``:

.. code-block:: shell

    conda env remove -n stenv

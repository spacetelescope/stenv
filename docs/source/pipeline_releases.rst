.. _pipeline_install:

Pipeline Releases
#################

.. note::

    - A working `conda` installation (Miniconda, Mamba, Anaconda, etc.) is required.
    - Python 2 is not supported (unless noted otherwise).
    - 32-bit operating systems are not supported.

Pipeline releases differ from the standard software stack and serve a different purpose.
The release files, described below, are immutable snapshots of STScI operational software
and can be used to replicate the environment used by STScI to perform mission-specific data processing.
Be aware that upgrading packages with ``conda update [pkg]`` or ``conda update --all`` is not recommended,
as it will likely introduce unwanted bugs and / or break the environment all together.

If you have any questions, comments, or concerns related to pipeline releases, please feel free to contact
`help@stsci.edu <mailto:help@stsci.edu>`_

Installation
============

Pipeline release installations use the following ``conda create`` command format:

.. code-block:: sh

    conda create -n [custom_env_name] --file [URL]
    source activate [custom_env_name]


Example
-------

.. code-block:: sh

    conda create -n demo_2016.1 --file http://ssb.stsci.edu/releases/hstdp/2016.1/hstdp-2016.1-linux-py35.0.txt
    source activate demo_2016.1

.. note::

    The URL shown in this example does not necessarily reflect the latest iteration available.
    Please consult the :ref:`file_urls` section to ensure you are installing the correct release.


.. _file_urls:

File URLs
=========

Select the URL that matches your intended platform and environment.

HST Data Processing (HSTDP)
---------------------------

*HSTDP* was previously known as *OPUS*.

Instructions for installation of each delivery may be found in the respective subdirectories of the releases repository:
https://github.com/astroconda/astroconda-releases/tree/master/caldp

.. code-block:: sh

    20200323  (Note: the date here represents the initial testing iteration and not the final public release date.)

Historical deliveries used an older naming convention:
https://github.com/astroconda/astroconda-releases/tree/master/hstdp

.. code-block:: sh

    2019.3a 
    2019.5 	
    2019.5.2
    2019.5.1
    2019.4 	
    2019.3c 
    2019.3b 
    2019.3 	
    2019.2 	
    2018.3a 
    2018.3 	
    2018.1 	
    2017.3 	
    2017.2a 
    2017.2 	
    2017.1 	
    2016.2 	
    2016.1 	


Continuous Integration
======================

This example BASH function provides a starting point for users intending to execute pipeline software from within a
continuous integration environment. This installation method is unsupported and your mileage may vary.
Use at your own risk.

.. code-block:: sh

    function get_pipeline()
    {
        # Do we have enough arguments?
        if [[ $# < 3 ]]; then
            echo "Not enough arguments."
            return 1
        fi

        # Setup basic argument list     & Example Input(s)
        local conda_env="$1"            # hst_env
        local name="$2"                 # hstdp, ...
        local build="$3"                # 2017.2, 2016.2 ...
        local python_version="$4"       # py[35, 27, ...]
        local iteration="$5"            # final | post[0, 1, 2, ...]

        # Detect platform
        local _platform=$(uname -s)
        local platform=""

        # Convert platform string to match file naming convention
        if [[ ${_platform} == Linux ]]; then
            platform="linux"
        elif [[ ${_platform} == Darwin ]]; then
            platform="osx"
        else
            echo "Unsupported platform: ${_platform}"
            return 1
        fi
        unset _platform

        # Handle optional arguments.
        if [[ -z ${python_version} ]]; then
            # Notice the "py" prefix and condensed version here
            python_version="py35"
        fi

        if [[ -z ${iteration} ]]; then
            iteration="final"
        fi

        # Assemble pipeline spec file URL
        local ac_root="http://ssb.stsci.edu/releases"
        local ac_base="${ac_root}/${name}/${build}"
        local ac_spec="${name}-${build}-${platform}-${python_version}.${iteration}.txt"
        local ac_url="${ac_base}/${ac_spec}"

        # Perform installation
        conda create -q -n "${conda_env}" --file "${ac_url}"
        return $?
    }

    #
    # Usage example:
    #

    # Silently generate a pipeline environment called "hst_env"
    get_pipeline hst_env hstdp 2017.2

    # Enter environment
    source activate hst_env

    # ... do work ...
    # EOF

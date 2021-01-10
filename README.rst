tpDcc-tools-cookiecutter
============================================================

Cookiecutter Project template for tpDcc tools

.. image:: https://img.shields.io/badge/Python-2.7-yellow?logo=python
    :target: https://www.python.org/

.. image:: https://img.shields.io/badge/Python-3.7-yellow?logo=python
    :target: https://www.python.org/

.. image:: https://img.shields.io/github/license/tpDcc/tpDcc-tools-cookiecutter
    :target: https://github.com/tpDcc/tpDcc-tools-cookiecutter/blob/master/LICENSE

.. image:: https://img.shields.io/badge/code_style-pep8-blue
    :target: https://www.python.org/dev/peps/pep-0008/

How to use (Manual Configuration)
============================================================

1. Go to the parent folder where you want to create project template into.

2. Open command line and execute cookiecutter command:

    .. code-block::

        cookiecutter https://github.com/tpDcc/tpDcc-tools-cookiecutter.git

    .. note::
        If you do not have Python available in your system paths, you can execute cookiecutter by launching the full path:

        .. code-block::

            "C:\Python27\Scripts\cookiecutter.exe" https://github.com/tpDcc/tpDcc-tools-cookiecutter.git


How to use (Automatic Configuration)
============================================================

1. Go to the parent folder where you want to create project template into.

2. Create a new file called **cookiecutter.yaml** and fill it with proper data. Here you have an example:

.. code-block:: yaml

    default_context:
        tool_name: "animpicker"
        tool_nice_name: "Anim Picker"
        tool_icon: "animpicker"
        tool_description: "Tool to easily create and visualize animation pickers"
        tool_class: "AnimPicker"
        tool_tags: "['tpDcc', 'dcc', 'tool', 'animation', 'picker', 'rig']"
        author: "Tomas Poveda"
        email: "tpovedatd@gmail.com"
        year: "{% now 'utc', '%Y' %}"
        version: "0.0.1"
        supported_dccs: {'maya': ['2017', '2018', '2019', '2020']}


3. Open command line and execute cookiecutter command:

    .. code-block::

        cookiecutter https://github.com/tpDcc/tpDcc-tools-cookiecutter.git --config-file "D:\tpDcc\cookiecutter.yaml" --no-input

    .. note::
        If you do not have Python available in your system paths, you can execute cookiecutter by launching the full path:

        .. code-block::

            "C:\Python27\Scripts\cookiecutter https://github.com/tpDcc/tpDcc-tools-cookiecutter.git --config-file "D:\tpDcc\cookiecutter.yaml" --no-input

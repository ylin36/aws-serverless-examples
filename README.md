- [1. Environment setup](#1-environment-setup)
- [2 Run as module](#2-run-as-module)
- [3 Install python package using pyproject.toml to generate entry](#3-install-python-package-using-pyprojecttoml-to-generate-entry)
  - [3 Install project using setup.py (DEPRECATED in lieu of pyproject.toml)](#3-install-project-using-setuppy-deprecated-in-lieu-of-pyprojecttoml)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>



# 1. Environment setup
https://docs.python.org/3/library/venv.html

Add python extension to vscode
Add boto3 extension to vscode

after creating new venv
```
/pathtoversionofpython/python -m venv /path/to/new/virtual/environment_name
source /path/to/new/virtual/environment_name/activate
```

vscode ctrl+shift+p and python interpreter to match the new venv, to set it as default in vscode and have it activate for this project

activate boto3 ctrl+shift+p AWS Boto3: Quick Start

# 2 Run as module
install the package to run the package folder as a module

**if you don't install the package first, any imports in __main__.py reference to the src folder will not work due to python pathing in its imports to sibling files**

if you want it to be editable. this allows the module to be called with python -m modulename
without having to reinstall

```
pip install -e . 
```
execute the module, now that it's been installed, python -m src 
will now execute from the sys path.
```
python -m src
```

# 3 Install python package using pyproject.toml to generate entry

https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html


pip install the module to capture any changes to toml
```
pip install .
```

## 3 Install project using setup.py (DEPRECATED in lieu of pyproject.toml)
install wheel
```
pip install --upgrade setuptools wheel
```

```
python setup.py install
```

source distribution
```
python setup.py sdist
```

wheel
```
python setup.py bdist_wheel
```

Installing the package
```
pip install aws-serverless-examples
```



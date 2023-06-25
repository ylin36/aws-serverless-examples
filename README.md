- [1. aws-serverless-examples](#1-aws-serverless-examples)
  - [1.1 Install python package using pyproject.toml to generate entry](#11-install-python-package-using-pyprojecttoml-to-generate-entry)
  - [1.2 Run as module](#12-run-as-module)
  - [1.3 Install project using setup.py (DEPRECATED in lieu of pyproject.toml)](#13-install-project-using-setuppy-deprecated-in-lieu-of-pyprojecttoml)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


# 1. aws-serverless-examples
serverless sample codes

## 1.1 Install python package using pyproject.toml to generate entry

https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html


pip install the module to capture any changes to toml
```
pip install .
```

## 1.2 Run as module
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

## 1.3 Install project using setup.py (DEPRECATED in lieu of pyproject.toml)
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


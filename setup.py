"""
To understand this project's build structure
 - This project uses setuptools, so it is declared as the build system in the pyproject.toml file
 - We use as much as possible `setup.cfg` to store the information
See also:
  https://setuptools.readthedocs.io/en/latest/setuptools.html#configuring-setup-using-setup-cfg-files
"""
from setuptools import setup

# (1) read the setup.cfg to grab useful metadata
from setuptools.config import read_configuration
conf_dict = read_configuration("setup.cfg")
PKG_NAME = conf_dict['metadata']['name']


# (2) Call setup() with as little args as possible
# Unfortunately, currently the only way to use setuptools_scm and get "author" and "maintainer" metadata in 
# PKG-INFO is to employ the use_scm_version here instead of in setup.cfg
# See https://stackoverflow.com/questions/73279327/how-to-indicate-use-scm-version-in-setup-cfg for solution
# used in https://github.com/smarie/python-genbadge
setup(
    use_scm_version={
        "write_to": "src/%s/_version.py" % PKG_NAME
    },  # we can't put `use_scm_version` in setup.cfg yet unfortunately
)

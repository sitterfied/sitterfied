#!/bin/bash
# "Strict Mode" http://redsymbol.net/articles/unofficial-bash-strict-mode/
set -euo pipefail
IFS=$'\n\t'

ENV_PATH=/opt/envs/sitterfied

# Create the environment without pip
pyenv-3.4 --without-pip "$ENV_PATH"

cd /tmp

# Install setuptools
wget https://pypi.python.org/packages/source/s/setuptools/setuptools-3.4.4.tar.gz
tar -xvzf setuptools-3.4.4.tar.gz
cd setuptools-3.4.4
$ENV_PATH/bin/python setup.py install
cd ..

# Install pip
wget https://pypi.python.org/packages/source/p/pip/pip-1.5.6.tar.gz
tar -xvzf pip-1.5.6.tar.gz
cd pip-1.5.6
$ENV_PATH/bin/python setup.py install


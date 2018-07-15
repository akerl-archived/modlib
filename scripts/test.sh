#!/usr/bin/bash

set -euo pipefail

[ -e /etc/profile ] && source /etc/profile

for i in ${PYENV_VERSION//:/ } ; do
    pyenv install -s "$i"
done

pip install -r requirements.txt
tox -v
codecov

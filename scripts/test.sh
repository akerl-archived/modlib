#!/usr/bin/env bash

set -euo pipefail

for i in ${PYENV_VERSION//:/ } ; do
    pyenv install -s "$i"
done

pip install -r requirements.txt
tox -v
codecov

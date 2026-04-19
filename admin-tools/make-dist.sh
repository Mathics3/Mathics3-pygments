#!/bin/bash
PACKAGE=mathics-pygments
package=mathics_pygments

# FIXME put some of the below in a common routine
function finish {
  cd $mathics_pygments_owd
}

cd $(dirname ${BASH_SOURCE[0]})
mathics_pygments_owd=$(pwd)
trap finish EXIT

if ! source ./pyenv-versions ; then
    exit $?
fi


cd ..
source mathics_pygments/version.py
echo $__version__
pyenv local 3.13
python -m build --wheel --no-isolation
python ./setup.py sdist
finish

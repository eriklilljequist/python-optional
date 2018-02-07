rm -rf build
rm -rf dist
rm -rf htmlcov
rm -rf virt-env
rm -rf YetAnotherPyOptional.egg-info
rm -rf .coverage
find . -type d -name '*cache[__]?' | xargs -L 1 rm -rf
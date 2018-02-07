#!/bin/bash

pytest Optional/tests\
  --cov Optional/src/optional\
  --cov-branch\
  --cov-report=html\
  --cov-report=term\
  --verbose

pylint Optional/optional

echo 'View coverage in browser?'
read yn
if echo $yn | grep -iq ^y ; then
  xdg-open htmlcov/index.html
fi
#!/bin/bash

pytest Optional/tests\
  --cov Optional/src/optional\
  --cov-branch\
  --cov-report=html\
  --cov-report=term\
  --verbose

pylint Optional/src/optional

#!/bin/bash
pip3 install virtualenv
virtualenv virt-env

source virt-env/bin/activate

pip3 install -r requirements.txt
#!/bin/bash
module load python/3.5.2
pyvenv es_env 
source es_env/bin/activate
pip install elasticsearch
pip install certifi
deactivate
tar -cvzf es_env.tar.gz es_env

#!/bin/bash
source  /cvmfs/oasis.opensciencegrid.org/osg/modules/lmod/current/init/bash
module load python/3.5.2
#tar -xzf es_env.tar.gz
pyvenv es_env
source es_env/bin/activate
#python es_connectProj_query.py 
python es_connectProj_query.py -days 7
deactivate


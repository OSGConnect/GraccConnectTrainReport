#!/bin/bash
source  /cvmfs/oasis.opensciencegrid.org/osg/modules/lmod/current/init/bash
module load python/3.5.2
#tar -xzf es_env.tar.gz
pyvenv es_env
source es_env/bin/activate
python es_connectProj_query.py > es.out
deactivate

nlines=$(wc -l es.out | awk '{print $1}' | sed "s/ //g")
echo "$nlines"
cat ./es.out

# send alert email
subject="ConnectTrain Usage Statistics"
recipients="dmbala@gmail.com, bala.desinghu@gmail.com, OSG-JOINT-USCG@opensciencegrid.org, gardnergroup@lists.uchicago.edu"

if [ $nlines -gt 9 ]
then
    cat ./es.out | mail -s "$subject" $recipients 

fi



# Generate daily report on the usage of ConnectTrian project


`ConnectTrain` is a project used for training purposes on OSG Connect. Sometimes, the
connectTrian project has been used beyond its scope of training purposes. It is good to keep track of 
the `ConnectTrian` project so that the user support team can check which user needs a new project. 

The scripts in this git repo are useful to collect the usage of  `ConnectTrain` project from 
GRACC (GRid ACcounting Collector) and send an email alert to the user support team.  The data in [GRACC has been made 
available to the public](https://opensciencegrid.github.io/gracc/user/direct/). The public interface is 
useful to get additional data that are not available via [graphana summary pages](https://gracc.opensciencegrid.org/dashboard/db/osg-connect-summary-osg-connect?orgId=1). 


## Set up

One may query elasticsearch indices via curl, Perl, Python, Ruby, java, or PHP (maybe more options). Here, the Python API has been used to query the GRACC.  Python virtual environment is utilized to install the required external modules: `elasticsearch` and `certifi`.  

To create the virtual environment on login01 or login02 (you may slightly change this shell script to work on other machines with Python), type

    $ ./create_virtenv.sh

The shell script `create_virtenv.sh` creates the virtual environment `es_env`. 

## Run Query 

The shell script `run_query.sh` activates the virtual environment `es_env` and runs the query on GRACC to collect 
the usage of `ConnectTrain` project. 

    $ ./run_query.sh 
    --------------------------------------------------
    ConnectTrain project usage     
    Begin Date= 2017-06-19     End Date= 2017-06-26    
 
    --------------------------------------------------
    USERNAME           NUMBER OF JOBS        WALLTIME     
    --------------------------------------------------
 
    dbala                    1400.0             42.8
    --------------------------------------------------

The Python script `es_connectProj_query.py` is the main program that interacts with GRACC. If you have activated 
the virtual environment `es_env` or you have relevant modules, type

    $ python es_connectProj_query.py
    
The above execution collects the usage of `ConnectTrain` during the last day. 

To collect the usage of `ConnectTrain` for the last seven days, type  

    $ python es_connectProj_query.py -days 7



## Run query and send an email report

The shell script `run_query_and_report.sh` runs the query on GRACC and sends the usage statistics to the user 
support team. 

    $ ./run_query_and_report.sh


The above command is being executed on login02 at 2.10 AM, everyday. An email report is send to the user support 
team only if anyone used the connectTrain project. 


## List of Files

* `create_virtenv.sh`: Set up file to create the virtual environment and install relevant packages. 
* `es_connectProj_query.py`: Python script interacts with GRACC 
* `run_query.sh`: Shell script to activate the virtual environment and query GRACC
* `run_query_and_report.sh`: Shell script to activate the virtual environment, query GRACC, and send email to the user support team 
* `es_env.tar.gz`: Compressed file of the virtual environment
* `es.out`: Sample output from the query. 



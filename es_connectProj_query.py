#!/usr/bin/python
#title           :es_connectProj_query.py 
#author          :Bala
#date            :June-9-2017
#version         :1.0
#usage           :python program.py -days 2 ( start_date is set from the supplied days. default = 1 day)
#help            :python program.py --help
#notes           :Extracts ConnectTrain usage from GRACC. 
#python_version  :2.7

import argparse
from elasticsearch import Elasticsearch
from datetime import date, timedelta

def get_connectTrain_usage_information(start_date, end_date, es=None):
    """
    Gathers the usage of ConnectTrain Project by users. 
    :param 
          start_date: The start date to begin the search
          start_date: The end date to begin the search
          es:         elasticsearch object to use
    
    :return:           Nothing, (prints out results to stdout)
    """
    if es is None:
        return

    #start_date="2017-05-01"
    #end_date = "2017-06-01"

    query_variable =  "(VOName:osg connect OR VOName:osg) AND ProjectName: ConnectTrain AND ResourceType:Payload AND EndTime:[" + start_date + " TO " + end_date + "]"
    
    es_data = es.search(body= 
         { 
           "query": {
            "query_string": {
                "query": query_variable
            }
        },
        "aggs": { "userstats": { "terms": { "field": "DN" },
                                 "aggs": { "walltime": { "sum": { "field": "CoreHours" } }, 
                                           "jobs": { "sum": { "field": "Njobs" } } 
                                         } 
                               }
               },

        "size": 0
 
         })

    agg = es_data['aggregations']['userstats']['buckets']
    return agg 

def get_args():
    """ Get the arguments for this program: Give number of days in iteger to set the start date. End date is today """
    parser = argparse.ArgumentParser(description=' Usage: python program.py -days 7 (default value is 1 day)')
    parser.add_argument('-days','--days', dest="start_days", type = int, help=' number of days to set the start date from today', default = 1)
    args = parser.parse_args()
    return args



if __name__ == "__main__":

    n_days  = get_args().start_days 
    begin_date = (date.today() - timedelta(n_days)).strftime("%Y-%m-%d")
    end_date = date.today().strftime("%Y-%m-%d")

    es = Elasticsearch(['https://gracc.opensciencegrid.org/q/gracc.osg.summary'])
    ct_usage = get_connectTrain_usage_information(begin_date, end_date, es)

    print("-"*50) 
    print("{0:30s}".format( "ConnectTrain project usage     "))
    print("Begin Date= {0:14s} End Date= {1:14s}".format( begin_date , end_date ))
    print(" ") 
    print("-"*50) 
    print("{0:16s} {1:18s} {2:18s}".format("USERNAME", "  NUMBER OF JOBS  ", "     WALLTIME     "))
    print("-"*50) 
    print(" ") 

    for rec in ct_usage:
        words = rec['key'].split("/")[-1]
        sub_words = words.split(" ")[0]
        username = sub_words.replace("CN=","").replace("UID:","")
        print("{0:16s} {1:16.1f} {2:16.1f}".format(username,rec['jobs']['value'], rec['walltime']['value']))
    print("-"*50) 



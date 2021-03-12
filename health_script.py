from bottle import route, run
import glob
import json
import os
import subprocess
import time
import socket

 # This method is used to check the status of health of the node
 # on which this script is running. It makes used of nodetool and figures out the
 #  status of node.
@route('/check')
def getNodeStatus():
        list = []
        result = 1
        p = os.popen("nodetool status")
        while 1:
            line = p.readline()
            print ("Line"), line
            if not line =="":
                        ipData = line.split(" ")
                        if len(ipData) > 3:
                                localPort = socket.gethostbyname(socket.gethostname())
                                if ipData[2] == localPort:
                                                if ipData[0] == "UN":
                                                        return  "cassandra is running"
            if not line: break
        return "cassandra is Not running"


# This method will tell overall health on the cluster by returning 0 for healthy cluster and 1
# as a response if more than onw third of nodes are unhealthy.
@route('/health')
def getclusterStatus():
        p = os.popen("nodetool status")
        count = 0
        healthynodes =0
        while 1:
            line = p.readline()
            if not line =="":
                        ipData = line.split(" ")
                        if len(ipData) > 3:
                                #Check for ipNodes
                                ipNode = ipData[2].split(".")
                                if len(ipNode) == 4:
                                        count = count +1
                                        localPort = socket.gethostbyname(socket.gethostname())
                                        if ipData[0] == "UN":
                                               healthynodes = healthynodes + 1
            if not line: break
       # return "cassandra is Not running"
        health = healthynodes/count *100
        if(health > 66):
               return "cassandra is running"
        return "cassandra is Not running"

def main():
    run(host='localhost', port=8080)

if __name__ == '__main__':
    main()
# centos 7 error check and common problem
#
#

import subprocess # this is to required to run bash command
import os

'''
check logs
read from a file each line checking for corrispondence of a string TXT or json file
'''

''' this is an example
def check():
    with open('example.txt') as f:
        datafile = f.readlines()
    found = False  # This isn't really necessary
    for line in datafile:
        if blabla in line:
            # found = True # Not necessary
            return True
    return False  # Because you finished the search without finding
'''
## create a list of messagess file

logs = []
for file in os.listdir("/var/log"):
    if file.startswith("messages"):
        # add the output to a list
       # print(os.path.join("/mydir", file))
        logs.append(file)
# check len of logfile
logfile_len = len([logs])

######

'''
for each logfile in logfile_len
    read line in logfile[x]
        for each line check for an error log
        print line to the screen

'''

for x in logfile_len:
    with open(logfile[x]) as f:
        datafile = f.readlines()

    for line in datafile:
        ### read line in error file
        if error_msg[y] in line:
            print ("line")




''' check network card '''
# example
# logs = subprocess.check_output(["sudo", "apt", "update"])
# for line in logs.splitlines():


''' user_data permissions error '''
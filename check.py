# centos 7 error check and common problem
#

from check_def import *
import os

# Global variable variable
log_output = ("/user_data/.tmp/check_output.txt") 
errors_msg = ("error_list.txt")  # future improvement need to be a json file
log_dir = ("/var/log")
##### End list of global variable

# Adding to a list of all "messages" file from /var/log

logs_file = []
for file in os.listdir(log_dir):
    if file.startswith("messages"):
        logs_file.append( os.path.join(log_dir, file))
# count how many messages file are in the list
logs_file_len = len(logs_file)


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

'''
for each logfile in logfile_len
    read line in logfile[x]
        for each line check for an error log
            if the error match with the line in messagess
            print the line and add it to the log_output

'''
# TIPs instead of while ( for x in range(logfile_len): )
count = 0
while ( logs_file_len >= count ):
#  Iterate over the lines
    for line in logs_file_len:
        for line in error_msg:
            if line == error_msg:
                print (line)      
                write_log(log_output,line)
                #print if a corrispondence is found
        #count = count - 1


'''


for x in logfile_len:
    with open(logfile[x]) as f:
        datafile = f.readlines()

    for line in datafile:
        ### read line in error file
        if error_msg[y] in line:
            print ("line")

'''




''' check network card '''
# example
# logs = subprocess.check_output(["sudo", "apt", "update"])
# for line in logs.splitlines():

# example of shell command to call the function shell
command = ["sudo", "apt", "update"]
shell(command)




''' user_data permissions error '''
chmod_ok = ("777")
#### calling function from a variable
check_perm = {'shell':[ ''' ls file permissions command with grep '''] }### add command
fix_perm = {'shell':["chmod", "777", "/user_data"]}

'''  ## here an example how to call funtion from bariable
def test():
        print 'test'

def test2():
        print 'test2'

mydict = {'test':'blabla','test2':'blabla2'} '''

if check_perm != chmod_ok:
    print ("User_data permissions are wrong\n")
    fix_perm
else:
    print (" User_data permission are fine")
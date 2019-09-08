# centos 7 error check and common problem
#
#
import check_def

import os

# common variable

log_output = ("/user_data/.tmp/check_output.txt") 
errors_msg = errors.txt  # future improvement need to be a json file


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
## create a list of messages file ( from here should be completed )
logs = []
for file in os.listdir("/var/log"):
    if file.startswith("messages"):
        # add the output to a list
       # print(os.path.join("/mydir", file))
        logs.append('/var/log/'file)
# check len of logfile
logfile_len = len([logs])

######  ( up to here should be working )
'''
for each logfile in logfile_len
    read line in logfile[x]
        for each line check for an error log
            if the error match with the line in messagess
            print the line and add it to the log_output

'''
# instead of while ( for x in range(logfile_len): )
i = 0
while (count < logfile_len):
    # Iterate over the lines
    for line in logs[logfile_len]:
        for line in error_msg:
            if line == error_msg:
             print (line)      
             write_log(log_output,line)
             #print if a corrispondence is found
    count = count + 1


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
run_perm = shell([ ''' ls file permissions command with grep '''])

if run_perm != chmod_ok:
    print ("User_data permissions are wrong\n")
    shell(["chmod", "777", "/user_data"])
else:
    print (" User_data permission are fine")
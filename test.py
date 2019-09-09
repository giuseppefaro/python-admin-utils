import os

log_output = ("/user_data/.tmp/check_output.txt") 
#errors_msg = errors.txt  # future improvement need to be a json file
log_dir = ("c:/test")

logs_file = []
for file in os.listdir(log_dir):
    if file.startswith("messages"):

        # add the output to a list
       # print(os.path.join("/mydir", file))
       #print (file)
        logs_file.append( os.path.join(log_dir, file))
        #logs_file = [os.path.join(log_dir, file)]
        print (logs_file)
        
        #logs_file_len = len(logs_file)
        print (len(logs_file))
      # logs_file.append('/var/log/',file)
# check len of logfile
#logs_file_len = len([logs_file])
#print (logs_file_len)
print (len(logs_file))
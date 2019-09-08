import subprocess # this is to required to run bash command

def write_log(log_output,line):
    open(log_output, "a+").write(line).close()
    return
    
def shell(cmd):
    subprocess.check_output([cmd])
    shell_return = ""
    return shell_return

    


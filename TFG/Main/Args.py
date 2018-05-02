import sys
import getopt


def main(argv):
    inputfile = ''
    function = ''
    try:
        opts, args = getopt.getopt(argv, "hi:f:", ["ifile=", "func="])
    except getopt.GetoptError:
        print('usage: test.py -i <inputfile> -f <function>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('usage: test.py -i <inputfile> -f <function>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-f", "--func"):
            function = arg
    print('Input file is "', inputfile)
    print('Function is "', function)


if __name__ == "__main__":
    main(sys.argv[1:])

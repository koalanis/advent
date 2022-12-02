import os
import argparse
 

def main():
    # create parser object
    parser = argparse.ArgumentParser(description = "An Advent of Code Utility")
 
    # # defining arguments for parser object
    # parser.add_argument("-r", "--read", type = str, nargs = 1,
    #                     metavar = "file_name", default = None,
    #                     help = "Opens and reads the specified text file.")
     
    # parser.add_argument("-s", "--show", type = str, nargs = 1,
    #                     metavar = "path", default = None,
    #                     help = "Shows all the text files on specified directory path.\
    #                     Type '.' for current directory.")
     

    subparsers = parser.add_subparsers(help="the available actions in the AoC utility")
    subparsers.add_parser('check', help='verifies whether a problem directory exists for a solution configuration')
    subparsers.add_parser('data', help='b help')
    subparsers.add_parser('open', help='b help')
    # subparsers.add_parser('calendar', help='b help')

    # parse the arguments from standard input
    args = parser.parse_args()
     
    # calling functions depending on type of argument
    # if args.read != None:
    #     read(args)
    # elif args.show != None:
    #     show(args)
    # elif args.delete !=None:
    #     delete(args)
    # elif args.copy != None:
    #     copy(args)
    # elif args.rename != None:
    #     rename(args)
  
if __name__ == "__main__":
    # calling the main function
    main()
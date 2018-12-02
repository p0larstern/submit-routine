import argparse,site

parser = argparse.ArgumentParser(description="Submit your codechef's solution directly from command-line!!")
parser.add_argument("file", type=str, help="expects code of question in lowercase")
parser.add_argument("-s", "--same", help="solution file must have its name as the code of the question",
                    action="store_true")
args = parser.parse_args()
code = args.file
if args.same :
    print("file name is same")
else:
    print("file name is different")
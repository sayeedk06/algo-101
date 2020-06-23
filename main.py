import argparse
from sort import merge



parser = argparse.ArgumentParser(description='Process sorting data')

parser.add_argument("file", type=str, help="Filename with data")
parser.add_argument("--sort_type", type=str, help="Enter the type of sorting you want")

args = parser.parse_args()

try:
    data = open('data/%s.txt'% args.file, encoding='utf-8').read().splitlines()
    print("Unsorted = " + str(data))
    intdata = [int(item) for item in data]
except IOError:
    print("File not found or path is incorrect")
# finally:
#     print("File reading successful")

def sortResult(data):
    f = open("sorted/mergeSort.txt", "w")
    for item in data:
        f.write(str(item) + "\n")
    f.close()



if(args.sort_type == 'mergeSort'):
    merge.merge_sort(intdata)
    sortResult(intdata)
    print("\nSorted = " + str(intdata))

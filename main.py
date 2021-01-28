import argparse
import importlib
import time

"""Commandline argument paser starts here"""
parser = argparse.ArgumentParser(description='Process sorting data')
parser.add_argument("file", type=str, help="Filename with data")
parser.add_argument("--sort_type", type=str, help="Enter the type of sorting you want")
args = parser.parse_args()
"""Commandline argument paser Ends here"""

try:
    data = open('data/%s.txt'% args.file, encoding='utf-8').read().splitlines()
    print("Unsorted = " + str(data))
    intdata = [int(item) for item in data]
except IOError:
    print("File not found or path is incorrect")


def sortResult(data, filename):
    f = open("sorted/%s.txt"% filename, "w")
    for item in data:
        f.write(str(item) + "\n")
    f.close()
try:    
    PLUGIN_NAME = 'sort.' + args.sort_type
    plugin_module = importlib.import_module(PLUGIN_NAME, '.')
    # print(plugin_module)
    plugin = plugin_module.Plugin(args.sort_type, key=123)
    print(plugin)
except IOError:
    print("Wrong sorting algorithm or given name doesn not exits")


start_time = time.time()
plugin.Sort(intdata)
print("Execution time: %s seconds" % (time.time() - start_time))
sortResult(intdata, args.sort_type)
print("\nSorted = " + str(intdata))

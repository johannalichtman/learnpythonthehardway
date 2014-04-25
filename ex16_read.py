from sys import argv

script, filename = argv

target = open(filename, 'r') # 'r' parameter is for read

print target.read()

target.close()
import os
import sys

size = {}

def scan_mem(pth):

    if not os.path.exists(pth):
        return
    with os.scandir(pth) as files:

        for node in files:

            if os.path.isfile(node):

                mem = 10 ** len(str(os.stat(node).st_size))
                size[mem] = size.get(mem, 0) + 1
            elif os.path.isdir(node):
                scan_mem(os.path.join(pth, node))

if __name__ == "__main__":
    if len(sys.argv) == 2:
        pth = sys.argv[1]
    else:
        pth = os.getcwd()
    scan_mem(pth)
    print(size)
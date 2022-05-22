import os
import sys

size = {}


def scan_mem(pth):

    if not os.path.exists(pth):
        return

    with os.scandir(pth) as files:

        for node in files:

            if node.is_file():

                mem = 10 ** len(str(os.stat(node).st_size))

                file_extend = os.path.splitext(node)[-1]

                count, extends = size.get(mem, (0, set()))

                extends.add(file_extend)
                count += 1

                size[mem] = (count, extends)

            elif node.is_dir():
                scan_mem(os.path.join(pth, node))


if __name__ == "__main__":

    if len(sys.argv) == 2:
        pth = sys.argv[1]
    else:
        pth = os.getcwd()

    scan_mem(pth)
    print({ k:(size[k][0], list(size[k][1])) for k in size})

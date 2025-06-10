# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os
import sys
from base.index import run as run_base
from num_py.index import run as run_numpy
from matplot_lib.index import run as run_matplotlib
from sym_py.index import run as run_sympy


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sys.stdout.write(f'\n当前工作目录：{os.getcwd()}\n')
    # run_base()
    # run_numpy()
    run_matplotlib()  # 2d or 3d or None
    # run_sympy()

else:
    print_hi('other file')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

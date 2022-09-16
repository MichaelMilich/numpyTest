# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    a=np.zeros(10)
    print(a)
    print(a.size * a.itemsize)
    x1 = np.arange(9.0).reshape((3, 3))
    x2 = np.arange(3.0)
    print(x1)
    print()
    print(x2)
    print()
    print(x1+x2)
    a[4]=1
    print(a)
    a=np.arange(10,50)
    print(a)
    a=a[::-1]
    print(a)
    a=np.arange(0,9).reshape(3,3)
    print(a)
    a=np.array([1,2,0,0,4,0])
    print(a)
    b=np.nonzero(a)
    print(b)
    """
    Got to question number 11, continue in home at according to notion
    """
    print(np.identity(3))
    #np.info(np.arange)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import sys

def doubleit(x):
    var = x * 2
    return var

if __name__ == '__main__':
    input_val = sys.argv[1]
    doubled_val = doubleit(input_val)
    print("the value of {0} is {1}".format(input_val, doubled_val))



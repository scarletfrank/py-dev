import sys
from basic import timer, setclass, fastset

def setops(Class):
    a = Class(range(50))
    b = Class(range(20))
    c = Class(range(10))
    d = Class(range(5))
    for i in range(5):
        t = a & b & c & d
        t = a | b | c | d
    
if __name__ == '__main__':
    rept = int(sys.argv[1])
    print('set => ', timer.test(rept, setops, setclass.Set))
    print('fastset => ', timer.test(rept, setops, fastset.Set))
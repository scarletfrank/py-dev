from sys import argv
from basic import timer
from basic import stackmod
from basic import stackclass
from basic import tuplestack
from basic import tail_class

rept = 200
pushes, pops, items = (int(arg) for arg in argv[1:])

def stackops(stackClass):
    x = stackClass('spam')
    for i in range(pushes): x.push(1)
    for i in range(items): t = x[i]
    for i in range(pops): x.pop()

for mod in (stackclass, tuplestack, tail_class):
    print(f'{mod.__name__}', end=' ')
    print(timer.test(rept, stackops, getattr(mod, 'Stack')))
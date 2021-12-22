from itertools import permutations,combinations
from math import factorial,sqrt,log

#números envolvidos, acrescentar oper1 se necessário
num= (1,2,3,4)

#número de repitições: 1, 2 ou 3
numOfRep=3

#resultado pretendido
result=24

oper2= {'+':(lambda x,y:x+y),
        '-':(lambda x,y:x-y),
        '*':(lambda x,y:x*y),
        '/':(lambda x,y:x/y),
        '^':(lambda x,y:x**y)}

oper1= {'!':(lambda x:factorial(x)),
        '$':(lambda x:sqrt(x))}

operations=tuple(oper2.keys())*numOfRep

def compute(lst):
    stack=[]
    while lst:
        op=lst.pop()
        if isinstance(op,int):
            stack.append(op)
        elif op in oper1:
            try:
                x=stack.pop()
                if(op=='!' and x>10):
                    return None
                z=oper1[op](x)
                stack.append(z)
            except (IndexError,TypeError,ValueError):
                return None
        elif op in oper2:
            try:
                x=stack.pop()
                y=stack.pop()
                if(op=='^' and y>10):
                    return None
                z=oper2[op](x,y)
                stack.append(z)
            except (IndexError,ZeroDivisionError,ValueError,OverflowError):
                return None
        else:
            return None
    return stack.pop()

for lstOp in combinations(operations,3):
    for calc in permutations(num+lstOp):
        res=compute(list(calc))
        if res and res==result:
            print(calc,'=',int(res))




import time
import sys
from random import randint
from random import uniform

lbound = '['
rbound = ']'
track = ' '
bar = '█'
width = 60
perc=True

splashlist=[
    'stealing a bike...\n',
    'fucking a mole...\n',
    'downloading porn...\n',
    'hacking pentagon...\n',
    'looking for a bike...\n',
    'installing malware...\n',
    'starting fire...\n',
    'reading holy bible...\n'
]

def returnBar(value:int=0, max:int=100):
    value+=1
    val=((value/max)*width)+1
    construct = lbound
    for x in range(width):
        if x>int(val):
            construct+=track
        else:
            construct+=bar
    construct+=rbound
    if perc:construct+=f' {round((value/max)*100,2)}%'
    return construct

while(True):
    print(
        splashlist[
            randint(0,len(splashlist)-1)
        ]
    )
    for i in range(100):
        time.sleep(uniform(0.1,0.4))
        sys.stdout.write("\033[F")
        print(returnBar(i, 100))
import random,os,time
n=10
a=[[random.getrandbits(1)for x in range(n)]for y in range(n)]
while 1:
    os.system('clear')
    b=a
    for y in range(n):
        for x in range(n):
            l=0-a[x][y]
            d=[-1,0,1]
            for v in d:
                for w in d:
                    l+=a[(x+v+n)%n][(y+w+n)%n]
            b[x][y]={(1,2):1,(1,3):1,(0,3):1}.get((a[x][y],l),0)
            print(b[x][y],end='')
        print('')
    time.sleep(1)

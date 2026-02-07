import random
import time
def M(list, funct):#Среднее
    sum=0
    for i in list:
        sum+=funct(i)
    return sum/float(len(list))

def D(list): return M(list,lambda x:x*x)-M(list,lambda x:x)**2#Нахождение дисперсии

def razdelrandom(list,n,s=None):#стохастическая
    minlist=[]
    minD=77777777777777777777777777777777777777777
    if s is None:  s=10**n if n<=6 else 10**6
    for i in range(s):
        listresult=[[]]
        for a in list:
            if listresult[-1]==[] or len(listresult)==n or random.randint(0,2):
                listresult[-1].append(a)
            else:
                listresult.append([a])
        listresult2=[sum(a) for a in listresult ]
        if D(listresult2)<minD and len(listresult)==n:
            minD=D(listresult2)
            minlist=listresult
    return minlist

def binary(n):
    b = ''
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    return(b)

def nachin(m,n):#полный перебор
    global greatlist
    greatlist=[]
    for a in range(1,m+2-n):
        s="1"+"0"*(a-1)+"1"
        pomos(m,n,a,s,2)

def pomos(m,n,a,s,glubina):#полный перебор
     for b in range(a+1,m-n+glubina+1):
        s0=s+"0"*(b-a-1)+"1"
        if glubina < n - 1:
            pomos(m,n,b,s0,glubina+1)
        else:
            s0=s0+"0"*(m-b-1)
            greatlist.append(s0)

def razdel_plus(list,n):#полный перебор
    minlist = []
    minD = 77777777777777777777777777777777777777777
    nachin(len(list),len(list)-n+1)
    for binaryi in greatlist:
        listresult = [[]]
        a=0
        while a<len(list):
            if binaryi[a]=='0':
                listresult.append([list[a]])
            else:
                listresult[-1].append(list[a])
            a+=1
        listresult2 = [sum(a) for a in listresult]
        if D(listresult2) < minD  :
            minD = D(listresult2)
            minlist = listresult
    return minlist

def razdel_plus01(list,n):#полный перебор
    minlist = []
    minD = 77777777777777777777777777777777777777777
    m1=2**(len(list))-2**(len(list)-n-1)
    for i in range(1,m1):
      binaryi=binary(i)
      if binaryi.count('1')==(n-1):
        while (len(binaryi) < len(list)): binaryi = '0'+ binaryi
        listresult = [[]]
        a=0
        while a<len(list):
            if binaryi[a]=="1":
                listresult.append([list[a]])
            else:
                listresult[-1].append(list[a])
            a+=1
        listresult2 = [sum(a) for a in listresult]
        if D(listresult2) < minD  :
            minD = D(listresult2)
            minlist = listresult
    return minlist

random.seed(7)
l0=[4,1,2,4,5,3,6,9,8,9]
l1=l0+[1,9,1,1,9,3,1,4,8,2]
l2=[random.randint(5,25) for a in range(150)]
n0=4
n1=8
for l in l0,l1:
    for n in n0,n1:
        print(l,n)
        print("Показатели случайного разделения")
        start=time.time()
        result=razdelrandom(l,n)
        end=time.time()
        print("D=",D([sum (a) for a in result]))
        print("Time=",end-start)
        print("Показатели первого полного разделения")
        start = time.time()
        result = razdel_plus(l, n)
        end = time.time()
        print("D=",D([sum (a) for a in result]))
        print("Time=",end - start)
        print("Показатели второго полного разделения")
        start = time.time()
        result = razdel_plus01(l, n)
        end = time.time()
        print("D=",D([sum (a) for a in result]))
        print("Time=",end - start)

for n in n0,n1:
        print(l2,n)
        print("Показатели случайного разделения")
        start=time.time()
        result=razdelrandom(l2,n)
        end=time.time()
        print("D=",D([sum (a) for a in result]))
        print("Time=",end-start)
        print("Показатели первого полного разделения")
        start = time.time()
        result = razdel_plus(l2, n)
        end = time.time()
        print("D=",D([sum (a) for a in result]))
        print("Time=",end - start)






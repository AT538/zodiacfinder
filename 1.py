
n=int(input("Enter the no:of numbers"))
i=0
l=[]
while i<n:
    N=int(input("Enter the number"))
    x=[N]
    l=l+x
    i+=1
def mean(l):
    s=0
    for x in l:
        s+=x
    avg=s/len(l)
    print("Mean is",avg)


def mode(l):
    j=[];m=[]
    for x in l:
     if x not in j:
         j=j+[x]
         k=[l.count(x)]
         m=m+k
    MAX=max(m)
    ind=m.index(MAX)
    print("Mode is",l[ind])


def median(l):
    l=sorted(l)
    if n%2==0:
        print("Median is",(l[n//2]+l[n//2+1])/2)
    else:
        print("Median is",l[n//2])
         




c=0
while(c!=4):
 print("Enter any of the options")
 print("1:Mean")
 print("2:Mode")
 print("3:Median")
 print("4:Exit")
 c=int(input("Enter"))
 if c==1:
     mean(l)
     
 elif c==2:
     mode(l)
     
 elif c==3:
     median(l)
     
 elif c==4:
     print("Exiting")
     
 else:
     print("Invalid value")
     
     

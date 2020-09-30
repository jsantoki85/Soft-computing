n=int(input("Enter the No of elements in input Vector"))
s = [] 
for i in range(0, n): 
	ele = int(input()) 
	s.append(ele) 
print(s)

#s=[1,1,1,-1]
w=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
x=[0,0,1,0]
y=[0,0,0,0]
yin=[0,0,0,0]
dyin=0
print("\nWeight matrix is-")
for i in range(4):
    for j in range(4):
        w[i][j]=s[i]*s[j]
#for self connection we are setting value = 0
        if (i==j):
            w[i][j]=0
for i in w:
   print(i)


Y=[1,1,1,0]

print("\n")
for i in range(len(x)):
    for j in range(i,len(x)):
        if(i==j):
            w[i][j] = 0
        else:
            w[i][j] = s[i]*s[j]
            w[j][i] = w[i][j]

y=x
print("NO\t\ty\t\tCheck");
for i in range(4):
    for j in range(4):
        dyin = w[i][j]*y[j]
        yin[i] = x[i]+dyin
        if(yin[i] >0):
            y[i]=1
        elif(yin[i] <0 ):
            y[i] = 0

    if(Y==y):
        print(i+1,"\t"+str(y)+"\t No updation ")
    else:
        print(i+1,"\t"+str(y)+"\tUpdation is done")

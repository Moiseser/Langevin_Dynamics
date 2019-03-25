start = -1.5
end = 1.5 
N = 100
dx = (end - start)/float(N)  
f1 = open("energy","w")
for i in range(100):
    y = start + i*dx
    for j in range(100):
        x =  start + j*dx
        print >>f1, x, y, V([x,y])
f1.close()


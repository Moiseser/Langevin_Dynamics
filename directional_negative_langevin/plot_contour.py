####CREATED BY Dhiman Ray####
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate

N = 100 #number of points for plotting/interpolation

m = 50   #number of contours

x, y, z = np.genfromtxt(r'traj.out', unpack=True)

xi = np.linspace(x.min(), x.max(), N)
yi = np.linspace(y.min(), y.max(), N)
zi = scipy.interpolate.griddata((x, y), z, (xi[None,:], yi[:,None]), method='cubic')

X, Y = np.meshgrid(xi, yi)

fig = plt.figure()
cp = plt.contourf(X, Y, zi, m, cmap='rainbow_r')
plt.plot(xi,yi)
plt.clim(-0.3,2.5)
plt.colorbar(cp)
#plt.contour(xi, yi, zi, m)
plt.xlabel("r($\AA$)")
plt.ylabel("Z($\AA$)")
plt.show()
#plt.savefig("contour.pdf")

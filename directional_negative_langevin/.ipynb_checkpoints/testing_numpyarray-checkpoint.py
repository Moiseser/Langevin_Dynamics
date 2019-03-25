{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0. 0.]\n",
      " [0. 0.]]\n",
      "[[1. 1.]\n",
      " [1. 1.]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np \n",
    "#In this script I will play around with np arrays/matrices to learn them \n",
    "#numpy.array(object, dtype=None, copy=True, order='K', subok=False, ndmin=0)\n",
    "\n",
    "#This is how you reading a 2D array AKA matrix \n",
    "Gamma = np.array([[5.,1],[3,8.]])\n",
    "#print Gamma\n",
    "#print Gamma*.5\n",
    "#I was messing with order option, F = fortran = column major, C= row major\n",
    "xGamma = np.array([[5,0],[0,8]],order = 'F')\n",
    "this_is_column = np.array([[5,1],[2,8]],order = 'F')\n",
    "this_is_row = np.array([[5,1],[2,8]],order = 'C')\n",
    "#print this_is_column\n",
    "#print this_is_row\n",
    "#Still not sure how this works? Ill deal with it later. \n",
    "\n",
    "#A matrix can be created from np.array which is a subclass of ndarray\n",
    "#In other words matrices are strictly 2-dimensional arrays. \n",
    "\n",
    "a=np.mat('4 3; 2 1')\n",
    "b=np.mat('1 2; 3 4')\n",
    "#print a, b \n",
    "#matrices are handy because you can do matrix multiplication with '*' operator \n",
    "#print a*b\n",
    "\n",
    "#Lets try this with our 2d array generated above\n",
    "#print Gamma * Gamma\n",
    "#As you can see this simply takes each element and multiply them \n",
    "# A(i)*B(i), this does not do actual matrix multiplication \n",
    "#To do matrix multiplication with ndarrays you use the np.dot object\n",
    "#print (np.dot(Gamma,Gamma))\n",
    "\n",
    "#Some final notes \n",
    "#the '**' operator behaves different. , .H abd .I are mat exclusive objects\n",
    "#np.asmatrix and np.asarray allow you to convert one to the other (as long as the array is 2-dimensional)\n",
    "\n",
    "#Initializing arrays\n",
    "#this fills your array with zeros \n",
    "zero = np.zeros((2,2))\n",
    "print zero \n",
    "#this fills with ones \n",
    "ones = np.ones((2,2))\n",
    "print ones \n",
    "\n",
    "# np.empty fills with random numbers and is faster , np.full can specific a number to fill it with \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.15"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

#! /usr/bin/python
import sys
PI=3.14159265358979323846264338327950288

def h(n):
 
  if(n!=0):
    suma = 0
    for i in range(1,n+1):
      a = float(i-1)/float (n)
      b = float(i)/float (n)
      xi = float(i-0.5)/float (n)
      fxi = 4.0/(1.0 + xi*xi)
      #print  a, b, xi, fxi
      suma += fxi
    pi=float (suma)/float (n)
    return pi
    #print 'El valor aproximado de pi es: ', pi
    #print 'El valor de pi con 35 cifras decimales es: %1.35g' % PI
  
n = int(sys.argv[1])
m = int(sys.argv[2])
lista=[]
for i in range (0, m):
   pi=h(n)
   lista.append(pi)
#print "pi: %.35f" % (pi)
#print "El valor de pi con 35 cifras decimales es:%.35f" % (PI)
print lista

  
  
  
def modular_pow(a,x,p):
	c = 1
	for i in range(1,x+1):
		c = (c * a) % p
	return c

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
        gcd = b
    return gcd, x, y

def gcd(a,b):
	return(egcd(a,b)[0])

def invert(x,p):
	return(egcd(x,p)[2])
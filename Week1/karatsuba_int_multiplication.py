#!/bin/env python
import sys;

# this program is to implement the algorithm of Karatsuba integer
# multiplication algorithm, which reduce the computation time to
# O(n^log2(3)).
# The algorithm is, let 
# x=10^(n/2)*a + b,
# y=10^(n/2)*c + d,
# Then x*y=10^n*a*c + 10^(n/2)*(ad+bc)+bd,
# where n is the number of digits in x and y, for example, if x=1234
# and y=5678, then n=4.
# The key here is to recursively call to get the product of a*c, b*d,
# and (a+b)*(c+d), and then apply the above formula to get x*y.
def pad_0(i,n):
	"""add n zeros at the end of i"""
	si=str(i)+'0'*n;
	return int(si);

def get_abcd(x,y):
	"""disassemble x and y to get the left and right havlves of x and
	y"""
	x=str(x);y=str(y);
	lx=len(x);
	ly=len(y);
	n=max(lx,ly); # the number of digits in x and y after pre-padding 0
	n=n+1 if n%2 != 0 else n;
	# get 0-prepadded string x and y
	sx='0'*(n-lx)+x;
	sy='0'*(n-ly)+y;
	half=n/2;
	a=int(sx[:half]);
	b=int(sx[half:]);
	c=int(sy[:half]);
	d=int(sy[half:]);
	return [a,b,c,d,n];

def kara_mult(x,y):
	"""The main function to get the product of two integers"""
	# get the numbers a, b, c, and d.
	a,b,c,d,n=get_abcd(x,y); # returned are numbers n

	# x or/and y is single-digit number
	if (a==0 and b<10) or (c==0 and d < 10):
		return x*y;
	# otherwise use recursive call
	ac=kara_mult(a,c);
	bd=kara_mult(b,d);
	s1=kara_mult(a+b,c+d) - ac -bd;
	xy=pad_0(ac,n) + pad_0(s1,n/2) + bd;
	return xy;

try:
	x=int(sys.argv[1]);
	y=int(sys.argv[2]);
except:
	print "Usage: {0:s} <x> <y>".format(sys.argv[0]);
	sys.exit(1);

sign=1;
if x < 0: sign*=-1; x=abs(x);
if y < 0: sign*=-1; y=abs(y);

prod=kara_mult(x,y)*sign;

print "{0:4d} x {1:4d} = {2:8d}".format(x,y,prod);

sys.exit(0);


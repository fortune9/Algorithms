#!/bin/env python

# this program implements the quicksort algorithm by random selecting
# a pivot
import sys;
import csv;
import random as rd;

def swap(a,i,j):
	"""swap two elements given by i and j in array a"""
	if i==j:
		return a;
	tmp=a[i];
	a[i]=a[j];
	a[j]=tmp;
	return a;

def quick_sort(a,l=None,r=None):
	"""sort the elements given by [l,r] index boundaries in the 
	input array 'a' using quick sort method"""
	# set default values
	l=0 if l==None else l;
	r=len(a)-1 if r==None else r;
	if r-l <= 0: # < 0 happen when the array is empty
		#return [a[l]]; # return as a list
		return; # return nothing, as the sorting is in place
	# otherwise choose a pivot and call sub arrays
	pivotIndex=rd.choice(range(l,r+1));
	pivot=a[pivotIndex];
	# put the pivot as the first element for the array block
	swap(a,pivotIndex,l);
	splitIndex=l+1; # the boundary between the sub array smaller than
	# and bigger than the pivot, which is just the first element of
	# the bigger sub array
	j=l+1; # traverse the array
	while j<=r:
		if a[j] <= pivot:
			swap(a,j,splitIndex);
			splitIndex+=1;
		j+=1;
	# put pivot to its position
	swap(a,l,splitIndex-1);
	# now sub recursive calls if there are elements in sub arrays
	quick_sort(a,l,splitIndex-2); # exclude the pivot point
	quick_sort(a,splitIndex,r);

try:
	inFile=sys.argv[1];
except:
	print "Usage: %s <infile> [<outfile>]" % sys.argv[0];
	print """
	The <infile> should contain the numbers to be sorted. One line can
	contain more than one numbers separated by any white space.
	""";
	sys.exit(1);

out=sys.stdout;
if len(sys.argv) > 2:
	out=open(sys.argv[2],"w");

f=open(inFile,'rb');

ar=[];
for row in f:
	ar.extend(map(int,row.split()));

f.close();

quick_sort(ar);
#output the array in a pretty format
i=0;
arSize=len(ar);
size=10;
while i < arSize:
	last=i+size if i+size < arSize else arSize;
	subAr=ar[i:last];
	fmt="{:4d} " * len(subAr)+"\n";
	out.write(fmt.format(*subAr));
	i+=size;
out.close;

sys.exit(0);


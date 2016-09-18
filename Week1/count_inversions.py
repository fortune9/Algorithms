#!/bin/env python
import sys;

def count_inversions(a):
	"""This is the main function to count array using the MergeSort
	algorithms"""
	if len(a) == 1: # only one element
		return [0,a];
	#split the data into two halves and count the inversions in each
	# half and then add the inversions at this step
	midPoint=len(a)//2;
	[nl,al] = count_inversions(a[:midPoint]);
	[nr,ar] = count_inversions(a[midPoint:]);
	# sort and count inversions for this step
	anew=[];
	count=nl+nr;
	i=j=k=0;
	lLen=len(al);
	rLen=len(ar);
	while k < lLen + rLen:
		if i == lLen: # left array reach the end
			anew.extend(ar[j:]);
			break;
		if j == rLen: # right array reach the end
			anew.extend(al[i:]);
			break;
		if al[i] > ar[j]:
			anew.append(ar[j]);
			count+=len(al)-i;
			j+=1;
		else:
			anew.append(al[i]);
			i+=1;
		k+=1;
	return [count,anew];

# read into the data
try:
	inFile=sys.argv[1];
except:
	print "Usage: {0} <input-file>".format(sys.argv[0]);
	sys.exit(1);

printArray=False; # an option to determine whether the final sorted
#array should be printed

if len(sys.argv) > 2:
	printArray=bool(int(sys.argv[2]));

f=open(inFile, 'r');
#nums=list(f); # read into list, equivalent to f.readlines()
nums=[];
for r in f:
	r.strip();
	nums.append(int(r));
#print nums;
result=count_inversions(nums);
print "{0:d}".format(result[0]);
if printArray:
	print "{0:s}".format(result[1]);

sys.exit(0);

def Split(A):
	n=len(A)
	mid=n/2
	if(n<2):
		return A
	'''Create a Left and Right Array. We must consider if Array A is an odd length size, when spliting 
	There maybe a leftover. In order to account for this. The right array's size is equal to the length of A minus mid
	'''	
	left=[0]*mid
	right=[0]*(n-mid)
#Create the Left Array	
	for i in range(0,mid):
		left[i]=A[i]
#Create the Right array
	for i in range(mid, n):
		right[i-mid]=A[i]
	#Split the left array down till its size is equal to 1.	
	Split(left)
	#Split the right array down till its size is equal to 1
	Split(right)
	#Merge the two arrays 
	Merge(left,right,A)

def Merge(left, right, A):
	NL=len(left)
	RL=len(right)
	i=0
	j=0
	k=0

	while(i<NL and j<RL):
		if(left[i]<=right[j]):
			A[k]=left[i]
			i+=1
			k+=1
		else:
			A[k]=right[j]
			j+=1
			k+=1

	while(j<RL):
		A[k]=right[j]
		k+=1
		j+=1

	while(i<NL):
		A[k]=left[i]
		k+=1
		i+=1

if __name__ == '__main__':
	A=[2,2,5,1,8,3,22,4,7]
	Split(A)
	print(A)


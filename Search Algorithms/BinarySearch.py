def BinarySearch(A,length,element):
	print(element)
	high=length-1
	low=0

	while(low<=high):
		mid=int((high+low)/2)
		print("entered")
		if(element==A[mid]):
			return mid
		elif(A[mid]>element):
			high=mid-1
		else:
			print("entered again")
			low=mid+1

	return -1

if __name__== '__main__':
	A=[1,2,3,4,5,8,11]
	length=7
	element=8
	print(BinarySearch(A,length,element))


def modInverse(e, base): # or euclid algorithm
    for x in range(1, base):
        if e * x % base == 1:
            return x
    return -1

print(modInverse(550,1759))#invese of 9 in range 34


# Function to find inverse permutations
def inversePermutation(arr:list):

	# Loop to select Elements one by one
	for i in range(0, len(arr)):

		# Loop to print position of element
		# where we find an element
		for j in range(0, len(arr)):

		# checking the element in increasing order
			if (arr[j] == i + 1):

				# print position of element where
				# element is in inverse permutation
				print(j + 1, end = " ")
				break

# Driver Code
arr = [3 ,1 ,2 ,5 ,4]

inversePermutation(arr)

#This code is contributed by Smitha Dinesh Semwal

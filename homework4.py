# harc 1
def binary_search_iterative(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

    
        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

arr = [2, 3, 4, 10, 40]
target = 10
result = binary_search_iterative(arr, target)
if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")




def binary_search_recursive(arr, target, left, right):
    if right >= left:
        mid = left + (right - left) // 2

        
        if arr[mid] == target:
            return mid

        elif arr[mid] > target:
            return binary_search_recursive(arr, target, left, mid - 1)
    
        else:
            return binary_search_recursive(arr, target, mid + 1, right)
    else:
    
        return -1


arr = [2, 3, 4, 10, 40]
target = 10
result = binary_search_recursive(arr, target, 0, len(arr) - 1)
if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")








# harc 2



MAX = 100

def printDiagonalSums(mat, n):

	principal = 0
	secondary = 0
	for i in range(0, n): 
		principal += mat[i][i]
		secondary += mat[i][n - i - 1]
		
	print("Principal Diagonal:", principal)
	print("Secondary Diagonal:", secondary)


a = [[ 1, 2, 3, 4 ],
	[ 5, 6, 7, 8 ], 
	[ 1, 2, 3, 4 ],
	[ 5, 6, 7, 8 ]]
printDiagonalSums(a, 4)





# harc 3


def auxiliary_diagonal_sum(matrix):
    size = len(matrix)
    diagonal_sum = 0
    for i in range(size):
        diagonal_sum += matrix[i][size - i - 1]
    return diagonal_sum


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Sum of auxiliary diagonal elements:", auxiliary_diagonal_sum(matrix))



# harc4


N = 4;


def rotateMatrix(mat):
	
	
	i = N - 1; 
	while(i >= 0):
		j = N - 1;
		while(j >= 0):
			print(mat[i][j], end = " ");
			j = j - 1;
		print();
		i = i - 1;

mat = [[1, 2, 3,4],
	[5, 6,7,8 ],
	[9,10,11,12 ],
    [13,14,15,16]];
rotateMatrix(mat);


# harc 5


def get2NonRepeatingNos(nums, n):

	nums.sort();

	ans=[];
	
	i=0;
	while(i<n-1):
		if (nums[i] != nums[i + 1]):
			ans.append(nums[i])
			i = i + 1
		else:
			i=i+2;
		
			
	if (len(arr) == 1):
		ans.append(nums[n - 1]);
		
	return ans;


arr = [ 2, 3, 7, 9, 11, 2, 3, 11 ];
n = len(arr);
ans = get2NonRepeatingNos(arr, n);
print("The non-repeating elements are ", ans[0], " and ", ans[1]);



# harc6

def Selection_Sort(arr, n):
	
	for i in range(n - 1):
		min_index = i 
		
		for j in range(i + 1, n):
			if (arr[j] < arr[min_index]):
				min_index = j
				
		arr[i], arr[min_index] = arr[min_index], arr[i] 
		

n = 5
arr = [ 2, 0, 1, 4, 3 ]
Selection_Sort(arr, n)

print("The Sorted Array by using " \
	"Selection Sort is : ", end = '')
for i in range(n):
	print(arr[i], end = " ")
	


# harc 7


def custom_zip(*iterables):
    return [tuple(next(it) for it in map(iter, iterables)) for _ in range(min(map(len, iterables)))]


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = [True, False, True]

result = custom_zip(list1, list2, list3)
print(result)


# harc 8

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def nth_prime(n):
    count = 0
    candidate = 1
    while count < n:
        candidate += 1
        if is_prime(candidate):
            count += 1
    return candidate


n = 10
print(f"The {n}th prime number is:", nth_prime(n))


# harc 9


def highestPowerof2(n):

	res = 0;
	for i in range(n, 0, -1):
		
	
		if ((i & (i - 1)) == 0):
		
			res = i;
			break;
		
	return res;


n = 10;
print(highestPowerof2(n));
	

# harc 10

# Python3 program to find the element that
# appears only once

# A Linear Search based function to find
# the element that appears only once


def search(arr, n):

	ans = -1
	for i in range(0, n, 2):
		if (arr[i] != arr[i + 1]):
			ans = arr[i]
			break
	if(arr[n-2] != arr[n-1]):
		ans = arr[n-1]

	
	print("The required element is", ans)


arr = [1, 1, 2, 4, 4, 5, 5, 6, 6]
Len = len(arr)

search(arr, Len)





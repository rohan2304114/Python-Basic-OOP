# # Read four integers from input
# A, B, C, D = map(int, input().split())

# # Calculate the difference
# X = (A * B) - (C * D)

# # Print the result in the required format
# print(f"Difference = {X}")

# a,b,c,d = map(int,input().split())

# x=(a*b)-(c*d)
# print(f"Difference ={x}")

# Read the radius
# R = float(input())

# # Given value of pi
# pi = 3.141592653

# # Calculate area
# area = pi * R * R

# # Print result with 9 digits after decimal
# print(f"{area:.9f}")
# r= float(input())
# pi=3.1416
# area= pi*r*r;

# print(f"{area:.9f}")
# Read the two numbers as strings
# N, M = input().split()

# # Get the last digits and convert to int
# last_N = int(N[-1])
# last_M = int(M[-1])

# # Print the sum of last digits
# print(last_N + last_M)


# a,b= input().split()
# lastA=int(a[-a])
# lastB=int(b[-1])
# print(lastA+lastB)

# # Read input
# N = int(input())

# # Calculate summation using formula
# result = N * (N + 1) // 2

# # Print the result
# print(result)


# a= int (input())
# result=a*(a+1)//2
# print(result)
# a= 6/2
# print(a)

# b=6//2
# print(b)

# a=2
# print(a**a)

# # Read input
# N = int(input())

# # Print numbers from 1 to N
# for i in range(1, N + 1):
#     print(i)

# a=int(input())

# for i in range (1,a+1):
#     print(i)

# Read input
# N = int(input())

# # Flag to check if any even number is printed
# found = False

# # Loop through numbers from 1 to N
# for i in range(1, N + 1):
#     if i % 2 == 0:
#         print(i)
#         found = True

# # If no even numbers found, print -1
# if not found:
#     print(-1)

# n = int(input())
# found=False

# for i in range (1, n+1):
#     if i%2 ==0:
#        found= True
#        print(i)
       
# if not found:
#     print(-1)

# boss =True

# if boss is True:
#     print("Boss in the house ")

# elif boss is not True:
#     print("No boss is the not in house")

# else:
#     print ("Madarchod")

# n= int(input())

# found= True
# for i in range (1,n+1):
#     if i%2==0:
#         found=False
#         print(i)

#     elif found:
#       print("Thats means number is true ")
# def myFunction(num):
#     result =num+ 5
#     print(result)

 
#     myFunction(10)

#     def number(num1, num2):
#         result =num1+ num2
#         return result
           
# Read number of elements
# n = int(input())

# # Read the array of numbers
# arr = list(map(int, input().split()))

# # Calculate the sum
# total_sum = sum(arr)

# # Print absolute value of the sum
# print(abs(total_sum))

# n= int( input())
# arr= list (map(int, input().split()))
# totalsum= sum(arr)
# print(abs(totalsum))

# # Read number of elements
# n = int(input())

# # Read the array
# arr = list(map(int, input().split()))

# # Read the number to search
# x = int(input())

# # Search for x
# position = -1
# for i in range(n):
#     if arr[i] == x:
#         position = i
#         break

# # Print result
# print(position)


# n= int(input())
# arr=list(map(int,input().split()))
# x=int(input())
# position =-1
# for i in range(n):
#     if arr[i]==x:
#         position =i
#         break

# print(position)

# Read number of elements
# n = int(input())

# # Read the array
# arr = list(map(int, input().split()))

# # Assume first element is minimum
# min_value = arr[0]
# min_pos = 1  # 1-indexed position

# # Traverse the array
# for i in range(1, n):
#     if arr[i] < min_value:
#         min_value = arr[i]
#         min_pos = i + 1  # convert to 1-index

# # Print result
# print(min_value, min_pos)

# n= int(input())
# arr= list(map(int,input().split()))
# minValue= arr[0]
# minpos=1
# for i in range (1,n):
#     if arr[i]>minValue:
#         minvalue=arr[i];
#         minpos=i;
# print(minvalue,minpos)
# # Read number of elements
# n = int(input())

# # Read the array
# arr = list(map(int, input().split()))

# # Print in reverse order
# for i in range(n - 1, -1, -1):
#     print(arr[i], end=" ")

# n= int(input())
# arr= list(map,int(input().split()))
# for i in range(n-1,-1,-1):
#     print(arr[i],end=" ")

# def average(arr, n):
#     total = 0.0
#     for num in arr:
#         total += num
#     return total / n


# # Read input
# n = int(input())
# arr = list(map(float, input().split()))

# # Calculate average
# avg = average(arr, n)

# # Print with 6 digits after decimal
# print(f"{avg:.6f}")

# def average(arr,n):
#     total=0
#     for i in arr:
#         total+=i 
#         return total 




# n=int(input())
# arr=list(map(float,input().split))
# avg=average(arr,n)
# print(f"{avg: .6f}")


# def get_max(arr):
#     return max(arr)


# def get_min(arr):
#     return min(arr)


# def is_prime(x):
#     if x <= 1:
#         return False
#     for i in range(2, int(x ** 0.5) + 1):
#         if x % i == 0:
#             return False
#     return True


# def count_primes(arr):
#     count = 0
#     for x in arr:
#         if is_prime(x):
#             count += 1
#     return count


# def is_palindrome(x):
#     s = str(x)
#     return s == s[::-1]


# def count_palindromes(arr):
#     count = 0
#     for x in arr:
#         if is_palindrome(x):
#             count += 1
#     return count


# def count_divisors(x):
#     cnt = 0
#     for i in range(1, int(x ** 0.5) + 1):
#         if x % i == 0:
#             cnt += 1
#             if i != x // i:
#                 cnt += 1
#     return cnt


# def max_divisors_number(arr):
#     max_div = -1
#     result = -1

#     for x in arr:
#         d = count_divisors(x)
#         if d > max_div or (d == max_div and x > result):
#             max_div = d
#             result = x

#     return result


# # -------- Main Program --------
# n = int(input())
# arr = list(map(int, input().split()))

# print(f"The maximum number : {get_max(arr)}")
# print(f"The minimum number : {get_min(arr)}")
# print(f"The number of prime numbers : {count_primes(arr)}")
# print(f"The number of palindrome numbers : {count_palindromes(arr)}")
# print(f"The number that has the maximum number of divisors : {max_divisors_number(arr)}")


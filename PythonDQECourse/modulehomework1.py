#--------------------------create list of 100 random numbers from 0 to 100-----------------------
##---Using While for getting the 100 numbers from 0 to 100
# i = 0               # initiate the i with 0
# while i < 100:      # added the limit for i so that it would not exceed from 100
#     print(i)        # printing the 1
#     i = i +1        # getting the new value of i

#or we can use range as well
# for a in range(100):
#     print(a)


#--------------------------sort list from min to max (without using sort(),sorted())

# a = [64, 25, 12, 22, 11, 1,2,44,3,122, 23, 34]  # initiate the a with list of values
#
# for i in range(len(a)):                         #assigning the lenght of a to i
#     for j in range(i + 1, len(a)):              #assigning the lenght of a to J
#         if a[i] > a[j]:                         #if value of i (64) which is on place of 0 is greater than J (25) which is on place of 1
#            a[i], a[j] = a[j], a[i]              #then replace i with J else move forward and it will continue till range of i
#
# print(a)

#-------------------------Calculate average for even and odd numbers

# Sample list of even_numbers and odd_number
# even_numbers = [2,4,6,8,10,12,14]
# odd_number = [1,3,5,7,9,11,13]

# Calculate the average for even numbers
# if even_numbers:
#     avg_even = sum(even_numbers) / len(even_numbers)
# else:
#     avg_even = 0  # Handle the case when there are no even numbers
#
# # Calculate the average for odd numbers
# if odd_number:
#     avg_odd = sum(odd_number) / len(odd_number)
# else:
#     avg_odd = 0  # Handle the case when there are no odd numbers
#
# print(f"Average of even numbers: {avg_even}")
# print(f"Average of odd numbers: {avg_odd}")

#-------------------------Calculate average for even and odd numbers

# Sample list of even_numbers and odd_number
list_numbers = [2,4,6,8,10,12,14,1,3,5,7,9,11,13]
even_num= []   #empty strings even_number
odd_num=[]     #empty string odd number
# Calculate the average for even numbers
for i in list_numbers:
    if i%2 == 0:
        even_num.append(i)   #append function is used to add value of list in empty string
    else:
        odd_num.append(i)

# Calculate the average for even numbers
if even_num:
    avg_even = sum(even_num) / len(even_num)   # Sum function will add the value of even_num and length will check the length of list
else:
    avg_even = 0  # Handle the case when there are no even numbers

# Calculate the average for odd numbers
if odd_num:
    avg_odd = sum(odd_num) / len(odd_num)
else:
    avg_odd = 0  # Handle the case when there are no odd numbers

print(f"Average of even numbers: {avg_even}")
print(f"Average of odd numbers: {avg_odd}")

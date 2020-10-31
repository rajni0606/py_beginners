# Program to check a number is perfect square or not

def is_num_perfect_square(num):
    if num < 0:                     # square of any real number would always be non-negative
        return false
        
    low, high = 0, num + 1
    
    root_value = 0
    
    while high - low > 1:
        mid = (low + high) // 2
        if mid * mid <= num:
            root_value = mid
            low = mid
        else:
            high = mid
            
    return root_value * root_value == num


# Taking input
num = int(input())

# Checking if a input value is perfect square or not
if(is_num_perfect_square(num)):
    print(str(num) + ' is a perfect square')
else:
    print(str(num) + ' is not a perfect square')
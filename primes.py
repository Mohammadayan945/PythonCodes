# def is_prime(n):
#     if n <= 1:
#         return False

#     for i in range(2, n):
#         if n % i == 0:
#             return False

#     return True
    

# print(is_prime(25))

# def prime_info(num):
    
#     if num <= 1:
#         isPrime = False
#     else:
#         isPrime = True
#         for i in range(2, num):
#             if num % i == 0:
#                 isPrime = False
#                 break

    
#     prev = num - 1
#     while prev > 1:
#         check = True
#         for i in range(2, prev):
#             if prev % i == 0:
#                 check = False
#                 break
#         if check:
#             break
#         prev -= 1

    
#     next_num = num + 1
#     while True:
#         check = True
#         for i in range(2, next_num):
#             if next_num % i == 0:
#                 check = False
#                 break
#         if check:
#             break
#         next_num += 1

#     return isPrime, prev, next_num


# num = int(input("Enter a number: "))

# prime_status, previous_prime, next_prime = prime_info(num)

# print("Is prime:", prime_status)
# print("Nearest previous prime:", previous_prime)
# print("Nearest next prime:", next_prime)

def prime_and_closest(num):
    # check if num is prime
    if num <= 1:
        is_prime = False
    else:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

    prev = num - 1
    next_num = num + 1

    prev_found = False
    next_found = False

    # single while loop
    while not prev_found or not next_found:

        # check previous number
        if prev > 1 and not prev_found:
            flag = True
            for i in range(2, prev):
                if prev % i == 0:
                    flag = False
                    break
            if flag:
                prev_found = True
            else:
                prev -= 1

        # check next number
        if not next_found:
            flag = True
            for i in range(2, next_num):
                if next_num % i == 0:
                    flag = False
                    break
            if flag:
                next_found = True
            else:
                next_num += 1

    return is_prime, prev, next_num

num = int(input("Enter a number: "))

prime_status, prev_prime, next_prime = prime_and_closest(num)

print("Is prime:", prime_status)
print("Nearest previous prime:", prev_prime)
print("Nearest next prime:", next_prime)

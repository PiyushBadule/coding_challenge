# Challenge: Reversed Prime Numerology
# You are on a quest in a mystical world of numerology. Your task is to take two cryptic integers, A and B, separated by a comma (e.g., 123,456). Reverse their digits, determine their primality efficiently, and perform one of three sacred calculations:

# If both reversed numbers are prime, return their sum.
# If only one of the reversed numbers is prime, return the sum of the original numbers.
# If neither reversed number is prime, return the product of the original numbers.
# Your solution should be both accurate and efficient, capable of handling large numbers, and it should follow coding best practices.

# Deliverables: Submit a Python script that accomplishes this mystical task.



def is_prime(num):
    """
    Determine if a number is prime.
    :param num: int, the number to check for primality.
    :return: bool, True if the number is prime, otherwise False.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def calculate_mystical_sum(A, B):
    """
    Perform the sacred calculation based on the primality of the reversed numbers.
    :param A: str, the first arcane number.
    :param B: str, the second arcane number.
    :return: int, the result of the sacred calculation.
    """
    X, Y = int(A[::-1]), int(B[::-1])
    prime_count = is_prime(X) + is_prime(Y)

    if prime_count == 2:
        return X + Y
    elif prime_count == 1:
        return int(A) + int(B)
    else:
        return int(A) * int(B)

def main():
    """
    The main ritual function where the numerologists provide their inputs.
    """
    A, B = input("Enter the two arcane numbers separated by a mystical comma: ").split(',')
    result = calculate_mystical_sum(A, B)
    print("The result of the sacred calculation is:", result)

if __name__ == '__main__':
    main()

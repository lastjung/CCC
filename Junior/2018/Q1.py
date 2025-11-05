def is_telemarketer(digits):
    """Return True if digits match the telemarketer pattern."""
    first, second, third, fourth = digits

    is_tele =  first in {8, 9} and fourth in {8, 9} and second == third
       
    return is_tele


digits = [int(input()) for _ in range(4)]

# print("ignore" if is_telemarketer(digits) else "answer")

if is_telemarketer(digits):
    print("ignore")
else:
    print("answer")

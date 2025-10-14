apples_three = int(input())
apples_two = int(input())
apples_one = int(input())
bananas_three = int(input())
bananas_two = int(input())
bananas_one = int(input())

def total_score(three_point, two_point, one_point):
    return three_point * 3 + two_point * 2 + one_point


apples_score = total_score(apples_three, apples_two, apples_one)
bananas_score = total_score(bananas_three, bananas_two, bananas_one)

if apples_score > bananas_score:
    print("A")
elif apples_score < bananas_score:
    print("B")
else:
    print("T")

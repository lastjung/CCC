def longest_palindrome_length(text):
    text_length = len(text)

    # """Return the length of the longest palindromic substring in text."""
    # best = 0
    # length = len(text)
    # for start in range(length):
    #     for end in range(start + 1, length + 1):
    #         segment = text[start:end]
    #         if segment == segment[::-1]:
    #             if len(segment) > best:
    #                 best = len(segment)
    # return best

    for i in range(text_length):
        sub_length =  text_length - i
        for j in range(i+1):
            # print(i, j, text[j:j + sub_length])
            sub_text = text[j:j + sub_length]

            if sub_text == sub_text[::-1]:
                return sub_length

    return -1 

word = input()
print(longest_palindrome_length(word))

# abracadabra


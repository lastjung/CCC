total_t = input()
cyclic_t = input()

len_total = len(total_t)
len_cyclic = len(cyclic_t)


for i in range(len_total - len_cyclic + 1):
    slice_cyclic = total_t[i:i+len_cyclic]
    slice_cyclic += slice_cyclic

    if cyclic_t in slice_cyclic:
        print("yes")
        # print(slice_cyclic)
        break
else:
    print("no")
def largest(listnums):
    max = listnums[0]
    for i in range(len(listnums)):
        if listnums[i] > max:
            max = listnums[i]
    if any(listnums):
        print("At least one number is not zero")
    else:
        print("All values are zero")
    print(max)

list = [1,3,3,5,87,2,1]
largest(list)
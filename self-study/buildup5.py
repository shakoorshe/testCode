
def odds(list):
    counter = 0
    for i in range(len(list)):
        if list[i] % 2 != 0:
            counter +=1
    print(counter)

nums = [4,7,73,3,1,5,84,7,844]

odds(nums)
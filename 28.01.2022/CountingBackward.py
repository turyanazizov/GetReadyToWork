#Counting backward by 1
def backwardsby2(num):
    if num <= 0:
        print('Zero!')
        return
    else:
        item = []
        for i in range(0, num):
            item += '*'
        print(num, ' '.join(item))
        backwardsby2(num - 1)

backwardsby2(5)
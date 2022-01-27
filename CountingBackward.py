#Counting backward by 1
def backwardsby2(num):
    if num <= 0:
        print('Zero!')
        return
    else:
        emojismiles = []
        for i in range(0, num):
            emojismiles += '*'
        print(num, ' '.join(emojismiles))
        backwardsby2(num - 1)

backwardsby2(5)
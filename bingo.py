#import cgi
#import random
#form = cgi.FieldStorage()
#size = form.getfirst('size')

size = input()

def rand_swap(max_value,arr):
    rand1 = random.randint(0,max_value)
    rand2 = random.randint(0,max_value)
    tmp = arr[rand1]
    arr[rand1] = arr[rand2]
    arr[rand2] = tmp

def bingo(size):
    try:
        size = int(size)
        max_value = size*size*4
        #数字の配列
        arr = []
        bingo_card=[]
        for i in range(max_value):
            arr.append(i+1)
        #数字ランダムに
        rand_swap(max_value,arr)
        #分割して2次元に
        for i in range(size)
            bingp_card.append(arr.array_split(i*size,(i+1)*size))
    except ValueError:
        return('数字じゃないよ！')
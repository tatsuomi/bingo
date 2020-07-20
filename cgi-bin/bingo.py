import cgi
import random
form = cgi.FieldStorage()

def rand_swap(max_value,arr):
    #回数
    x = 100
    i = 0
    while i < x:
        rand1 = random.randint(0,max_value-1)
        rand2 = random.randint(0,max_value-1)
        tmp = arr[rand1]
        arr[rand1] = arr[rand2]
        arr[rand2] = tmp
        i = i + 1

def make_arr():
    #数字の配列
    arr = []
    for i in range(100):
        arr.append(i+1)
    #数字ランダムに
    rand_swap(100,arr)
    return arr

def print_matrix(bingo_card):
    for i in range(len(bingo_card)):
        for j in range(len(bingo_card[i])):
            print(str(bingo_card[i][j]).rjust(3),end="")
        print()
    print()

def check_bingo(bingo_card):
    counter = 0
    check_list = [[[0,0],[0,1],[0,2],[0,3],[0,4]],
                  [[1,0],[1,1],[1,2],[1,3],[1,4]],
                  [[2,0],[2,1],[2,2],[2,3],[2,4]],
                  [[3,0],[3,1],[3,2],[3,3],[3,4]],
                  [[4,0],[4,1],[4,2],[4,3],[4,4]],
                  [[0,0],[1,0],[2,0],[3,0],[4,0]],
                  [[0,1],[1,1],[2,1],[3,1],[4,1]],
                  [[0,2],[1,2],[2,2],[3,2],[4,2]],
                  [[0,3],[1,3],[2,3],[3,3],[4,3]],
                  [[0,4],[1,4],[2,4],[3,4],[4,4]],
                  [[0,0],[1,1],[2,2],[3,3],[4,4]]]

    for i in check_list:
        for j in i:
            #ビンゴじゃない行
            if bingo_card[j[0]][j[1]] > 0:
                counter = 0
                break
            #穴空いてた時カウント
            else:
                counter += 1
        #ビンゴの時
        if counter == 5:
            return 1
    return 0

def check_num(bingo_card,num):
    for i in range(len(bingo_card)):
        for j in range(len(bingo_card[i])):
            if bingo_card[i][j] == num:
                bingo_card[i][j] = 0
    return bingo_card

def make_bingo_card():
    size = 5
    bingo_card=[]
    arr = make_arr()

    #ランダムにしたやつ必要部分だけソート
    sorted_arr = sorted(arr[0:size*(size+1)])
    #分割して2次元に
    for i in range(size):
        bingo_card.append(sorted_arr[size*i:size*(i+1)])
    #対角入れ替え
    for i in range(size):
        for j in range(i,size):
            tmp = bingo_card[i][j]
            bingo_card[i][j] = bingo_card[j][i]
            bingo_card[j][i] = tmp
    return bingo_card

#def bingo():

bingo_card = make_bingo_card()
number = make_arr()
counter = 0

while check_bingo(bingo_card) == 0:
    #番号の確認
    bingo_card = check_num(bingo_card,number[counter])
    print_matrix(bingo_card)
    counter += 1


import crt_function
import random
import sys
sys.setrecursionlimit(100000)


def create_li(num, n, d):  # 建立按顺序的随机数列表
    li = []
    n_range = len(str(n))
    low = n_range//d+1
    high = n_range//(d-1)
    for i in range(num):
        temp = random.randrange(pow(10,low),pow(10,high))
        while temp in li:
            temp = random.randrange(pow(10,low),pow(10,high))
        li += [temp]
    li.sort()
    return li


def check_li(t, d, PLAINTEXT):  # 基于（3,5）密钥为PLAINTEXT
    first = 1
    last = 1
    dset = [2, 4]
    while (not (first > PLAINTEXT > last)) or crt_function.check(dset) == 0:
        dset = create_li(d, PLAINTEXT, t)
        first = 1
        last = 1
        for i in range(t):  # 计算前t项乘积
            first = first * dset[i]
        for j in range(t-1):  # 计算后d-t项乘积
            last = last * dset[-j-1]
    return dset, first, last


def caculate_ki(d, KEY, dset):  # 计算第i个人的密钥
    k = []
    user = []
    for i in range(d):
        k.append(KEY % dset[i])
        temp = (k[i], dset[i])
        user.append(temp)  # 第i个人的密钥
    return user, k


with open("./secret7.txt") as f:
    PLAINTEXT = int(f.readline())
    t = 3     # 安全参数
    d = 5
    dset, first, last = check_li(t, d, PLAINTEXT)
    user, k = caculate_ki(d, PLAINTEXT, dset)
    m = random.sample([i for i in range(d)], t)  # 5个值中任意选择3个值的索引
    k_solve = [k[i] for i in m]
    d_solve = [dset[i] for i in m]
    print("选择的三组数为：")
    print([user[i] for i in m])
    solved_crt = crt_function.crt_funtion(k_solve + d_solve)
    print("明文是：" + str(solved_crt))

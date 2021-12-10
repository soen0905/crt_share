import copy


def inverse(a, b):  # x为待模数，y为模数 求逆元
    if b == 0:
        return 1, 0
    else:
        x, y = inverse(b, a % b)
        return y, (x - (a // b) * y)


def create_M(Y):  # 建立对应数的其它数的乘积
    M = []
    temp = 1
    for i in Y:
        temp = i * temp
    for k in Y:
        M.append(temp // k)
    return M, temp


def solve(T, X, M):  # 求解函数 T中是对应的模逆元的列表，X中是对应的模数
    result = 0
    for num in range(len(T)):
        i, j, m = T[num], X[num], M[num]
        result += i * j * m

    return result


def init(Data):  # 对数据进行初始化，X中存储待模数，Y中存储模数
    X = []
    Y = []
    for i in range(len(Data) // 2):
        X.append(Data[i])
        Y.append(Data[i + len(Data) // 2])
    return X, Y


def check(li):  # 确认数之间是否两两互素
    check_li = copy.deepcopy(li)
    for i in check_li:
        check_li.remove(i)
        for j in check_li:
            p, q = i, j
            while p % q != 0:
                p, q = q, p % q
            if q != 1:
                # print(str(i) + "\n和" + str(j) + "\n不互素")
                return 0
            else:
                pass
    return 1


# 主函数：
def crt_funtion(r_data):
    X, Y = init(r_data)
    if check(Y) == 0:
        pass
    else:
        M, multi_m = create_M(Y)
        INVERSE = []
        for s in range(len(M)):
            m, y = M[s], Y[s]
            T_m, T_y = inverse(m, y)
            INVERSE.append(T_m % y)
        print("选择的三个数的模逆是")
        print(INVERSE)
        result = solve(INVERSE, X, M) % multi_m
        # print("解为：" + str(result))
        return result


if __name__ == '__main__':
    with open("./16.txt") as f:
        r_data = []
        for i in f.readlines():
            r_data.append(int(i))
    crt_funtion(r_data)

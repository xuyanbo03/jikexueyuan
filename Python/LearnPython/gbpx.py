def gb(arr):  # 第一次归并排序，以及持续调用rg()函数进行后续的归并
    arr_t = [[arr[0]]]  # 把传进去的数组的元素变为数组的形式，后续使用
    k = 0
    m = ""

    if len(arr) % 2 == 0:  # 如果原长度为偶数，l均分
        l = len(arr) / 2
    else:  # 原长度为奇数，l分一半后+1
        l = len(arr) + 1

    for t in range(0, l):
        m = "h" + m
    arr_rg = list(m)  # 生成一个存储数据的列表arr_rg，长度为l
    for i in range(1, len(arr)):
        arr_t = arr_t + [[arr[i]]]  # 生成一个列表，将原列表的元素变为列表，即两层列表，调用rg函数，该函数数据类型为列表

    if len(arr_t) % 2 == 0:  # 第一次归并，为偶数
        for i in range(0, len(arr_t), 2):  # 从0位开始，每次增加2个
            arr_rg[k] = dg(arr_t[i], arr_t[i + 1])  # 第i位与i+1位排列
            k += 1
    else:  # 为奇数
        for i in range(0, len(arr_t) - 2, 2):  # 先进行偶数位
            arr_rg[k] = dg(arr_t[i], arr_t[i + 1])
            k += 1
        arr_rg[k] = arr_t[len(arr_t) - 1]  # 偶数位排完，直接将一个奇数位移到新存储数组arr_rg最后一位

    n = 0
    while 1:  # 第一趟结束，后续归并一直调用arr_rg函数，直到长度为1
        if len(arr_rg) == 1:  # 长度为1，停止
            break
        else:  # 调用arr_rg函数参数是每次归并的结果
            arr_rg = rg(arr_rg)


def rg(arr_rg):  # 依次对arr_rg进行归并
    k = 0
    s = len(arr_rg[0])  # s代表每组多少元素
    l = len(arr_rg)  # l代表一共有多少组，比较多少组

    if len(arr_rg) % 2 == 0:  # 组的个数为偶数
        for i in range(0, len(arr_rg), 2):
            arr_rg[k] = dg(arr_rg[i], arr_rg[i + 1])  # 将两个有序列表arr_[i],arr_rg[i+1]用dg函数合并
            k += 1  # k为排序后数组arr_rg的下标
        arr_rg = arr_rg[:l / 2]  # arr_rg二合一，产生多余元素，将多余元素舍去
        return arr_rg
    else:  # 为奇数
        for i in range(0, len(arr_rg) - 2, 2):
            arr_rg[k] = dg(arr_rg[i], arr_rg[i + 1])  # 将两个有序列表arr_[i],arr_rg[i+1]用dg函数合并
            k += 1  # k为排序后数组arr_rg的下标
        arr_rg = arr_rg[:l / 2] + [arr_rg[len(arr_rg) - 1]]  # arr_rg二合一，产生多余元素，将多余元素舍去，将最后一个奇数放下来
        return arr_rg


def dg(arr1, arr2):  # 两个有序数列之间排序
    x = len(arr1)  # x为有序列表arr1的长度
    y = len(arr2)  # y为有序列表arr2的长度
    i = 0
    j = 0
    k = 0
    m = ""

    for t in range(0, x + y):
        m = "h" + m
    arr_ok = list(m)  # 生成一个列表，长度为x+y，合并之后长度增大

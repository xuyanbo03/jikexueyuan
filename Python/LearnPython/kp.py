# 快排总调用函数
def kp(arr, i, j):
    if i < j:
        base = kpgc(arr, i, j)
        kp(arr, i, base)  # 递归,以base为分割
        kp(arr, base + 1, j)


# 快排排序过程
def kpgc(arr, i, j):
    base = arr[i]  # 以第一个为基准点
    while i < j:
        while i < j and arr[j] >= base:
            j -= 1
        # 交叉变换转为单向变换，把左基准指针赋给右基准指针
        while i < j and arr[j] < base:
            arr[i] = arr[j]
            i += 1
            arr[j] = arr[i]
    arr[i] = base
    return i


ww = [3, 2, 4, 1, 59, 23, 13, 1, 3]
kp(ww, 0, len(ww) - 1)
print(ww)

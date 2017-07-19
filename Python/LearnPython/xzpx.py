def xzpx(arr):
    for i in range(0, len(arr)):  # 每一趟排序
        k = i  # k为标记位，指向最小的数
        for j in range(i + 1, len(arr)):  # 每一趟选择最小的这个数
            if arr[j] < arr[k]:
                k = j
        arr[i], arr[k] = arr[k], arr[i]  # 交换为止


abc = [3, 2, 4, 14, 6, 27, 1, 70]
xzpx(abc)
print(abc)

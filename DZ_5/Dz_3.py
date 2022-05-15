import time
if __name__ == "__main__":
    in_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    # res_list = [number for i, number in enumerate(in_list) if i > 0 and in_list[i] > in_list[i - 1]]
    res_list = [num1 for num1, num2 in zip(in_list[1:], in_list[:-1]) if num1 > num2]
    t = time.perf_counter()
    print(time.perf_counter() - t)
    print(res_list)
from sqlalchemy import Boolean


def check_dominant(n: int) -> Boolean:
    n_str = str(n)
    s = set(list(n_str))
    for i in list(s):
        if list(n_str).count(i) > len(n_str) / 2:
            return True
    return False

N = 6
cnt = 0
# for i in range(10**(N-1),10**N):
#     if check_dominant(i):
#         # print(i)
#         cnt += 1

# print(cnt)

print(check_dominant(232322))

# 1: 9
# 2: 9
# 3: 9*9*3 + 9
# 4: 9*9*4 + 9
# 5: 9*9*8*(5 over 3) + 9*9*(5 over 3) + 9*9*(5 over 4) + 9
# 6: 9*9*8*(6 over 4) + 9*9*(6 over 4) + 9*9*(6 over 5) + 9
# 7: 9*9*8*7*(7 over 4) + 9*9*
x5 = 603
x6 = 9*9*8*(5*4) + 9*9*20 + 9*9*6 + 9
x7 = 9*9*8*7*(7*6*5/6) + 9*9


# print(check_dominant(223))
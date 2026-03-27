def reverse_digit(num):
    for i in range(len(num)-1, -1, -1):
       print(num[i], end='')

tr = str(input("뒤집을 숫자나 문자열을 입력하세요: "))

reverse_digit(tr)


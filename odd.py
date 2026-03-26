i = int(input("어디 까지 홀수를 골라 드릴까요? "))
for j in range(1, i+1):
    if j % 2 == 1:
        print(f"{j}, ", end='')



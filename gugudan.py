#구구단 출력하기
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i * j:2d}", end='|')
    print(' ')

#약간 수정
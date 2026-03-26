k = int(input("몇층을 만들까요?"))

for i in range(1, k*2, 2):
    j = (k*2-i)//2
    print(" "*j + "*"*i + " "*j)

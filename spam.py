from operator import truediv

title = input("제목을 입력하세요: ")
banned_set = {'free', 'money', 'lucky', '행운', '바보', '성인'}

def Isspam(tt):
    tt = tt.lower()
    tt = tt.replace('!', '')
    tt = tt.replace('.', '')
    tt = tt.replace('?', '')
    words = tt.split(" ")
    words_set = set(words)
    print(words_set)
    print(words_set.intersection(banned_set))
    if words_set.intersection(banned_set):
        return True
    else:
        return False


if Isspam(title):
    print("스팸입니다.")
else:
    print("스팸이 아닙니다.")


text = input("판별할 문장을 입력하세요 : ")

def ispalindrome(words):
    cleaned = [ch.lower() for ch in text if ch.isalnum() ]
    print(words)
    print(words[::-1])
    return cleaned == cleaned[::-1]

if ispalindrome(text):
    print("팰린드롬입니다")
else:
    print("팰린드롬이 아닙니다.")
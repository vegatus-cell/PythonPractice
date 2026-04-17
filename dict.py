d1 = {"a":10, "b":20, "c":30, "d":40}
d2 = {"가":10, "나":20, "다":30, "라":40}

print(min(d1.values()))
print(min(d1.keys()))

pc_parts = { "CPU": 950000, "RAM": 420000, "SSD": 195000, "GPU": 1850000, "Mainboard": 330000, "Case": 75000,"Power": 98000 }

a_parts = {k: v for k, v in pc_parts.items() if v<=200000}
usd_parts = {k.lower():round(v/1450) for k,v in pc_parts.items()}

print(pc_parts)
print(a_parts)
print(usd_parts)

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ' ': '/'
}

def encrypt(message):
    cipher = ''
    for letter in message:
        if letter.upper() in MORSE_CODE_DICT:
            cipher += MORSE_CODE_DICT[letter.upper()] + ' '
        else:
            # 딕셔너리에 없는 특수문자 등은 무시
            continue
    return cipher.strip()

if __name__ == "__main__":
    text = input("문장을 입력하세요: ")
    print(encrypt(text))
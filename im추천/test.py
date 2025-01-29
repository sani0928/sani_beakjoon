arr = [0,0,0,1,0]
n = len(arr)

if all(arr[i] == 0 for i in range(n)):
    print('True')
else:
    print('False')

words = ["hello", "3", "python"]
if all(word.isalpha() for word in words):
    print("모든 요소가 알파벳만 포함합니다.")
else:
    print("알파벳 이외 문자가 있는 요소가 있습니다.")

words = "1ab2"
if any(word.isdigit() for word in words):
    print("숫자가 포함되어 있습니다.")
else:
    print("숫자가 포함되지 않았습니다.")
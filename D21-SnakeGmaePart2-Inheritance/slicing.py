piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
piano_tuple = ["do", "re", "mi", "fa", "so", "la", "si"]

print(piano_keys[::2])   # 하나씩 거르고 모두 가져온다
print(piano_keys[::-1])  # 맨뒤에서부터 가져온다 reverse
print(piano_keys[:5])    # 다섯번째 까지 모두 가져온다
print(piano_keys[1:])    # 첫번째 띄고 가져온다
print(piano_keys[1:5:2]) # 첫번째부터 다섯번쨰까지 가져오는데 하나 걸러 하나씩 가져온다

# tuple도 완전히 똑같이 작용한다
# 파일을 열어주는 방법1. close()를 항상 해줘야 하고 잊으면 자원 낭비!!
file = open("my_file.txt")
content = file.read()
print(content)
file.close()        # 굉장히 중요, open()으로 열었으면 close()로 무조건 닫아주자


# 파일을 열어주는 방법2.
with open("my_file.txt") as file:
    content = file.read()
    print(content)

# 파일을 쓰는법
with open("my_file.txt", mode="w") as file:
    content = file.write("바꿔버려!!!!!!!!!!!!")
    print(content)  # 몇글자인지를 출력 해주네...!?!?

# 파일에 추가 하는법
with open("my_file.txt", mode="a") as file:
    file.write("\n추가한 줄")

# 원래 없던 파일명을 작성하면 새롭게 만들어줌
with open("new_my_file.txt", mode="w") as file:
    file.write("파일을 만들면서 새로운 텍스트 추가")
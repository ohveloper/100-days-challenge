class User:

    ### init 함수를 생성하면 새로운 객체를 생성 할때마다 무조건 데이터를 전달 해야 한다.
    def __init__(self, user_id, username):  # parameter (매개변수)
        print("new user being created...")
        self.id = user_id  # attributes (속성)
        self.username = username
        self.follower = 0  # 기본값을 할당할수 있음
        self.following = 0

    def follow(self, user):
        user.follower += 1
        self.following += 1


# def function():
#     pass # 무엇이 되었던 빈 상태로 두고 넘어가는것

# 최초에 배우는 방식
# user1 = User()
# user1.name = "minkyo"
# user1.id = "001"

# __init__ 배운뒤
user_1 = User("001", "Minkyo")
user_2 = User("002", "Shay")

user_1.follow(user_2)

print(user_1.username, "follower", user_1.follower)
print(user_1.username, "following", user_1.following)
print(user_2.username, user_2.follower)
print(user_2.username, user_2.following)

# print(user_1.id)
# print(user_1.follower)

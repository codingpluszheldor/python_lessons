class Autorization():
    def __init__(self):
        self.user_names = {}

    def adminka(self):
        self.user_names["root"] = "root123"
        self.user_names["user"] = "user123"
        self.user_names["admin"] = "admin123"

    def login(self, user_name, password):
        for user, passw in self.user_names.items():
            if user_name == user and password == passw:
                return True
        return False

sys_auth = Autorization()
sys_auth.adminka()
print(sys_auth.user_names)
user_name = input("Введите имя пользователя: ")
password = input("Введите пароль: ")
result = sys_auth.login(user_name, password)
if result == True:
    print(">__")
else:
    print("Ошибка авторизаци")
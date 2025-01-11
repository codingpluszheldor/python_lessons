class Autorization():
    def __init__(self):
        self.users_params = {}

    def adminka(self):
        self.users_params["root"] = "root12345"
        self.users_params["user"] = "user12345"
        self.users_params["admin"] = "admin12345"
        print(self.users_params)

    def safe_login(self, user_name, password):
        for user in self.users_params:
            if user_name == user and password == self.users_params[user]:
                return True

        return False

    def version(self):
        return "Версия 3.0"

sys_auth = Autorization()
print(sys_auth.version())
sys_auth.adminka()
user_name = input("Введите имя пользователя: ")
password = input("Введите пароль: ")
if sys_auth.version() == "Версия 3.0":
    result = sys_auth.safe_login(user_name, password)
else:
    result = sys_auth.login(user_name, password)

if result == True:
    print(">_")
else:
    print("Ошибка авторизации")

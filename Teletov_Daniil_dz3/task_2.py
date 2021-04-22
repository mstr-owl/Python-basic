def user_info(**kwargs):
    return list(kwargs.values())


def en_user_info():
    return
print(user_info(name="Henry", surname="Cavill", birth_year=1983, live_town="New_York", email="henrycav83@mail.com", phone=892222123239))
# print(user_info(name=input('Enter name: '), surname=input('Enter second name: '), birth_year=input('Enter birth year: '), live_town=input('Enter live town: '), email=input('Enter email: '), phone=input('Enter phone number: ')))

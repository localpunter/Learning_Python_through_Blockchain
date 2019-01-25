name = "Alan Hunter"
age = 45

print(name, age)


def concat_name_and_age(user_name, user_age):
    name_and_age = (user_name, user_age)
    return name_and_age


def get_user_name():
    user_name = str(input("Please type your name: "))
    return user_name


def get_user_age():
    user_age = str(input("Please enter your age: "))
    return user_age

def get_decades_you_have_lived():
    decades_lived = int(45 // 10)
    return decades_lived

user_name = get_user_name()
user_age = get_user_age()
name_and_age = (user_name, user_age)
concat_name_and_age(user_name, user_age)
int_age = int(user_age)
decades_lived = (int_age // 10)

print("You are", user_name, "-", "Age:", user_age)
print("You have lived for", decades_lived, "decades")

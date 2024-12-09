"""
student = {"name": "鈴木", "class": "3A"}
student["score"] = 85
del student["class"]
print(student)

print("更新表示")


age = input("年齢を入力してください：")
print("あなたは" + age + "歳です")

def add(x, y):

    return x + y

result = add(1,3)

print(result)


def multiply(a, b=2):
    return a * b
print(multiply(3))
"""

def modify_value(x):
    x = x + 1
    return x

num = 6
modify_value(num)
print(num)

def calculate_points(score, bonus=10):
    return score + bonus
print(calculate_points(80))
print(calculate_points(80, 20))
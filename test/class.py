# 面向对象
# 设计一个类
"""
class Student:
    name = None
    gender = None
    country = None
    native_place = None
    age = None

# 创建一个对象并且进行赋值
stu_1 = Student()
stu_1.name = "林俊杰"
stu_1.gender = "男"
stu_1.country = "中国"
stu_1.native_place = "山东省"
stu_1.age = 19
"""

# 类 变量与方法
# self
import random

"""
class Student:
    name = None

    def say_hi(self):
        print("hello")
        print(f"大家好， 我是{self.name}")

    def say_hi2(self, msg):
        print(f"hello. {msg}")

stu = Student()
stu.name = "陈奕迅"
stu.say_hi()
stu.say_hi2("大家好")
"""

# 属性和行为
"""
class Clock:
    id = None
    price = None

    def ring(self):
        import winsound
        winsound.Beep(2000, 3000)

clock1 = Clock()
clock1.id = "003032"
clock1.price = "19.9"
print(f"id:{clock1.id}, price:{clock1.price}")
clock1.ring()
"""

# 构造方法 __init__()
"""
class Student:
    name = None
    age = None
    tel = None

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("Student类创建了一个类对象")

stu = Student("张敬轩", "19", "187182")
"""

# Exercise
"""
class Student:
    name = None
    age = None
    address = None

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

for i in range(10):
    stu = Student(input("请输入学生姓名："), input("请输入学生年龄："), input("请输入学生家庭住址:"))
    print(f"学生{i+1}信息录入完成， 信息为：【学生姓名：{stu.name}, 年纪：{stu.age}, 地址：{stu.address}】")
"""


# 内置方法
# __str__：字符串方法 控制类转化为字符串的方法
# __lt__: 小于/大于符号比较方法 return
# __le__: 小于等于/大于等于符号比较方法
# __eq__: 等于符号比较方法

# 封装
# 私有成员 以__开头
"""
class Phone:
    __current_voltage = 0.1

    def __keep_single_core(self):
        print("让cpu以单核模式运行")

    def call_by_5g(self):
        if self.__current_voltage >= 1:
            print("5g通话已经开启")
        else:
            print("电量不足")
            self.__keep_single_core()

phone = Phone()
# phone.__keep_single_core()
phone.call_by_5g()
"""

# Exercise 详见视频117
# 单继承 多继承（继承顺序从左到右）
# pass
"""
class Phone:
    IMEI = None
    producer = "HM"

    def call_by_4g(self):
        print("4g,正在通话中")

class Phone2024(Phone):
    face_id = "19829"

    def call_by_5g(self):
        print("5g,正在通话中")

phone = Phone2024
print(phone.producer)
"""

# 复写父类成员
"""
class Phone:
    IMEI = None
    producer = "ITCAST"

    def call_by_5g(self):
        print("父类的5g,正在通话中")

class Myphone(Phone):
    producer = "huawei"

    def call_by_5g(self):
        # 父类的调用
        print(f"{Phone.producer}")
        print(f"父类的厂商是：{super().producer}")
        super().call_by_5g()
        
        print("子类的5g,正在通话中")

phone = Myphone()
print(phone.producer)
phone.call_by_5g()
"""

# 类型注解
# 基础数据类型注解
"""
var_1: int = 10
var_2: str = "ithema"
var_3: bool = True

# 类对象类型注解
class Student:
    pass
stu: Student = Student()

# 基础容器类型注解
my_list: list[int] = [1, 2, 3]
my_tuple: tuple[int, str, bool] = (1, "ithema", True)
my_dict: dict[str, int] = {"ithema": 666}


# 在注释中进行类型注解
var_4 = random.randint(1, 10)  # type: int
"""

# 类型注解的限制: 提示性而非决定性 注解错误不会报错

# 形参注解 返回值注解
"""
def add(x: int, y: int):
    return x + y

def func(data: list) -> list:
    return data

add()
func()
"""

# Union类型
"""
from typing import Union

my_list: list[Union[str, int]] = [1, 2, "ithema", "itcast"]
my_dict: dict[str, Union[str, int]] = {"name": "周杰伦", "age": 31}

def func(data: Union[int, str]) -> Union[int, str]:
    pass

func()
"""

# 多态
"""
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("汪汪汪")

class Cat(Animal):
    def speak(self):
        print("喵喵喵")

def make_noise(animal: Animal):
    animal.speak()

dog = Dog()
cat = Cat()

make_noise(dog)
make_noise(cat)
"""

# 演示抽象类
"""
class AC:
    def cool_wind(self):
        pass

    def hot_wind(self):
        pass

    def swing_l_r(self):
        pass

class Midea_AC(AC):
    def cool_wind(self):
        print("美的空调制冷")

    def hot_wind(self):
        print("美的空调制热")

    def swing_l_r(self):
        print("美的空调左右摆风")

class GREE_AC(AC):
    def cool_wind(self):
        print("格力空调制冷")

    def hot_wind(self):
        print("格力空调制热")

    def swing_l_r(self):
        print("格力空调左右摆风")

def make_cool(ac: AC):
    ac.cool_wind()

midea_ac = Midea_AC()
gree_ac = GREE_AC()

make_cool(midea_ac)
make_cool(gree_ac)
"""
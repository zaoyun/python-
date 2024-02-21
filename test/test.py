# print的用法 以及传递变量
"""
money = 50
money = money - 10
print("购买了冰激凌，钱包里面还有:", money)
money = money - 5
print("购买了可乐，钱包里面还有:", money)

"""

# 字符串 浮点数 整数的转换

"""
num_str = str(11)
print(type(num_str), num_str)

float_str = str(11.345)
print(type(float_str), float_str)

num = int("11")
print(type(num), num)

num2 = int("11")
print(type(num2), num2)

"""

# 复合赋值运算符
# +=： c = c + a

# 字符串定义法
'黑马'
"黑马"
# name = """黑马"""

"""
单引号
双引号
三引号
转义字符
"""

# 字符串拼接: +
# 字符串格式化: %占位符
"""
print("我的名字是" + name + ",我可以")

class_num = 57
avg_salary = 16781
print("Python大数据学科，北京%s期，毕业平均工资：%s" % (class_num, avg_salary))
"""

# s将变量转换为了字符串
# %d 整数
# %f 浮点数 需要数字精度控制：m.n m控制宽度 n控制小数点精度+四舍五入 %3.5f

"""
name = "wwn"
print("我的名字是%", name)
"""

# 字符串格式化： f 不做精度控制 可以格式化表达式
"""
name = "传智播客"
set_up_year = 2006
stock_price = 19.99
print(f"我是{name}, 我成立于：{set_up_year}, 我今天的股票价格是：{stock_price}")
"""

# Exercise
""""
name = "传智播客"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth_factor = 1.2
growth_days = 7
print(f"公司：{name}，股票代码：{stock_code}，当前股价：{stock_price}")
print("每日增长系数是：%.1f, 经过%d天的增长后，股价达到了：%.2f" % (
    stock_price_daily_growth_factor, growth_days, stock_price * stock_price_daily_growth_factor ** 7))
"""

# 输入input
"""
print("请告诉我你是谁")
name = input()
print("Get!!! 你是：%s" % name)
"""
"""
user_name = input("用户名称:")
user_type = input("用户类型:")
print(f"您好：{user_name}，您是尊贵的：{user_type}用户，欢迎您的光临")
"""

# True = 1 and False = 0 bool
"""
result1 = 10 > 5
print(f"输出结果是：{result1}")

result2 = "it cast" == "isuid"
print(f"输出结果是：{result2},类型是：{type(result2)}")
"""

# bool 类型的定义
"""
bool_1 = True
bool_2 = False
print(f"bool_1变量的内容是:{bool_1},类型是{type(bool_1)}")
print(f"bool_2变量的内容是:{bool_2},类型是{type(bool_2)}")
"""

# if 语句的基本格式: 缩进部分收到if控制 + Exercise
"""
print("欢迎来到黑马儿童游乐园，儿童免费，成人收费。")
age = input("请输入你的年龄:")
age = int(age)
if age >= 18:
    print("您已经成年，游玩需要补票10元。")

print("祝您游玩愉快")
"""

# if else 组合用法 + Exercise
"""
age = int(input("请输入你的年龄："))
if age > 18:
    print("您已经成年")
else:
    print("您未成年")
"""

"""
print("欢迎来到黑马动物园")
height = int(input("请输入你的身高（cm):"))

if height > 120:
    print("您的身高超出120cm，游玩需要购票10元。")
else:
    print("您的身高未超出120cm，可以免费游玩。")

print("祝您游玩愉快")
"""

# if +多个elif+else 注意顺序 多条件互斥
"""
print("欢迎来到黑马游乐园。")
if int(input("请输入你的身高（cm):")) < 120:
    print("您的身高小于120cm，可以免费游玩。")
elif int(input("请输入你的vip级别（1-5):")) > 3:
    print("您的vip级别大于三，可以免费游玩")
elif int(input("请告诉我今天是几号：")) == 1:
    print("今天是一号，是免费日可以免费游玩")
else:
    print("不好意思所有条件都不满足，需要购票10元。")

print("祝您游玩愉快。")
"""

# 判断语句的嵌套：空格缩进决定层次
"""
print("欢迎来到黑马游乐园")
if int(input("请输入你的身高（cm):")) > 120:
    print("您的身高大于120cm，不可以免费游玩")
    print("不过如果你的vip等级高于3，可以免费游玩")
    if int(input("请输入你的vip级别（1-5):")) > 3:
        print("您的vip级别大于三，可以免费游玩")
    else:
        print("Sorry, 你需要补票10元")
else:
    print("祝您游玩愉快。")
"""

# 随机数
"""
import random
num = random.randint(1, 10)
"""

# while 循环
"""
i = 1
num = 0
while i <= 100:
    num += i
    i += 1
print(f"1-100累加的结果是：{num}")
"""

# while 猜数字
"""
num = random.randint(1, 100)
count = 0
flag = True
while flag:
    guess = int(input("请输入猜测的数字："))
    count += 1
    if guess == num:
        print("恭喜你猜对了")
        flag = False
    elif guess > num:
        print("猜大了")
    elif guess < num:
        print("猜小了")

print(f"一共猜了{sum}次")
"""

# while 嵌套运用 99乘法表
# 想要print不换行 end=''
# \t 可以使得多行字符串进行对齐
"""
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j}*{i}={j * i}\t ", end='')
        j += 1
    print()
    i += 1
"""

# for循环
# for临时变量 in待处理数据集：循环满足条件时所执行的代码
# 遍历
"""
name = "itheima"
for x in name:
    print(x)

"""

# Exercise
"""
name = "itheima is a brand of itcast"
count = 0
for x in name:
    if x == "a":
        count += 1
        
print(f"次数为{count}")
"""

# range语句 数字序列(从0开始，不包括括号里面的数字本身）2为步长
"""
range(5)
range(5, 10)
range(5, 10, 2)

for x in range(5, 10, 2):
    print(x)

count = 0
for x in range(1, 100):
    if x % 2 == 0:
        count += 1
print(f"{count}")
"""

# for循环 99乘法表
"""
for x in range(1, 10):
    for y in range(1, x + 1):
        print(f"{y}*{x}={y * x}\t", end='')
    print()
"""

# break and continue
# break 直接跳出循环
# continue 中断本次循环，直接进行下一次循环
"""
for i in range(1, 6):
    print("语句1")
    continue
    print("语句2")
"""

# 发工资案例
"""
salary = 10000

for x in range(1, 21):
    import random
    performance = random.randint(1, 10)
    if performance < 5:
        print(f"员工{x}，绩效分{performance}，低于5，不发工资，下一位。")
        continue
    else:
        salary -= 1000
        print(f"满足条件，向员工{x}发放工资1000元，账户余额还剩余{salary}元。")
        if salary == 0:
            print("工资发完了，下一个月再领取吧。")
            break
        else:
            continue
"""

# 函数：将特定功能封装在函数内， 可供随时重复利用
"""
def 函数名(传入参数)：
    函数体
    return 返回值
"""

# 传入参数
"""
def add(x, y, z):
    result = x + y + z
    print(f"{x}+{y}+{z}的结果是：{result}")


add(5, 6, 9)
"""

# 函数的返回值
# 空返回值 None
# 对于函数进行文档说明
"""
def add(a, b):
    result = a + b
    return result


r = add(1, 2)
print(r)
"""

# 函数的嵌套
"""
def func_b():
    print("2")


def func_a():
    print("1")
    func_b()
    print("3")


func_a()
"""

# 局部变量：函数体内部的变量
# 全局变量：在函数体内部和外部都可以使用的变量
# global 修改全局变量
# 综合案例：ATM
"""
money = 5000000
name = input("请输入您的姓名：")


def query():
    print("---------查询余额---------")
    print(f"{name},您好，您的余额剩余：{money}")


def saving(num):
    global money
    money += num
    print("---------存款---------")
    print(f"{name},您好，您存款{num}元成功。")
    print(f"{name},您好，您的余额剩余：{money}")


def get_money(num):
    global money
    money -= num
    print("---------取款---------")
    print(f"{name},您好，您取款{num}元成功。")
    print(f"{name},您好，您的余额剩余：{money}")


def main():
    print("---------主菜单---------")
    print(f"{name},您好，欢迎来到ICBC银行。请选择操作：")
    print("查询余额\t\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return input("请输入您的选择：")


while True:
    keyboard_input = main()
    if keyboard_input == "1":
        query()
        continue
    elif keyboard_input == "2":
        num = int(input("您想要存多少钱？请输入："))
        saving(num)
        continue
    elif keyboard_input == "3":
        num = int(input("您想要取多少钱？请输入："))
        get_money(num)
        continue
    else:
        print("程序退出啦")
        break
"""

# 数据容器：列表list 元组tuple 字符串str 集合set 字典dict

# list + 嵌套列表
"""
name_list = ['clion', 'java', 'python']
print(name_list)
print(type(name_list))

my_list = [[1, 2, 3], 1, 2, 3]
print(my_list)
"""

# 列表中的下标索引
# 0 1 2 3... 正向索引
# -1 -2 -3 -4... 反向索引
"""
name_list = ['clion', 'java', 'python']
print(name_list[0])
print(name_list[1])
print(name_list[2])

my_list = [[1, 2, 3], [4, 5, 6]]
print(my_list[1][1])
"""

# 列表方法
# index 查询下表索引数(正向）
# 修改特定位置（索引）的元素值
# insert 插入元素
# append 追加元素
# extend 追加元素（多个）
# del / pop 删除元素
# remove 删除第一个匹配项
# clear 清空列表
# count 某一个元素在列表中的数量
# len 统计列表中的全部元素数量
"""
my_list = ['clion', 'java', 'python']
index = my_list.index('java')
print(index)

my_list = ['clion', 'java', 'python']
my_list[1] = "kkv"
print(my_list)

my_list = ['clion', 'java', 'python']
my_list.insert(1, "opencv")
print(my_list)

my_list = ['clion', 'java', 'python']
my_list.append("opencv")
print(my_list)

my_list = ['clion', 'java', 'python']
my_list2 = [1, 2, 3]
my_list.extend(my_list2)
print(my_list)

my_list = ['clion', 'java', 'python']
del my_list[2]
print(my_list)

my_list = ['clion', 'java', 'python']
element = my_list.pop(2)
print(element)
print(my_list)

my_list = ['clion', 'java', 'python', 'clion']
my_list.remove('clion')
print(my_list)

my_list = ['clion', 'java', 'python', 'clion']
my_list.clear()
print(my_list)

my_list = ['clion', 'java', 'python', 'clion']
count = my_list.count('clion')
print(count)

my_list = ['clion', 'java', 'python', 'clion']
count = len(my_list)
print(count)
"""

# Exercise
"""
my_list = [21, 25, 21, 23, 22, 20]
print(my_list)

my_list.append(31)
print(my_list)

my_list = [21, 25, 21, 23, 22, 20]
my_list2 = [29, 33, 30]
my_list.extend(my_list2)
print(my_list)

my_list = [21, 25, 21, 23, 22, 20]
num1 = my_list[0]
num2 = my_list[-1]

num3 = my_list.index(31)
"""

# while 遍历列表
"""
mylist = ['clion', 'java', 'python', 'clion']
index = 0
while index < len(mylist):
    print(mylist[index])
    index += 1
"""

# for 遍历列表
"""
mylist = ['clion', 'java', 'python', 'clion']
for i in mylist:
    print(i)
"""

# Exercise
"""
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = []
index = 0
while index < len(list1):
    yuansu = list1[index]
    if yuansu % 2 == 0:
        list2.append(yuansu)
    index += 1

print(list2)

print("---------------------------------------")

list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
list4 = []
for yuansu in list3:
    if yuansu % 2 == 0:
        list4.append(yuansu)

print(list4)
"""

# 元组一旦定义完成，不可修改
# 嵌套
# index count len 与list相似
# while 遍历列表
# for 遍历列表
"""
t1 = (1, 'hello', True)
t2 = (1,)
t3 = ((1, 2, 3), (4, 5, 6))

t4 = (1, 'hello', True, 66, 89)

index = 0
while index < len(t4):
    print(f'{t4[index]}')
    index += 1
    
for i in t4:
    print(f'{i}')
"""

# Exercise
"""
q1 = ('周杰伦', 11, ['football', 'music'])
age = q1.index(11)
print(f'年龄所在下标：{age}')
print(f"姓名：{q1[0]}")
del q1[2][0]
print(f'删掉足球爱好{q1}')
q1[2].insert(0, 'coding')
print(f'添加爱好coding{q1}') 
"""

# 字符串：不可修改数据容器，只可以存储字符串
# 下标索引取值
# index
# replace
# split 分割字符串为列表
# strip 规整字符串
# count
# len
# 遍历
"""
name = 'itheima and itcast'
print(name[0])
print(name[-1])

new = name.replace('it', '程序')
print(new)

my_str = "hello python itheima itcast"
my_str_list = my_str.split(" ")
print(my_str_list)

my_str = '  itheima and itcast  '
new_my_str = my_str.strip() # 不传入参数去除收尾空格
print(new_my_str)

my_str = '12itheima and itcast21'
new_my_str = my_str.strip('12') #去除字符串1和2
print(new_my_str)
"""

# 序列list str tuple+切片[起始：结束：步长] 步长可以为正/负，不包含结束本身
"""
my_list = [0, 1, 2, 3, 4, 5, 6]
result = my_list[1:4:1]
print(result)
"""

# Exercise
"""
my_str = '万过薪月，员序程马黑来,nohtyP学' 
result1 = my_str[::-1][9:14]
print(result1)


result2 = my_str.split("，")[1].replace("来", "")[::-1]
print(result2)
"""

# 集合{}:去重，乱序
# add 添加新元素
# remove 移除新元素
# pop随机取出一个元素
# clear清空
# 取两个集合的差集 difference （集合1有的 集合2没有的）
# 消除差集 difference_update (在集合1内部， 删除和集合2相同的元素）
# 合并集合 union
# 长度 len
# 集合的遍历 不支持while（无下标索引） 支持for
"""
my_set = {"传智教育", "黑马程序员", "itheima", "传智教育", "黑马程序员", "itheima", "传智教育", "黑马程序员", "itheima"}
print(my_set)

my_set.add("python")
my_set.add("传智教育")
print(my_set)

my_set.remove("python")
print(my_set)

element = my_set.pop()
print(element)

my_set.clear()
print(my_set)

set1 = {1, 2, 3}
set2 = {1, 4, 5}
set3 = set1.difference(set2)
print(set3)

set1 = {1, 2, 3}
set2 = {1, 4, 5}
set1.difference_update(set2)
print(set1)
print(set2)

set1 = {1, 2, 3}
set2 = {1, 4, 5}
set3 = set1.union(set2)
print(set3)

set1 = {1, 2, 3, 6, 7}
num = len(set1)
print(num)

set1 = {1, 2, 3, 6, 7}
for i in set1:
    print(i)
"""

# 字典
# 定义空字典
# 使用key进行索引
# 字典的嵌套
# 新增元素
# 更改元素
# pop 删除元素
# clear 清空
# keys 获取全部的key
# for 遍历
# len 长度
"""
my_dict_1 = dict()
my_dict_2 = {}

stu_score = {"王力宏": 99, "周杰伦": 88, "陈奕迅": 77}
print(stu_score["王力宏"])

stu_score = {
    "王力宏": {"语文": 99, "数学": 66, "英语": 89},
    "周杰伦": {"语文": 45, "数学": 63, "英语": 48},
    "陈奕迅": {"语文": 76, "数学": 61, "英语": 78}
}
print(stu_score["王力宏"]["数学"])

stu_score = {"王力宏": 99, "周杰伦": 88, "陈奕迅": 77}
stu_score["张学友"] = 32
print(stu_score)

stu_score["王力宏"] = 66
print(stu_score)

stu_score = {"王力宏": 99, "周杰伦": 88, "陈奕迅": 77}
stu_score.pop("王力宏")
print(stu_score)

stu_score.clear()
print(stu_score)

stu_score = {"王力宏": 99, "周杰伦": 88, "陈奕迅": 77}
keys = stu_score.keys()
print(keys)

for element in keys:
    print(element)

for i in stu_score:
    print(i)
"""

# Exercise
"""
stu_score = {
    "王力宏": {"部门": "科技部", "工资": 3000, "级别": 1},
    "周杰伦": {"部门": "市场部", "工资": 5000, "级别": 2},
    "陈奕迅": {"部门": "市场部", "工资": 7000, "级别": 3},
    "张敬轩": {"部门": "科技部", "工资": 4000, "级别": 1},
    "林俊杰": {"部门": "市场部", "工资": 6000, "级别": 2}
}

for worker in stu_score:
    if stu_score[worker]["级别"] == 1:
        stu_score[worker]["工资"] += 1000
        stu_score[worker]["级别"] += 1

print(stu_score)
"""

# max最大元素
# min最小元素
# 容器转换 list() tuple() str() set()
# sorted 排序的结果都会成为列表对象
# 正向排序 sorted()
# 反向排序 sorted(my_list, reverse = True)

# ASCII 码表
# 字符串大小比较

# 函数多返回值
"""
def test_return():
    return 1, 2, "Hello"
x, y, z = test_return()
print(x)
print(y)
print(z)
"""

# 函数传参
# 位置参数
"""
def user_info(name, age, gender):
    print(f"您的名字是{name}, 年龄是{age}, 性别是{gender}")
user_info("TOM", 20, "男")"""

# 关键字传参 可以不按照顺序
"""
def user_info(name, age, gender):
    print(f"您的名字是{name}, 年龄是{age}, 性别是{gender}")

user_info(name="小明", age=20, gender="男")
"""

# 缺省参数 默认参数必须写到最后面
"""
def user_info(name, age, gender='男'):
    print(f"您的名字是{name}, 年龄是{age}, 性别是{gender}")

user_info('小天', 13)
user_info('小天', 13, '女') 
"""

# 位置不定长传递(元组）
"""
def user_info(*args):
    print(args)

user_info('Tom')
user_info('Tom', 19)
"""

# 关键字不定长传递（字典）
"""
def user_info(**kwargs):
    print(kwargs)
    
user_info(name="小明", age=18, gender="男")
"""

# 回调函数
"""
def test_func(compute):
    result = compute(1, 2)
    print(result)

def compute(x, y):
    return x + y

test_func(compute)
"""

# 匿名函数 lambda 只可以临时使用一次
# lambda 传入参数： 函数体（一行代码）
"""
def test_func(compute):
    result = compute(1, 2)
    print(result)

test_func(lambda x, y: x + y)
"""

# 文件编码: 内容与二进制相互转换 一般是UTF-8
# 打开文件 open(name, mode, encoding)
# mode r只读 w写入 a追加
# read：读取指定长度字节
# readlines：一次性读取所有内容
# readline()：一次读取一行内容
# for 循环读取 一次读取一行内容
# f.close() 关闭文件
# with open 关闭

"""
f = open("E:/Python_project/测试.txt", "r", encoding="UTF-8")
print(f.read(8))
print(f.read())

f = open("E:/Python_project/测试.txt", "r", encoding="UTF-8")
content = f.readlines()
print(content)

f = open("E:/Python_project/测试.txt", "r", encoding="UTF-8")
content1 = f.readline()
content2 = f.readline()
print(content1)
print(content2)

f = open("E:/Python_project/测试.txt", "r", encoding="UTF-8")
for line in f:
    print(line)

f.close()
time.sleep(500000)

with open("E:/Python_project/测试.txt", "r", encoding="UTF-8") as f:
    for line in f:
        print(line)

time.sleep(500000)
"""

# Exercise
"""
# 方法1
f = open("E:/Python_project/word.txt", "r", encoding="UTF-8")
content = f.read()
count = content.count("itheima")
print(count)

# 方法2
f = open("E:/Python_project/word.txt", "r", encoding="UTF-8")
count = 0
for line in f:
    line = line.replace("\n", "")
    words = line.split(" ")
    print(words)
    for word in words:
        if word == "itheima":
            count += 1

print(count)
f.close()
"""

# 文件写入 write w模式
# 内容刷新 flush/close自带flush功能
"""
f = open("E:/Python_project/测试.txt", "w")
f.write("hello world")
f.flush()
f.close()
"""

# 文件的追加 a模式
"""
f = open("E:/Python_project/测试.txt", "a")
f.write("\nhello world")
f.flush()
f.close()
"""

# Exercise 文件的读取与选择性备份
"""
fr = open("E:/Python_project/bill.txt", "r", encoding="UTF-8")
fw = open("E:/Python_project/bill.txt.bak", "w", encoding="UTF-8")

for line in fr:
    line = line.strip()
    if line.split("，")[-1] == '测试':
        continue

    fw.write(line)
    fw.write("\n")

fr.close()
fw.close()
"""

# 代码异常 debug
# 捕获异常
"""
try:
     可能发生错误的代码
except:
     如果出现异常执行的代码
"""

# 捕获指定的异常
# 捕获多个异常
"""
try:
    print(name)
    print(1/0)
except (NameError, ZeroDivisionError) as e:
    print("出现了未被定义的变量")
    print("ZeroDivision错误")
"""

# 捕获全部异常
"""
try:
    print(name)
except Exception as e:
    print("出现异常")
"""

# 没有异常 else
# finally 无论如何是否异常都要执行的代码: 例如关闭文件
"""
try:
    print("hello")
except Exception as e:
    print("出现异常")
else:
    print("没有异常")
finally:
    fileinput.close()
"""

# 异常的传递性

# 模块的导入
# [from 模块名] import [模块|类|变量|函数|*][as 别名]
"""
import time
print("你好")
time.sleep(5)
print("我好")
"""

# from
"""
from time import sleep
print("开始")
sleep(5)
print("结束")
"""

# * 导入所有内容
"""
from time import *
print("开始")
sleep(5)
print("结束")
"""

# 别名定义
"""
import time as tt
tt.sleep(2)
print("hello")
"""

# 自定义模块.py
# 导入不同模块的同名功能 最后的被执行
# __main__ 变量 __name__内置变量
# _all_变量 当使用from xxx import * 导入时， 只能导入这个列表中的元素
"""
if __name__ == '__main__':
    test(1, 2)
"""

# python包
# import 包名.模块名
# 包名.模块名.目标
# _all_变量 控制 import*
# 第三方包安装 python内部安装/命令行安装 清华包位置：https://pypi.tuna.tsinghua.edu.cn/simple

# Exercise
"""
import my_utils.str_util
from my_utils import file_util

print(my_utils.str_util.str_reverse("黑马程序员"))
print(my_utils.str_util.substr("ithema", 0, 4))

file_util.print_file_info("E:/Python_project/bill.txt")
file_util.append_to_filr("E:/Python_project/bill.txt", "hello")
"""

# json 轻量级的数据交互格式
# 格式 字典dict / 列表里面嵌套字典

"""
# 导入json模块
import json

# 符合格式的数据
data = [{"name": "老王", "age": 16}, {"name": "张三", "age": 20}]

# python数据转化为了json数据
# ensure_ascii=False确保中文编码问题
data = json.dumps(data, ensure_ascii=False)
print(data)

# json数据转化为了python数据
data = json.loads(data)
print(data)
"""

# pyecharts 模块
# 基础折线图
"""
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts

# x, y轴坐标设置
line = Line()
line.add_xaxis(["中国", "美国", "英国"])
line.add_yaxis("GDP", [30, 20, 10])

# 设置全局配置项
# 标题名称与位置设置
line.set_global_opts(
    title_opts=TitleOpts(title="各国GDP展示", pos_left="center", pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)
)
# 将代码生成为图像
line.render()
"""

# 数据处理
"""
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, LabelOpts

f_us = open("E:/Python_project/折线图数据/美国.txt", "r", encoding="UTF-8")
us_data = f_us.read()

f_jp = open("E:/Python_project/折线图数据/日本.txt", "r", encoding="UTF-8")
jp_data = f_jp.read()

f_in = open("E:/Python_project/折线图数据/印度.txt", "r", encoding="UTF-8")
in_data = f_in.read()

# 删除不符合JSON规范的开头和结尾
us_data = us_data.replace("jsonp_1629344292311_69436(", "")
us_data = us_data[:-2]

jp_data = jp_data.replace("jsonp_1629350871167_29498(", "")
jp_data = jp_data[:-2]

in_data = in_data.replace("jsonp_1629350745930_63180(", "")
in_data = in_data[:-2]

# JSON转化为字典
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)

# 获取trend key
us_trend_data = us_dict['data'][0]['trend']
jp_trend_data = jp_dict['data'][0]['trend']
in_trend_data = in_dict['data'][0]['trend']

# 获取日期数据， 用于x轴， 取2020年(到314下标结束）
us_x_data = us_trend_data['updateDate'][:314]
jp_x_data = jp_trend_data['updateDate'][:314]
in_x_data = in_trend_data['updateDate'][:314]

# 获取确认数据， 用于y轴， 到2020年（到314下标结束）
us_y_data = us_trend_data['list'][0]['data'][:314]
jp_y_data = jp_trend_data['list'][0]['data'][:314]
in_y_data = in_trend_data['list'][0]['data'][:314]

# 生成图表
line = Line()

line.add_xaxis(us_x_data)
line.add_yaxis("美国确诊人数", us_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本确诊人数", jp_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度确诊人数", in_y_data, label_opts=LabelOpts(is_show=False))

# 设置全局选项
line.set_global_opts(
    title_opts=TitleOpts(title="2020年美日印三国确诊人数对比折线图", pos_left="center", pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True)
)

line.render()

f_us.close()
f_jp.close()
f_in.close()
"""

# 地图可视化的基本使用
# RGB
"""
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

map = Map()

data = [
    ("北京市", 99),
    ("上海市", 199),
    ("湖南省", 299),
    ("台湾省", 399),
    ("广东省", 499)
]

map.add("测试地图", data, "china")

map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 9, "label": "1-9", "color": "#CCFFFF"},
            {"min": 10, "max": 99, "label": "10-99", "color": "#FF6666"},
            {"min": 100, "max": 500, "label": "100-500", "color": "#990033"}
        ]
    )
)

map.render
"""

# Exercise
"""
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts, TitleOpts

f = open("E:/Python_project/地图数据/疫情.txt", "r", encoding="UTF-8")
data = f.read()
f.close()

data_dict = json.loads(data)
province_data_list = data_dict["areaTree"][0]["children"]

data_list = []
for province_data in province_data_list:
    province_name = province_data["name"] + "市"         # 省份名称
    province_confirm = province_data["total"]["confirm"] # 确诊人数
    data_list.append((province_name, province_confirm))

map = Map()
map.add("各个省份确诊人数", data_list, "china")
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 99, "label": "1-99", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "label": "100-999", "color": "#FFF999"},
            {"min": 1000, "max": 4999, "label": "1000-4999", "color": "#FF9966"},
            {"min": 5000, "max": 9999, "label": "5000-9999", "color": "#FF6666"},
            {"min": 10000, "max": 99999, "label": "10000-99999", "color": "#CC3333"},
            {"min": 100000, "label": "100000+", "color": "#990033"},
        ]
    ),
)

map.render("全国疫情地图.html")
"""

# 动态柱状图+时间线
"""
from pyecharts.charts import Bar, Timeline
from pyecharts.options import *

bar1 = Bar()
bar1.add_xaxis(["中国", "美国", "英国"])
bar1.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position="right"))
# 反转x， y轴
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(["中国", "美国", "英国"])
bar2.add_yaxis("GDP", [50, 30, 20], label_opts=LabelOpts(position="right"))
bar2.reversal_axis()

timeline = Timeline()
timeline.add(bar1, "2021年GDP")
timeline.add(bar2, "2022年GDP")
# 自动播放
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)
timeline.render("动态柱状图+时间线.html")
"""

# Exercise
"""
from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType

f = open("E:/Python_project/动态柱状图数据/1960-2019全球GDP数据.csv", "r", encoding="GB2312")
data_lines = f.readlines()
f.close()

# 删除第一条没用的数据
data_lines.pop(0)
# 将数据转换为字典存储
# {1960:[[美国，123],[中国,321],....],1961:[[美国，123],[中国,321],....],......}
data_dict = {}
for line in data_lines:  # line是str,所以才要用split
    year = int(line.split(',')[0])  # 年份
    country = line.split(',')[1]  # 国家
    gdp = float(line.split(',')[2])  # GDP 不用考虑\n因为尽管data_lines 里面有\n，但是遍历变成lines之后\n变成了下一行，运行后可以看到。
    # 如何判断字典里面有没有指定的key呢
    try:
        data_dict[year].append([country, gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country, gdp])

# 创建时间线对象(设置主题)
timeline = Timeline({'theme': ThemeType.LIGHT})
# 排序年份
sorted_year_list = sorted(data_dict.keys())
for year in sorted_year_list:
    data_dict[year].sort(key=lambda element: element[1], reverse=True)
    # 取出本年前8名的国家
    year_data = data_dict[year][0:8]
    x_data = []
    y_data = []
    for country_gdp in year_data:
        x_data.append(country_gdp[0])
        y_data.append(country_gdp[1] / 100000000)

    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis('GDP(亿)', y_data, label_opts=LabelOpts(position='right'))
    # 反转X轴和Y轴
    bar.reversal_axis()
    # 设置每一年图表的标题
    bar.set_global_opts(
        title_opts=TitleOpts(title=f'{year}年全球GDP前8数据')
    )
    timeline.add(bar, str(year))

# 设置时间自动播放
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=False
)

timeline.render('1960-2019全球GDP前8国家.html')
"""
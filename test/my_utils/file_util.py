def print_file_info(file_name):
    """
    功能是：将给定路径的文件内容输出到控制台中
    :param file_name: 即将读取的文件路径
    :return: None
    """
    f = None
    try:
        f = open(file_name, "r", encoding="UTF-8")
        content = f.read()
        print("文件的全部内容如下：")
        print(content)
    except Exception as e:
        print(f"程序出现异常了，原因是：{e}")
    finally:
        if f:
            f.close()

def append_to_filr(file_name, data):
    """
    功能：将指定的数据追加到指定的文件中
    :param file_name:指定文件的路径
    :param data:指定的数据
    :return:None
    """
    f = open(file_name, "a", encoding="UTF-8")
    f.write("\n")
    f.write(data)
    f.write("\n")
    f.close()



if __name__ == '__main__':
    print_file_info("E:/Python_project/bill.txt")
    append_to_filr("E:/Python_project/bill.txt", "hello")
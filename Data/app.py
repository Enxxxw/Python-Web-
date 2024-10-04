"""
用户注册：
    - 用户信息需要存储在 users/account.txt
"""
import os

while True:
    user = input(">>>")
    line = "{}\n".format(user)

    # 确保文件所在目录已存在 users（不存在，就创建）
    folder_path = os.path.join("users")
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # 所在文件夹必须已存在
    file_path = os.path.join(folder_path, 'account.txt')
    file_object = open(file_path, mode='a', encoding='utf-8')
    file_object.write(line)
    file_object.close()
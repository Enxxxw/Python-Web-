import shutil

# base_name，压缩包的文件名
# format，后缀名
# root_dir，压缩的文件夹的路径
# shutil.make_archive(base_name='db', format='zip', root_dir="db")


# filename，压缩包的文件名
# extract_dir，要解压的目录
# format，后缀名
shutil.unpack_archive(filename="db.zip", extract_dir="DB", format='zip')
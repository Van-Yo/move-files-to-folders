import os	# 对文件操作
import shutil	# 移动文件用
# 遍历其中的文件
# 判断是否有对应的文件夹，如果没有就先创建文件夹然后移动文件，如果有，直接移动文件

# 找到打开文件的路径
path = './'
# 将路径中的文件列成一个列表
files = os.listdir(path)
for f in files:
	# 对文件进行以后缀进行分割，并取后缀作为文件夹的名称
	folder_name = path + f.split('.')[-1]
	if not os.path.exists(folder_name):
		# 创建文件夹
		os.makedirs(folder_name)
		# 移动文件
		shutil.move(f,folder_name)
	else:
		# 移动文件
		shutil.move(f,folder_name)

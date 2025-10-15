import os
import tifffile
import numpy as np
from PIL import Image

# 读取单个图像
def read_image(image_path):
    image = Image.open(image_path)  # 使用PIL库读取图像
    return np.array(image)

# 处理文件夹中的所有PNG文件并拼接成3D TIFF
def process_folder(input_folder, output_folder):
    # 获取所有子文件夹
    subfolders = [f.path for f in os.scandir(input_folder) if f.is_dir()]
    
    # 遍历每个子文件夹
    for subfolder in subfolders:
        # 获取子文件夹中的所有PNG文件
        png_files = sorted([f for f in os.listdir(subfolder) if f.endswith('.png')])
        
        # 读取所有PNG图像并堆叠成三维数组
        image_stack = []
        for png_file in png_files:
            image_path = os.path.join(subfolder, png_file)
            image = read_image(image_path)
            image_stack.append(image)

        # 将所有图像堆叠为三维数组（假设是 (num_images, height, width)）
        image_stack = np.stack(image_stack, axis=0)
        
        # 保存为TIFF文件
        output_filename = os.path.basename(subfolder) + ".tiff"
        output_path = os.path.join(output_folder, output_filename)
        tifffile.imwrite(output_path, image_stack)
        
        print(f"Saved 3D TIFF for folder: {subfolder}")

# 设置输入和输出文件夹路径
input_folder = "/mnt/no1/chenzh/Data/一影/metal_trace_人工/标注数据"  # 替换为你包含子文件夹的父文件夹路径
output_folder = "/mnt/no1/chenzh/Data/一影/metal_trace_人工_tiff"  # 替换为保存输出TIFF文件的文件夹路径

# 确保输出文件夹存在
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 处理文件夹
process_folder(input_folder, output_folder)
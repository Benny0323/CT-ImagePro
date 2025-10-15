import os
import tifffile
import numpy as np

# 读取图像
def read_image(image_path):
    image = tifffile.imread(image_path)  # 使用 tifffile 读取 .tif 文件
    return image

# 执行转置操作
def process_image(image):     # 假设图像是三维的 (300, 1024, 1024)
    # 执行转置
    return np.transpose(image, (1, 0, 2))  # 转置为 (1024, 300, 1024)

# 保存图像
def save_image(image, output_path):
    tifffile.imwrite(output_path, image)

# 提取每个切片并保存
def process_image_slices(image, output_folder, base_filename):
    # 获取图像的维度 (depth, height, width)
    image = process_image(image)    
    depth = image.shape[0]

    # 遍历每一张切片
    for i in range(depth):
        slice_image = image[i, :, :]  # 假设是 (depth, height, width) 的三维图像
        slice_filename = f"{base_filename}_slice_{i+1}.tif"
        output_path = os.path.join(output_folder, slice_filename)
        
        # 保存每个切片
        save_image(slice_image, output_path)
        print(f"Saved slice {i+1} as {output_path}")

# 处理文件夹中的所有 .tif 文件
def process_images_in_folder(input_folder, output_folder):
    # 获取文件夹中的所有 .tif 文件
    tif_files = [f for f in os.listdir(input_folder) if f.endswith('.tiff')]

    # 遍历每个 .tif 文件
    for tif_file in tif_files:
        input_path = os.path.join(input_folder, tif_file)
        base_filename = os.path.splitext(tif_file)[0]  # 获取文件名不包含扩展名
        
        # 读取图像
        image = read_image(input_path)

        # 提取并保存每一张切片
        process_image_slices(image, output_folder, base_filename)

# 设置输入文件夹和输出文件夹
input_folder = "/mnt/no1/chenzh/Data/一影/proj_img_tif"  # 替换为你的输入文件夹路径
output_folder = "/mnt/no1/chenzh/Data/一影/proj_img_sinogram_slices"  # 替换为你的输出文件夹路径

# 确保输出文件夹存在
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 处理文件夹中的所有 .tif 文件
process_images_in_folder(input_folder, output_folder)
from PIL import Image
import os
import sys

def compress_png(image_path, output_path, quality=60, resize_percent=None):
    try:
        with Image.open(image_path) as img:
            # 如果指定了调整大小的百分比，则调整图像大小
            if resize_percent and resize_percent < 100:
                original_width, original_height = img.size
                new_width = int(original_width * resize_percent / 100)
                new_height = int(original_height * resize_percent / 100)
                img = img.resize((new_width, new_height), Image.LANCZOS)
                
            # 最大化压缩 - 降低位深度并增加压缩选项
            if img.mode == 'RGBA':
                # 保持透明度但最大化压缩
                img = img.convert('RGBA')
                # 尝试减少颜色深度但保留透明度
                img = img.quantize(colors=256, method=2, kmeans=1, dither=Image.FLOYDSTEINBERG).convert('RGBA')
            else:
                # 对非透明图像进行更强的压缩
                img = img.convert('P', palette=Image.ADAPTIVE, colors=256)
            
            # 保存时应用最大压缩
            img.save(output_path, "PNG", optimize=True, quality=quality, compress_level=9)
            
            # 显示压缩前后的文件大小
            original_size = os.path.getsize(image_path) / 1024  # KB
            compressed_size = os.path.getsize(output_path) / 1024  # KB
            reduction = (1 - compressed_size / original_size) * 100
            
            print(f"压缩: {os.path.basename(image_path)}")
            print(f"  原始大小: {original_size:.2f} KB")
            print(f"  压缩后大小: {compressed_size:.2f} KB")
            print(f"  减少: {reduction:.2f}%")
            
            return True
    except Exception as e:
        print(f"压缩 {image_path} 时出错: {str(e)}")
        return False

def batch_compress_png(input_folder, output_folder, quality=60, resize_percent=None):
    if not os.path.exists(input_folder):
        print(f"错误: 输入文件夹 '{input_folder}' 不存在")
        return False
        
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"创建输出文件夹: {output_folder}")

    success_count = 0
    fail_count = 0
    total_files = 0
    
    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.png'):
            total_files += 1
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            
            if compress_png(input_path, output_path, quality, resize_percent):
                success_count += 1
            else:
                fail_count += 1
    
    print(f"\n压缩完成:")
    print(f"  总文件数: {total_files}")
    print(f"  成功: {success_count}")
    print(f"  失败: {fail_count}")
    
    return success_count > 0

if __name__ == "__main__":
    # 允许通过命令行参数指定文件夹和质量
    if len(sys.argv) > 2:
        input_folder = sys.argv[1]
        output_folder = sys.argv[2]
        quality = int(sys.argv[3]) if len(sys.argv) > 3 else 60
        resize_percent = int(sys.argv[4]) if len(sys.argv) > 4 else None
    else:
        # 默认设置
        input_folder = 'halloffamesrc'  # 输入文件夹路径
        output_folder = 'halloffame'  # 输出文件夹路径
        quality = 60
        resize_percent = 80  # 默认调整为原始大小的80%
    
    print(f"开始压缩PNG图片:")
    print(f"  输入文件夹: {input_folder}")
    print(f"  输出文件夹: {output_folder}")
    print(f"  质量设置: {quality}")
    if resize_percent:
        print(f"  调整大小: 原始尺寸的{resize_percent}%\n")
    else:
        print(f"  调整大小: 保持原始尺寸\n")
    
    batch_compress_png(input_folder, output_folder, quality=quality, resize_percent=resize_percent)

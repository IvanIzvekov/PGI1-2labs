# 1lab

# def convert_to_grayscale(input_file, output_file):
#     with open(input_file, 'rb') as f:
#         header = f.read(54)
#
#         palette = f.read(1024)
#
#         new_palette = bytearray()
#         for i in range(0, len(palette), 4):
#             average_color = sum(palette[i:i+3]) // 3
#             new_palette.extend([average_color, average_color, average_color, 0])
#
#         with open(output_file, 'wb') as new_f:
#             new_f.write(header)
#             new_f.write(new_palette)
#             new_f.write(f.read())
#
def get_bmp_info(file):
    with open(file, 'rb') as f:
        header = f.read(54)

        file_type = header[:2].decode('utf-8')
        file_size = int.from_bytes(header[2:6], byteorder='little')
        reserved1 = int.from_bytes(header[6:8], byteorder='little')
        reserved2 = int.from_bytes(header[8:10], byteorder='little')
        pixel_array_offset = int.from_bytes(header[10:14], byteorder='little')
        width = int.from_bytes(header[18:22], byteorder='little')
        height = int.from_bytes(header[22:26], byteorder='little')
        color_depth = int.from_bytes(header[28:30], byteorder='little')
        print(f"Width: {width}, Height: {height}, Color Depth: {color_depth} bits")
        print(f'File type: {file_type}')
        print(f'File size: {file_size} bytes')
        print(f'Reserved 1: {reserved1}')
        print(f'Reserved 2: {reserved2}')
        print(f'Color depth: {color_depth}')
        print(f'Pixel array offset: {pixel_array_offset}')


# input_file = 'CAT256.BMP'
# output_file = 'CAT256_gray.BMP'
#
# get_bmp_info(input_file)
# convert_to_grayscale(input_file, output_file)
#


# 2lab


# import random
# import struct
#
# def add_random_border(input_file, output_file, border_width):
#     with open(input_file, 'rb') as f:
#         header = f.read(54)
#
#         image_data = f.read()
#
#         width = int.from_bytes(header[18:22], byteorder='little')
#         height = int.from_bytes(header[22:26], byteorder='little')
#         bits_per_pixel = int.from_bytes(header[28:30], byteorder='little')
#
#         border_colors = [bytes([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]) for _ in range(border_width)]
#
#         new_image_data = bytearray()
#         for y in range(height):
#             for x in range(width):
#                 if x < border_width or x >= width - border_width or y < border_width or y >= height - border_width:
#                     new_image_data.extend(border_colors[x % border_width])
#                 else:
#                     new_image_data.extend(image_data[y * width * 3 + x * 3 : y * width * 3 + x * 3 + 3])
#
#             padding = b'\x00' * (4 - (len(new_image_data) % 4)) if len(new_image_data) % 4 != 0 else b''
#             new_image_data.extend(padding)
#
#         new_header = bytearray(header)
#         new_header[18:22] = width.to_bytes(4, byteorder='little')
#         new_header[22:26] = height.to_bytes(4, byteorder='little')
#
#         with open(output_file, 'wb') as new_f:
#             new_f.write(new_header)
#             new_f.write(new_image_data)
#
# input_file = '_сarib_TC.bmp'
# output_file = '_carib_TC_with_border.bmp'
# # input_file = 'CAT256.BMP'
# # output_file = 'CAT256.BMP_with_border.bmp'
# border_width = 15
#
# add_random_border(input_file, output_file, border_width)


# 3lab

# def add_random_border(input_file, output_file):
#     with open(input_file, 'rb') as f:
#         header = f.read(54)
#
#         image_data = f.read()
#
#         width = int.from_bytes(header[18:22], byteorder='little')
#         height = int.from_bytes(header[22:26], byteorder='little')
#
#         new_image_data = bytearray()
#         for x in range(width):
#             for y in range(height):
#                 new_image_data.extend(image_data[y * width * 3 + x * 3 : y * width * 3 + x * 3 + 3])
#
#             padding = b'\x00' * (4 - (len(new_image_data) % 4)) if len(new_image_data) % 4 != 0 else b''
#             new_image_data.extend(padding)
#
#         new_header = bytearray(header)
#         new_header[18:22] = height.to_bytes(4, byteorder='little')
#         new_header[22:26] = width.to_bytes(4, byteorder='little')
#
#         with open(output_file, 'wb') as new_f:
#             new_f.write(new_header)
#             new_f.write(new_image_data)
#
# input_file = '_сarib_TC.bmp'
# output_file = '_carib_TC_rotate.bmp'
#
# add_random_border(input_file, output_file)

# 5lab ДОДЕЛАТЬ

# import struct
# 
# # Открываем исходный BMP файл
# with open('CAT256.BMP', 'rb') as file:
#     header = file.read(54)
#     pallet = file.read(1024)
#     pixels = file.read()
# 
# # Получаем ширину и высоту изображения из заголовка
# width = struct.unpack('<i', header[18:22])[0]
# height = struct.unpack('<i', header[22:26])[0]
# 
# # Создаем список коэффициентов масштабирования от 0.1 до 10
# scaling_factors = [0.1, 0.5, 1, 2, 5]
# 
# # Применяем каждый коэффициент масштабирования к изображению
# for factor in scaling_factors:
#     # Масштабируем изображение
#     new_width = int(width * factor)
#     new_size = int(len(pixels) * factor ** 2 + 54 + 1024)
#     new_height = int(height * factor)
# 
#     scaled_pixels = bytearray()
#     count = 0
#     for y in range(new_height):
#         buff = bytearray()
#         for x in range(new_width):
#             orig_x = int(x / factor)
#             orig_y = int(y / factor)
#             buff.append(pixels[orig_y * width + orig_x])
#         if len(buff) % 4 != 0:
#             padding = b'\x00' * (4 - (len(buff) % 4))
#         else:
#             padding = b''
#         buff.extend(padding)
#         scaled_pixels.extend(buff)
#     # Обновляем заголовок файла с новой шириной и высотой
#     new_header = bytearray(header)
#     new_header[18:22] = new_width.to_bytes(4, byteorder='little')
#     new_header[22:26] = new_height.to_bytes(4, byteorder='little')
#     new_header[2:6] = new_size.to_bytes(4, byteorder='little')
# 
#     # Записываем новый BMP файл с масштабированным изображением
#     with open(f'scaled_image_{factor}.bmp', 'wb') as new_file:
#         new_file.write(new_header)
#         new_file.write(pallet)
#         new_file.write(scaled_pixels)
#     print(f'Масштабирование {factor} завершено')
# 
# print("Масштабирование завершено")
# get_bmp_info('CAT256.BMP')
# get_bmp_info('scaled_image_1.bmp')


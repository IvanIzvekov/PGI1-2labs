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
# file = open('CAT256.BMP', 'rb')
# header = file.read(54)
# pallet = file.read(1024)
# pixels = bytearray()
#
# # Получаем ширину и высоту изображения из заголовка
# width = struct.unpack('<i', header[18:22])[0]
# height = struct.unpack('<i', header[22:26])[0]
# old_pad = 4 - width % 4
# for y in range(height):
#     pixels.extend(file.read(width))
#     file.read(old_pad)
#
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
#
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

# lab 6

# import struct
#
#
# file = open('_сarib_TC.bmp', 'rb')
# original_header = file.read(54)
# original_pixels = bytearray()
#
# original_width = struct.unpack('<i', original_header[18:22])[0]
# original_height = struct.unpack('<i', original_header[22:26])[0]
#
# print(original_width)
# print(original_height)
#
#
# old_pad = 4 - (original_width * 3) % 4
# for y in range(original_height):
#     original_pixels.extend(file.read(original_width * 3))
#     if old_pad > 0 and old_pad != 4:
#         file.read(old_pad)
#
# file = open('logo.bmp', 'rb')
# logo_header = file.read(54)
# trash = file.read(84)
# logo_pixels = bytearray()
#
# logo_width = struct.unpack('<i', logo_header[18:22])[0]
# logo_height = struct.unpack('<i', logo_header[22:26])[0]
#
# for y in range(logo_height):
#     for x in range(logo_width):
#         logo_pixels.extend(file.read(3))
#         file.read(1)
#
# x_margin = 675
# y_margin = 25
# transparency = 0.3
#
# result_pixels = bytearray()
#
# for y in range(original_height):
#     buff = bytearray()
#     for x in range(original_width):
#         for i in range(3):
#             if x_margin <= x < logo_width + x_margin and y_margin <= y < logo_height + y_margin:
#                 if logo_pixels[(y - y_margin) * logo_width * 3 + (x - x_margin) * 3 + 0] == 255 and logo_pixels[(y - y_margin) * logo_width * 3 + (x - x_margin) * 3 + 1] == 255 and logo_pixels[(y - y_margin) * logo_width * 3 + (x - x_margin) * 3 + 2] == 255:
#                     buff.append(original_pixels[y * original_width * 3 + x * 3 + i])
#                 else:
#                     one_byte = int(logo_pixels[(y - y_margin) * logo_width * 3 + (x - x_margin) * 3 + i] * (1 - transparency) + original_pixels[y * original_width * 3 + x * 3 + i] * transparency)
#                     buff.append(one_byte)
#             else:
#                 buff.append(original_pixels[y * original_width * 3 + x * 3 + i])
#
#     if len(buff) % 4 != 0:
#         padding = b'\x00' * (4 - (len(buff) % 4))
#     else:
#         padding = b''
#
#     buff.extend(padding)
#     result_pixels.extend(buff)
#
#     with open('result_with_logo.bmp', 'wb') as new_f:
#         new_f.write(original_header)
#         new_f.write(result_pixels)


# lab 8

# import numpy as np
# import matplotlib.pyplot as plt
#
# def DecodePCX(filePath):
#     with open(filePath, 'rb') as file:
#         header = file.read(128)
#
#         depth = int.from_bytes(header[3:4], 'little')
#
#         width = header[8] + (header[9] << 8) - header[4] - (header[5] << 8) + 1
#         height = header[10] + (header[11] << 8) - header[6] - (header[7] << 8) + 1
#
#         file.seek(-768, 2)
#         palette = np.frombuffer(file.read(), dtype=np.uint8).reshape((256, 3))
#         graphImg = np.zeros((height, width, 3), dtype=np.uint8)
#
#         file.seek(128)
#         x, y = 0, 0
#         while y < height:
#             x = 0
#             while x < width:
#                 byte = int.from_bytes(file.read(1), 'little')
#                 if byte < 192:
#                     graphImg[y, x] = palette[byte]
#                     x += 1
#                 else:
#                     count = byte - 192
#                     repeatedByte = int.from_bytes(file.read(1), 'little')
#                     if count == 1 and repeatedByte == 0:
#                         continue
#
#                     for _ in range(count):
#                         if x >= width:
#                             break
#                         graphImg[y, x] = palette[repeatedByte]
#                         x += 1
#             y += 1
#
#     plt.imshow(graphImg)
#     plt.axis('off')
#     plt.show()
#
#
# DecodePCX("200001.PCX")

# lab7

import struct


def convert_to_bin(s: str):
    c = 0b0
    for i in s:
        c = c | int(i)
        c = c << 1
    c = c >> 1
    return c


file = open('_сarib_TC.bmp', 'rb')
header = file.read(54)
file_size = int.from_bytes(header[2:6], byteorder='little')

width = struct.unpack('<i', header[18:22])[0]
height = struct.unpack('<i', header[22:26])[0]

pixels = bytearray()

old_pad = 4 - (width * 3) % 4
for y in range(height):
    pixels.extend(file.read(width * 3))
    if old_pad > 0 and old_pad != 4:
        file.read(old_pad)

size_mass = [1, 2, 4, 8]

t = 0b11111111
b = "text from file"
w = ''
for i in b:
    w += (format(ord(i), '08b'))

for iteration in size_mass:
    new_image = bytearray()
    step = 0
    for y in range(height):
        buff = bytearray()
        for x in range(width):
            for i in range(3):
                c = w[step:step + iteration]
                c = c[::-1]
                step += iteration
                if step + iteration >= len(w):
                    step = 0

                temp = pixels[y * width * 3 + x * 3 + i]
                temp = temp >> iteration
                temp = temp << iteration
                temp2 = convert_to_bin(c)
                temp = temp | temp2
                # if i > 0:
                #     temp = pixels[y * width * 3 + x * 3 + i]
                buff.append(temp)

        if len(buff) % 4 != 0:
            padding = b'\x00' * (4 - (len(buff) % 4))
        else:
            padding = b''

        buff.extend(padding)
        new_image.extend(buff)

    with open(f'result_stenography_{iteration}.bmp', 'wb') as new_f:
        new_f.write(header)
        new_f.write(new_image)


# izvekov RGR 


import numpy as np
import matplotlib.pyplot as plt


def colorPicker(new_palette, color):
    temp = tuple(color)
    if temp in new_palette:
        return color
    else:
        min = 999999
        min_color = ()
        for i in new_palette:
            delta = pow((temp[0] - i[0]), 2) + pow((temp[1] - i[1]), 2) + pow((temp[2] - i[2]), 2)
            if delta < min:
                min = delta
                min_color = i
        return min_color


def Convert256PCXTo16PCX(filePath):
    with open(filePath, 'rb') as file:
        header = file.read(128)
        new_header = bytearray(header)
        depth = int.from_bytes(header[3:4], 'little')
        new_depth = 2
        width = header[8] + (header[9] << 8) - header[4] - (header[5] << 8) + 1
        height = header[10] + (header[11] << 8) - header[6] - (header[7] << 8) + 1
        new_palette_byte = bytearray()
        file.seek(-768, 2)
        palette = np.frombuffer(file.read(), dtype=np.uint8).reshape((256, 3))
        graphImg = np.zeros((height, width, 3), dtype=np.uint8)

        all_color = {}

        file.seek(128)
        x, y = 0, 0
        while y < height:
            x = 0
            while x < width:
                byte = int.from_bytes(file.read(1), 'little')
                if byte < 192:
                    graphImg[y, x] = palette[byte]

                    temp = tuple(palette[byte])
                    if temp in all_color:
                        all_color[temp] += 1
                    else:
                        all_color[temp] = 1

                    x += 1
                else:
                    count = byte - 192
                    repeatedByte = int.from_bytes(file.read(1), 'little')
                    if count == 1 and repeatedByte == 0:
                        continue

                    for _ in range(count):
                        if x >= width:
                            break
                        graphImg[y, x] = palette[repeatedByte]

                        temp = tuple(palette[repeatedByte])
                        if temp in all_color:
                            all_color[temp] += 1
                        else:
                            all_color[temp] = 1
                        x += 1
            y += 1
        # plt.imshow(graphImg)
        # plt.axis('off')
        # plt.show()

        count = 0
        new_palette = []
        for w in sorted(all_color, key=all_color.get, reverse=True):
            if count == 16:
                break
            temp = []
            for i in range(3):
                if w[i] + 25 >= 256:
                    correct = 255
                    temp.append(correct)
                    new_palette_byte.extend(correct.to_bytes(1, byteorder='little'))
                else:
                    correct = w[i] + 25
                    temp.append(correct)
                    new_palette_byte.extend(correct)
            new_palette.append(temp)
            count += 1

        new_header[3:4] = new_depth.to_bytes(4, byteorder='little')
        new_header[16:64] = new_palette_byte
        file.seek(128)
        x, y = 0, 0
        while y < height:
            x = 0
            while x < width:
                byte = int.from_bytes(file.read(1), 'little')
                if byte < 192:
                    graphImg[y, x] = colorPicker(new_palette, palette[byte])
                    x += 1
                else:
                    count = byte - 192
                    repeatedByte = int.from_bytes(file.read(1), 'little')
                    if count == 1 and repeatedByte == 0:
                        continue
                    for _ in range(count):
                        if x >= width:
                            break
                        graphImg[y, x] = colorPicker(new_palette, palette[repeatedByte])
                        x += 1
            y += 1

    # plt.imshow(graphImg)
    # plt.axis('off')
    # plt.show()

    result_pixels = bytearray()
    y = 0
    while y < height:
        x = 0
        #    2 2  2
        count_repeat = 1
        graph_str = []
        while x < width:
            graph_str.append(tuple(graphImg[y, x]))
            x += 1
        while i < len(graph_str):
            if i != len(graph_str) - 1:
                while graph_str[i] == graph_str[i + 1]:
                    count_repeat += 1
                    i += 1
                    if i == len(graph_str) - 1:
                        break
                    if count_repeat == 63:
                        break
                if count_repeat > 1:
                    result_pixels.extend((192 + count_repeat).to_bytes(1, byteorder='little'))
                    for item in graph_str:
                        temp.append(item)
                    color_index_in_pallet = new_palette.index(temp)
                    result_pixels.extend(color_index_in_pallet.to_bytes(1, byteorder='little'))
                    count_repeat = 1
                else:
                    for item in graph_str:
                        temp.append(item)
                    color_index_in_pallet = new_palette.index(temp)
                    result_pixels.extend(color_index_in_pallet.to_bytes(1, byteorder='little'))
                i += 1
        y += 1

    with open('Converted16.PCX', 'wb') as new_f:
        new_f.write(new_header)
        new_f.write(result_pixels)


Convert256PCXTo16PCX("200001.PCX")

# def convert_to_grayscale(input_file, output_file):
#     with open(input_file, 'rb') as f:
#         # Считываем заголовок файла
#         header = f.read(54)
#
#         # Считываем палитру
#         palette = f.read(1024)
#
#         # Преобразуем палитру в оттенки серого
#         new_palette = bytearray()
#         for i in range(0, len(palette), 4):
#             average_color = sum(palette[i:i+3]) // 3
#             new_palette.extend([average_color, average_color, average_color, 0])
#
#         # Записываем новый файл
#         with open(output_file, 'wb') as new_f:
#             new_f.write(header)
#             new_f.write(new_palette)
#             new_f.write(f.read())
#
# def get_bmp_info(file):
#     with open(file, 'rb') as f:
#         header = f.read(54)
#
#         file_type = header[:2].decode('utf-8')
#         file_size = int.from_bytes(header[2:6], byteorder='little')
#         reserved1 = int.from_bytes(header[6:8], byteorder='little')
#         reserved2 = int.from_bytes(header[8:10], byteorder='little')
#         pixel_array_offset = int.from_bytes(header[10:14], byteorder='little')
#         width = int.from_bytes(header[18:22], byteorder='little')
#         height = int.from_bytes(header[22:26], byteorder='little')
#         color_depth = int.from_bytes(header[28:30], byteorder='little')
#         print(f"Width: {width}, Height: {height}, Color Depth: {color_depth} bits")
#         print(f'File type: {file_type}')
#         print(f'File size: {file_size} bytes')
#         print(f'Reserved 1: {reserved1}')
#         print(f'Reserved 2: {reserved2}')
#         print(f'Pixel array offset: {pixel_array_offset}')
#
# # Пример использования
# input_file = 'CAT256.BMP'
# output_file = 'CAT256_gray.BMP'
#
# get_bmp_info(input_file)
# convert_to_grayscale(input_file, output_file)


import random
import struct

def add_random_border(input_file, output_file, border_width):
    with open(input_file, 'rb') as f:
        # Считываем заголовок файла
        header = f.read(54)

        # Считываем палитру (для TrueColor BMP палитры нет)

        # Считываем данные изображения
        image_data = f.read()

        # Извлекаем информацию о размере изображения
        width = int.from_bytes(header[18:22], byteorder='little')
        height = int.from_bytes(header[22:26], byteorder='little')
        bits_per_pixel = int.from_bytes(header[28:30], byteorder='little')

        # Генерируем цвета для рамки
        border_colors = [bytes([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]) for _ in range(border_width)]

        # Добавляем рамку к изображению
        new_image_data = bytearray()
        for y in range(height):
            for x in range(width):
                if x < border_width or x >= width - border_width or y < border_width or y >= height - border_width:
                    new_image_data.extend(border_colors[x % border_width])
                else:
                    new_image_data.extend(image_data[y * width * 3 + x * 3 : y * width * 3 + x * 3 + 3])

            # Добавляем выравнивающие байты, если необходимо
            padding = b'\x00' * (4 - (len(new_image_data) % 4)) if len(new_image_data) % 4 != 0 else b''
            new_image_data.extend(padding)

        # Обновляем заголовок файла с учетом изменений
        new_header = bytearray(header)
        new_header[18:22] = width.to_bytes(4, byteorder='little')
        new_header[22:26] = height.to_bytes(4, byteorder='little')

        with open(output_file, 'wb') as new_f:
            new_f.write(new_header)
            new_f.write(new_image_data)

# Пример использования
input_file = '_сarib_TC.bmp'
output_file = '_carib_TC_with_border.bmp'
# input_file = 'CAT256.BMP'
# output_file = 'CAT256.BMP_with_border.bmp'
border_width = 15

add_random_border(input_file, output_file, border_width)



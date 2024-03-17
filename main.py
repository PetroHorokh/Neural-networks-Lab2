import supporting_functions as sup_func
from copy import copy
import numpy as np

pic1_pixels = [[0, 0, 0, 0], [255, 0, 255, 255], [255, 0, 255, 255], [255, 0, 255, 255]]
pic2_pixels = [[255, 0, 0, 255], [0, 255, 255, 0], [0, 0, 0, 0], [0, 255, 255, 0]]

sup_func.image_generate(pic1_pixels, "pic1")
sup_func.image_generate(pic2_pixels, "pic2")

pic_test1_pixels = [[0, 255, 0, 0], [255, 0, 255, 255], [255, 0, 255, 255], [255, 0, 255, 255]]
pic_test2_pixels = [[255, 255, 255, 255], [0, 255, 255, 0], [0, 0, 0, 0], [0, 255, 255, 0]]
pic_test3_pixels = [[0, 255, 255, 0], [0, 255, 255, 0], [0, 0, 0, 0], [255, 255, 255, 0]]

sup_func.image_generate(pic_test1_pixels, "pic_test1")
sup_func.image_generate(pic_test2_pixels, "pic_test2")
sup_func.image_generate(pic_test3_pixels, "pic_test3")

path = ["pic1.png", "pic2.png"]
test_images_path = ["pic_test1.png", "pic_test2.png", "pic_test3.png"]

template_images = sup_func.load_standards(path)

n = sup_func.image_size ** 2
m = len(template_images)
T = n / 2
E_max = 1
e = 1 / n
w = [[template_images[i][j] / 2 for j in range(n)] for i in range(m)]

for test_image_path in test_images_path:
    test_image = sup_func.read_image(test_image_path)

    Y = [[sup_func.action_function(sum([test_image[i] * w[j][i] for i in range(n)]), T) for j in range(m)], [[]]]
    Y[1] = Y[0]
    while 1:
        temp_y = copy(Y[1])
        for j in range(m):
            c = sum(Y[1][0:j])
            d = sum(Y[1][j + 1:])
            s = Y[1][j] - e * (c + d)
            Y[1][j] = sup_func.action_function(s, T)
        if np.linalg.norm(np.array(Y[1]) - np.array(temp_y)) < E_max:
            break
    print(f"for image \"{test_image_path}\" result is:{Y[1]}")


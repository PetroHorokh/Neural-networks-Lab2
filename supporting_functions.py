from PIL import Image, ImageDraw

image_size = 4


def image_generate(coloring: list[list[int]], file_name):
    img = Image.new("L", (image_size, image_size))
    draw = ImageDraw.Draw(img)
    try:
        for i in range(image_size):
            for j in range(image_size):
                draw.point((i, j), fill=coloring[j][i])
    except Exception as e:
        print(e)
    else:
        img.save(f"{file_name}.png")
    finally:
        del draw


def load_standards(paths: list[str]):
    x = []
    for path in paths:
        binary_vector = read_image(path)
        x.append(binary_vector)
    return x


def read_image(file_name):
    img = Image.open(file_name)

    if img.mode != 'RGB':
        img = img.convert('RGB')

    pix = img.load()
    width, height = img.size
    t = []
    for i in range(height):
        for j in range(width):
            if (pix[j, i]) != (0, 0, 0):
                t.append(-1)
            else:
                t.append(1)
    return t


def action_function(s, T):
    if s <= 0:
        return 0
    elif 0 < s <= T:
        return s
    elif s > T:
        return T

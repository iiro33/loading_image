from PIL import Image, ImageDraw
import math

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)


def get_circle_sections(divisions, r):
    angle = 2 * math.pi / divisions
    angles = [i*angle for i in range(divisions)]
    return [[r*math.cos(a), r*math.sin(a)] for a in angles]


def create_loading_ball(ball_x, ball_y, bg_color, ball_color, size, ball_size):
    img = Image.new('RGB', (size, size), bg_color)
    draw = ImageDraw.Draw(img)
    draw.ellipse((ball_x, ball_y, ball_x+ball_size, ball_y+ball_size), fill=ball_color)
    return img


def create_loading_screen(size, bg_color, ball_color, r, scale):
    all_images = []
    blank_space = 2
    ball_size = size / (r / scale)
    center = [size / 2, size / 2]
    circumference = 2 * math.pi * r
    num_balls = int(circumference // (ball_size + blank_space))
    locs = get_circle_sections(num_balls, r)
    for location in locs:
        location[0] += center[0]
        location[1] += center[1]

    for i in range(num_balls):
        img = Image.new('RGB', (size, size), bg_color)
        draw = ImageDraw.Draw(img)
        for j in range(3):
            a = i + j
            if a > len(locs)-1:
                a -= num_balls
            draw.ellipse((locs[a][0], locs[a][1], locs[a][0] + ball_size, locs[a][1] + ball_size), fill=ball_color)
        all_images.append(img)

    return all_images


frames = create_loading_screen(800, BLACK, BLUE, 200, 5)

frames[0].save('loading_balls.gif', format='GIF', append_images=frames[1:], save_all=True, duration=100, loop=0)
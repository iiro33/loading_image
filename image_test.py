from PIL import Image, ImageDraw


def create_ball(ball_x, ball_y, size, color, width=400, height=400, bg_color=(255, 255, 255)):
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    draw.ellipse((ball_x, ball_y, ball_x + size, ball_y + size), fill=color)
    return img


# create array to hold images
frames = []
x, y = 0, 0
# loop-create images
for i in range(80):
    new_frame = create_ball(x, y, 30, (0, 255, 0), bg_color=(0, 0, 255))
    frames.append(new_frame)
    x += 5
    y += 5


# save image
frames[0].save('ball.gif', format='GIF', append_images=frames[1:], save_all=True, duration=20, loop=0)

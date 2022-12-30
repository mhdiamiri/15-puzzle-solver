from PIL import Image, ImageDraw, ImageFont
import numpy as np

font_path = 'times.ttf'
background_color = 'white'
number_color = 'black'
text_color = 'black'
outline = 'white'
fill_color = 'darkgray'
empty = 'lightgray'

def draw(matrix, caption):
    width, height = 170, 190
    textsize, numbersize = 8, 20
    
    img = Image.new("RGB", (width, height), color = background_color)
    font = ImageFont.truetype(font_path, size=numbersize,)
    draw = ImageDraw.Draw(img)

    for i in range(4):
        for j in range(4):
            shape = [(i * 40 + 5, j * 40 + 5) , ((i + 1) * 40 + 5, (j+1) * 40 + 5)]
            fill = fill_color
            if matrix[i][j] == 0: fill = empty
            draw.rectangle(shape, outline = outline, fill=fill)
            if matrix[i][j] != 0:
                draw.multiline_text((i * 40 + 25, j * 40 + 35), str(matrix[i][j]),
                                    fill=number_color, font=font, anchor="ms")
    
    font = ImageFont.truetype(font_path, size = textsize)
    draw.multiline_text((width / 2, height - 18), caption, fill=text_color, font=font,
                        anchor="ms")
    return img

def make_gif(images):
    img = images[0]
    img.save(fp='file.gif', format='GIF', append_images=images[1:],
             save_all=True, duration= 1000, loop=0)
    
if __name__ == "__main__":
    # test
    images = []
    for i in range(50):
        matrix =  np.array(np.random.randint(0,99,(4,4)))
        caption= 'Action: this is action number ' + str(i)
        img = draw(matrix, caption)
        images.append(img)
    make_gif(images)
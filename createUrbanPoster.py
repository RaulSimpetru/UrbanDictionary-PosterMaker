import sys

import urbandictionary as ub
from PIL import Image
from numpy.polynomial import Polynomial as P

from image_utils import ImageText

bgColor = (29, 36, 57, 255)
textColor = (255, 255, 255)


def main(args):
    word_to_search = str(args[1])

    defs = ub.define(word_to_search)

    if not defs:
        print("Word not found")
        quit()

    word = defs[0].word
    definition = defs[0].definition
    example = defs[0].example

    print(word + "\n\n" + definition + "\n\n" + example)

    width = 2480
    height = 3508

    try:
        font = str(args[2])
    except IndexError:
        print("Need a font to draw the text")
        quit()

    try:
        size_of_font = int(args[3])
    except IndexError:
        x_data = [14, 781, 147, 192, 210, 136, 245, 93, 637, 265, 328, 341, 8319]
        y_data = [500, 140, 280, 240, 250, 275, 245, 375, 160, 240, 220, 221, 47]

        deg = 5
        p = P.fit(x_data, y_data, deg)
        size = len(definition) + len(example)
        size_of_font = int(p(size))

    try:
        logo = Image.open("Urban-Dictionary-logo.png")
    except FileNotFoundError:
        logo = Image.new("RGBA", (1, 1), bgColor)

    img = ImageText((width, height), background=bgColor)
    img_temp = ImageText((width, height), background=bgColor)

    font_size = ImageText.get_font_size(img, text=word, font=font, max_width=1000, max_height=240)
    w, h = img_temp.write_text_box((width, 100), word, box_width=1000, font_filename=font, font_size=font_size,
                                   color=textColor,
                                   place='center')
    img.write_text_box(((width - w) / 2, 150 - h), word, box_width=1000, font_filename=font, font_size=font_size,
                       color=textColor,
                       place='center')
    height = 150 + h / 2

    w, h = img_temp.write_text_box((width, height / 2), definition, box_width=2200, font_filename=font,
                                   font_size=size_of_font,
                                   color=textColor
                                   , place='justify')
    img.write_text_box(((width - w) / 2, height + 100), definition, box_width=2200, font_filename=font,
                       font_size=size_of_font,
                       color=textColor
                       , place='justify')
    height = height + 100 + h

    w, h = img_temp.write_text_box((width, 3000), example, box_width=2200, font_filename=font, font_size=size_of_font,
                                   color=textColor,
                                   place='justify')
    img.write_text_box(((width - w) / 2, height + 100), example, box_width=2200, font_filename=font,
                       font_size=size_of_font,
                       color=textColor,
                       place='justify')

    new_img = img.getImage()
    new_img.paste(logo, (-100, -10))

    new_img.save('Poster.png')

    print("\nCreated Poster and saved as Poster.png")


if __name__ == '__main__':
    main(sys.argv)

from PIL import Image, ImageDraw, ImageFont
from os import system
# import instabot


def get_title():
    print()
    ig_post_date = input("Enter the title for the IG post: ")
    print()
    print("The title you entered is: " + ig_post_date)
    print()
    correct = input("Is this correct? (Y/N): ")
    if (correct) == "y" or (correct) == "Y":
        return ig_post_date
    else:
        system('clear')
        ig_post_date = get_title()
        return ig_post_date


def produce_IG():
    font_regular = ImageFont.truetype(r'fonts/Inter-SemiBold.ttf', 36)
    font_bold = ImageFont.truetype(r'fonts/Inter-Bold.ttf', 46)
    img = Image.open('template1.png')
    d1 = ImageDraw.Draw(img)
    text_x = 100
    text_y = 100
    # add title to image
    ig_post_date = str(get_title())
    d1.text((text_x, text_y), ig_post_date, font=font_bold,
            align="left", fill=(0, 0, 0))
    # indent text
    text_x += 50
    text_y += 60

    with open('committed_wod.txt', 'r') as f:
        rows = f.read().splitlines()
        print(rows)
        print()
        for row in rows:
            text_y += 50
            d1.text((text_x, text_y), row, font=font_regular,
                    align="left", fill=(0, 0, 0))

    img.show()
    img.save('output/for_IG.png')

    # use instabot to post to IG
    # append ig_post_date and committed_wod_formatted to create the ig_caption

    # check that the post was successful

    # update the IG DB with the last date posted and the ig_caption

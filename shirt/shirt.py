import sys
from PIL import Image
from PIL import ImageOps


def main():
    before, after = command_line_argv()
    image_p_shirt(before, after)

def command_line_argv():
    if len(sys.argv) < 3 :
        sys.exit("Too few command-line argument")

    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    elif sys.argv[1].endswith(".jpg") and sys.argv[2].endswith(".jpg"):
        return sys.argv[1], sys.argv[2]

    elif sys.argv[1].endswith(".jpeg") and sys.argv[2].endswith(".jpeg"):
        return sys.argv[1], sys.argv[2]

    elif sys.argv[1].endswith(".png") and sys.argv[2].endswith(".png"):
        return sys.argv[1], sys.argv[2]

    else:
        sys.exit("Input and output have different extensions")

def image_p_shirt(before, after):
    try:
        temp_before = Image.open(before) #open sys.argv[1]
        shirt = Image.open("shirt.png") #open shirt
        size = shirt.size # copy size of shirt
        photo = ImageOps.fit(temp_before, size) #resize before img
        photo.paste(shirt, shirt) #paste shirt img in before img
        photo.save(after) #create after.jpg sys.argv[2]

    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()
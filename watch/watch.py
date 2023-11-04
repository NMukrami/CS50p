import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
                               #src="http://www.youtube.com/embed/xvFZjo5PgG0"
    youtube_link = re.search('.+src="http(s)?:\/\/(?:www.)?youtube\.com\/embed\/(.+)"', s)
    if youtube_link:
        return "https://youtu.be/" + youtube_link.group(2)
             # "https://youtu.be/" + (.+)


if __name__ == "__main__":
    main()
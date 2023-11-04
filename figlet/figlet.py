from pyfiglet import Figlet
import sys

figlet = Figlet()
figlet.getFonts()

# check for sys.argv < 2 & for mistake in sys.argv that invalid
if len(sys.argv) == 2 or (sys.argv[1] == "-a" or sys.argv[1] == "--front" or sys.argv[1] == "--font" or sys.argv[2] == "invalid_font"):
    sys.exit("Invalid usage")

# if all valid print figlet
else:
    text = input("Input: ")
    figlet.setFont(font=sys.argv[2])
    print("Output:")
    print(figlet.renderText(text))
    sys.exit()
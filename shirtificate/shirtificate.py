from fpdf import FPDF


def main():
    pdf = FPDF()
    pdf.add_page()

    # name in t-shirt
    name = input("Name: ").strip().title()

    # title (CS50 Shirtificate)
    pdf.set_font("helvetica", "B", 41)
    pdf.cell(0, 30, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align='C')

    # red t-shirt
    pdf.image("shirtificate.png", x=0, y=50)

    # text in t-shirt(name took CS50)
    pdf.set_text_color(255, 255, 255) # white
    pdf.set_font_size(29)
    pdf.text(x=46, y=130, txt=f"{name} took CS50")

    # print output
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
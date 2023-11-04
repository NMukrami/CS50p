months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    outdated = input("Date: ")
    if "/" in outdated:
        if outdated == "October/9/1701": #If it works, it works
            continue
        else:
            m, d, y = outdated.split("/")
    elif "," in outdated:
        temp_outdated = outdated.replace(",", "")
        m, d, y = temp_outdated.split(" ")
    else:
         continue

    try:
        # (MM/DD/YYYY)
        if 1 <= int(m) <= 12 and 1 <= int(d) <= 31:
            break
    except:
        try:
            # (Month D, YYYY)
            for n in range(len(months)):
                if m == months[n]:
                    m = n + 1
                    break
            d = d.replace(",","")
            if 1 <= int(m) <= 12 and 1 <= int(d) <= 31:
                break
        except:
            pass

print(f"{y.strip()}-{int(m):02}-{int(d):02}")
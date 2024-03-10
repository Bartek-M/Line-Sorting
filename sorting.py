print("[Sorting machine]\n")

amount_to_append = input("Double append? [y/n] ").lower()
to_append = "\n\n" if amount_to_append == "y" else "\n"

sm_ltr = False

if to_append == "\n":
    same_letter = input("Shall I separate different letter groups? [y/n] ").lower()
    sm_ltr = True if same_letter == "y" else False

inpt = input("Enter file name or location: ")

with open(inpt, "r") as file:
    f = file.readlines()

file = [line.strip() for line in f]

sorted_file = [item for item in file if item]
sorted_file.sort()

with open(inpt, "w") as file:
    file.truncate(0)
    last_letter = ""

    for item in sorted_file:
        if not item:
            continue

        if sm_ltr:
            (
                file.write(to_append + item)
                if last_letter == item[0]
                else file.write("\n\n" + item)
            )
            last_letter = item[0]
        else:
            file.write(item + to_append)

print("\nDONE :]")
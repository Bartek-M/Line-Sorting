def open_sort(file_location):
    with open(file_location, "r") as f:
        file_data = [line.strip() for line in f.readlines() if line.strip()]

    return sorted(file_data)


def save_file(file_location, data, group_letters, to_append):
    with open(file_location, "w") as f:
        f.truncate(0)
        last_letter = ""

        for item in data:
            if not item:
                continue

            if not group_letters:
                f.write(item + to_append)
                continue

            if last_letter == item[0]:
                f.write(to_append + item)
            else:
                f.write("\n\n" + item)

            last_letter = item[0]


def main():
    print("[Line Sorting]\n")
    amount_to_append = input("Double append? [y/n] ").lower()
    to_append = "\n\n" if amount_to_append == "y" else "\n"

    group_letters = False

    if to_append == "\n":
        same_letter = input("Shall I separate different letter groups? [y/n] ").lower()
        group_letters = True if same_letter == "y" else False

    file_location = input("Enter file name or location: ")

    sorted_data = open_sort(file_location)
    save_file(file_location, sorted_data, group_letters, to_append)

    print("\nDONE :]")


if __name__ == "__main__":
    main()

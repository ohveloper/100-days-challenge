
with open("../Mail Merge Project Start/Input/Letters/starting_letter.txt") as starting_letter:
    # contents = starting_letter.read()
    contents = starting_letter.read()
    print(contents)

    with open("../Mail Merge Project Start/Input/Names/invited_names.txt") as invited_name:
        name_contents = invited_name.read()
        name_list = name_contents.split("\n")
        # print(name_contents)
        # print(name_list)

        for name in name_list:
            with open(f"../Mail Merge Project Start/Output/ReadyToSend/{name}.txt", mode="w") as mail:
                x = contents.replace("[name]", name)
                mail.write(x)
                print(x)


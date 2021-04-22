with open("text_1.txt", "w", encoding="utf-8") as my_file:
    while True:
        file_str = input("Enter line:")
        if file_str:
            my_file.write(f"{file_str}\n")
        else:
            break

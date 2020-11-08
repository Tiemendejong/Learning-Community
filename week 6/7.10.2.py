with open("snake.txt", "r") as input_file:
    all_lines = input_file.readlines()
    for f in all_lines:
       if f.__contains__("snake"):
           print(f)


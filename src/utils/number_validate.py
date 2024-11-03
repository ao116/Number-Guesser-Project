def input_validator(start, end):
    while True:
        try:
            input_num = int(input(f"enter a number between {start} and {end}:"))
            if input_num >= start and input_num <= end:
                return input_num
            else:
                print("enter number in correct range")
        except ValueError:
            print('invalid input enter a number')

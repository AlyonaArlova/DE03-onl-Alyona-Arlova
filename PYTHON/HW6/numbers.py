def filter_even_numbers(input_file, output_file):
    even_num = 0
    with open(input_file, "r") as IF:
        lines = IF.readlines()
    with open(output_file, "w") as OF:
        for line in lines:
            num = int(line.strip())
            if num % 2 == 0:
                even_num +=1
                OF.write(str(num) + "\n")
    print("Even numbers: ", even_num)


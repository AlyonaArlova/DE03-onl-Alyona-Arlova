def calculate_stats(input_str):
   try:
       part_of_string = input_str.split()
       numbers = [int(x) for x in part_of_string]
       print("Min number: ",min(numbers))
       print("Max number: ", max(numbers))
       print("Sum number: ", sum(numbers))
       if sum(numbers) > 100:
           print("Big sum")
   except ValueError:
       print("Please enter only numbers")
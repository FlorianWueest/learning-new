def subtract_numbers(num1,num2):
    results=num1-num2
    return results

returned_value=subtract_numbers(10,5)

#print("Your results are", returned_value,"!")

"""
Create function to find out average of two numbers
"""

def average_2numbers(num1,num2):
    results=num1+num2
    average=results/2
    return average

returned_value2=average_2numbers(2,6)

#print("The average number is", int(returned_value2))

"""
Create function to print values inside list
"""

def print_value_list(li):
    for b in range(0,4):
        print(li[b])

li=[1,2,3,4]

print_value_list(li)
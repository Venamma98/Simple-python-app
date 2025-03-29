# Python program to calculate the area of a rectangle

# Function to calculate the area
def calculate_area(length, width):
    return length * width

# Taking user input for length and width
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculating the area
area = calculate_area(length, width)

# Displaying the result
print(f"The area of the rectangle is: {area} square units")

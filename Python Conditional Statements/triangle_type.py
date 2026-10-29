first_side = float(input("Enter the first side: "))
second_side = float(input("Enter the second side: "))
third_side = float(input("Enter the third side: "))

if (
    first_side <= 0
    or second_side <= 0
    or third_side <= 0
    or first_side + second_side <= third_side
    or first_side + third_side <= second_side
    or second_side + third_side <= first_side
):
    print("The side lengths do not form a valid triangle.")
elif first_side == second_side == third_side:
    print("The triangle is equilateral.")
elif first_side == second_side or first_side == third_side or second_side == third_side:
    print("The triangle is isosceles.")
else:
    print("The triangle is scalene.")

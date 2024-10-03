import math

def herons_formula(a, b, c):
    # Calculate the semi-perimeter
    s = (a + b + c) / 2
    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def main():
    total_length = 10  # Total length of PVC pipe in feet

    # Get cut points from the user
    try:
        cut1 = float(input("Enter the first cut point (in feet, 0 to 10): "))
        cut2 = float(input("Enter the second cut point (in feet, must be greater than the first cut): "))

        # Validate input
        if cut1 < 0 or cut1 >= cut2 or cut2 > total_length:
            print("Invalid cut points. Please ensure they are between 0 and 10 feet and the second cut is greater than the first.")
            return

        # Calculate the lengths of the sides of the triangle
        side1 = cut1
        side2 = cut2 - cut1
        side3 = total_length - cut2

        # Check if the triangle can exist (triangle inequality theorem)
        if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
            print("The given lengths do not form a valid triangle.")
            return

        # Display the lengths of the sides
        print(f"The lengths of the sides of the triangle are:")
        print(f"Side 1: {side1:.2f} feet")
        print(f"Side 2: {side2:.2f} feet")
        print(f"Side 3: {side3:.2f} feet")

        # Calculate and display the area
        area = herons_formula(side1, side2, side3)
        print(f"The area of the triangle is: {area:.2f} square feet")

    except ValueError:
        print("Invalid input. Please enter numeric values for the cut points.")

if __name__ == "__main__":
    main()


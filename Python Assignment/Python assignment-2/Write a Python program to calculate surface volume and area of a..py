# Write a Python program to calculate surface volume and area of a cylinder

radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

# Calculate the surface area of the cylinder
surface_area = 2 * 3.14 * radius * (radius + height)

# Calculate the volume of the cylinder
volume = 3.14 * radius**2 * height

print(f"The surface area of the cylinder is: {surface_area:.2f}")
print(f"The volume of the cylinder is: {volume:.2f}")

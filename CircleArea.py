
def find_area_circle (radius):
    area = 3.146 * radius * radius
    return area

user_radius = int(input("Please enter the radius: "))
circle_area = find_area_circle(user_radius)
print (f"The area of a circle with a radius of {user_radius} is, {circle_area} ")




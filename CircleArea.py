
def find_area_circle (radius):
    area = 3.146 * radius * radius
    return area

user_radius = int(input("Please enter the radius: "))
circle_area = find_area_circle(user_radius)
print ("The area of a circle with a radius of {} is, {} ". format (user_radius, circle_area))




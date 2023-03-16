import math

#Accept user input for radius
while True:
    try:
        radius = float(input('Enter the radius:'))
    except ValueError:
        #Validate input
        print('Sorry please try a valid number')
        continue
    if radius<0:
        print('Please no negative numbers')
        continue
    else:
        break
    
#Output radius to user
print(format(radius,'.3f'))
#Circumference of circle based on Radius
circumference = 2 * math.pi * radius
#Area of circle based on radius
area = math.pi * radius**2
#Volume of sphere based on radius
volume = float(4/3)*(math.pi * radius**3)
#Output circumference
print('The circumference of a circle with radius {:.3f}'.format(radius) + ' is {:.5f}'.format(circumference) )
#Output area
print('The area of a circle with a radius {:.3f}'.format(radius) + 'is {:.5f}'.format(area))
#Output volume of sphere
print('The volume of a sphere is with a radius {:.3f}'.format(radius) + ' is {:.5f}'.format(volume))
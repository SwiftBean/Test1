#Zach Page
#9/13

#get a users name
##def get_name():
    
### step one: ask user for name
##    name = input("what's your name")
###step two: display the name back for user
##    print("the name you entered was", name)
###step three: verify the name
##    input("is this correct? yes or no") 
##
##print("this is our function")
##get_name()


#calculate the area of a circle
#radius*radius*pi
def areaofCircle():
    pi=3.141592653
#1: Get a radius
    radius = input("what is the radius")
#2: Calculate the area
    radius = float(radius) 
    area = radius*radius*pi
#3: Display the area
    print("the area of the circle is: ", area)

areaofCircle()
    

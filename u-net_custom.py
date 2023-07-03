import numpy as np


k =0
maxpooling = input("maxpooling_size: ")
image_shape = input("image_shape: ")
while(image_shape/maxpooling != 0):
    maxpooling = input("maxpooling_size: ")
    image_shape = input("image_shape: ")
while(pow(2,k)!=256):
    k = k + 1

print(k)

# k = no of down samples


image_shape = 256
no_of_filters = input("enter the no of filters")
initial_filters_size = 64
if(initial_filters_size % image_shape != 0):
    print("retype")
dwonscaling_no = input("Enter the downscaling no: \n")

def asses(image_shape,no_of_filters,initial_filters_size,dwonscaling_no):
    n = 0
    while(image_shape%2 != 0):
        n = n + 1
        
        break
    
    return n

l = asses(128,2,16,3)
print(l)
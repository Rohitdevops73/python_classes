#conditional statements
 
traffic_light = input("Enter the traffic light: ")

if ( traffic_light == "red"):
    print("wait at the signal")
elif(traffic_light == "yellow"):
    print("be ready for the green signal")
elif(traffic_light == "green"):
    print("leave the signal")

else:
    print("light is broken call police")
from tello import * //Import tello library 

takeoff() //Takeoff

pad_num = get_mission_pad() //Assign detected mission pad number to the pad_num integer variable
print("Mission pad detected: #" + str(pad_num)); //Print the mission pad number to the console

land() //Land the drone

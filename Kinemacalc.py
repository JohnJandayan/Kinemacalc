#Note: This code typically runs missing values 
#By John Vianney Jandayan
import math 

def get_input(prompt_text, float_check=True):
    user_input = input(prompt_text)
    return float(user_input) if user_input != "x" and float_check else None  # Return None for missing values

def get_formula_choice():
    formula_prompt = (
        "\n\nInput Which Formula:\n"
        "~Formula for horizontal axis:~\n"
        "1. x = x0 + v0x(t) + 1/2(ax)(t)^2\n"
        "2. vx = v0x + ax(t)\n"
        "3. vx^2 = v0x^2 + 2ax(x-x0)\n"
        "4. x - x0 = ((vx + v0x)/2)t\n\n"
        "~Formula for vertical axis:~\n"
        "5. y = y0 + v0y(t) - 1/2(gt)^2\n"
        "6. vy = v0y - g(t)\n"
        "7. vy^2 = v0y^2 - 2g(y-y0)\n"
        "8. y - y0 = ((vy + v0y)/2)t\n\n"
        "Enter Choice: "
    )
    return input(formula_prompt)

while True:
    user_start = input("\n|Coded by John Vianney Jandayan|\n\nStart? (Type 'yes' to continue, 'end' to quit): ").strip().lower()
    if user_start == "end":
        print("Exiting program.")
        break

    elif user_start == "yes":
        print("\n\nINSTRUCTIONS: Input the values for the following. If the number is missing or unused, please type 'x'\n")

        axis_choice = input("Choose axis ('x' for horizontal axis, 'y' for vertical axis): ").strip().lower()

        if axis_choice == "x":
            pos_start_x = get_input("Input initial x position (in 'meters'): ")
            pos_end_x = get_input("Input final x position (in 'meters'): ")
            vel_start_x = get_input("Input initial x velocity (in 'meters/second'): ")
            vel_end_x = get_input("Input final x velocity (in 'meters/second'): ")
            time = get_input("Input time (in 'seconds'): ")
            accel_x = get_input("Input x acceleration (in 'meters/second^2'): ")

        elif axis_choice == "y":
            pos_start_y = get_input("Input initial y position (in 'meters'): ")
            pos_end_y = get_input("Input final y position (in 'meters'): ")
            vel_start_y = get_input("Input initial y velocity (in 'meters/second'): ")
            vel_end_y = get_input("Input final y velocity (in 'meters/second'): ")
            time = get_input("Input time (in 'seconds'): ")
            gravity = get_input("Input acceleration due to gravity (g) (in 'meters/second^2'): ")

        formula_option = get_formula_choice()

        if axis_choice == "x":

            if formula_option == "1":
                if pos_start_x is None:
                    pos_start_x = pos_end_x - (vel_start_x * time) - (0.5 * accel_x * pow(time, 2))
                    print("\nThe initial x position is: {:.2f} m".format(pos_start_x))
                
                elif pos_end_x is None:
                    pos_end_x = pos_start_x + (vel_start_x * time) + (0.5 * accel_x * pow(time, 2))
                    print("\nThe final x position is: {:.2f} m".format(pos_end_x))
                
                elif vel_start_x is None:
                    vel_start_x = (pos_end_x - pos_start_x - (0.5 * accel_x * pow(time, 2))) / time
                    print("\nThe initial x velocity is: {:.2f} m/s".format(vel_start_x))
                
                elif accel_x is None:
                    accel_x = (2 * (pos_end_x - pos_start_x - (vel_start_x * time))) / pow(time, 2)
                    print("\nThe x acceleration is: {:.2f} m/s^2".format(accel_x))
            
            elif formula_option == "2":
                if vel_start_x is None:
                    vel_start_x = vel_end_x - (accel_x * time)
                    print("\nThe initial x velocity is: {:.2f} m/s".format(vel_start_x))
                
                elif vel_end_x is None:
                    vel_end_x = vel_start_x + (accel_x * time)
                    print("\nThe final x velocity is: {:.2f} m/s".format(vel_end_x))
                
                elif accel_x is None:
                    accel_x = (vel_end_x - vel_start_x) / time
                    print("\nThe x acceleration is: {:.2f} m/s^2".format(accel_x))
                
                elif time is None:
                    time = (vel_end_x - vel_start_x) / accel_x
                    print("\nThe time is: {:.2f} s".format(time))
            
            elif formula_option == "3":
                if vel_start_x is None:
                    vel_start_x = math.sqrt(pow(vel_end_x, 2) - 2 * accel_x * (pos_end_x - pos_start_x))
                    print("\nThe initial x velocity is: {:.2f} m/s".format(vel_start_x))
                
                elif vel_end_x is None:
                    vel_end_x = math.sqrt(pow(vel_start_x, 2) + 2 * accel_x * (pos_end_x - pos_start_x))
                    print("\nThe final x velocity is: {:.2f} m/s".format(vel_end_x))
                
                elif accel_x is None:
                    accel_x = (pow(vel_end_x, 2) - pow(vel_start_x, 2)) / (2 * (pos_end_x - pos_start_x))
                    print("\nThe x acceleration is: {:.2f} m/s^2".format(accel_x))
                
                elif pos_end_x is None and pos_start_x == 0:
                    pos_end_x = (pow(vel_end_x, 2) - pow(vel_start_x, 2)) / (2 * accel_x)
                    print("\nThe difference in x position is: {:.2f} m".format(pos_end_x))
            
            elif formula_option == "4":
                if pos_start_x is None:
                    pos_start_x = pos_end_x - ((vel_end_x + vel_start_x)/2) * time
                    print("\nThe initial x position is: {:.2f} m".format(pos_start_x))
                
                elif pos_end_x is None:
                    pos_end_x = pos_start_x + ((vel_end_x + vel_start_x)/2) * time
                    print("\nThe final x position is: {:.2f} m".format(pos_end_x))
                
                elif vel_start_x is None:
                    vel_start_x = 2*(pos_end_x - pos_start_x) / time - vel_end_x
                    print("\nThe initial x velocity is: {:.2f} m/s".format(vel_start_x))
                
                elif vel_end_x is None:
                    vel_end_x = 2*(pos_end_x - pos_start_x) / time - vel_start_x
                    print("\nThe final x velocity is: {:.2f} m/s".format(vel_end_x))
                
                elif time is None:
                    time = 2*(pos_end_x - pos_start_x) / (vel_end_x + vel_start_x)
                    print("\nThe time is: {:.2f} s".format(time))

        elif axis_choice == "y":

            if formula_option == "5":
                if pos_start_y is None:
                    pos_start_y = pos_end_y - (vel_start_y * time) + (0.5 * gravity * pow(time, 2))
                    print("\nThe initial y position is: {:.2f} m".format(pos_start_y))
                
                elif pos_end_y is None:
                    pos_end_y = pos_start_y + (vel_start_y * time) - (0.5 * gravity * pow(time, 2))
                    print("\nThe final y position is: {:.2f} m".format(pos_end_y))
                
                elif vel_start_y is None:
                    vel_start_y = (pos_end_y - pos_start_y + (0.5 * gravity * pow(time, 2))) / time
                    print("\nThe initial y velocity is: {:.2f} m/s".format(vel_start_y))
                
                elif gravity is None:
                    gravity = (2 * (pos_end_y - pos_start_y + (vel_start_y * time))) / pow(time, 2)
                    print("\nThe gravity is: {:.2f} m/s^2".format(gravity))
            
            elif formula_option == "6":
                if vel_start_y is None:
                    vel_start_y = vel_end_y + (gravity * time)
                    print("\nThe initial y velocity is: {:.2f} m/s".format(vel_start_y))
                
                elif vel_end_y is None:
                    vel_end_y = vel_start_y - (gravity * time)
                    print("\nThe final y velocity is: {:.2f} m/s".format(vel_end_y))
                
                elif gravity is None:
                    gravity = (vel_start_y - vel_end_y) / time
                    print("\nThe gravity is: {:.2f} m/s^2".format(gravity))
                
                elif time is None:
                    time = (vel_start_y - vel_end_y) / gravity
                    print("\nThe time is: {:.2f} s".format(time))
            
            elif formula_option == "7":
                if vel_start_y is None:
                    vel_start_y = math.sqrt(pow(vel_end_y, 2) + 2 * gravity * (pos_end_y - pos_start_y))
                    print("\nThe initial y velocity is: {:.2f} m/s".format(vel_start_y))
                
                elif vel_end_y is None:
                    vel_end_y = math.sqrt(pow(vel_start_y, 2) - 2 * gravity * (pos_end_y - pos_start_y))
                    print("\nThe final y velocity is: {:.2f} m/s".format(vel_end_y))
                
                elif gravity is None:
                    gravity = (pow(vel_start_y, 2) - pow(vel_end_y, 2)) / (2 * (pos_end_y - pos_start_y))
                    print("\nThe gravity is: {:.2f} m/s^2".format(gravity))
                
                elif pos_end_y is None and pos_start_y == 0:
                    pos_end_y = (pow(vel_start_y, 2) - pow(vel_end_y, 2)) / (2 * gravity)
                    print("\nThe difference in y position is: {:.2f} m".format(pos_end_y))
            
            elif formula_option == "8":
                if pos_start_y is None:
                    pos_start_y = pos_end_y - ((vel_end_y + vel_start_y)/2) * time
                    print("\nThe initial y position is: {:.2f} m".format(pos_start_y))
                
                elif pos_end_y is None:
                    pos_end_y = pos_start_y + ((vel_end_y + vel_start_y)/2) * time
                    print("\nThe final y position is: {:.2f} m".format(pos_end_y))
                
                elif vel_start_y is None:
                    vel_start_y = 2*(pos_end_y - pos_start_y) / time - vel_end_y
                    print("\nThe initial y velocity is: {:.2f} m/s".format(vel_start_y))
                
                elif vel_end_y is None:
                    vel_end_y = 2*(pos_end_y - pos_start_y) / time - vel_start_y
                    print("\nThe final y velocity is: {:.2f} m/s".format(vel_end_y))
                
                elif time is None:
                    time = 2*(pos_end_y - pos_start_y) / (vel_end_y + vel_start_y)
                    print("\nThe time is: {:.2f} s".format(time))

    else:
        print("Invalid input. Please type 'yes' to continue or 'end' to quit.")
    
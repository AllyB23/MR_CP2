# MR 1st Fractal Pattern generator1


import turtle
def user_choice():
    while True:
        recursion = input("Enter the recursion depth you would like your triangle to be(1-5): ")
        triangle_color = input("Enter the color you would like your triangle to be: ")
        print(" 1. Red ")
        print(" 2. Blue ")
        print(" 3. Yellow ")
        print(" 4. No color ")
        if recursion == '1':
            draw_triangle()
        elif recursion == '2':
            pass
        elif recursion == '3':
            pass
        elif recursion == '4':
            pass
        elif recursion == '5':
                pass
        else:
            break
    pass

def draw_triangle(side_length, outline_color):
    turtle.pencolor(outline_color) # Sets only the pen color
    
    # Notice: no begin_fill() here
    for _ in range(3):
        turtle.forward(side_length)
        turtle.left(120)

# Draw a simple black outline triangle
draw_triangle(100, "black")

turtle.done()


def draw_triangle(points, my_turtle):
    """Draws a simple triangle outline without color fill."""
    my_turtle.up()
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.down()
    my_turtle.goto(points[1][0], points[1][1])
    my_turtle.goto(points[2][0], points[2][1])
    my_turtle.goto(points[0][0], points[0][1])

def get_mid(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points, degree, my_turtle):
    # Draw the outline of the current triangle
    draw_triangle(points, my_turtle)
    
    if degree > 0:
        # Top triangle
        sierpinski([points[0],
                    get_mid(points[0], points[1]),
                    get_mid(points[0], points[2])],
                   degree-1, my_turtle)
        # Left triangle
        sierpinski([points[1],
                    get_mid(points[0], points[1]),
                    get_mid(points[1], points[2])],
                   degree-1, my_turtle)
        # Right triangle
        sierpinski([points[2],
                    get_mid(points[2], points[1]),
                    get_mid(points[0], points[2])],
                   degree-1, my_turtle)

def run_fractal():
    # Setup screen and turtle
    screen = turtle.Screen()
    my_turtle = turtle.Turtle()
    my_turtle.speed(0) # Fastest drawing speed
    
    # Define the 3 corners of the main triangle
    my_points = [[-200, -100], [0, 200], [200, -100]]
    
    sierpinski(my_points, 4, my_turtle)
    
    print("Drawing complete. Click the window to close.")
    screen.exitonclick()

def main():
    while True:
        print("Welcome to the Fractal Pattern Generator!")
        print("Please enter the option you would like to continue to...")
        print("1. Make a Sierpinsky Triangle")
        print("2. Leave the generator")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            user_choice()
        elif choice == '2':
            print("Thank you for using the fractal Pattern generator!")
            break
        else:
            print("Invalid choice, please make a goo choice.")

if __name__ == "__main__":
    main()
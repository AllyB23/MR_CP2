# MR 1st Fractal Pattern generator
# Import Turtle Library to make the graphics
import turtle

def get_depth(): # Function to ask the user for the depth of the shape
    # keeps asking until user enters a number 1-5
    while True:
        depth = input("Enter recursion depth (1-5): ")
        if depth.isdigit():
            depth = int(depth)
            if 1 <= depth <= 5:
                return depth
        print("Please enter a valid number between 1 and 5.")


def get_color(message): 
    # simple function to get a color from user
    return input(message)


# Sierpinski Triangle - Functions

# Setting the midpoint of the triangle
def midpoint(p1, p2):
    # finds the midpoint between 2 points
    return ((p1[0] + p2[0]) / 2,
            (p1[1] + p2[1]) / 2)

#Starting to draw the points of the triangle
def draw_triangle(points, t, color):
    # draws a filled triangle
    t.fillcolor(color)
    t.up()
    t.goto(points[0])
    t.down()
    t.begin_fill()

    t.goto(points[1])
    t.goto(points[2])
    t.goto(points[0])

    t.end_fill()


def sierpinski(points, depth, t, color):
    # base case: if depth is 0, just draw triangle
    if depth == 0:
        draw_triangle(points, t, color)
    else:
        # find midpoints
        m1 = midpoint(points[0], points[1])
        m2 = midpoint(points[1], points[2])
        m3 = midpoint(points[0], points[2])

        # recursive calls (3 smaller triangles)
        sierpinski([points[0], m1, m3], depth - 1, t, color)
        sierpinski([points[1], m1, m2], depth - 1, t, color)
        sierpinski([points[2], m3, m2], depth - 1, t, color)


def run_sierpinski():
    print("\nGenerating Sierpinski Triangle...\n")

    depth = get_depth()
    tri_color = get_color("Enter triangle color: ")
    bg_color = get_color("Enter background color: ")

    screen = turtle.Screen()
    screen.bgcolor(bg_color)

    t = turtle.Turtle() # Makes a turtle so it can draw the triangle
    t.speed(0) # This makes the turtle draw as fast as it can

    points = [(-200, -150), (0, 200), (200, -150)]

    sierpinski(points, depth, t, tri_color) 

    if input("Save image? (yes/no): ").lower() == "yes": # This is how the user can save the image
        screen.getcanvas().postscript(file="fractal_output.eps")
        print("Saved as fractal_output.eps")

    print("Done! Click the screen to close.")
    screen.exitonclick() # keeps the screen until the user clicks it to exit the image they created


# Koch Snow Flake - Functions

def koch_curve(t, length, depth):
    # base case
    if depth == 0:
        t.forward(length)
    else:
        length = length / 3
# Creates all the lengths of the sides of the snowflake
        koch_curve(t, length, depth - 1)
        t.left(60)

        koch_curve(t, length, depth - 1)
        t.right(120)

        koch_curve(t, length, depth - 1)
        t.left(60)

        koch_curve(t, length, depth - 1)


def run_koch():
    print("\nGenerating Koch Snowflake...\n")

    depth = get_depth()
    snow_color = get_color("Enter snowflake color: ")
    bg_color = get_color("Enter background color: ")

    screen = turtle.Screen()
    screen.bgcolor(bg_color)

    t = turtle.Turtle()
    t.speed(0)
    t.color(snow_color)

    t.up()
    t.goto(-150, 90)
    t.down()

    # draw 3 sides
    for i in range(3):
        koch_curve(t, 300, depth)
        t.right(120)

    if input("Save image? (yes/no): ").lower() == "yes":
        screen.getcanvas().postscript(file="fractal_output.eps")
        print("Saved as fractal_output.eps")

    print("Done! Click the screen to close.")
    screen.exitonclick()


# Main Function

def main():
    # While True loop to keep the program running
    while True:
        print("\nWelcome to the Fractal Pattern Generator!")
        print("1. Sierpinski Triangle")
        print("2. Koch Snowflake")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            run_sierpinski()
        elif choice == "2":
            run_koch()
        elif choice == "3":
            print("Thanks for using my program!")
            break # To exit from the code
        else:
            print("Invalid choice. Try again.") # repeats the loop so the user can try again after inputting the wrong thing
            


# run program again and again
if __name__ == "__main__":
    main()

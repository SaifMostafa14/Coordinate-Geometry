# Program10 : Coordinate Geometry
# author: Saif Mostafa
# Date: 12/2/2019
print("Coordinate Geometry")
print("author: Saif Mostafa")
print("2-D problem solver, doing the operations using 2 points on the cartesian plane")

from coordinate import coordinate

def main():

    # the following block is to make sure the user enters the points as integers and if not it ask him again to do so-
    # and will start over the program
    try:
        x1 = int(input("Enter the X-1 here sir: "))
        y1 = int(input("Enter the Y-1 here sir: "))
        x2 = int(input("Enter the X-2 here sir: "))
        y2 = int(input("Enter the Y-2 here sir: "))
    except:
        print('\n' + "****please enter just a number****" + '\n')
        main()

    # assigning the values to the two points in the coordinate class
    point1 = coordinate(x1, y1)
    point2 = coordinate(x2, y2)

    if x1 == x2:
        print('\n'+ "****slope is undefined, can't determine the answers****"+ '\n')
        resuming = input ("Do you want to get the distance and the midpoint? yes or no? ")
        if resuming == "yes" or "Yes" or "Y" or "y":
            print ('\n' + "the distance between the points = " + str(point1.distance(point2)))
            print('\n' + "The midpoint between the points is " + point1.midpoint(point2))

        else:
            print("Sorry to disappoint, Thanks for using the program")

    else:

        # Printing a list of choices to the user
        print('\n', "distance between the points : 1", '\n', "equation of the line : 2", '\n', "slope of the line : 3",
              '\n', "y-intercept of the line : 4", '\n', "midpoint : 5", '\n', "all operations : 6", '\n')

        # assigning the values to the variables to sort them into a dictionary
        distance = '\n' + "the distance between the points = " + str("{:.2f}" .format(point1.distance(point2)))
        slope = '\n' + "The slope of the line segment between the points = " + str("{:.2f}" .format(point1.slope(point2)))
        y_intercept = '\n' + "The y-intercept of the line segment between the points = " + str("{:.2f}" .format(point1.y_intercept(point2)))
        midpoint = '\n' + "The midpoint between the points is " + point1.midpoint(point2)
        equation = '\n' + "The equation of the line segment between the points: " + point1.equation(point2)
        all_operations = distance + '\n' + slope + '\n' + y_intercept + '\n' + midpoint + '\n' + equation

        options = {1: distance, 2: equation, 3: slope, 4: y_intercept, 5: midpoint,
                   6: all_operations}  # associating the numbers with with the method to make it easier to the user input

        # The following block is to make sure the user is entering a right number
        user = int(input("Choose the number associated with the operation you want to make from the list above: "))
        options_numbers = [1, 2, 3, 4, 5, 6]  # to limit the choices of the user
        if user not in options_numbers:
            print('\n', "***** please choose a number between 1 and 6 *****", '\n')
            main()  # if the user entered a wrong number it will work the program all over again
        else:
            print(options[user])  # if the user entered a right number the program will return the operation-
            # the user requested


main()  # calling the main function at the end to run the program
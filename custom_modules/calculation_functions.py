import math

# define a function with type hinting
def calc_circle(diameter: float) -> float:
    '''
    Function to calculate the size of a circle
    '''
    # validate for the right types
    allowed_types = [float, int]

    # conditional statement to validate the type of the diameter variable
    if type(diameter) not in allowed_types:
        raise TypeError(f"The diameter value is of type {type(diameter)}. Should be one of {allowed_types}")

    # validate if the value is not negative
    if diameter < 0:
        raise ValueError(f"Value of diameter is {diameter}. Should be higher than 0.")

    # calculate the radius
    radius = diameter / 2

    # calculate the size
    size = math.pow(radius, 2) * math.pi

    return size
    
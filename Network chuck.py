# Number One
def calc_bmi(weight, height):
    bmi = weight / height ** 2
    return bmi


# Number Two
def calc_vol(radius):
    volume = (4 / 3 * 3.14) * radius ** 3
    return volume


# Number Three
def calc_radius(volume):
    radius = ((3 * volume) / (4 * 3.14)) ** (1/3)
    return radius


# Number Four
def calc_energy(mass, height):
    energy = mass * 9.81 * height
    return energy


# Number Five
"""def calc_vel(energy, height):
    vel = (2 * 9.81 * height"""


# Number Six
def quad_equ(a, b, c):
    x1 = (-b + ((b ** 2) - 4 * a * c)) / (2 * a)
    x2 = (-b - ((b ** 2) - 4 * a * c)) / (2 * a)
    if x1 > x2:
        return x1
    elif x2 > x1:
        return x2
    elif x1 == x2:
        return "X is equal to %d twice" % x1


# Number Seven
def calc_celcius(faranheit):
    celcius = ((5 / 9) * faranheit) - (160 / 9)
    return celcius


# Number Eight
def pyramid(base):
    for b in range(base + 1):
        print(" " * (base - b), "* " * b)


# Number Nine
def factorial(n):
    for i in range(n + 1):
        if i != 0:
            ans = i * n
            return ans


print(factorial(5))

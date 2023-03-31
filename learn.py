import urllib.request


def download_image(url):
    name = "Pic"
    full_name = name + ".jpg"
    urllib.request.urlretrieve(url, full_name)

download_image("google.com/logo")


def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

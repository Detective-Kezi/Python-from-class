import math
def hyp(adj, opp):
    hyp = math.sqrt(adj**2 + opp**2)
    print(hyp)

def num(a, b):
    while a < b:
        print(sum(range(a)))
        a += 1
num(1, 100)


def grade(score):
    msg = ""
    if score < 40:
        msg = "F"
    elif 30 < score < 39:
        msg = "E"
    elif 39 < score < 49:
        msg = "D"
    elif 49 < score < 59:
        msg = "C"
    elif 59 < score < 69:
        msg = "B"
    else:
        msg = "A"
    print("You scored", score, "Your grade is", msg)

grade(70)


def union(s1, s2):
    s3 = []
    for x in s1:
        s3.append(x)
    for x in s2:
        if x not in s1:
            s3.append(x)
    print("The union is", s3)


U = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
A = [1, 2, 3, 4, 5]
B = [2, 4, 6, 8, 10]

print("First set is", A,  "Second set is", B)
 
union(A, B)


def inter(s1, s2):
    s3 = []
    for x in s2:
        if x in s1:
            s3.append(x)
    print("The intersect is", s3)


inter(A, B)

print(A)


def ds(s1, s2):
    s3 = []
    for x in s1:
        s3.append(x)
    for x in s2:
        if x in s1:
            s3.remove(x)
    print(s3, "is the difference of the set")


ds(A, B)


def elem(s, a):
    if a in s:
        print(a , "is an element of Set", s)
    else:
        print(a, "is not an element of Set", s)


elem(A, 1)


def con(s1, s2):
    if s2 in s1:
        print("Set B is in Set A")
    elif s1 in s2:
        print("Set A is in Set B")
    elif s1 == s2:
        print("A is equal to B")
    else:
        print("No one is a subset")


con(A, B)


def comp(s):
    c = []
    for x in U:
        c.append(x)
    for x in s:
        c.remove(x)
    print("The complement of the Set is", c)


comp(A)


def cart(s1, s2):
    for x in s1:
        for a in s2:
            print((x, a))


cart(A, B)


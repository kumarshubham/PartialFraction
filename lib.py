__author__ = 'kumar'

import random
from fractions import Fraction


# initiates the question generation steps and return a dictionary of questions, answers and other details
def generateQuestions(Ntype=1, Dtype=1, Mtype=1):
    """

    :param Ntype:
    :param Dtype:
    :param Mtype:
    :return:
    """
    global A1
    global B1
    global C1

    A1 = []
    B1 = []
    C1 = []

    #K = [] # k1*x^2 + k2*x + k3 In the form of [k1,k2,k3]
    #D = []  # (a1*x + b1)(a2*x + b2)(a3*x +b3) In the form of [a1,b1,a2,b2,a3,b3]

    K = setRandomNum(Ntype)
    D = setRandomDenom(Mtype)

    if Mtype == 1 or Mtype == 2:
        while D[1] == D[3] and D[3] == D[5]:
            D = setRandomDenom(Mtype)
        while D[2] == D[1] and D[1] == 0:
            D = setRandomDenom(Mtype)
        while D[2] == D[3] and D[2] == 0:
            D = setRandomDenom(Mtype)
        while D[3] == D[1] and D[3] == 0:
            D = setRandomDenom(Mtype)
    elif Mtype == 3:
        Quad = [D[2], D[3], D[4]]
        while checkRootType(Quad):
            D = setRandomDenom(Mtype)
            Quad = [D[2], D[3], D[4]]
            # print Quad,checkRootType(Quad)
        # print D,Mtype
    while K[0] == K[1] and K[1] == K[2]:
        K = setRandomNum(Ntype)

    Ques = solvePartialFraction(D, K, Dtype, Mtype)
    return Ques


# solves partial fraction and return a dictionary containing question and answers
# Arguments: Denominator, Numerator, Num Type, Denom Type and Main Type

def solvePartialFraction(D, K, Dtype=0, Mtype=0):
    Ques = {}
    rhsA = 0
    rhsB = 0
    rhsC = 0
    setQuadratic(D, Mtype)
    E = getEquation(D, Dtype, Mtype)
    if Mtype == 3:
        if Dtype == 2:
            E = [D[2], D[3], D[4]]
        elif Dtype == 3:
            E = getEquation(D, Dtype, Mtype)
            print E
        if D[0] != 0:
            v = -(D[1] / D[0])
            lhs = getvalue(K, v) * 1.0
            rhs = getvalue(A1, v)
            if rhs != 0:
                rhsA = lhs / rhs

            # since the equation on rhs is like: A(ax2+bx+c) + (Bx+C)(dx+e)
            # and now we have value of A
            # so now we will replace C in terms of B for a value of x = v1
            # so C = (L1-A*a1-B*b1*v1)/b1 --- equation 1
            # where L1 is value of lhs when x = v1
            # a1 = (a*v1*v1+b*v1+c) and b1 = (d*v1+e)
            # a1 and b1 are values of multiplier of A and B respectively when x = v1
            # meaning of L2,a2,b2 are same as above, just here x = v2
            # it's time to replace C in terms of B as above
            v1 = v
            while v1 == v:
                v1 = random.randint(-12, 12)
            L1 = getvalue(K, v1) * 1.0
            a1 = getvalue(A1, v1)
            b1 = getvalue(B1, v1)
            A = rhsA

            v2 = v
            while v2 == v or v2 == v1:
                v2 = random.randint(-12, 12)
            L2 = getvalue(K, v2) * 1.0
            a2 = getvalue(A1, v2)
            b2 = getvalue(B1, v2)
            # now replacing C in terms of B
            rhsB = ((L2 * b1 - A * a2 * b1) / b2 - L1 + A * a1) / (b1 * v2 - b1 * v1)
            B = rhsB
            # now place the value of B in equation 1 to find the value of C
            rhsC = (L1 - A * a1 - B * b1 * v1) / b1

    if Mtype == 1 or Mtype == 2:
        if D[0] != 0:
            v = -(D[1] / D[0])
            lhs = getvalue(K, v) * 1.0
            rhs = getvalue(A1, v)
            if rhs != 0:
                rhsA = lhs / rhs
        if D[4] != 0:
            v = -(D[5] / D[4])
            lhs = getvalue(K, v) * 1.0
            rhs = getvalue(C1, v)
            if rhs != 0:
                rhsC = lhs / rhs
        if D[2] != 0:
            if Mtype == 1:
                v = -(D[3] / D[2])
                lhs = getvalue(K, v) * 1.0
                rhs = getvalue(B1, v)
                if rhs != 0:
                    rhsB = lhs / rhs
            if Mtype == 2:
                temp = -(D[3] / D[2])
                temp1 = -(D[1] / D[0])
                v = temp
                while v == temp or v == temp1:
                    v = random.randint(-12, 12)

                lhs = getvalue(K, v) * 1.0
                a = getvalue(A1, v)
                b = getvalue(B1, v)
                c = getvalue(C1, v)
                print D[1], D[3], v, b
                rhsB = (lhs - a * rhsA - c * rhsC) / b

    ans = [rhsA, rhsB, rhsC]
    Ques['Num'] = K
    Ques['Denom'] = D
    Ques['E'] = E
    Ques['Dtype'] = Dtype
    Ques['Mtype'] = Mtype
    Ques['Ans'] = ans
    return Ques


# Returns denominator according to Dtype and Mtype
# For Mtype 1 and 2 D returns in the form of (ax+b)(cx+d)(ex+f)
# For Mtype 3 D returns in the form of (ax+b)(cx2+dx+e)
def setRandomDenom(Mtype=0):
    D = [random.randint(-12, 12), random.randint(-12, 12), random.randint(-12, 12), random.randint(-12, 12),
         random.randint(-12, 12), random.randint(-12, 12)]
    D[0] = 1
    if Mtype == 1 or Mtype == 2:
        D[2] = 1
        D[4] = 1
        if Mtype == 2:
            D[3] = D[5]
    if Mtype == 3:
        D[5] = 0
    return D


# Returns a rlist of random number as a quadratic ax2+bx+c depending on Numerator Type
def setRandomNum(types):
    K = [random.randint(-12, 12), random.randint(-12, 12), random.randint(-12, 12)]
    if types == 1:
        K[0] = 0
    if types == 2:
        K[1] = 0
    if types == 4:
        K[0] = 0
        K[1] = 0
    if types == 5:
        K[2] = 0
    if types == 6:
        K[1] = 0
        K[2] = 0
    if types == 7:
        K[0] = 0
        K[2] = 0

    return K


# Convert a list of linear multiplers as in (ax+b)(cx+d)(ex+f) to quadratic
# or cubic equations depending on Dtype and Mtype
def getEquation(D, Dtype, Mtype=0):
    temp = []
    if Mtype == 1 or Mtype == 2:
        temp1 = D[2] * D[4]
        temp2 = D[2] * D[5] + D[3] * D[4]
        temp3 = D[3] * D[5]
        if Dtype == 2:
            temp.append(temp1)
            temp.append(temp2)
            temp.append(temp3)
            return temp
        if Dtype == 3:
            temp4 = temp1 * D[0]
            temp5 = temp1 * D[1] + temp2 * D[0]
            temp6 = temp2 * D[1] + temp3 * D[0]
            temp7 = temp3 * D[1]
            temp.append(temp4)
            temp.append(temp5)
            temp.append(temp6)
            temp.append(temp7)
            return temp
    elif Mtype == 3:
        temp1 = D[2] * D[0]
        temp2 = D[2] * D[1] + D[3] * D[0]
        temp3 = D[3] * D[1] + D[4] * D[0]
        temp4 = D[4] * D[1]
        temp.append(temp1)
        temp.append(temp2)
        temp.append(temp3)
        temp.append(temp4)
        return temp
    return temp


# when solving partial fraction, this function generates three quadratic, each as a multiplier of
# A, B and C same as of this form: lhs = A(quad) + B(quad) + C(quad)
# input list D is in the form (ax+b)(cx+d)(ex+f) where a = D[0], b = D[1] and so on
def setQuadratic(D, Mtype=0):
    if Mtype == 1 or Mtype == 2:
        temp1 = D[2] * D[4]
        temp2 = D[2] * D[5] + D[3] * D[4]
        temp3 = D[3] * D[5]
        A1.append(temp1)
        A1.append(temp2)
        A1.append(temp3)

        temp1 = D[4] * D[0]
        temp2 = D[4] * D[1] + D[5] * D[0]
        temp3 = D[5] * D[1]
        B1.append(temp1)
        B1.append(temp2)
        B1.append(temp3)

        if Mtype == 1:
            temp1 = D[0] * D[2]
            temp2 = D[0] * D[3] + D[1] * D[2]
            temp3 = D[1] * D[3]
            C1.append(temp1)
            C1.append(temp2)
            C1.append(temp3)

        elif Mtype == 2:
            temp1 = 0
            temp2 = D[0]
            temp3 = D[1]
            C1.append(temp1)
            C1.append(temp2)
            C1.append(temp3)
    if Mtype == 3:
        temp1 = D[2]
        temp2 = D[3]
        temp3 = D[4]
        A1.append(temp1)
        A1.append(temp2)
        A1.append(temp3)

        temp4 = 0
        temp5 = D[0]
        temp6 = D[1]
        B1.append(temp4)
        B1.append(temp5)
        B1.append(temp6)


# returns the value of a quadratic k when passing some value of x
def getvalue(k, x):
    return k[0] * x * x + k[1] * x + k[2]


# checks for any two matches in the list
def checkEqual(items):
    i = 0
    index = []
    for item in items:
        for x in range(len(items)):
            if x != i:
                if items[x] == item:
                    index.append(i)
                    index.append(x)
                    return index
        i += 1
    index.append(-1)
    return index


# take a list of correct answers(A,B,C) and create 4 options
def getOptions(ans, correct=0):
    option = []
    temp = random.sample(range(3), 3)
    option.append(str(ans[0]))
    option.append(str(ans[1]))
    option.append(str(ans[2]))
    temp1 = ans[temp[0]]
    temp2 = temp1.find('-')
    if temp1 != '0' and temp1 != '0':
        if temp2 == -1:
            temp1 = '-' + temp1
        else:
            temp1 = temp1.replace('-', '')
        option.append(temp1)
    else:
        option.append(str(random.randint(-50, 50)))
    index = checkEqual(option)
    while index[0] != -1:
        for x in index:
            if x != correct:
                option[x] = str(random.randint(-50, 50))
        index = checkEqual(option)
    option = random.sample(option, 4)
    # print option
    return option


# convert a float number to a rational number and returns it as a string
def getAnsString(ans):
    temp = Fraction(ans).limit_denominator(100)
    num = temp.numerator
    denom = temp.denominator
    if num == 0:
        str1 = "0"
    elif denom == 1:
        str1 = str(num)
    else:
        str1 = str(num) + "<span>/</span>" + str(denom)
    return str1


# append a '+' sign before a number if a number is greateer than 0
def getSignedString(num):
    if num != 0:
        if num > 0:
            return '+' + str(num)
        else:
            return str(num)
    else:
        return ''


# checks whether coefficient of a variable is 1 or not
# and if it is 1 it removes 1
def GetCoeffString(num):
    if num != 0:
        if num == 1:
            return ''
        elif num == -1:
            return str(num).replace('1', '')
        else:
            return str(num)
    else:
        return ''


# check whether roots of the given quadratic equation are real or imaginary.
# Returns True when Real and False when Imaginary
# Quad in the form ax^2 + bx + c
def checkRootType(Quad):
    D = (Quad[1] ** 2) - (4 * Quad[0] * Quad[2])
    if D < 0:
        return False
    else:
        return True

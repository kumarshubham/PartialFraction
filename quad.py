__author__ = 'kumar'

# import math
# import random
# import csv
# from xhtml2pdf import pisa
# from  fractions import Fraction
# from lib import *
from generate import *


def main():  # beginning of the code
    print "Hello! This program finds the partial fraction to a quadratic upon cubic Equation\n\n"
    # Qtype = 0
    # Mtype = 0
    # while(Qtype == 0):
    # 	print "Enter Type of Questions  you want to generate: "
    # 	Qtype = input("To know type details please enter 0: ")
    # 	if(Qtype == 0):
    # 		getNumTypeDetail()
    # 	print "\n"

    # while(Mtype == 0 or Mtype > 3):
    # 	print "Enter Type of Questions  you want to generate: "
    # 	Mtype = input("To know details please enter 0:")
    # 	if(Mtype == 0):
    # 		getMainTypeDetail()
    # 	print "\n"

    # print "\n\n"
    Qnumbers = input("Enter number of questions you want to generate: ")
    # Qtype = 1
    Ques = []
    Dtype = 1
    Otype = 1  # 1 for one option, 2 for two options and 3 for all options
    for types in range(2):
        Mtype = types + 1
        for num in range(7):
            Qtype = num + 1
            for x in range(Qnumbers*3):
                if (x % 5) == 0:
                    Dtype = 1
                    if Mtype == 3:
                        continue
                if (x % 5) == 1:
                    Dtype = 2
                if (x % 5) == 2:
                    Dtype = 3
                Ques.append(generateQuestions(Qtype, Dtype, Mtype))

    # for num in range(Qnumbers*3*7):
    # 	if(num<(Qnumbers*7)):
    # 		Dtype = 1
    # 	if(num>(Qnumbers*7-1) and num<(Qnumbers*14)):
    # 		Dtype = 2
    # 	if(num>(Qnumbers*14-1)):
    # 		Dtype = 3
    # 	Ques.append(generateQuestions(Qtype,Dtype))
    # print Ques

    generateHTML(Ques)
    generateCSV(Ques)
    #generateImages(Ques)


def getNumTypeDetail():
    print "Welcome to Type detail introduction of partial fraction: \n"
    print "Types are defined on the basis of numerator of a Equation.\n"
    print "k1, k2 and k3 are coefficients of x's in quadratic Equation."
    print "Here are the available types:\n"
    print "\nType 1: k1 = 0, k2 != 0 and k3 != 0"
    print "\nType 2: k1 != 0, k2 = 0 and k3 != 0"
    print "\nType 3: k1 != 0, k2 != 0 and k3 != 0"
    print "\nType 4: k1 = 0, k2 = 0 and k3 != 0"
    print "\nType 5: k1 != 0, k2 != 0 and k3 = 0"
    print "\nType 6: k1 != 0, k2 = 0 and k3 = 0"
    print "\nType 7: k1 = 0, k2 != 0 and k3 = 0"


def getMainTypeDetail():
    print "Welcome to Type detail introduction of partial fraction: \n"
    print "There are basically three types of partial fraction problem.\n"
    print "Here is the list of all the three types:\n"
    print "\nType 1: 'Distinct Linear Factor' -> When denominator has three distinct linear factor" \
          " such as (x+a)(x+b)(x+c)"
    print "\nType 2: 'Repeated Linear Factor' -> When denominator has three linear factor but two of them are same" \
          " such as (x+a)(x+b)(x+c)"
    print "\nType 3: 'Distinct Irreducible Quadratic Factors' When denominator has two factor one linear and" \
          " one irreducible quadratic type such as (x+d)(ax2+bx+c) where b2-4ac < 0"


main()
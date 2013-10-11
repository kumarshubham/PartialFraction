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
    # ask !!!  0 for A, 1 for B, 2 for C, 3 for (A,B), 4 for (B,C), 5 for (A,C), 6 for (A,B,C)
    Qnumbers = input("Enter number of questions you want to generate: ")
    # Qtype = 1
    Ques = []
    Dtype = 1
    ask = 0
    Otype = 1  # 1 for one option, 2 for two options and 3 for all options
    Mtype = 1
    total = 0
    MtypeList = [4]  # Defines Main Type
    subList = [2, 2, 2, 3, 3, 3]    # Defines number of question for corresponding Dtype and askList
    DtypeList = [1, 2, 2, 1, 2, 2]  # Defines Denominator Type
    askList = [3, 4, 5, 1, 1, 1]    # Defines whether asking for A or B or C or A and B or so on

    ### Use it for Mix Bag only
    # for q in MtypeList:
    #     Mtype = q
    #     for r in range(len(subList)):
    #         Dtype = DtypeList[r]
    #         ask1 = askList[r]
    #         ask = askList[r]
    #         for s in range(subList[r]):
    #             ask = random.randint(0, 6)
    #             Qtype = random.randint(1, 7)
    #             temp = generateQuestions(Mtype, Dtype, Qtype)
    #             temp['ask'] = ask
    #             Ques.append(temp)

    ### !!! Do not use this
    # for types in range(1):
    #     Mtype = types + 1
    #     for num in range(7):
    #         Qtype = num + 1
    #         for x in range(Qnumbers):
    #             if (x % 5) == 0:
    #                 Dtype = 1
    #                 if Mtype == 3:
    #                     continue
    #             if (x % 5) == 1:
    #                 Dtype = 2
    #             if (x % 5) == 2:
    #                 Dtype = 3
    #             temp = generateQuestions(Mtype, Dtype, Qtype)
    #             temp['ask'] = ask
    #             Ques.append(temp)

    ### Use it for normal combinations
    count = 1
    for q in MtypeList:
         Mtype = q
         for r in range(len(subList)):
             Dtype = DtypeList[r]
             ask = askList[r]
             ask1 = askList[r]
             for s in range(subList[r]):
                 if Dtype != 1:
                     if ask1 == 3 or ask1 == 4 or ask1 == 5:
                         ask = random.randint(3, 5)
                 if Mtype == 3 and Dtype == 1:
                     continue
                 Qtype = random.randint(1, 7)
                 temp = generateQuestions(Mtype, Dtype, Qtype, count)
                 temp['ask'] = ask
                 Ques.append(temp)
                 count += 1

    #generateHTML(Ques)
    #generateCSV2(Ques)    # Use this for type 1, 2 and 3 with LaTex
    generateCSV3(Ques)     # Use this for type 4 with LaTex
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
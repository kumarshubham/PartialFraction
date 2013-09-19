__author__ = 'kumar'

import csv
# from xhtml2pdf import pisa
from lib import *
#from sympy import latex, Symbol
from latexmath2png import math2png


def generateHTML(ques):
    """

    :param ques:
    """
    html = "<html>"
    html += "<head><link rel='stylesheet' type='text/css' href='bootstrap.css'>"
    html += "<style type='text/css'>td{text-align: center;}.c{border-top: 1px solid;position: relative;top: 23px;" \
            "margin-left: -78px;padding-top: 3px;}"
    html += ".option{margin-left: 70px;}.optionAns{margin-left:30px}.d{border-top: 1px solid;position: relative;" \
            "top: 20px;margin-left: -21px;}</style></head>"
    html += "<body style='background-color:#cccccc'><div style='background-color:#ffffff' class='container'>"
    html += "<div style='font-family: Open sans;text-align: center;height: 70px;padding-top: 23px;'><h2>" \
            "Topic: Distinct Linear Factor</h2></div>"
    html += "<div><table class='table-striped table-bordered' style='width:100%'><thead>"
    html += "<tr><th>Qno.</th><th>Question</th>"
    html += "<th>Options</th>"
    html += "<th>Answer</th></tr></thead><tbody>"
    count = 1
    temphtml = ""
    for q in ques:
        html += "<tr>"
        html += "<td>" + str(count) + "</td>"
        html += "<td><span style='margin-right: 60px;position: relative;top: 10px;'>If</span><span> "
        if q['Num'][0] != 0:
            html += GetCoeffString(q['Num'][0])
            html += "x<sup>2</sup>"
            if q['Num'][1] > 0:
                html += "+"
        if q['Num'][1] != 0:
            html += GetCoeffString(q['Num'][1])
            html += "x"
        if q['Num'][2] > 0 and (q['Num'][0] != 0 or q['Num'][1] != 0):
            html += "+"
        if q['Num'][2] != 0:
            html += str(q['Num'][2])

        html += "<span class='c'>"

        if q['Dtype'] == 1 or q['Dtype'] == 0:
            html += "("
            if q['Denom'][0] != 0:
                if q['Denom'][0] > 1:
                    html += str(q['Denom'][0]) + "x"
                else:
                    html += "x"
                if q['Denom'][1] > 0:
                    html += "+"
            if q['Denom'][1] != 0:
                html += str(q['Denom'][1])
            html += ")"
            html += "("
            if q['Denom'][2] != 0:
                if q['Denom'][2] > 1:
                    html = html + str(q['Denom'][2]) + "x"
                else:
                    html += "x"
            if q['Denom'][3] > 0:
                html += "+"
            if q['Denom'][3] != 0:
                html += str(q['Denom'][3])
            html += ")"
            html += "("
            if q['Denom'][4] != 0:
                if q['Denom'][4] > 1:
                    html = html + str(q['Denom'][4]) + "x"
                else:
                    html += "x"
                if q['Denom'][5] > 0:
                    html += "+"
            if q['Denom'][5] != 0:
                html += str(q['Denom'][5])
            html += ")"
            html += "</span></span>"
            html = html + "<span style='position: relative;top: 10px;'> =</span><span style='margin-left: 15px;'>" \
                          " A<span class='d'>(x" + getSignedString(q['Denom'][1]) + ")</span> + " \
                          "B<span class='d'>(x" + getSignedString(q['Denom'][3]) + ")</span> + " \
                          "C<span class='d'>(x" + getSignedString(q['Denom'][5]) + ")"
            if q['Mtype'] == 2:
                html += "<sup>2</sup>"
            html += "</span></span>"
            html += "<p style='margin-left: -117px;'><br/><br/> then find the value of A</p>"

        if q['Dtype'] == 2:
            html += "("
            if q['Denom'][0] != 0:
                if q['Denom'][0] > 1:
                    html += str(q['Denom'][0]) + "x"
                else:
                    html += "x"
                if q['Denom'][1] > 0:
                    html += "+"
            if q['Denom'][1] != 0:
                html += str(q['Denom'][1])
            html += ")"

            if q['Mtype'] == 1 or q['Mtype'] == 3:
                html += "("
                if q['E'][0] != 0:
                    html += GetCoeffString(q['E'][0])
                    html += "x<sup>2</sup>"
                    if q['E'][1] > 0:
                        html += "+"
                if q['E'][1] != 0:
                    html += GetCoeffString(q['E'][1])
                    html += "x"
                if q['E'][2] > 0:
                    html += "+"
                if q['E'][2] != 0:
                    html += str(q['E'][2])
                html += ")"

            elif q['Mtype'] == 2:
                html += "("
                if q['Denom'][2] != 0:
                    if q['Denom'][2] > 1:
                        html += str(q['Denom'][2]) + "x"
                    else:
                        html += "x"
                    if q['Denom'][3] > 0:
                        html += "+"
                if q['Denom'][3] != 0:
                    html += str(q['Denom'][3])
                html += ")"
                html += "<sup>2</sup>"

            html += "</span></span>"
            html = html + "<span style='position: relative;top: 10px;'> can be split into partial fractions where " \
                          "one of the terms is  A<span class='d'>(x" + \
                          getSignedString(q['Denom'][1]) + ")</span></span>"
            html += "<p style='margin-left: -117px;'><br/><br/> then find the value of A</p>"

        if q['Dtype'] == 3:
            html += "("
            if q['E'][0] != 0:
                html = html + GetCoeffString(q['E'][0])
                html += "x<sup>3</sup>"
                if q['E'][1] > 0:
                    html += "+"
            if q['E'][1] != 0:
                html = html + GetCoeffString(q['E'][1])
                html += "x<sup>2</sup>"
                if q['E'][2] > 0:
                    html += "+"
            if q['E'][2] != 0:
                html = html + GetCoeffString(q['E'][2])
                html += "x"
            if q['E'][3] > 0:
                html += "+"
            if q['E'][3] != 0:
                html += str(q['E'][3])
            html += ")"
            html += "</span></span>"
            html = html + "<span style='position: relative;top: 10px;'> can be split into partial fractions where " \
                          "one of the terms is  A<span class='d'>(x" + \
                          getSignedString(q['Denom'][1]) + ")</span></span>"
            html += "<p style='margin-left: -117px;'><br/><br/> then find the value of A</p>"
        html += "</td>"

        str1 = getAnsString(q['Ans'][0])
        str2 = getAnsString(q['Ans'][1])
        str3 = getAnsString(q['Ans'][2])

        ans = [str1, str2, str3]
        html += "<td style='text-align:left;width:250px;'>"
        option = getOptions(ans)
        html = html + "<span class='option'><b>a.</b></span><span class='optionAns'> " + option[0] + "</span><br/>"
        html = html + "<span class='option'><b>b.</b></span><span class='optionAns'> " + option[1] + "</span><br/>"
        html = html + "<span class='option'><b>c.</b></span><span class='optionAns'> " + option[2] + "</span><br/>"
        html = html + "<span class='option'><b>d.</b></span><span class='optionAns'> " + option[3] + "</span><br/>"

        html += "</td>"

        html += "<td>"
        str1 = getAnsString(q['Ans'][0])
        str2 = getAnsString(q['Ans'][1])
        str3 = getAnsString(q['Ans'][2])
        html = html + "<h4><span style='text-align:left'>A = </span>" + str1 + "</h4>"
        html = html + "<h4><span style='text-align:left'>B = </span>" + str2 + "</h4>"
        html = html + "<h4><span style='text-align:left'>C = </span>" + str3 + "</h4>"
        html += "</td></tr>"
        count += 1
        temphtml += "<p><img src='"+ str(count-1) + ".png'/></p>"
    html += "</tbody></table></div></div></body></html>"
    # generatePDF(html)
    with open('equation.html', 'w+') as f:
        f.write(temphtml)


def generateCSV(ques):
    """

    :param ques:
    """
    count = 0
    data = []
    for q in ques:
        html = ""
        hint1 = ""
        hint2 = ""
        ask = 0
        local = " "
        if q['Dtype'] == 2 or q['Dtype'] == 3:
            html += "<span style='float:left;'>If </span><table style='float: left;position: relative; bottom: 31px; " \
                    "margin-left: 15px; margin-right: 15px;'><tbody><tr style='text-align:center'><td><span>"
            if q['Num'][0] != 0:
                html = html + GetCoeffString(q['Num'][0])
                html += "x<sup>2</sup>"
                if q['Num'][1] > 0:
                    html += "+"
            if q['Num'][1] != 0:
                html = html + GetCoeffString(q['Num'][1])
                html += "x"
            if q['Num'][2] > 0 and (q['Num'][0] != 0 or q['Num'][1] != 0):
                html += "+"
            if q['Num'][2] != 0:
                html += str(q['Num'][2])
            html += "</span></td></tr>"
            html += "<tr><td style='padding:0px;height:1px;background:#8C9009;'></td></tr>"
            html += "<tr><td>"
            html += "<span>"

        if q['Dtype'] == 1 or q['Dtype'] == 0:
            html += "<span style='position: relative;float:left;top:12px;'>If </span><span style='margin-left:50px;'>" \
                    "<span style='float: left;margin-left: 50px;margin-top: -18px;'><table><tbody><tr " \
                    "style='text-align:center'><td><span>"
            if q['Num'][0] != 0:
                html = html + GetCoeffString(q['Num'][0])
                html += "x<sup>2</sup>"
                if q['Num'][1] > 0:
                    html += "+"
            if q['Num'][1] != 0:
                html = html + GetCoeffString(q['Num'][1])
                html += "x"
            if q['Num'][2] > 0 and (q['Num'][0] != 0 or q['Num'][1] != 0):
                html += "+"
            if q['Num'][2] != 0:
                html += str(q['Num'][2])
            html += "</span></td></tr>"
            html += "<tr><td style='padding:0px;height:1px;background:#8C9009;'></td></tr>"
            html += "<tr><td>"
            html += "<span>"
            html += "("
            if q['Denom'][0] != 0:
                if q['Denom'][0] > 1:
                    html = html + str(q['Denom'][0]) + "x"
                else:
                    html += "x"
                if q['Denom'][1] > 0:
                    html += "+"
            if q['Denom'][1] != 0:
                html += str(q['Denom'][1])
            html += ")"
            html += "("
            if q['Denom'][2] != 0:
                if q['Denom'][2] > 1:
                    html = html + str(q['Denom'][2]) + "x"
                else:
                    html += "x"
                if q['Denom'][3] > 0:
                    html += "+"
            if q['Denom'][3] != 0:
                html += str(q['Denom'][3])
            html += ")"
            html += "("
            if q['Denom'][4] != 0:
                if q['Denom'][4] > 1:
                    html = html + str(q['Denom'][4]) + "x"
                else:
                    html += "x"
                if q['Denom'][5] > 0:
                    html += "+"
            if q['Denom'][5] != 0:
                html += str(q['Denom'][5])
            html += ")"
            html += "</span></span></td></tr></tbody></table></span>"
            html = html + "<span style='position: relative;top: 12px;'> = </span><span style='margin-left:20px;'> " \
                          "A<span style='border-top: 1px solid;position: relative;top: 29px;margin-left: -25px;'>(x" + \
                          getSignedString(q['Denom'][1]) + ")</span> + B<span style='border-top: 1px solid;position: " \
                          "relative;top: 29px;margin-left: -25px;'>(x" + \
                          getSignedString(q['Denom'][3]) + ")</span> + C<span style='border-top: 1px solid;position: " \
                          "relative;top: 29px;margin-left: -25px;'>(x" + \
                          getSignedString(q['Denom'][5]) + ")"
            if q['Mtype'] == 2:
                html += "<sup>2</sup>"
            html += "</span></span>"
            html += "<br/><br/><div style='clear:both'></div> then find the value of A"
            hint1 = "on the LHS of the equation"

        if q['Dtype'] == 2:
            html += "("
            if q['Denom'][0] != 0:
                if q['Denom'][0] > 1:
                    html = html + str(q['Denom'][0]) + "x"
                else:
                    html += "x"
                if q['Denom'][1] > 0:
                    html += "+"
            if q['Denom'][1] != 0:
                html += str(q['Denom'][1])
            html += ")"

            if q['Mtype'] == 1 or q['Mtype'] == 3:
                local = "("
                if q['E'][0] != 0:
                    local = local + GetCoeffString(q['E'][0])
                    local += "x<sup>2</sup>"
                    if q['E'][1] > 0:
                        local += "+"
                if q['E'][1] != 0:
                    local = local + GetCoeffString(q['E'][1])
                    local += "x"
                if q['E'][2] > 0:
                    local += "+"
                if q['E'][2] != 0:
                    local += str(q['E'][2])
                local += ")"
                html += local

            elif q['Mtype'] == 2:
                html += "("
                if q['Denom'][2] != 0:
                    if q['Denom'][2] > 1:
                        html = html + str(q['Denom'][2]) + "x"
                    else:
                        html += "x"
                    if q['Denom'][3] > 0:
                        html += "+"
                if q['Denom'][3] != 0:
                    html += str(q['Denom'][3])
                html += ")"
                html += "<sup>2</sup>"

            ask = 1
            html += "</span></span></td></tr></tbody></table>"
            html += "can be split into partial fraction where <br/><p style='position: relative;margin-top: 80px;" \
                    "bottom: 40px;'>one of the terms is<span  style='position: relative;bottom: 12px;" \
                    "margin-right: 10px;'><span style='margin-left:20px;'> "

            hint2 = "A/(x" + getSignedString(q['Denom'][1]) + ") + "
            if q['Mtype'] == 1 or q['Mtype'] == 2:
                hint2 = hint2 + "B/(x" + getSignedString(q['Denom'][3]) + ") + C/(x" + getSignedString(
                    q['Denom'][5]) + ")"
                html = html + "B</span><span style='border-top: 1px solid;position: relative;top: 29px;margin-left:" \
                              " -25px;'>(x" + getSignedString(q['Denom'][3]) + ")</span></span>"
            elif q['Mtype'] == 3:
                hint2 = hint2 + "(Bx+C)/(" + GetCoeffString(q['E'][0]) + "x<sup>2</sup>+" + GetCoeffString(
                    q['E'][1]) + "x" + str(q['E'][2])
                html = html + "(Bx+C)</span><span style='border-top: 1px solid;position: relative;top: 29px;" \
                              "margin-left: -75px;'>" + local + "</span></span>"
            html += "<span>then find the value of B</span></p>"

        if q['Dtype'] == 3:
            html += "("
            if q['E'][0] != 0:
                html = html + GetCoeffString(q['E'][0])
                html += "x<sup>3</sup>"
                if q['E'][1] > 0:
                    html += "+"
            if q['E'][1] != 0:
                html = html + GetCoeffString(q['E'][1])
                html += "x<sup>2</sup>"
                if q['E'][2] > 0:
                    html += "+"
            if q['E'][2] != 0:
                html = html + GetCoeffString(q['E'][2])
                html += "x"
            if q['E'][3] > 0:
                html += "+"
            if q['E'][3] != 0:
                html += str(q['E'][3])
            html += ")"
            html += "</span></span></td></tr></tbody></table>"
            html = html + "can be split into partial fraction where<br/><p style='position: relative;" \
                          "margin-top: 80px;bottom: 40px;'> one of the terms is<span style='position: relative;" \
                          "bottom: 12px;margin-right: 10px;'><span style='margin-left:20px;'> A</span>" \
                          "<span style='border-top: 1px solid;" \
                          "position: relative;top: 29px;margin-left: -25px;'>(x" + getSignedString(q['Denom'][1]) + \
                          ")</span></span>"
            html += "<span>then find the value of A</span></p>"
            hint2 = "A/(x" + getSignedString(q['Denom'][1]) + ") + "
            if q['Mtype'] == 1 or q['Mtype'] == 2:
                hint2 = hint2 + "B/(x" + getSignedString(q['Denom'][3]) + ") + C/(x" + getSignedString(
                    q['Denom'][5]) + ")"
            elif q['Mtype'] == 3:
                hint2 = hint2 + "(Bx+C)/(" + GetCoeffString(q['Denom'][2]) + "x<sup>2</sup>+" + GetCoeffString(
                    q['Denom'][3]) + "x" + str(q['Denom'][4])
        Question = html
        # generatePDF(html,count)

        str1 = getAnsString(q['Ans'][0])
        str2 = getAnsString(q['Ans'][1])
        str3 = getAnsString(q['Ans'][2])

        ans = [str1, str2, str3]
        option = getOptions(ans, ask)
        option1 = option[0]
        option2 = option[1]
        option3 = option[2]
        option4 = option[3]
        index = 0
        correct = 0
        correctOptions = {}
        if ask == 0:
            co = "A"
        elif ask == 1:
            co = "B"
        else:
            co = "C"
        feedback = []
        feedback1 = "Good Work! That\'s the correct Answer"
        feedback2 = "Sorry but this is the coefficient of the term 1/(x+"
        for x in option:
            index += 1
            if str1 == x:
                if ask == 0:
                    correct = index
                    feedback.append(feedback1)
                else:
                    feedback.append(feedback2 + getSignedString(q['Denom'][1]) + ") and not the value of " + co)
                correctOptions['A'] = index
            elif x == str2:
                if ask == 1:
                    correct = index
                    feedback.append(feedback1)
                else:
                    feedback.append(feedback2 + getSignedString(q['Denom'][3]) + ") and not the value of " + co)
                correctOptions['B'] = index
            elif x == str3:
                if ask == 2:
                    correct = index
                    feedback.append(feedback1)
                else:
                    feedback.append(feedback2 + getSignedString(q['Denom'][5]) + ") and not the value of " + co)
                correctOptions['C'] = index
            else:
                feedback.append("This is not the correct answer. Lets try the next one")

        topic = 7  # "topic_id"
        difficulty = q['Dtype']
        hint1 = "Check if the denominator of the expression \
				" + hint1 + " has been reduced to the lowest factors"
        hint2 = "Let the simplified expression (with factorized \
				denominator) be equal to" + hint2
        hint3 = "Substitute appropriate values of x in the equation to find the value of A"
        if q['Dtype'] == 1:
            hint2 = hint3
            data.append([Question, 4, option1, option2, option3, option4, correct, hint1, hint2, '', topic, difficulty])
        else:
            data.append(
                [Question, 4, option1, option2, option3, option4, correct, hint1, hint2, hint3, topic, difficulty])
        count += 1
    # data1 = data[0:18]
    # data2 = data[18:36]
    # data3 = data[36:]
    with open('test.csv', 'wb') as fp:
        a = csv.writer(fp, delimiter=',')
        a.writerows(data)

    # with open('Partial Fractions Complete - 2.2.csv', 'wb') as fp:
    #     a = csv.writer(fp, delimiter=',')
    #     a.writerows(data2)
    #
    # with open('Partial Fractions Complete - 3.2.csv', 'wb') as fp:
    #     a = csv.writer(fp, delimiter=',')
    #     a.writerows(data3)


def generateImages(ques):
    """

    :param ques:
    """
    #count = 0
    #data = []
    #eq1 = '\\frac{a x^{2} + b x + c}{\\left(d x + a\\right) \\left(e x + b\\right) \\left(f x + c\\right)}' << Dtype=1
    #eq2 = '\\frac{a x^{2} + b x + c}{\\left(a x + b\\right) \\left(c x^{2} + d x + e\\right)}' << Dtype = 2
    #eq3 = '\\frac{a x^{2} + b x + c}{d x^{3} + e x^{2} + f x + g}' << Equation for Dtype = 3
    count = 0
    equationList = []
    for q in ques:
        count += 1
        eq = '\\frac'
        eq += "{"
        if q['Num'][0] != 0:
            eq += GetCoeffString(q['Num'][0])
            eq += " x^{2} "
            if q['Num'][1] > 0:
                eq += " + "
        if q['Num'][1] != 0:
            eq = eq + GetCoeffString(q['Num'][1])
            eq += " x "
        if q['Num'][2] > 0 and (q['Num'][0] != 0 or q['Num'][1] != 0):
            eq += " + "
        if q['Num'][2] != 0:
            eq += str(q['Num'][2])
        eq += "}"

        if q['Dtype'] == 1 or q['Dtype'] == 0:
            eq += "{\\left("
            if q['Denom'][0] != 0:
                if q['Denom'][0] > 1:
                    eq += str(q['Denom'][0]) + " x "
                else:
                    eq += " x "
                if q['Denom'][1] > 0:
                    eq += " + "
            if q['Denom'][1] != 0:
                eq += str(q['Denom'][1])
            eq += "\\right) "
            eq += "\\left("
            if q['Denom'][2] != 0:
                if q['Denom'][2] > 1:
                    eq += str(q['Denom'][2]) + " x "
                else:
                    eq += " x "
                if q['Denom'][3] > 0:
                    eq += " + "
            if q['Denom'][3] != 0:
                eq += str(q['Denom'][3])
            eq += "\\right) "
            eq += "\\left("
            if q['Denom'][4] != 0:
                if q['Denom'][4] > 1:
                    eq += str(q['Denom'][4]) + " x "
                else:
                    eq += " x "
                if q['Denom'][5] > 0:
                    eq += " + "
            if q['Denom'][5] != 0:
                eq += str(q['Denom'][5])
            eq += "\\right)}"

        if q['Dtype'] == 2:
            eq += "{\\left("
            if q['Denom'][0] != 0:
                if q['Denom'][0] > 1:
                    eq += str(q['Denom'][0]) + " x "
                else:
                    eq += " x "
                if q['Denom'][1] > 0:
                    eq += " + "
            if q['Denom'][1] != 0:
                eq += str(q['Denom'][1])
            eq += "\\right)"

            if q['Mtype'] == 1 or q['Mtype'] == 3:
                eq += "\\left("
                if q['E'][0] != 0:
                    eq += GetCoeffString(q['E'][0])
                    eq += "x^{2}"
                    if q['E'][1] > 0:
                        eq += " + "
                if q['E'][1] != 0:
                    eq += GetCoeffString(q['E'][1])
                    eq += " x "
                if q['E'][2] > 0:
                    eq += " + "
                if q['E'][2] != 0:
                    eq += str(q['E'][2])
                eq += "\\right)}"

            elif q['Mtype'] == 2:
                eq += "\\left("
                if q['Denom'][2] != 0:
                    if q['Denom'][2] > 1:
                        eq += str(q['Denom'][2]) + " x "
                    else:
                        eq += " x "
                    if q['Denom'][3] > 0:
                        eq += " + "
                if q['Denom'][3] != 0:
                    eq += str(q['Denom'][3])
                eq += "\\right)^{2}}"

        if q['Dtype'] == 3:
            eq += "{\\left("
            if q['E'][0] != 0:
                eq += GetCoeffString(q['E'][0])
                eq += " x^{3} "
                if q['E'][1] > 0:
                    eq += " + "
            if q['E'][1] != 0:
                eq += GetCoeffString(q['E'][1])
                eq += " x^{2} "
                if q['E'][2] > 0:
                    eq += " + "
            if q['E'][2] != 0:
                eq += GetCoeffString(q['E'][2])
                eq += " x "
            if q['E'][3] > 0:
                eq += " + "
            if q['E'][3] != 0:
                eq += str(q['E'][3])
            eq += "\\right)}"

        print eq
        equationList.append(eq)
    math2png(equationList, '/home/kumar/mypy/images/',size=2)




# def generatePDF(html, count=0):
#     # print html
#     filename = str(count) + ".pdf"
#     pdf = pisa.CreatePDF(html, file(filename, "wb"))

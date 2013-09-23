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
    # temphtml = ""
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
        #temphtml += "<p><img src='"+ str(count-1) + ".png'/></p>"
    html += "</tbody></table></div></div></body></html>"
    # generatePDF(html)
    with open('equation.html', 'w+') as f:
        f.write(html)


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
        ask = random.randint(0, 6)  # 0 for A, 1 for B, 2 for C, 3 for (A,B), 4 for (B,C), 5 for (A,C), 6 for (A,B,C)
        local = " "
        numEq = ""
        ## co stands for correct option i.e. option asked in the question(A or B or C)
        ## nA stands for options not asked
        if ask == 0:
            co = "A"
            nA1 = "B"
            nA2 = "C"
            rootIndex1 = 1
        elif ask == 1:
            co = "B"
            nA1 = "A"
            nA2 = "C"
            rootIndex1 = 3
        elif ask == 2:
            co = "C"
            nA1 = "A"
            nA2 = "B"
            rootIndex1 = 5
        elif ask == 3:
            co = "A and B"
            nA1 = "C"
            nA2 = "B"
            rootIndex1 = 1
            rootIndex2 = 3
        elif ask == 4:
            co = "B and C"
            nA1 = "A"
            nA2 = "C"
            rootIndex1 = 3
            rootIndex2 = 5
        elif ask == 5:
            co = "A and C"
            nA1 = "B"
            nA2 = "C"
            rootIndex1 = 1
            rootIndex2 = 5
        elif ask == 6:
            co = "A,B and C"
            nA1 = "B"
            nA2 = "C"
            rootIndex1 = 1
            rootIndex2 = 3
            rootIndex3 = 5

        if q['Dtype'] == 2 or q['Dtype'] == 3:
            html += "<span style='float:left;'>If </span><table style='float: left;position: relative; bottom: 31px; " \
                    "margin-left: 15px; margin-right: 15px;'><tbody><tr style='text-align:center'><td><span>"
            if q['Num'][0] != 0:
                numEq += GetCoeffString(q['Num'][0])
                numEq += "x<sup>2</sup>"
                if q['Num'][1] > 0:
                    numEq += "+"
            if q['Num'][1] != 0:
                numEq += GetCoeffString(q['Num'][1])
                numEq += "x"
            if q['Num'][2] > 0 and (q['Num'][0] != 0 or q['Num'][1] != 0):
                numEq += "+"
            if q['Num'][2] != 0:
                numEq += str(q['Num'][2])
            html += numEq
            html += "</span></td></tr>"
            html += "<tr><td style='padding:0px;height:1px;background:#8C9009;'></td></tr>"
            html += "<tr><td>"
            html += "<span>"

        if q['Dtype'] == 1 or q['Dtype'] == 0:
            html += "<span style='position: relative;float:left;top:12px;'>If </span><span style='margin-left:50px;'>" \
                    "<span style='float: left;margin-left: 50px;margin-top: -18px;'><table><tbody><tr " \
                    "style='text-align:center'><td><span>"
            if q['Num'][0] != 0:
                numEq += GetCoeffString(q['Num'][0])
                numEq += "x<sup>2</sup>"
                if q['Num'][1] > 0:
                    numEq += "+"
            if q['Num'][1] != 0:
                numEq += GetCoeffString(q['Num'][1])
                numEq += "x"
            if q['Num'][2] > 0 and (q['Num'][0] != 0 or q['Num'][1] != 0):
                numEq += "+"
            if q['Num'][2] != 0:
                numEq += str(q['Num'][2])
            html += numEq
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
            html += "<br/><br/><div style='clear:both'></div> then find the value of " + co
            # hint1 = "on the LHS of the equation"

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

            html += "</span></span></td></tr></tbody></table>"
            if ask <= 2:
                tempStr1 = "can be resolved to partial fractions such that"
                tempStr2 = "one of the terms in its partial fractions is"
                tempStr3 = "then find the value of " + co
            else:
                if ask ==6:
                    tempWord = " all"
                else:
                    tempWord = ""
                tempStr1 = "can be resolved to partial fractions,"
                tempStr2 = "which of the following options contains" + tempWord + " the correct coefficients of its " \
                                                                                  "partial fractions"
                tempStr3 = ""

            html += tempStr1 + " <br/><p style='position: relative;margin-top: 80px;bottom: 40px;'>" + tempStr2 + \
                "<span  style='position: relative;bottom: 12px;" \
                "margin-right: 10px;'><span style='margin-left:20px;'> "

            if ask <= 2:
                if q['Mtype'] == 1 or q['Mtype'] == 2 or (q['Mtype'] == 3 and ask == 0):
                    html += co + "</span><span style='border-top: 1px solid;position: relative;top: 29px;margin-left:" \
                        " -25px;'>(x" + getSignedString(q['Denom'][2 * ask + 1]) + ")"
                    if q['Mtype'] == 2 and ask == 2:
                        html += "<sup>2</sup>"
                    html += "</span></span>"
                elif q['Mtype'] == 3 and ask != 0:
                    html = html + "(Bx+C)</span><span style='border-top: 1px solid;position: relative;top: 29px;" \
                                  "margin-left: -75px;'>" + local + "</span></span>"
            else:
                html += "</span></span>"
            html += "<span>" + tempStr3 + "</span></p>"

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
            if ask <= 2:
                tempStr1 = "can be resolved to partial fractions such that"
                tempStr2 = "one of the terms in its partial fractions is"
                tempStr3 = "then find the value of " + co
            else:
                if ask ==6:
                    tempWord = " all"
                else:
                    tempWord = ""
                tempStr1 = "can be resolved to partial fractions,"
                tempStr2 = "which of the following options contains" + tempWord + " the correct coefficients of its " \
                                                                                  "partial fractions"
                tempStr3 = ""

            html += tempStr1 + " <br/><p style='position: relative;margin-top: 80px;bottom: 40px;'>" + tempStr2 + \
                "<span  style='position: relative;bottom: 12px;" \
                "margin-right: 10px;'><span style='margin-left:20px;'> "

            if ask <= 2:
                if q['Mtype'] == 1 or q['Mtype'] == 2 or (q['Mtype'] == 3 and ask == 0):

                    html += co + "</span><span style='border-top: 1px solid;position: relative;top: 29px;margin-left:" \
                        " -25px;'>(x" + getSignedString(q['Denom'][2 * ask + 1]) + ")"
                    if q['Mtype'] == 2 and ask == 2:
                        html += "<sup>2</sup>"
                    html += "</span></span>"
                elif q['Mtype'] == 3 and ask != 0:
                    local = "("
                    if q['Denom'][2] != 0:
                        local = local + GetCoeffString(q['Demon'][2])
                        local += "x<sup>2</sup>"
                        if q['Denom'][3] > 0:
                            local += "+"
                    if q['Denom'][3] != 0:
                        local = local + GetCoeffString(q['E'][1])
                        local += "x"
                    if q['Denom'][4] > 0:
                        local += "+"
                    if q['Denom'][4] != 0:
                        local += str(q['Denom'][4])
                    local += ")"
                    html = html + "(Bx+C)</span><span style='border-top: 1px solid;position: relative;top: 29px;" \
                                  "margin-left: -75px;'>" + local + "</span></span>"
            else:
                html += "</span></span>"
            html += "<span>" + tempStr3 + "</span></p>"

            # html = html + "can be split into partial fraction where<br/><p style='position: relative;" \
            #               "margin-top: 80px;bottom: 40px;'> one of the terms is<span style='position: relative;" \
            #               "bottom: 12px;margin-right: 10px;'><span style='margin-left:20px;'> " + co + "</span>" \
            #               "<span style='border-top: 1px solid;" \
            #               "position: relative;top: 29px;margin-left: -25px;'>(x" + getSignedString(q['Denom'][1]) + \
            #               ")</span></span>"
            # html += "<span>then find the value of A</span></p>"
            # hint2 = "A/(x" + getSignedString(q['Denom'][1]) + ") + "
            # if q['Mtype'] == 1 or q['Mtype'] == 2:
            #     hint2 = hint2 + "B/(x" + getSignedString(q['Denom'][3]) + ") + C/(x" + getSignedString(
            #         q['Denom'][5]) + ")"
            #     if q['Mtype'] ==2:
            #         hint2 += "<sup>2</sup>"
            # elif q['Mtype'] == 3:
            #     hint2 = hint2 + "(Bx+C)/(" + GetCoeffString(q['Denom'][2]) + "x<sup>2</sup>+" + GetCoeffString(
            #         q['Denom'][3]) + "x" + getSignedString(q['Denom'][4]) + ")"
        Question = html
        # generatePDF(html,count)

        str1 = getAnsString(q['Ans'][0])
        str2 = getAnsString(q['Ans'][1])
        str3 = getAnsString(q['Ans'][2])

        ans = [str1, str2, str3]
        option = getOptions(ans, ask, q['Dtype'])
        option1 = option[0]
        option2 = option[1]
        option3 = option[2]
        option4 = option[3]
        index = 0
        correct = 0
        feedback = []
        feedback1 = "Your answer is correct! Let\'s try the next one"
        feedback2 = "The selected answer is the value of "
        feedback3 = "You've got one of the coefficients correct i.e. the value of "
        feedback4 = " but the second coefficient is incorrect. Let's try the next one"
        feedback5 = "You've got two of the coefficients correct i.e. the value of "
        feedback6 = " but the other two coefficients are incorrect. Let's try the next one"
        feedback7 = " but the third coefficient is incorrect. Let's try the next one"
        for x in option:
            index += 1
            find1 = x.find(str1)
            find2 = x.find(str2)
            find3 = x.find(str3)
            ans1 = None
            ansCount = 0
            if ask != 6:
                if find1 != -1:
                    ans1 = "A"
                elif find2 != -1:
                    ans1 = "B"
                elif find3 != -1:
                    ans1 = "C"
            else:
                if find1 != -1:
                    find4 = x.find("-" + str1)
                    if find4 == -1:
                        ans1 = "A"
                        ansCount += 1
                if find2 != -1:
                    find4 = x.find("-" + str2)
                    if find4 == -1:
                        if ansCount > 0:
                            ans1 += " and B"
                        else:
                            ans1 = "B"
                        ansCount += 1
                if find3 != -1:
                    find4 = x.find("-" + str3)
                    if find4 == -1:
                        if ansCount > 0:
                            ans1 += " and C"
                        else:
                            ans1 = "C"
                        ansCount += 1


            if x == str1:
                if ask == 0:
                    correct = index
                    feedback.append(feedback1)
                else:
                    feedback.append(feedback2 + "A and not " + co + ". Let's try the next one")
                print "Inside A", ask

            elif x == str2:
                if ask == 1:
                    correct = index
                    feedback.append(feedback1)
                else:
                    feedback.append(feedback2 + "B and not " + co + ". Let's try the next one")
                print "Inside B", ask

            elif x == str3:
                if ask == 2:
                    correct = index
                    feedback.append(feedback1)
                else:
                    feedback.append(feedback2 + "C and not " + co + ". Let's try the next one")
                print "Inside C", ask

            elif x == str1 + ", " + str2 or x == str2 + ", " + str1:
                if ask == 3 or (ask != 6 and q['Dtype'] != 1):
                    correct = index
                    feedback.append(feedback1)
                elif ask != 6 and q['Dtype'] == 1:
                    if ask == 4:
                        ans1 = "B"
                    else:
                        ans1 = "A"
                    feedback.append(feedback3 + ans1 + feedback4)
                # else:
                #     feedback.append(feedback2 + "A and B and not " + co + ". Let's try the next one")
                print "Inside A,B", ask

            elif x == str2 + ", " + str3 or x == str3 + ", " + str2:
                if ask == 4 or (ask != 6 and q['Dtype'] != 1):
                    correct = index
                    feedback.append(feedback1)
                elif ask != 6 and q['Dtype'] == 1:
                    if ask == 3:
                        ans1 = "B"
                    else:
                        ans1 = "C"
                    feedback.append(feedback3 + ans1 + feedback4)
                # else:
                #     feedback.append(feedback2 + "B and C and not " + co + ". Let's try the next one")
                print "Inside B,C", ask

            elif x == str1 + ", " + str3 or x == str3 + ", " + str1:
                if ask == 5 or (ask != 6 and q['Dtype'] != 1):
                    correct = index
                    feedback.append(feedback1)
                elif ask != 6 and q['Dtype'] == 1:
                    if ask == 3:
                        ans1 = "A"
                    else:
                        ans1 = "C"
                    feedback.append(feedback3 + ans1 + feedback4)
                # else:
                #     feedback.append(feedback2 + "A and C and not " + co + ". Let's try the next one")
                print "Inside A,C", ask

            elif x == str1 + ", " + str2 + ", " + str3:
                if ask == 6:
                    correct = index
                    feedback.append(feedback1)
                # else:
                #     feedback.append(feedback2 + "A,B and C and not " + co + ". Let's try the next one")
                print "Inside A,B,C", ask

            elif ans1:
                if ask != 6:
                    feedback.append(feedback3 + ans1 + feedback4)
                else:
                    if ansCount == 1:
                        feedback.append(feedback3 + ans1 + feedback6)
                    elif ansCount == 2:
                        feedback.append(feedback5 + ans1 + feedback7)
                print "Inside ans1", ask, ans1
            else:
                feedback.append("Unfortunately the selected answer is not a co-efficient of any of the partial"
                                " fractions. Let's try the next one")
                print "Inside Else", ask
        print option
        print feedback
        root1 = str(q['Denom'][rootIndex1])
        topic = 7  # "topic_id"
        difficulty = q['Dtype']
        hintText1 = "Rearrange the equation in the form " + numEq + " = " + getRHS(q)
        hintText2 = "Substitute the value of x such that terms " + nA1 + " and " + nA2 + " are removed from the equation"
        hintText3 = "Based on the above hint , you need to substitute the value of x = " + root1 + " to get the value of " + co[0]
        hintText4 = "Ensure that the denominator of the expression is factorized  and reduced  to factors of " \
                    "the lowest degree"
        hintText5 = " to get " + co[0] + "."
        if ask > 2:
            root3 = ""
            root2 = str(q['Denom'][rootIndex2])
            if ask == 6:
                root3 = str(q['Denom'][rootIndex3])
            hintText6 = " Similarly substitute a different value of x to get the value of " + co[6]
            hintText7 = " Similarly substituting the value of x = " + root2 +" will get you the value of " + co[6]
            hintText8 = "Substitute the value of x such that terms any two of the three terms of the equation shown " \
                        "in the previous hint are removed to get one coefficient. Repeat this step with appropriate " \
                        "values of x to find the coefficients of the other two terms as well"
            hintText9 = "Substitute different values of x such that two of the terms are removed from the equation " \
                        "to get one of the co-efficients. Repeat the process to get the values of the other coefficients"
            hintText10 = "Based on the above hint , you need to substitute the value of x = " + root1 + " to get the value of A ,"\
                         " x = " + root2 + " to get the value of B and x = " + root3 + " to get the value of C"
        if q['Dtype'] == 2 or q['Dtype'] == 3:
            hint1 = hintText4
            hint2 = hintText1
            if ask == 3 or ask ==4 or ask == 5 or ask == 6:
                hint3 = hintText8
            else:
                hint3 = hintText2

        if q['Dtype'] == 1:
            hint1 = hintText1
            if ask == 3 or ask == 4 or ask == 5:
                hint2 = hintText2 + hintText5 + hintText6
                hint3 = hintText3 + hintText7
            elif ask == 0 or ask == 1 or ask == 2:
                hint2 = hintText2
                hint3 = hintText3
            else:
                hint2 = hintText9
                hint3 = hintText10
        data.append(
            [Question, 4, option1, option2, option3, option4, correct, hint1, hint2, hint3, topic, difficulty,
                feedback[0], feedback[1], feedback[2], feedback[3]])
        count += 1
        print hint1, hint2, hint3
    # data1 = data[0:18]
    # data2 = data[18:36]
    # data3 = data[36:]
    with open('test.csv', 'wb') as fp:
        a = csv.writer(fp, delimiter=',')
        a.writerows(data)
    print "Done", len(data)
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
    math2png(equationList, '/home/kumar/mypy/images/', size=2)




# def generatePDF(html, count=0):
#     # print html
#     filename = str(count) + ".pdf"
#     pdf = pisa.CreatePDF(html, file(filename, "wb"))

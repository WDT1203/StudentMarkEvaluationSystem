# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20231194
# Date: 12/13/2023

#variables and list to save outcomes
pro = 0
trailer = 0
retriver = 0
exclude = 0
resultList = []         #list of final results

#main programming code user defined,
def mainpro_():
    credit_range = [0,20,40,60,80,100,120]          #to limit the input ranges
    while True:
        try:
            pass_ = int(input("Enter the Pass credits : "))
            while pass_ not in credit_range:
                print("Out of range.\n")
                pass_ = int(input("Enter the Pass credits : "))
                
            defer_ = int(input("Enter the Defer credits : "))
            while defer_ not in credit_range:
                print("Out of range.\n")
                defer_ = int(input("Enter the Defer credits : "))

            fail_ = int(input("Enter the Fail credits : "))
            while fail_ not in credit_range:
                print("Out of range.\n")
                fail_ = int(input("Enter the Fail credits : "))
        except ValueError:
            print("Integer Required.\n")
            continue
        break  
        
    
    sum_ = pass_ + defer_ + fail_      #sum of inputs to check whether its valid

    global reList       #using variables outside of user defined function                 

    if sum_ != 120:
        print("Total incorrect.\n")
    elif pass_ == 120:
        result = "Progress"
        resultList.append([result,pass_,defer_,fail_])  #saving inputs to the list
        print(result,'\n')
        global pro
        pro += 1
    elif pass_ ==100:
        result = "Progress (module trailer)"
        resultList.append([result,pass_,defer_,fail_])
        print(result,'\n')
        global trailer
        trailer += 1
    elif fail_ >=80:
        result = "Exclude"
        resultList.append([result,pass_,defer_,fail_])
        print(result,'\n')
        global exclude
        exclude += 1
    else:
        result = "Do not progress - module retriever"
        resultList.append([result,pass_,defer_,fail_])
        print(result,'\n')
        global retriver
        retriver += 1



#staff, student menu for user to choose        
import sys    #https://www.altcademy.com/blog/how-to-end-program-in-python/

while True:
    print("Are you a student or staff member?")
    staff_student = str(input("Enter 'student' or 'staff' : "))
    if staff_student == "student":
        print("")
        mainpro_()
        sys.exit()
    elif staff_student == "staff":
        print("")
        mainpro_()
        break
    else:
        print("Invalid input")
        continue

#multiple outcomes for staff member
while True:

    print("Would you like to enter another set of data?")
    continue_ = str(input("Enter 'y' for yes or 'q' to quit and view results: "))
    print("")

    if continue_ == "y":
        mainpro_()
        continue
    elif continue_ == "q":
        print("END")
        print("")
        break
    else:
        print("Inavalid input.\n")
        continue




sumOut = pro + trailer + retriver + exclude    #total outcomes


from graphics import*

win = GraphWin("Histogram",495,600)
win.setBackground("Lightcyan")
aline = Line(Point(20,win.getHeight()-60),Point(475,win.getHeight()-60))
aline.draw(win)
text = Text(Point(120,win.getHeight()-550),str("Histogram Results"))
text.draw(win)
text.setSize(18)
text.setStyle("bold")
text.setTextColor("green")
text = Text(Point(495/2,win.getHeight()-20),str(str(sumOut)+ " outcomes in total"))
text.draw(win)
text.setStyle("bold italic")
text.setTextColor("dimgray")

#user defined function for histogram
def bar(a,b):   #a is index of bar, b is variable for the bar data.
    if a == 1:                              #websites used to choose colours
        status_ = "Progress"                #https://www.learnui.design/tools/data-color-picker.html
        colour_ = "paleturquoise"           #https://matplotlib.org/3.1.0/gallery/color/named_colors.html
    elif a == 2:                            #https://www.colorabout.com/color/hex/80adad/#google_vignette
        status_ = "Trailer"
        colour_ = "cadetblue"
    elif a == 3:
        status_ = "Retriver"
        colour_ = "teal"
    else:
        status_ = "Exclude"
        colour_ = "lightpink"
        
    width = 100   #width of a bar
    bar_a = Rectangle(Point(40+(width*(a-1))+(5*(a-1)), win.getHeight()-60), Point(40+(width*a)+(5*(a-1)),win.getHeight()-60 - 20*b))
    bar_a.setFill(colour_)
    bar_a.draw(win)
    text = Text(Point(40+(width*(a-1))+(5*(a-1))+ width/2,win.getHeight()-60 - 10 - 20*b ), str(b))
    text.draw(win)
    text.setStyle("bold")
    text.setTextColor("dimgray")
    text = Text(Point(40+(width*(a-1))+(5*(a-1))+width/2,win.getHeight() - 60 + 10 ), str(status_))
    text.draw(win)
    text.setStyle("bold")
    text.setTextColor("dimgray")

#create the bar chart using user defined function
bar(1,pro)
bar(2,trailer)
bar(3,retriver)
bar(4,exclude)



print("Part 2 :\n")
#prints results and input credits as a list
for i in range(len(resultList)):
    print(f"{resultList[i][0]} - {resultList[i][1]} ,{resultList[i][2]} ,{resultList[i][3]}")
    
print("")

print("Part 3 :\n")
#saves results and input credits to a text file
f = open("Part_3.txt","w")
for i in range(len(resultList)):
    ress = (f"{resultList[i][0]} - {resultList[i][1]} ,{resultList[i][2]} ,{resultList[i][3]}")
    f.write(ress + "\n")


f = open("Part_3.txt", "r")
print(f.read())















    

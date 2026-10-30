#Engineering Result Calculator
#Function Definition
def getmark1():
    global a,b,c,d,e
    print("Enter marks for Semester 1:")
    a=int(input("Subject 1 (CE-I) :"))
    b=int(input("Subject 2 (CFE)  :"))
    c=int(input("Subject 3 (BAP)  :"))
    d=int(input("Subject 4 (EC)   :"))
    e=int(input("Subject 5 (PSCP) :"))
    print()
    print("~!!!*** SEMESTER -I RESULT ***!!!~")
    print()

def design():
    print("- "*24)
    print("Subject","Marks ","Grade ","Grade_Point |",sep="  |  ")
    print("- "*24)    

def find(x):
    if 90<x and x<=100:
        print("|",'O ',"|","10","    |",sep="    ")
        print("- "*24)    
    elif 80<x and x<=90:
        print('|','A+',"|"," 9","    |",sep="    ")
        print("- "*24)    
    elif 70<x and x<=80:
        print('|','A ',"|"," 8","    |",sep="    ")
        print("- "*24)      
    elif 60<x and x<=70:
        print('|','B+',"|"," 7","    |",sep="    ")
        print("- "*24)
    elif 50<x and x<=60:
        print('|','B ',"|"," 6","    |",sep="    ")
        print("- "*24)
    else:
        print('|','U ',"|"," 5","    |",sep="    ")
        print("- "*24)

def gradepoint(x):
    if 90<x and x<=100:
        return 10
    elif 80<x and x<=90:
        return 9
    elif 70<x and x<=80:
        return 8
    elif 60<x and x<=70:
        return 7
    elif 50<x and x<=60:
        return 6
    else:
        return 5

def gpafunc():
    global k,m,n,o,l
    k=gradepoint(a)
    l=gradepoint(b)
    m=gradepoint(c)
    n=gradepoint(d)
    o=gradepoint(e)  

def loop():
    tup=((1,a),(2,b),(3,c),(4,d),(5,e))
    for i ,char in tup:
        print("",i,"|",char,sep="    ",end="    ")
        find(char)

def perchantage():
    global r,h
    print("Semester GPA:",end='\n')
    r=(m+n+o+k+l)/5
    print("(",k,"+",l,"+",m,'+',n,'+',o,')','/ 5 =',r,end='\n')
    print("Semester Perchantage:",end='\n')
    h=(a+b+c+d+e)/5
    print("(",a,"+",b,"+",c,'+',d,'+',e,')','/ 5 =',h,'%')
    print()

def getmark2():
    global a,b,c,d,e
    print("Enter marks for Semester 2:")
    a=int(input("Subject 1 (CE-II) :"))
    b=int(input("Subject 2 (VCNM)  :"))
    c=int(input("Subject 3 (UHVE)  :"))
    d=int(input("Subject 4 (EG&ND) :"))
    e=int(input("Subject 5 (OOPS)  :"))
    print()
    print("~!!!*** SEMESTER -II RESULT ***!!!~")
    print()
    design() 
    loop()
    gpafunc()
    perchantage()    

def summary():
    print("Final Summary :")
    print("- "*16)
    print("Semester","GPA","Perchantage  |",sep=' | ')
    print("- "*16)
    print("","1",'|',sep='    ',end=' ')
    print(temp1,'|',"  ",temp2,'%','   |',sep=' ')
    print("- "*16)
    print("","2",'|',sep='    ',end=' ')
    print(temp3,'|',"  ",temp4,'%','   |',sep=' ')
    print("- "*16)
    print("CGPA:",end='\n')
    totalcgpa=(temp1+temp3)/2
    x=round(totalcgpa,1)
    print("(",temp1,'+',temp3,') / 2 = ',x)
    print("Overall Perchantage:",end='\n')
    totalperchantage=(temp2+temp4)/2
    y=round(totalperchantage,1)
    print("(",temp2,'+',temp4,') / 2 = ',y,'%')
    
#Functions Calling   
getmark1()
design()
loop()
gpafunc()
perchantage()
temp1=r
temp2=h
getmark2()
temp3=r
temp4=h
summary()

        
    


    

    
    

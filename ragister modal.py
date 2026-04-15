class school:
    def __init__(self,grade,div):
        self.grade=grade
        self.div=div

          
class classes:
   
    present9_h=[]
    present9_s=[]
    absent9_h=[]
    absent9_s=[]
    num_ab_9h=0
    num_pre_9h=0
    num_pre_9s=0
    num_ab_9s=0
    num_student_9h=1
    num_student_9s=3
    pre_per_9h=0
    pre_per_9s=0
    password=int(input("of you are a andmin enter the password"))
    grade=int(input("enter your grade:-"))
    div=input("enter the division:-")
    def nine_h():
         
         list=["shamosihan"]
         classes.num_student_9h=len(list)
         for x in list:
                 print(f"{x}")
                 a=input("enter present to P and absent to A:-")
                 if a=="P"or a=="p":
                     classes.present9_h.append(x)
                     classes.num_pre_9h+=1
                    
                 elif a=="A" or a=="a":
                      classes.absent9_h.append(x)
                      classes.num_ab_9h+=1
         classes.pre_per_9h=(classes.num_pre_9h/classes.num_student_9h)*100
         classes.password=int(input("of you are a andmin enter the password"))
         classes.grade=int(input("enter your grade:-"))
         classes.div=input("enter the division:-")
         if classes.grade==9 and classes.div=="s" and classes.password==5555: 
            classes.nine_s() 
         if classes.grade==9 and classes.div=="h" and classes.password==6602:
            print("_________code by shamo________")
 #        if classes.grade==0 and classes.div=="" and classes.password==123456:
 #           classes.pricial()
       
    def nine_s():      

         list1=["jathuswarman","seshnu","yugesh"]
         classes.num_student_9s=len(list1)
  #       list1=["jathuswarman","seshnu","yugesh"]
         for y in list1:
                print(f"{y}")
                a=input("enter present to P and absent to A:-")
                if a=="P"or a=="p":
                    classes.present9_s.append(y)
                    classes.num_pre_9s+=1

                elif a=="A" or a=="a":
                     classes.absent9_s.append(y)
                     classes.num_ab_9s+=1 
         classes.password=int(input("of you are a andmin enter the password"))
         classes.grade=int(input("enter your grade:-"))
         classes.div=input("enter the division:-")
         if classes.grade==9 and classes.div=="s" and classes.password==5555: 
            print("_________code by shamo________") 
         if classes.grade==9 and classes.div=="h" and classes.password==6602:
            classes.nine_h()
         classes.pre_per_9s=(classes.num_pre_9s/classes.num_student_9s)*100
#         if classes.grade==0 and classes.div=="" and classes.password==123456:
#             classes.pricial()

    def pricial():
        
        if classes.present9_h==[]:
             a=print("the 9h calsss have not been entered their registations!")
        else:
            a=print(f"present students in class 9H are {classes.present9_h}")
        if   classes.num_ab_9h==0 and classes.num_pre_9h==classes.num_student_9h :
             b=print("all students are present in 9H")
        elif classes.num_pre_9h==0 and classes.num_ab_9h==0:
             b=print("the 9h calsss have not been entered their registations!")        
        else:
            b= print(f"absent students in class 9h are {classes.absent9_h}")
        print(f"present percentage of 9H is {classes.pre_per_9h}")

        
        if classes.present9_s==[]:
             c=print("the 9s calsss have not been entered their registations!")
        else:
            c= print(f"present students in class 9S are {classes.present9_s}")
        if classes.num_pre_9s==classes.num_student_9s and classes.num_ab_9s==0 :
             d=print("all students are present in 9S")
        elif classes.num_pre_9s==0 and classes.num_ab_9s==0 :
             d=print("the 9s calsss have not been entered their registations!")
        else:
            d= print(f"absent students in class 9s are {classes.absent9_s}")
        print(f"present percentage of 9H is {classes.pre_per_9s}")
        a=a
        b=b
        c=c
        d=d
if classes.grade==9 and classes.div=="s" and classes.password==5555: 
    classes.nine_s() 
if classes.grade==9 and classes.div=="h" and classes.password==6602:
    classes.nine_h()
if classes.grade==0 and classes.div=="" and classes.password==123456:
    classes.pricial()


print("__________project by shamo__________")
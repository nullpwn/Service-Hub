from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.core.files.storage import FileSystemStorage
import webbrowser
import datetime

import MySQLdb
db=MySQLdb.connect("localhost","root","","servicehub")
c=db.cursor()


def login(request):
    msg=""
    if request.POST:
        uname=request.POST.get("email")
        password=request.POST.get("password")
       
        request.session['uname']=uname
        print(uname)
        print(password)
        query="select * from login where uname='"+uname+"' and password='"+password+"'"
        c.execute(query)
        data=c.fetchone()
        print(data)
        if data:
            if data[2]=='admin':
                return HttpResponseRedirect("/adminhome/")
            elif data[2]=='servicecenter' and data[3]=="approved":
                c.execute("select scid from screg where email='"+request.session['uname']+"'")
                owner=c.fetchone()
                request.session['scid']=owner[0]
                return HttpResponseRedirect("/schome/")
            elif data[2]=='user' and data[3]=="approved":
                print("hello")
                a="select uid from userreg where email='"+str(uname)+"'"
                c.execute(a)
                userid=c.fetchone()
                print(a)
                print(userid)
                request.session['userid']=userid[0]
                return HttpResponseRedirect("/userhome/")
        else:
            msg="invalid username or password"
           


    return render(request,"common/login.html",{"msg":msg})




def index(request):
    return render(request,"common/index.html")

def adminhome(request):
    return render(request,"admin/adminhome.html")
def schome(request):
    return render(request,"sc/schome.html")
def userhome(request):
    return render(request,"user/userhome.html")

def adminbase(request):
    return render(request,"admin/adminbase.html")






def userreg(request):
    

    msg=""
    word=""
    if request.POST:
        name=request.POST.get("name")
        email=request.POST.get("email")
        address=request.POST.get("address")
        phoneno=request.POST.get("phoneno")
        password=request.POST.get("password")
        cpassword=request.POST.get("cpassword")
        if password==cpassword:
            status='approved'
            qq="select count(*) from userreg where email='"+email+"'"
            c.execute(qq)
            data=c.fetchone()
            print(qq)
            print(data)
 
            if int(data[0])<1:
                query="insert into userreg(name,email,address,phoneno) values('"+str(name)+"','"+str(email)+"','"+str(address) +"','"+str(phoneno)+"')"
                c.execute(query)
                db.commit()
                usertype='user'

                qqq="insert into login(uname,password,usertype,status) values('"+str(email) +"','"+str(password)+"','"+str(usertype)+"','"+str(status)+"')"
                c.execute(qqq)
                db.commit()
                msg="Account successfully Created"
            else:
                msg="Allready have an account with same mail id"
        else:
            word="Sorry your password and confirm password are not matching"

        # return HttpResponseRedirect("/index/")
    return render(request,"common/userreg.html",{"msg":msg,"word":word})


def screg(request):
        c.execute("select * from company")
        data=c.fetchall()
        msg=""
        word=""
        if request.POST:
            name=request.POST.get("name")
            email=request.POST.get("email")
            address=request.POST.get("address")
            district=request.POST.get("district")
            phoneno=request.POST.get("phoneno")
            company=request.POST.get("company")
            product=request.POST.get("product")
            aid=request.POST.get("aid")
            password=request.POST.get("password")
            cpassword=request.POST.get("cpassword")
            if password==cpassword:
                qq="select count(*) from userreg where email='"+email+"'"
                c.execute(qq)
                data=c.fetchone()
                print(qq)
                print(data)
 
                if int(data[0])<1:
                    status='requested'
                    query="insert into screg(name,email,address,phoneno,company,product,aid,password,district) values('"+str(name)+"','"+str(email)+"','"+str(address)+"','"+str(phoneno)+"','"+str(company)+"','"+ str(product) +"','"+str(aid) +"','"+str(password) +"','"+str(district) +"')"
                    c.execute(query)
                    db.commit()
                    usertype='servicecenter'
                    
                    qqq="insert into login(uname,password,usertype,status) values('"+str(email)+"','"+str(password)+"','"+str(usertype)+"','"+str(status)+"')"
                    c.execute(qqq)
                    db.commit()
                    msg="Account successfully Created"
                else:
                    msg="Allready have an account with same mail id"
            else:
                word="Sorry your password and confirm password are not matching"

            # return HttpResponseRedirect("/index/")
        return render(request,"common/screg.html",{"msg":msg,"word":word,"data":data})




def addcompany(request):
    msg = ""
    if request.POST:
        company=request.POST.get("company")
        if request.FILES["file"]:
            myfile=request.FILES["file"]
            fs=FileSystemStorage()
            filename=fs.save(myfile.name,myfile)
            fileurl=fs.url(filename)
            query="insert into company(companyname,photo) values('"+str(company)+"','"+str(fileurl)+"')"
            c.execute(query)
            db.commit()
            msg = "added"
    return render(request,"admin/addcompanies.html",{"msg":msg})


# def addquestion(request):

#     if request.POST:
#         company=request.POST.get("company")
#         product=request.POST.get("product")
#         question=request.POST.get("question")
#         query="insert into question(companyname,product,question) values('"+ company +"','"+ product +"','"+ question +"')"
#         c.execute(query)
#         db.commit()

#     return render(request,"user/question.html")


def addquestionandanswer(request):
        if request.POST:
            company=request.POST.get("company")
            product=request.POST.get("product")
            question=request.POST.get("question")
            answer=request.POST.get("answer")
            query="insert into question(companyname,product,questionn,answer) values('"+str(company)+"','"+ str(product) +"','"+str(question)+"','"+ str(answer) +"')"
            c.execute(query)
            db.commit()

        return render(request,"sc/answer.html")


def searchforsc(request):
    if request.POST:
        district=request.POST.get("district")
        request.session['district']=district
        company=request.session['company']


        c.execute("select * from screg where district='"+ str(district) +"' and company='"+str(company)+"'")
        data=c.fetchall()
        request.session['search']=data

        return HttpResponseRedirect('/searchdisplay/') 
    return render(request,"user/search.html")


def searchdisplay(request):
        data=request.session['search']
        userid=request.session['userid']

        return render(request,"user/searchdisplay.html",{"data":data,"userid":userid})


def booking(request):
    if request.GET.get("id"):
        idd=request.GET.get("id")


    if request.POST:
            company=request.session['company']
            # product=request.POST.get("product")
            problem=request.POST.get("problem")
            userid=request.session['userid']
            image=request.FILES["image"]
            fs=FileSystemStorage()
            filename=fs.save(image.name,image)
            uploaded_file_url=fs.url(filename)
            todate=datetime.date.today()
            bookingdate=todate
            enddate=todate + datetime.timedelta(days=7)
            status="complaint registerred"
            query="insert into booking(company,bookingdate,problem,image,status,userid,scid,enddate) values('"+str(company)+"','"+str(bookingdate) +"','"+str(problem)+"','"+str(uploaded_file_url)+"','"+str(status)+"','"+str(userid)+"','"+str(idd)+"','"+str(enddate) +"')"
            c.execute(query)
            db.commit()
    return render(request,"user/booking.html",{"scid":idd})



def viewquestion(request):
    data=""
    if request.POST:
            company=request.POST.get("company")
            product=request.POST.get("product")
            c.execute("select * from question where companyname='"+ str(company) +"' and product='"+ str(product) +"'")
            data=c.fetchall()
    return render(request,"user/viewquestion.html",{"data":data})
 





def approvesc(request):
    c.execute("SELECT screg.* ,login.* from screg join login on screg.email=login.uname where login.status='requested'")
    data=c.fetchall()
    if request.GET.get("id"):
        email=request.GET.get("id")
        
        status=request.GET.get("status")
        c.execute("update login set status='"+status+"' where uname='"+email+"'")
        db.commit()
        return HttpResponseRedirect('/approvesc/') 
    c.execute("SELECT screg.* ,login.* from screg join login on screg.email=login.uname where login.status='approved'")
    data1=c.fetchall()
   
    return render(request,"admin/approvesc.html",{"data":data,"data1":data1})




def gallery(request):
    msg=""
    if request.GET.get('id')=='0':
        msg=request.session['msg']
    c.execute("select * from company")
    data=c.fetchall()
    return render(request,"user/gallery.html",{"data":data,"msg":msg})




# def gallery(request):
#     c.execute("select * from company where CustomerName LIKE '%tru%'")
#     data=c.fetchall()
#     return render(request,"user/gallery.html",{"data":data}) 



def wtsurproblem(request):
    data=[]
    msg=""
    if request.GET.get("id"):
        company=request.GET.get("id")
        request.session['company']=company
        qq="select count(*) from screg where company='"+company+"'"
        c.execute(qq)
        data=c.fetchone()
        print(company)
        if data[0]<1:
            request.session['msg']="sorry  no service hubs are available for this company"
            return HttpResponseRedirect("/gallery/?id=0")
        else:
            msg=request.session['msg']=""

        


    if request.POST:
        data=[]
        question=request.POST.get("question")
        question=question.split(' ')
        for i in question:        
            #c.execute("select * from question where  questionn LIKE '%"+ i +"%'")
            c.execute("select * from faq where  faq LIKE '%"+ i +"%' and company='"+str(company)+"'")
            z=c.fetchall()
            for zz in z:
                if zz not in data:
                    data.append(zz)
         
        request.session['answers']=data

        print(data)
     
        return HttpResponseRedirect('/viewanswers/') 
    return render(request,"user/question.html",{"data":data,"msg":msg}) 


def viewanswers(request):
    answers=request.session['answers']
    return render(request,"user/viewanswers.html",{"answers":answers})



def viewbooking(request):

    m="select booking.*,userreg.* from booking,userreg,screg where screg.scid='"+str(request.session['scid'])+"' and booking.scid=screg.scid and booking.userid=userreg.uid and booking.status!='delivered'"
    
    c.execute(m)
    print(m)
    data=c.fetchall()
    return render(request,"sc/viewbookings.html",{"data":data})




def updatebookingstatus(request):
    if request.GET.get("id"):
        bid=request.GET.get("id")
        c.execute("select * from booking where bid='"+str(bid)+"'")
        data=c.fetchone()
        print(data)
        print(bid)
        print(data[5])
        if data[5]=='complaint registerred':
            print("hello")
            status='pending'
            c.execute("update booking set status='"+status+"' where bid='"+str(bid)+"'")
            db.commit()
        elif data[5]=='pending':
            status='Scheduled'
            c.execute("update booking set status='"+status+"' where bid='"+str(bid)+"'")
            db.commit()
        elif data[5]=='Scheduled':
            status='Processing'
            c.execute("update booking set status='"+status+"' where bid='"+str(bid)+"'")
            db.commit()
        elif data[5]=='Processing':
            status='completed'
            c.execute("update booking set status='"+status+"' where bid='"+str(bid)+"'")
            db.commit()
        elif data[5]=='completed':
            status='delivered'
            c.execute("update booking set status='"+status+"' where bid='"+bid+"'")
            db.commit()


            
        return HttpResponseRedirect('/viewbooking/') 
    return render(request,"sc/viewbookings.html")





def viewstatusbyuser(request):

    c.execute("select * from booking where userid='"+str(request.session['userid'])+"'")
    data=c.fetchall()

    return render(request,"user/viewstatus.html",{"data":data})


def feedbackpreview(request):
    c.execute("SELECT booking.* ,screg.* from screg join booking on screg.scid=booking.scid where booking.userid='"+str(request.session['userid'])+"' and booking.status='delivered'")
    data1=c.fetchall()

    return render(request,"user/feedbackpreview.html",{"data":data1})


def feedback(request):
    idd=""
    if request.GET.get("id"):
        idd=request.GET.get("id")
        print(idd)  
    if request.POST: 
        servicecenter=request.POST.get("servicecenter")
        feedback=request.POST.get("feedback")
        userid=request.session['userid']
        query="insert into feedback(feedback,userid,scid) values('"+str(feedback)+"','"+str(userid)+"','"+str(idd)+"')"
        c.execute(query)
        db.commit()
    return render(request,"user/feedback.html")



def viewfeedbackbyadmin(request):
    c.execute("SELECT screg.* ,feedback.* from screg join feedback on screg.scid=feedback.scid ")

    data=c.fetchall()

    return render(request,"admin/viewfeedbackbyadmin .html",{"data":data})



def viewfeedbackbysc(request):

    # c.execute("select * from feedback where scid='"+str(request.session['scid'])+"'")
    c.execute("SELECT userreg.* ,feedback.* from userreg join feedback on userreg.uid=feedback.userid and feedback.scid='"+str(request.session['scid'])+"' ")
    data=c.fetchall()

    return render(request,"sc/viewfeedbackbysc.html",{"data":data})



def faq(request):
        if request.POST:
            company=request.POST.get("company")
            faq=request.POST.get("question")
            answer=request.POST.get("answer")
            query="insert into faq(company,faq,answer) values('"+str(company) +"','"+str(faq) +"','"+str(answer)+"')"
            c.execute(query)
            db.commit()
        return render(request,"sc/faq.html")


def viewfaq(request):

    # c.execute("select * from feedback where scid='"+str(request.session['scid'])+"'")
    c.execute("select * from faq")
    data=c.fetchall()

    return render(request,"user/viewfaq.html",{"data":data})


def adminaddmessage(request):
    c.execute("select * from screg")
    data=c.fetchall()
    c.execute("select * from userreg")
    data1=c.fetchall()
    if request.POST:
        message=request.POST.get("message")
        recept=request.POST.get("reciepient")
        messenger=request.session["uname"]
        qq="insert into message(message,messenger,recipient) values('"+str(message)+"','"+str(messenger)+"','"+str(recept)+"')"
        c.execute(qq)
        print(qq)
        db.commit()
    return render(request,"admin/addmessage.html",{"data":data,"data1":data1})

def scaddmessage(request):
    c.execute("select * from userreg")
    data1=c.fetchall()
    if request.POST:
        message=request.POST.get("message")
        recepient=request.POST.get("reciepient")
        messenger=request.session["uname"]
        qq="insert into message(message,messenger,recipient) values('"+str(message) +"','"+str(messenger) +"','"+str(recepient)+"')"
        c.execute(qq)
        db.commit()
    return render(request,"sc/scaddmessage.html",{"data1":data1})


def useraddmessage(request):
    c.execute("select * from screg")
    data1=c.fetchall()
    if request.POST:
        message=request.POST.get("message")
        recepient=request.POST.get("reciepient")
        messenger=request.session["uname"]
        qq="insert into message(message,messenger,recipient) values('"+str(message) +"','"+str(messenger) +"','"+ str(recepient) +"')"
        c.execute(qq)
        db.commit()
    return render(request,"user/useraddmessage.html",{"data1":data1})




def adminviewmessage(request):
    c.execute("select * from message where recipient='admin@gmail.com'")
    data=c.fetchall()
    return render(request,"admin/adminviewmessages.html",{"data":data})

def scviewmessage(request):
    c.execute("select * from message where recipient='"+request.session["uname"]+"'")
    data=c.fetchall()
    return render(request,"sc/scviewmessage.html",{"data":data})

def userviewmessage(request):
    c.execute("select * from message where recipient='"+request.session["uname"]+"'")
    data=c.fetchall()
    return render(request,"user/userviewmessage.html",{"data":data})


def viewupcomings(request):
    todate=datetime.date.today()
    enddate=todate + datetime.timedelta(days=5)
    c.execute("select * from booking where enddate<='"+str(enddate)+"' and scid='"+str(request.session["scid"])+"'")
    data=c.fetchall()
    return render(request,"sc/upcomingdates.html",{"data":data})


def scviewprofile(request):
    msg=""
    data=""
    item=""
    scid = request.session['scid']
    s="select * from screg where scid='"+str(scid)+"'"
    data=c.execute(s)
    print(s)
    data=c.fetchall()
    c.execute("select uname from login,screg where login.uname=screg.email and screg.scid='"+str(scid)+"'")
    dd=c.fetchone()
    cemail=dd[0]
    print(data)
    c.execute("select * from login where uname='"+str(cemail)+"'")
    item=c.fetchall()
    print(data)
    if(request.POST):
        na=request.POST.get('t1')
        email=request.POST.get('t2')
        add=request.POST.get('t3')
        mob=request.POST.get('t4')
        com=request.POST.get('t5')
        pro=request.POST.get('t6')
        
        aid=request.POST.get('t7')
 
        pwd=request.POST.get('t8')
        dist=request.POST.get('t9')
        
        
        c.execute("update screg set name='"+str(na)+"',email='"+str(email)+"',address='"+str(add)+"',phoneno='"+str(mob)+"',company='"+str(com)+"',product='"+str(pro)+"',aid='"+str(aid)+"',password='"+str(pwd)+"',district='"+str(dist)+"' where scid='"+str(scid)+"'")
        db.commit() 
        c.execute("update login set uname='"+ str(email) +"',password='"+str(pwd) +"' where uname='"+str(cemail)+"' ")
        db.commit()
        msg="updated successfully"
        # data.cname=na
        # data.address=add
        # data.district=loc
        # data.location=dis
        # data.mobile=mob
        # data.email=email
        # data.aadhar=aadhar
        # data.ksebcno=kno
        # data.waternum=wno
        # data.password=password
        # item.uname=email
        # item[1]=password
        # data.save()
        # item.save()
        
    return render(request,"sc/scviewprofile.html",{"data":data,"item":item,"msg":msg})


import json
import math
print('Loading function')
# from docx import Document
# from docx.shared import Cm,Inches
# from docx.shared import Pt
# from docx.enum.style import WD_STYLE_TYPE
# from docx.enum.text import WD_ALIGN_PARAGRAPH

import pymysql as mdb

def lambda_handler(event, context):

    mail=event['mail_id']
    ps=event['pass']
    sub_code=event['sub_code']
    date=['exam_date']
    time=['exam_time']

    #connecting database
    db_con = mdb.connect(host='db.innocenter.tech',port=1136,user='paperout', password='SuJ4DI7I', database='testdb')
    cursor = db_con.cursor()

    #checking authentication
    qry="select pass from users where email='%s'"%(mail)
    cursor.execute(qry)
    rs=cursor.fetchall()
    if(rs[0][0]==ps):
        print('Mail Exist')
    else:
        print('fuck off')


    qry="select count(ccode) as n from chapter where ccode regexp '%s*'"%(sub_code)
    print(qry)
    cursor.execute(qry)
    rs=cursor.fetchall()
    n=rs[0][0]

    # storing chapterwise weitage into a list
    w=[]
    qry="select weight,ccode from chapter where ccode regexp '%s*' order by ccode asc"%(sub_code)
    print(qry)
    cursor.execute(qry)
    rs=cursor.fetchall()
    for i in range(0,len(rs)):
        c=rs[i][0]
        m=(c*119)/100
        w.append([i+1,round(m)])

    # getting the marks list
    m3=m4=m7=0
    while((m3!=8) or (m4!=8) or (m7!=9)):
        m3=m4=m7=0
        fisel=[]
        filsel=getmarks(w)
        for i in range(0,len(filsel)):
            m3=m3+filsel[i].count(3)
            m4=m4+filsel[i].count(4)
            m7=m7+filsel[i].count(7)

    #sequencing the selected questions in the marks pattern
    sequ=[]
    for i in range(0,8):
        for j in range(0,3):
            if(j==0):
                mark3[0]=((str(i+1)),'(a)',)+mark3[0]
                sequ.append(mark3[0])
                mark3.remove(mark3[0])
            elif(j==1):
                mark4[0]=('','(b)',)+mark4[0]
                sequ.append(mark4[0])
                mark4.remove(mark4[0])
            else:
                mark7[0]=('','(c)',)+mark7[0]
                sequ.append(mark7[0])
                mark7.remove(mark7[0])
                if(i==1):
                    mark7[0]=('','(c)',)+mark7[0]
                    sequ.append(mark7[0])
                    mark7.remove(mark7[0])
    for i in range(0,len(sequ)):
        sequ[i]=tuple(sequ[i][0:2])+tuple(sequ[i][3:])

    print(sequ)

    # creating pdfs and formatting
    # document = Document()

    # obj_styles = document.styles
    # obj_charstyle = obj_styles.add_style('GTU', WD_STYLE_TYPE.CHARACTER)
    # obj_font = obj_charstyle.font
    # obj_font.size = Pt(16)
    # obj_font.name = 'Times New Roman'

    # obj_styles = document.styles
    # obj_charstyle = obj_styles.add_style('SEM', WD_STYLE_TYPE.CHARACTER)
    # obj_font = obj_charstyle.font
    # obj_font.size = Pt(12)
    # obj_font.name = 'Times New Roman'

    # obj_styles = document.styles
    # obj_charstyle = obj_styles.add_style('SUB', WD_STYLE_TYPE.CHARACTER)
    # obj_font = obj_charstyle.font
    # obj_font.size = Pt(14)
    # obj_font.name = 'Times New Roman'

    # obj_styles = document.styles
    # obj_charstyle = obj_styles.add_style('INS', WD_STYLE_TYPE.CHARACTER)
    # obj_font = obj_charstyle.font
    # obj_font.size = Pt(11)
    # obj_font.name = 'Times New Roman'

    # #document.add_heading('Document Title', 0)
    # p = document.add_paragraph('')
    # p.add_run('Seat No.: ________\t\t\t\t\t\tEnrolment No.___________\n').bold = True
    # p.add_run('GUJARAT TECHNOLOGICAL UNIVERSITY\n',style='GTU').bold = True
    # p.add_run('BE - SEMESTER– IV (New) EXAMINATION –',style='SEM').bold = True

    # qry="select * from session"
    # cursor.execute(qry)
    # rs= cursor.fetchall()
    # if(rs[0]==0):
    #     p.add_run(' WINTER ',style=SEM).bold= True
    #     p.add_run(rs[1],style=SEM).bold = True

    # else:
    #     p.add_run(' SUMMER ',style=SEM).bold= True
    #     p.add_run(rs[1],style=SEM).bold = True

    # q = document.add_paragraph('')
    # #q.add_run(sub_code)
    # q.add_run('123\t\t\t\t\t\tDate: ',style='SUB').bold = True



    # q.add_run('123',style='SUB').bold = True
    # q.add_run('\nSubject Name: ',style='SUB').bold = True

    # qry="select sname from subjects where scode='%s"%(sub_code)
    # cursor.execute(qry)
    # rs=cursor.fetchall()
    # q.add_run(rs[0],style='SUB').bold = True

    # q.add_run('\nTime: ',style='SUB').bold = True
    # q.add_run('123',style='SUB').bold = True
    # q.add_run('\t\t\t\tTotal Marks: 70\n',style='SUB').bold = True
    # q.add_run('\nInstructions:\n\t1. Attempt all questions.\n\t2. Make suitable assumptions wherever necessary.\n\t3. Figures to the right indicate full marks.\n\t\t\t\t\t*************\n',style='INS').bold=True

    # p.alignment = 1
    # q.alingment = 0


    # #document.add_picture('monty-truth.png', width=Inches(1.25))

    # #records =

    # table = document.add_table(rows=1, cols=4)
    # table.autofit = True

    # hdr_cells = table.rows[0].cells
    # hdr_cells[0].text = ''
    # hdr_cells[1].text = ''
    # hdr_cells[2].text = ''
    # hdr_cells[3].text = 'Marks'

    # hdr_cells[0].width = 6879
    # hdr_cells[1].width = 9599
    # hdr_cells[2].width = 45000
    # hdr_cells[3].width = 5723

    # table.columns[0].bold = True
    # table.columns[3].bold = True

    # for SrNo,Subtype,Questions,Marks in sequ:
    #     row_cells = table.add_row().cells
    #     row_cells[0].text = str(SrNo)
    #     row_cells[1].text = Subtype
    #     row_cells[2].text = Questions
    #     row_cells[3].text = Marks


    # document.add_page_break()

    # document.save('demo.docx')

# function that returns marks list
def getmarks(li):
    print(li)
    fli=[]
    from itertools import combinations
    for i in range(0,len(li)):
        m=li[i][1]
        if((m%2)==0):
            import random
            c=random.randint(0,1)
            if(c==0):
                m=m-1;
            else:
                m=m+1;
        sel=[]
        if(m<3):
            sel.append(tuple([3]))
        elif(m==5):
            import random
            sl=random.randint(0,1)
            if(sl==0):
                sel.append(tuple([4]))
            else:
                sel.append(tuple([7]))
        else:
            for a in range(0,8):
                combi = combinations([3,4,7,7,4,7,3,4,7,3,4,7],a)
                for i in combi:
                    if(i not in sel and sum(i)==m):
                        sel.append(i)
        from random import choice
        x=choice(sel)
        fli.append(x)
    print(fli)
    return(fli)

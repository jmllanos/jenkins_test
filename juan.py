import datetime

def juan(section):

    if section==1.01:
        initDay=datetime.datetime(2020,9,4)
        period="15:00-19:00"
        weekinit=1
    elif section==1.02:
        initDay=datetime.datetime(2020,9,11)
        period="15:00-19:00"
        weekinit=2
    elif section==2.01:
        initDay=datetime.datetime(2020,9,5)
        period="08:00-12:00"
        weekinit=1
    elif section==2.02:
        initDay=datetime.datetime(2020,9,12)
        period="08:00-12:00"
        weekinit=2

    for number in range(8):

        delta=number*datetime.timedelta(days=14)
        sectionStr=str(section)

        day=initDay+delta
        strday=day.strftime("%m/%d")

        week=number*2 + weekinit
        weekstr="{:02d}".format(week)

        labname="2020-II EL4003 ES Circuitos Digitales, "+ sectionStr + ", Semana" + weekstr+", Juan Llanos, " + strday  + ", " + period + " Laboratorio "
        print("")
        print("Laboratorio "+str(number))
        print(labname)

section=input("Ingrese seccion: ")

juan(section)

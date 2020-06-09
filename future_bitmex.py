#Not financial advice
# -*- coding:UTF-8 -*-
import psycopg2

conn = psycopg2.connect(database="db_name", user="postgres",password="xxxxxxx", host="127.0.0.1", port="5432")
print("You are connected to the database")

cursor = conn.cursor()

listeBingo = []
liquidation = int(0)
NbreDeJoursMacro = 0
dateDepartFixe = "2012-11-28"

def funcLevier(levier):
    switch(levier){
        case 3:
            return 0.85
        case 5:
            return 0.90
        case 10:
            return 0.95
        case 20:
            return 0.98
        case 100:
            return 0.999
        default:
         print("You picked a leverage that is not allowed")

def mainFunc(NbreDeJoursMacro):
    a = float(1.00)
    NbreDeJoursMicro = int(0)
    #print(liquidation)
    while (a > liquidation) and (NbreDeJoursMicro < 180):
        sommeJours = int(NbreDeJoursMacro+NbreDeJoursMicro)
        cursor.execute("SELECT percentage FROM public.bitmexx WHERE datee - integer '%s' = %s;",(sommeJours, dateDepartFixe))
        records = cursor.fetchall()
        records = records[0]
        records = str(records)
        records = records.replace("(","")
        records = records.replace(",","")
        records = records.replace(")","")
        records = float(records)
        a = (1+(records/100))*a
        #print("the future contract held ",NbreDeJoursMicro," jours et a=",a)
        x = NbreDeJoursMicro
        y = a
        NbreDeJoursMicro = NbreDeJoursMicro+1
    if x == 179:
        return True

levier = int(input("Pick a leverage of 3, 5, 10, 20 or 100 : "))
liquidation = funcLevier(levier)

while NbreDeJoursMacro<400:
    if jeff(NbreDeJoursMacro):
        listeBingo.append(NbreDeJoursMacro)
    NbreDeJoursMacro = NbreDeJoursMacro+1
print("Here is the list of the increments of the valid dates for your position from the ", dateDepartFixe,"with your selected leverage : ",listeBingo)


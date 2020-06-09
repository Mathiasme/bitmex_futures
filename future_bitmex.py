#Not financial advice
# -*- coding:UTF-8 -*-
import psycopg2

conn = psycopg2.connect(database="db_name", user="postgres",password="xxxxxxx", host="127.0.0.1", port="5432")
print("You are connected to the database")

cursor = conn.cursor()

listeBingo = [] #Final list of increments
NbreDeJoursMacro = 0 
fixedStartingDate = "2012-11-28" #the date you want to start the contract from
levier = int(input("Pick a leverage of 3, 5, 10, 20 or 100 : ")) #The user will pick the leverage of the contact through this input

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
    }

liquidation = funcLevier(levier)
        
def microFunc(NbreDeJoursMacro, liquidation):
    a = float(1.00)
    NbreDeJoursMicro = int(0)
    #print(liquidation)
    while (a > liquidation) and (NbreDeJoursMicro < 180): #a is the variation and NbreDeJoursMicro is the duration of the contract in days from the fixedStartingDate
        daysSum = int(NbreDeJoursMacro + NbreDeJoursMicro)
        cursor.execute("SELECT percentage FROM public.bitmexx WHERE datee - integer '%s' = %s;",(daysSum, fixedStartingDate))
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
        NbreDeJoursMicro = NbreDeJoursMicro+1
        if x == 179: #179 is the number of days from the fixedStartingDate necessary to consider the contract as valid
          return True
        
while NbreDeJoursMacro < 400: #400 allows a period of days to test the contract equivalent to fixedStartingDate + 400 in this case
    if microFunc(NbreDeJoursMacro, liquidation):
        listeBingo.append(NbreDeJoursMacro)
    NbreDeJoursMacro = NbreDeJoursMacro+1
print("Here is the list of the increments of the valid dates for your position from the ", fixedStartingDate,"with your selected leverage : ",listeBingo)


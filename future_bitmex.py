# -*- coding:UTF-8 -*-
import psycopg2

conn = psycopg2.connect(database="final", user="postgres",password="xxxxxxx", host="127.0.0.1", port="5432")
print("ça marche connexion réussie")

cursor=conn.cursor()

listeBingo=[]
liquidation=int(0)
NbreDeJoursMacro=0
dateDepartFixe="2012-11-28"

def funcLevier(levier):
    if levier==3:
        return 0.85
    elif levier==5:
        return 0.90
    elif levier==10:
        return 0.95
    elif levier==20:
        return 0.98
    elif levier==100:
        return 0.999
    else:
        print("Vous avez choisi un mauvais levier")

def jeff(NbreDeJoursMacro):
    a=float(1.00)
    NbreDeJoursMicro=int(0)
    #print(liquidation)
    while (a>liquidation) and (NbreDeJoursMicro<180):
        sommeJours=int(NbreDeJoursMacro+NbreDeJoursMicro)
        cursor.execute("SELECT percentage FROM public.bitmexx WHERE datee - integer '%s' = %s;",(sommeJours, dateDepartFixe))
        records=cursor.fetchall()
        records=records[0]
        records=str(records)
        records=records.replace("(","")
        records=records.replace(",","")
        records=records.replace(")","")
        records=float(records)
        a=(1+(records/100))*a
        #print("Le contrat Future a tenu ",NbreDeJoursMicro," jours et a=",a)
        x=NbreDeJoursMicro
        y=a
        NbreDeJoursMicro=NbreDeJoursMicro+1
    if x==179:
        return True

levier=int(input("Entrez un levier de 3, 5, 10, 20 ou 100 : "))
liquidation=funcLevier(levier)

while NbreDeJoursMacro<400:
    if jeff(NbreDeJoursMacro):
        listeBingo.append(NbreDeJoursMacro)
    NbreDeJoursMacro=NbreDeJoursMacro+1
print("Voici la liste des increments des dates valides a partir du ", dateDepartFixe," : ",listeBingo)


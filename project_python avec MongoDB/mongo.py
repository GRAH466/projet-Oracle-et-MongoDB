
from pymongo import MongoClient
import pymongo

GRAH=MongoClient(host='localhost',port=27017)

db=GRAH.etd

yabi= {
    'nom':'vice versa',
   
    'annee':2022,
       'acteurs':'sidibe issa',
    'realisateurs':{ 
    'nom':'grah','prenom':'lowa-ezechiel'
    }}                  

result=db.Cinema.insert_one(yabi)
print(result)

balthazar=[{'$group':{'_id':'$realisateur','count':{'$sum':1}}}]
result=db.Cinema.aggregate(balthazar)
for b in result:
    print(b)

db.Cinema.update_one({'nom':'vice versa'}),{'$set':{'annee':2023}}
if result.modified_count>=1:
    print("Document modifié avec succès")
else:
    print("Aucune modification apportée")








GRAH.close()

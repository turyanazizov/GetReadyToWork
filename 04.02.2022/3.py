property=input('Axtarilan Property: ')

thisdict = {
  "name": "Turyan",
  "surname": "Azizov",
  "country":"Azerbaijan",
  "age": 21,
  'color':'white',
  'lenght':170,
  'location':'Baku',
  'point':648,
  'film':'Forrest Gump',
  'job':False
}

keys=list(thisdict.keys())
values=list(thisdict.values())

for i in range(len(keys)):
    if keys[i]==property:
        property_id=i
        break

print('Previus: \n',keys[i-1],':',values[i-1])
print('Next: \n',keys[i+1],':',values[i+1])


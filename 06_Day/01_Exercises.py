##1 Create an empty tuple
emptyTuple = ()

#2 Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
FamTuple = ( "paola", "Arturo", "Max", "Manuel" )

#3 Join brothers and sisters tuples and assign it to siblings
brothers = ( "Arturo", "Max", "Manuel")
sisters = ("Paola")
siblings = brothers + sisters
print (siblings)

#4 How many siblings do you have?
print ("Yo tengo {} hermanos" .format (len(siblings)))

#5 Modify the siblings tuple and add the name of your father and mother and assign it to family_members
Family_members = siblings + ("paula", "Alonso")
print (Family_members)



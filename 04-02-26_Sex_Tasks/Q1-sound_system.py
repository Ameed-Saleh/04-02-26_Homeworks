print("question", 1)
while True:
   volume:int = int(input("Enter a volume level to check a sound system:"))
   print(volume , end=" - ")
   match volume:
       case 1:
           print("Very Quit")
       case 2 :
           print("Quit")
       case 3 | 4 :
           print("Low")
       case 5 :
           print("Medium")
       case 6 :
           print("Medium High")
       case 7 :
           print ("Loud")
       case 8 :
         print("Very Loud")
       case 9 | 10 :
           print("Max Volume")
       case _ :
           print("invalid volume")
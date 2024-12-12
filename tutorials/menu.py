menu=["1 poratta","2 payasam","3 biriyani","4 tea"]
for x in menu:
    print(x)
    
choice=int(input("enter a number : "))
if choice==1:
    print("you Entered poratta")
elif choice==2:
    print("you have entered payasam")
elif choice==3:
    print(" you have enetred biriyani")
elif choice==4:
    print("you have entered tea")
else:
    print("error")
           

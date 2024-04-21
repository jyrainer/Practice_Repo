# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print(f"Values inside the function: {mylist}")
   return # or 없어도 똑같음
# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print(f"Values outside the function: {mylist}")
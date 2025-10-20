#change mile to kilometer , where 1mile=1.61km
mile=int(input("Enter the mile: "))
if mile>=0:    
    kilometer=mile*1.61    
    print(f"The conversion of",mile,f"mile is: ",kilometer)
else:    
    print("Mile can not measure in Negative.")

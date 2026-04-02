def main():
    print("Hello from datascience!")

if __name__ == "__main__":
    main()

grade = float(input("enter the value of grades:"))

if grade >= 3.6 and grade <= 4.0:
    print("A")

elif grade >= 3.4 and grade <= 3.6:
    print ("A-")

elif grade >= 3.2 and grade <=  3.4:
    print ("B")

else:
    print("C")
    
grade2 = (input("enter the value of grade2:")) 
# takes in string
print(type(grade2))



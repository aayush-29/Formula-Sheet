from PIL import Image

print ("="*50)
print ("Chapter Wise Formula Sheet for Class XI and XII")
print ("="*50)

c= input("Enter the subject you want (Physics/Mathematics): ")
if c.lower()=='physics'or c.lower()=='physic':
    print("Chapters")
    print("""          1. Kinematics 
          2. Fluid Mechanics
          3. Electrostats
          4. Magnetism
          5. Electro Magnetic Induction""")
    b= int(input("Enter the Chapter no. from following List: "))
    if b in range (1,6):
        if b==1:
            print('='*30)
            print('           Formulas')
            print('='*30)
            filename="images/Kinematics.jpg"
            try:
                img=Image.open(filename)
                img.show()
            except FileNotFoundError:
                print("Image File not found") 

        elif b==2:
            print('='*30)
            print('           Formulas')
            print('='*30)
            filename="images/Fluid mechanics.jpg"
            try:
                img=Image.open(filename)
                img.show()
            except FileNotFoundError:
                print("Image File not found") 

        elif b==3:
            print('='*30)
            print('           Formulas')
            print('='*30)
            filename="images/Electrostats.jpg"
            try:
                img=Image.open(filename)
                img.show()
            except FileNotFoundError:
                print("Image File not found") 

        elif b==4:
            print('='*30)
            print('           Formulas')
            print('='*30)
            filename="images/Magnetism.jpg"
            try:
                img=Image.open(filename)
                img.show()
            except FileNotFoundError:
                print("Image File not found")           
        elif b==5:
            print('='*30)
            print('           Formulas')
            print('='*30)
            filename="images/Electro Magnetic Induction.jpg"
            try:
                img=Image.open(filename)
                img.show()
            except FileNotFoundError:
                print("Image File not found") 
    else:
        print("No Chapter Exsist")
    
elif c.lower()=='mathematics'or c.lower()=='maths':
    print('Chapters')
    print("""          1.Trigonometry
          2.Complex No.
          3.Statistics
          4.Probablity
          5.Integrals""")
    a=int(input("Enter the Chapter no. from following List: "))
    if a in range(1,6):
        if a==1:
            print('='*30)
            print('           Formulas')
            print('='*30)
            filename="images/Trigonometry.jpg"
            try:
                img=Image.open(filename)
                img.show()
            except FileNotFoundError:
                print("Image File not found")

        elif a==2:
            print('='*30)
            print('           Formulas')
            print('='*30)
            filename="images/Complex No.jpg"
            try:
                img=Image.open(filename)
                img.show()
            except FileNotFoundError:
                print("Image File not found")

        elif a==3:
            print('='*30)
            print('           Formulas')
            print('='*30)
            filename="images/Statistics.jpg"
            try:
                img=Image.open(filename)
                img.show()
            except FileNotFoundError:
                print("Image File not found")
        elif a==4:
            print('='*30)
            print('           Formulas')
            print('='*30)
            filename="images/Probablity.jpg"
            try:
                img=Image.open(filename)
                img.show()
            except FileNotFoundError:
                print("Image File not found") 
            
        elif a==5:
            print('='*30)
            print('           Formulas')
            print('='*30)
            filename="images/Integrals.jpg"
            try:
                img=Image.open(filename)
                img.show()
            except FileNotFoundError:
                print("Image File not found") 
    else:
        print("No Chapter Exsist")
else:
    print("Invalid input")
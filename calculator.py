print("Welcome User!!!")
    
print("To Exit Calculator Enter 'x' " )
while True:
    num1_input=input('Enter 1st number: ' )
    
    if num1_input.lower() =='x':
        print("Exiting Calculator.....")
        print("Calculator exited")
        break
    try:
        num1=float(num1_input)
    except ValueError:
        print("MATH ERROR!! Please enter a number: ")
        continue
        
    num2_input=input('Enter 2nd number: ' )
    
    if num2_input.lower() =='x':
        print ("Exiting Calculator.....")
        print("Calculator exited")
        break
    try:
        num2=float(num2_input)
    except ValueError:
        print("MATH ERROR!! Please enter a number: ")
        continue
        
    operator=input('Enter the operator: ')
    if operator.lower() == 'x':
        print('Exiting Calculator....')
        print("Calculator exited")
        break
    if operator == '+':
        result=num1+num2
    
    elif operator == '-':
        result=num1-num2
    
    elif operator == '*':
        result=num1*num2
    
    elif operator == '/':
        if num2!=0:
            result=num1/num2
        else:
            print('MATH ERROR!!' )
            print('A Value Cannot Be Divided By Zero')
            continue
    
    if operator == '/':     
        if result.is_integer():
            print(int(result))
        else:
            print(result)
    else:
        if num1.is_integer() and num2.is_integer():
            print(int(result))
        else:
            print(result)
        
        

        

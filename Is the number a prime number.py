def prime(number):
 
    if number>1:
        for i in range(2,number):
            if (number % i) == 0:
                print("It is a prime number")
                break
            else:
                print("It is not a prime number") 
        else: 
            print("It is a prime number")

prime(int(input("Input the number ")))            
        
 
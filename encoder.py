# encoding dictionary

def main():
   
    # dictionary for matching keys with user input
    encoding = {"a":"b","b":"c","c":"d","d":"e","e":"f","f":"g","g":"h","h":"i","i":"j","j":"k","k":"l","l":"m","m":"n","n":"o","o":"p","p":"q","q":"r","r":"s","s":"t","t":"u","u":"v","v":"w","w":"x","x":"y","y":"z","z":"a"," ":"-"}
   
    # user input to encode
    userName = input("Enter string to encode: ")
    
    # error check if input is num
    if userName.isnumeric():
        print("*** Alpha Characters Only ***")
        return
    
    # if error checking passed continue with encoding
    else:
    # print line on same line as encoded messag
        print('Encoded message: ', end='')
    
    # for chars in user input, match with keys in encoding
        for i in userName:
        
        #print encoded messag on same line
            print(end=encoding[i])
  
main()
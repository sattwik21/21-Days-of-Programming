binary_string=input("enter a binary string ")
binary_values=binary_string.split()
string_ascii=" "
for binary_value in binary_values:
    decimal=int(binary_value, 2)   #converting to base 2 decimal integer  
    
    ascii_character=chr(decimal)   #converting to character
    
    string_ascii+=ascii_character  #adding characters to ASCII string

print(string_ascii)    

#EASTER EGG
#USING THE ABOVE PROGRAM THE ASCII STRING OBTAINED FROM THE POSTER:
#EUREKA (01000101 01010101 01010010 01000101 01001011 01000001)
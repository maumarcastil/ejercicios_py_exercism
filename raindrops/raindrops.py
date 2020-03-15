def convert(number):
        
    r = ""
    if number%3== 0:
        mensaje = "Pling"
        r= mensaje
    if number%5==0:
        mensaje = "Plang"
        r += mensaje
    
    if number%7 == 0:
        mensaje = "Plong"
        r += mensaje
        
    if number%3!=0 and number%5!=0 and number%7!= 0:
        return str(number)
        
    return r

print(convert(5))
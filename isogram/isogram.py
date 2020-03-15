def is_isogram(string):
    
    especiales =["-", "_", " "]
    for i in especiales:
        string = string.replace(i, "")
        
        string = string.lower()
        
        return sum([string.count(y) > 1 for y in set(list(string))]) == 0
    

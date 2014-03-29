def reverse(text):
    x = len(text)
    counter = x - 1
    new_text = ""  
    
    for n in range(0, x):
        new_text += text[counter]   
        counter = counter - 1
    
    return new_text   

def reverse(text):
    reverse = ""
    for letter in text:
        reverse = letter + reverse
    return reverse
def convert(number):
    result = ""
    
    if number % 3 == 0 :
        result = "Pling"
        if number % 5 == 0:
            result = "PlingPlang"
        if number % 7 == 0:
            result = "PlingPlangPlong"
    if number % 5 == 0:
        result = "Plang"
        if number % 7 == 0:
            result = "PlangPlong"
    elif number % 7 == 0:
        result = "Plong"
        if number % 3 == 0:
            result = "PlingPlong"
    else:
       result = str(number)
    return result
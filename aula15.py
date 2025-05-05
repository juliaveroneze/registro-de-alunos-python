year = int(input('ano: '))

def is_leap(year):
    leap = False
    bissexto = year // 4
    
    if bissexto % 2 == 0:
        leap = True
        return leap
    else:
        leap = False
        return leap
print(is_leap(year))
    
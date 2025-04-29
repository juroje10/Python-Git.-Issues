def calc(x,y,o):
 if o=='+':
  return x+y
 elif o=='-':
  return x-y
 elif o=='*':
    return x*y
 elif o == '/':
    if y == 0:
        return 'Error: división por cero'
    return x / y
 else:
  print('Error')
  
print(calc(5,0,'/'))

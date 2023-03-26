def max_num(arg1,arg2,arg3):
    num = arg1
    if arg2 > num:
        num = arg2
    if arg3 > num:
        num = arg3
    return num
  
def mult_list(args_list):
  product = 1
  for i in args_list:
    i *=product
    
  return product

def revString(string):
  text = string[::-1]
  print(text)
  
def numWithin(num, range_low, range_high):
  return lower <= num <= upper
  
def pascal(n):
  row = [1]
  
  for i in range(n):
    print(row)
    next_row = [1]
    for j in range(1, len(row)):
      nex_row.append(row[j-1] + row[j])
    next_row.append(1)
    
    row = next_row
    
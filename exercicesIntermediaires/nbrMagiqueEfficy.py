def largest_magic_number(): 
  largest_magic_number = 0
  for i in range(100, 1000):
    for j in range(100, 1000):
      product = i * j
      if str(product) == str(product)[::-1] and product > largest_magic_number:
        largest_magic_number = product
  return largest_magic_number

print(largest_magic_number())
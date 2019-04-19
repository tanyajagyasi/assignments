# to get a single string from 2 given strings, separated by space and swap them

def chars(a, b):
  new_a = b[:2] + a[2:]
  new_b = a[:2] + b[2:]

  return new_a + ' ' + new_b
print(chars('hello', 'world'))

# Complete the function so that it takes an array of keys and a default value and returns a hash (Ruby) / dictionary (Python) with all keys set to the default value.



def populate_dict(keys, default):
  # your code here
  result = {}
  for x in keys:
    result[x] = default

  return result


print(populate_dict([1, 2, 3, 4], "OK")) #, {1: "OK", 2: "OK", 3: "OK", 4: "OK"})
"removing numbers and other characters from a string with a generator"

s = '12a67bc23d~405e!_/;]}'
result = ''.join(i for i in s if i.isalpha())
print(result)
sample_string = "32.054,23"
mod_string = ""

for char in sample_string:
    if char == '.':
        mod_string+=','
    elif char == ',':
        mod_string+='.'
    else:
        mod_string+=char

print(mod_string)
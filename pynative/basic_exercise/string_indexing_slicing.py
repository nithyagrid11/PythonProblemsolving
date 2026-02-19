def string_slicing(s):
    return "\n".join(s[::2])
print(f'Printing only even index chars \n{string_slicing("pynative")}')
def get_summ(one, two, delimiter = "&"):
    one = str(one)
    two = str(two)
    return one + delimiter + two 
a = get_summ("Learn", "python")
print(a.upper())
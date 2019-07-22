d = {"one":1,"two":2,"three":3}
print(d["three"])
d["two"]="hacker"
print(d)
del d["three"]
print(d)
if 2 in d:
    print("values")
if "two" in d:
    print("key")
if ("one",1) in d:
    print("kv")
def is_key(D,key):
    if(key in D.keys()):
        print("True")
    else:
        print("False")
def value(D,key):
    if(key not in D.keys):
        print("None")
    else:
        print(D[key])

is_key({"ridhi":2,"adya":5,"subbu":9},"subb")

def cost(L):
    sum = 0
    for i in range(0,len(L)):
        a = L[i].get("price")
        b = L[i].get("Qty")
        sum+= (a*b)
    return sum
def get_summary(trans):
    List = []
    for i in range(0,len(trans)):
        d1 = {}
        d1["TID"] = trans[i].get("TID")
        d1["cost"] = cost(trans[i].get("items"))
        List.append(d1)
    return List        
print(get_summary([{'TID': 'Gurunath_8528', 'items' : [{'name':'notebook','price':50,'Qty':4},{'name':'notebook','price':50,'Qty':4},{'name':'notes','price':10,'Qty':1},{'name':'nbook','price':20,'Qty':3}]},{'TID': 'Gurunath_8526', 'items' : [{'name':'notebook','price':50,'Qty':4},{'name':'notes','price':10,'Qty':1},{'name':'nbook','price':200,'Qty':3}]},{'TID': 'Gurunath_8328', 'items' : [{'name':'notebook','price':50,'Qty':4},{'name':'notebook','price':50,'Qty':4},{'name':'notes','price':100,'Qty':1},{'name':'nbook','price':10,'Qty':2}]}]))
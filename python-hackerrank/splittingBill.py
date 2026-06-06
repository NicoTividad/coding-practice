def bonAppetit(bill, k ,b):
    # print(bill)
    # print(f"Anna doesn't eat item {bill[k]}")
    bill.remove(bill[k])
    # print(bill)
    charged = (sum(bill)/2)
    # print(f"Anna is charged {charged}")
    if b > charged:
        owed = b - charged
        # print(f"Brian owes {owed}")
        print(int(owed))
    elif b == charged:
        print("Bon Appetit")

bill = [3,10,2,9]
b = 12
k = 1
print(bonAppetit(bill, k, b))
import question_b

while True:
    
    print("Stock Menu")
    print("1 - Display stock purchase history")
    print("3 - Exit")
    
    
    num = input("Choice number: ")
    if num == "1":
        question_b.stock_purchase_history()
    elif num == "3":
        break

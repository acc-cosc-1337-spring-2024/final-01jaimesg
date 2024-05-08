largest = None
smallest = None
List_collector=[]
while True:
    num = input("Enter 5 number and when complete type 'done'.Enter a number: ")
    if num == 'done':
        break
    n = int(num)
    List_collector.append(n)
    largest=max(List_collector)
    smallest=min(List_collector)
    
    #print("Invalid input")
    continue
print("Maximum number is", largest)
print("Minimum number is", smallest)
print("Average number is", sum(List_collector) / len(List_collector))
print("The sum of all numbers is", sum(List_collector))
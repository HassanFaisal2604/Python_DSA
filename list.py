list1=[]
def user_input():
    while True:
        inp=input("Enter a number or type exit")
        
        if inp=='exit':
            break   
        Value=float(inp)
        list1.append(Value)
user_input()
print(list1)
print("AVerage",sum(list1)/len(list1))   


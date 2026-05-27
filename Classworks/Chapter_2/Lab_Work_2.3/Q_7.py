for i in range(1,50+1):
    if i%2==0:
        if i%3==0:
            print(i,"is divisible by both.");
        else:    
            print(i,"is divisible by 2.");
    elif i%3==0:
        print(i,"is divisible by 3.")
    else:
        print(i,"Not divisible!")
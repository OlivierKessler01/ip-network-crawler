def infinite_sequence():
    num = 0
    while num < 1000:
        yield num
        num += 1



if __name__ == "__main__":
    #Function-based generator is iterated through
    for i in infinite_sequence():
        print(i, end=" ")

    
    n = (num**2 for num in range(10))
    
    for val in n:
        print(next(n))
    

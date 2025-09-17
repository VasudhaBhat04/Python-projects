def add(x,y):
    return x + y
 
if __name__ == '__main__': # this tells the function to run only when called directly , itls like gatekeeper for function whether to run or not...if you dont use this & import in scrip1.py the add function would run (so to safegaurd u will add this)
    print(add(3,4))  
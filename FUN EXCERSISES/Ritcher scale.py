while True:
    a=float(input())
    if(a<2.0):
        print("Micro")
    elif(a>=2.0 and a<3.0):
        print("Very minor")
    elif(a>=3.0 and a<4.0):
        print("Minor")
    elif(a>=4.0 and a<5.0):
        print("Light")
    elif(a>=5.0 and a<6.0):
        print("Moderate")
    elif(a>=6.0 and a<7.0):
        print("Strong")
    elif(a>=7.0 and a<8.0):
        print("Major")
    elif(a>=8.0 and a<10.0):
        print("Great")
    else:
        print("Meteoric")
        
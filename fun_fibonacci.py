def series():
    f=1
    s=1
    print(f)
    print(s)
    for n in range(1,5):
        t=f+s
        f=s
        s=t
        print(t)
series()

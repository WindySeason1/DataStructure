def dist(high, pop):
    if high*pop<0.1:
        return s
    else:
        s.append(2 * high * pop)
        high=high*pop
        print(high)
        dist(high,pop)


if __name__ == '__main__':
    h=float(input("球的高度h为:"))
    p=float(input("弹性p为："))
    s=[h]
    d=[]
    print(sum(s))
    dist(h,p)
    print(sum(s))


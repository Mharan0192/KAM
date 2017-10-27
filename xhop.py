def xhop(p):
    d = {}
    for i in range(0,p):
        if i == 0:
            x = 0
            y = 0
            d = dict({x,y})
            plt.scatter(x, y)
        else:
            if i % 8 == 1:
                for f in range(0,i)

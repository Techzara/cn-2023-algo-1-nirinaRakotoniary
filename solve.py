def share_candy(enfants, bonbons) :
    res = {}
    for e in enfants :
        res[e] = {}
        for v in enfants[e]:
            if(bonbons[v] > 0):
                res[e][v] = 1
                bonbons[v] -=  1
    for x in res :
        print(x,":",res[x])
    print(bonbons)
    return res

#input format & ohatra for testing
enfants = {
    "Alice" : ["chocolat", "guimauve"],
    "Bob" : ["caramel", "fruit"],
    "Charlie" : ["chocolat", "caramel"]
    }
bonbons = {
    "chocolat" : 10,
    "caramel" : 8,
    "guimauve" : 5,
    "fruit" : 6
}

share_candy(enfants, bonbons)
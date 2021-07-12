products=[
     {'item':'complan','mrp':240,'stock':10},
     {'item':'boost','mrp':290,'stock':50},
     {'item':'bornvita','mrp':320,'stock':20},
     {'item':'horlicks','mrp':280,'stock':13},
     {'item':'nutricharge','mrp':275,'stock':0}]
below=list(filter(lambda product:product['mrp']<250,products))
print(below)
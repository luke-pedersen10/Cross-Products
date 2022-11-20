getDimension = int(input("Enter two dimensions or three dimensions"))
dimensionNumber = getDimension()
if getDimension() = "3d":
    

def getPoint():
    x1=int(input("enter your x value for vector 1: "))
    y1=int(input("enter your y value for vector 1: "))
    z1=int(input("enter your z value for vector 1: "))
    return [x1,y1,z1]


def solve2DVector(a,b):
    vectorFinal = (a[0]*b[1])-(b[0]*a[1])
    return vectorFinal

def solve3DVector(a,b):
    # a = [x1, y1, z1]
    # b = [x2, y2, z2]
    ihat = ((a[1]*b[2])-(a[2]*b[1]))
    jhat = ((a[0]*b[2])-[b[0]*a[2]])
    khat = ((a[0]*b[2])-(b[0]*a[2]))
    return [ihat,jhat, khat]

v1 = getPoint() 
v2 = getPoint()
print(solve2DVector(v1,v2))

print(solve3DVector(v1,v2))
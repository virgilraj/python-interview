
def is_circularly_rotated(X,Y):

    n = len(X)
    if n != len(Y) or X == Y:
        print("Not rotated")
        return

    for i in range(n):
        X = X[1:] + X[0]
    
        if X == Y:
            print("Rotated")
            return
    print("Not rotated")


if __name__ == "__main__":
    is_circularly_rotated('ABCD', 'CDAB')
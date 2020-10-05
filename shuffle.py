from random import randrange

def shuffle(arr):
    for i in reversed(range(1,len(arr))):
        j = randrange(i+1)
        arr[i],arr[j] = arr[j], arr[i]
    print(arr)


if __name__ == "__main__":
    A = [1, 2, 3, 4, 5, 6]
    shuffle(A)
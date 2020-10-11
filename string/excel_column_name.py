
def get_column_name(n):
    # initialize output String as empty
    res = ""
    while n > 0:
        index = (n-1)%26
        print(index, ord('A'))
        print(chr(index + ord('A')))        
        res += chr(index + ord('A'))
        print(res)
        n = (n-1)//26
        print(res[::-1])


if __name__ == "__main__":
    get_column_name(527)
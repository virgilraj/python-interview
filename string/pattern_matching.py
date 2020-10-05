
def kmp_search(txt, pat):
    N = len(txt)
    M = len(pat)

    lps = [0] * M
    compute_LPS_arry(pat, M, lps)

    i= 0 # txt - index
    j = 0 # pat - index

    while i < N:
        if pat[j] == txt[i]:
            i = i +1
            j = j +1
        
        if j == M :
            print("Pattern found at index ", i-j)
            j = lps[j-1]
        elif i < N and pat[j] != txt[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i = i +1
        

def compute_LPS_arry(pat, M , lps):
    l = 0 #length of previous longest prefix or suffix
    
    print(lps)
    i =1
    # the loop calculates lps[i] for i = 1 to M-1 
    while i < M:
        if pat[i] == pat[l]:
            l += 1
            lps[i] = l
            i += 1
        else:
            if l != 0:
                l = lps[l -1]
            else:
                lps[i] = 0
                i += 1
    print(lps)

def find_one_string_rotation_of_nother(txt1, txt2):
    txt = txt1 + txt2
    kmp_search(txt, txt2)

if __name__ == "__main__":
    pat = "abcaby"
    #lps = [0, 0, 0, 1, 2, 0]
    txt = "AABAACAADAABAABA"
    pat = "AABA"
    #kmp_search(txt, pat)
    find_one_string_rotation_of_nother('mypencil', 'encilmyp')
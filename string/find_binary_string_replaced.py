from collections import deque

def print_all_combinations(pat):
    # create an empty stack (we can also use set, deque
	# or any other container)
    stack = deque()
    stack.append(pat)
    # loop till stack is empty
    while stack:
        cur = stack.pop()
        # index stores position of first occurrence of wildcard
        # pattern in curr
        index = cur.find('?')
        if index != -1:
            # replace '?' with 0 and 1 and push it to the stack
            for ch in "01":
                cur = cur[:index] + ch + cur[index+1:]
                stack.append(cur)
        else:
            print(cur)


if __name__ == "__main__":
    print_all_combinations('1?11?00?1?')
#try again, no lists
# amount of dashes at top left is ((2^N) // 2) - 1

def ascii_tree(n):

    counter = 1; # increment this to repeat lines. Without it,
                 #we only have the left-most parts of the tree.
    tree=''; # empty tree
    m = n # dummy var to decrement n while also preserving the og value thru n
    while m >= 0:
        dashes = (2**m//2)-1 # dashes at outer parts of each branch
        height = 2**m//2 # starts at og height, gets cut in half every iteration
        mid_dash = 0 # how many dashes between slashes? doubles in the for-loop iterations, but must be reset
        for x in range(height//2):
            tree +=(('-'*dashes)+'/'+('-'*mid_dash)+'\\'+('-'*dashes)) * counter + '\n' 
            dashes -= 1
            mid_dash += 2
        m -= 1;counter*=2
    tree += '/\\' * (2**(n-1))
    return tree

print(ascii_tree(5))



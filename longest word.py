# function to find the longest
# length in the list
def longestLength(a):
    max1 = len(a[0])
    temp = a[0]
    # for loop to traverse the list
    for i in a:
        if(len(i)>max1):
            max1 = len(i)
        temp = i
        print("the word with the longest lenth is:",temp," and length is",max1)
        # Driver program
        a = ["one","two","third","four"]
        longestLength(a)

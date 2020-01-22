#print("hello world!")

# Empty dictionary for Items and counts
my_dict ={}
frequent_item = {}

# a file named "geek", will be opened with the reading mode.
file = open('categories.txt', 'r')
# This will print every line one by one in the file
for line in file:
    #print (line)
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split(";")
    # increase counters
    for word in words:
        #print '%s\t%s' % (word, 1)
        if my_dict.get(word,"Not Found!")== "Not Found!" :
            my_dict[word] = 1
        else:
            my_dict[word] += 1

for keys in my_dict:
    #print items

    if my_dict[keys]> 771:
        frequent_item[keys] = my_dict[keys]

# This will close the file
for items in frequent_item.items():
    print items

file.close()
#print("hello world!")
#-----------------------------------------------------------------------
# This function will generate candidate itemset of length K from the
# frequent itemset of length K-1
# @input = frequent itemset of length K-1
# @return = candidate itemset of length K
#-----------------------------------------------------------------------

def apriori_gen(frequent_itemset):

    temp_dict = frequent_itemset
    candidate_dict = {}

    # self-join to create candidate itemset
    for keys_1 in frequent_itemset:
        for keys_2 in temp_dict:
            if(keys_1 != keys_2):
                items_1= keys_1.split(";")
                items_2= keys_2.split(";")

                # how to get the lenth of the items in a key
                if (len(items_1)==1 and items_1<items_2):

                    #for k=2 itemset,return the concatenated value if items in list 2 is greater
                    #than in list 1
                    candidate_dict[items_1[0]+";"+items_2[0]] = 1
                    #candidate_dict[items_1 + items_2] = 1
                else:

                    # do more work if k>2
                    # self join logic: when k-2 items in list 1 & 2 are equal and
                    # (k-1)th item in list 2 is greater than that in list 1
                    index = 0
                    candidate_item = ""
                    while index < len(items_1)-1:
                        if (items_1[index]!= items_2[index]):
                            #candidate_item = ""
                            exit()
                        else:
                            if (candidate_item ==""):
                                candidate_item = items_1[index]
                            else:
                                candidate_item = candidate_item + ";" + items_1[index]
                            index += 1

                    if (items_1[index] < items_2[index]):
                        # AB & AC, since A=A and B<c the candidate pattern of length K will be ABC
                        candidate_item = candidate_item + ";" + items_1[index] + ";" +items_2[index]

                    # Prune infrequent items from candidate_item if it contains infrequent item
                    # subsets else add to the candidate_dict of legth k items
                    if has_infrequent_subset(candidate_item,frequent_itemset)== False and candidate_item != "":
                        candidate_dict[candidate_item] = 1

    '''
    print("legth of itemset = " + str(len(candidate_dict.items())))
    print ("Printing candidate itemset from apriori_gen()...")
    for items in sorted(candidate_dict.items()):
        print items
    '''

    return candidate_dict
#-----------------------------------------------------------------------
# This function will check if candidate itemset has infrequent subsets
# i.e. support_count < minsup
# @input = candidate item of length K
# #return = TRUE/FALSE
#-----------------------------------------------------------------------

def has_infrequent_subset(candidate_item, frequent_itemset):

    items = candidate_item.split(";")
    #infrequent_item = False

    for item in items:
        if frequent_itemset.get(item,"Not Found!")!= "Not Found!":
            Return = True

    return False

    #print ("Printing candidate itemset from apriori_gen()...")
    #for items in candidate_item.items():
    #    print items

#-----------------------------------------------------------------------
# This function will check if candidate itemset has infrequent subsets
# i.e. support_count < minsup
# @input = candidate item of length K
# #return = TRUE/FALSE
#-----------------------------------------------------------------------

#Global variables
MIN_SUP = 771
INPUT_FILE = 'categories.txt'
OUTPUT_FILE = 'patterns.txt'
#test value for MIN_SUP
#MIN_SUP = 1

#-----------------------------------------------------------------------
# main function will invoke the Apriori Algorithm for a given txn set
#-----------------------------------------------------------------------
def main():

    #Empty dictionary for Items and counts
    my_dict = {}
    frequent_items = {}
    frequent_items_k = {}

    # a file named "geek", will be opened with the reading mode.
    file = open(INPUT_FILE, 'r')
    #file = open('categories_test.txt', 'r')
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

    # This will close the file
    file.close()

    for keys in my_dict:
        #print items

        if my_dict[keys]> MIN_SUP:
            frequent_items_k[keys] = my_dict[keys]

    '''-------------------------------------
    Generating output for Part 1
    ----------------------------------------'''

    outputfile = open(OUTPUT_FILE, 'a')

    for keys,values in frequent_items_k.items():
        outputfile.write(str(values)+":"+keys+"\n")

    #outputfile.close()


    #Iterate for all itemsets of size > 1
    while len(frequent_items_k.items()) > 0:

        print("legth of frequent k-itemset = " + str(len(frequent_items_k.items())))

        #get candidate itemset of k-length
        Candidate_items_k = apriori_gen(frequent_items_k)
        #print("legth of candidate k-itemset = " + str(len(Candidate_items_k.items())))
        # print candidate_items_k
        #for items in sorted(Candidate_items_k.items()):
        #    print items

        #iterate through the transactions to select k-itemsets with support > min_sup
        # increase counters
        for keys, values in Candidate_items_k.items():
            #print("New Candiate Itemset = " + keys)
            items = keys.split(";")
            support_count = 0

            # a file named "catgories.txt", will be opened with the reading mode.
            file = open(INPUT_FILE, 'r')
            #file = open('categories_test.txt', 'r')

            for line in file:

                #print line
                line = line.strip()
                '''
                #split the line into words
                words = line.split(";")

                #iterate through all items in the current candidate itemset and
                #chek if all of them present in the line i.e. Txn
                #If all items exits in the txn then increment count by 1
                for item in items:
                    #print "Candidate Item set components" + item
                   if words.count(item)==0:
                       support_count = 0
                       #print str(support_count)
                '''
                #if set(items).intersection(line.split(";")):
                if set(items).issubset(line.split(";")):
                       support_count += 1

            Candidate_items_k[keys] = support_count

            # Close categories.txt
            file.close()
        '''
        print("legth of candidate k-itemset = " + str(len(Candidate_items_k.items())))
        for items in Candidate_items_k.items():
            print items

        '''

        #Append frequent item sets of legth k with all itemsets of length<k
        #frequent_items_k contents in the frequent_items
        #for keys in frequent_items_k:
            #print(keys)
            #frequent_items[keys] = frequent_items_k[keys]
        #frequent_items.update(frequent_items_k)
        '''
        #Write/append frequent items to patterns.txt
        for keys, values in frequent_items_k.items():
            #print items
            outputfile.write(str(values) + ":" + keys + "\n")
        '''
        #get candidate itemmset with support > MIN_SUP into frequent_items_k
        frequent_items_k.clear()

        for keys,values in Candidate_items_k.items():

            if values > MIN_SUP:
                frequent_items_k[keys] = values
                #print(str(values) + ":" + keys + "\n")
                outputfile.write(str(values) + ":" + keys + "\n")
        Candidate_items_k.clear()

        '''
        print("legth of itemset = " + str(len(frequent_items_k.items())))
        for items in sorted(frequent_items_k.items()):
            print items
        '''
    '''
    #print frequent_items
    for items in sorted(frequent_items.items()):
       print items
    '''
    outputfile.close()

if __name__ == '__main__':
    main()
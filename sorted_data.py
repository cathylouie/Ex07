from sys import argv

"""Your job is to write a program named 'sorted_data.py' reads
the file, then spits out the ratings in alphabetical order 
by restaurant"""

script, filename = argv

# print script 
# print filename 

#open file
f = open(filename, "r")
 
#read file 
my_restaurants = f.read()
#close file 
f.close()

# my_sorted_restaurants = my_restaurants
#print my_sorted_restaurants

#my_sorted_restaurants.sort()
#print my_sorted_restaurants

my_rest = {}

my_restaurants = my_restaurants.split("\n")


for line in my_restaurants:
    split_txt = line.split(":")
    if len(split_txt) == 2:
        my_rest[split_txt[0]]=split_txt[1]

print my_rest

for r in sorted(my_rest, key=my_rest.get, reverse=True):
    print "Restaurant %r is rated %d" % (r, int(my_rest[r]))

    

#my_rest.append(my_restaurants)
#print my_rest



# print my_restaurants
# make empty dictionary 
# restaurant_scores = {}
"""for key,value in sorted(dic.items()):"""
#put items from scores.txt into dictionary 

# # for restaurant in restaurant_scores:
#     restaurant_scores[restaurant]

# print restaurant_scores
# sort keys into alphabetical order 
#print key, value
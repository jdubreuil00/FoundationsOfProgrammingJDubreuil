"""
Below are the three string functions I researched in context.
"""

# first is the count function 

"""
The count function is a string method that returns
the number of occurances of an item in a string.
See the example below.
"""

countstring = 'Even after death god blesses everyone.'

#If I want to know the number of times the letter e appears in the string I can use the count method like this.

print(countstring.count('e'))


# returns 8. Notice this does not account for capital E.

print(countstring.count('E'))

#So the method is case sensitive.

"""
Since the count functionis case sensitive, 
it would make sense to make the entire string lower cased. 
This would give us all the occurances of the letter e
without running the sane function twice and leads us to the 
second string function of this post.
"""

#The lower function is a method that makes the entire string lowercased.
# I will use this in the evaluation of countstring to get every instance of the letter e coupled with dot syntax

print(countstring.lower().count('e')) 

# returns 9

"""
Now for a little fun and to appease some
of the athiests who might not agree with my string. 
BTW countstring is an acronym someone taught me to remember the strings on a guitar.
Now for the last function. Lets try out replace.
"""

# The replace fucntion is a method that replaces all occurances of a substring with a new one.
# Here I will use the replace function to change god to google in the countstring variable.

print(countstring.replace('god', 'google'))

# returns Even after death google blesses everyone.

"""
So just to recap here are the three functions I researched

"some string".count(item)
Number of occurances of an item in a string.

"some string".lower()
Returns the string all lowercase.

"some string".replace('old item', 'new item')
Replaces all occurances of old substring with the new substring.

"""
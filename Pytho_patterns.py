import re
match = re.search(r'portal', 'GeeksForGeeks: A computer science \ portal for geeks')

print(match)
print(match.group())

print('Start Index:', match.start())
print('End Index:', match.end())

print(re.findall(r'[Gg]eeks', 'GeeksforGeeks: \
                 A computer science portal for geeks'))
print('Range',re.search(r'[a-zA-Z]', 'x'))

print(re.search(r'[^a-z]', 'c'))

# Beginning of String
match = re.search(r'^Geek', 'Campus Geek of the month')
print('Beg. of String:', match)

# End of String
match = re.search(r'Geeks$', 'Compute science portal-GeeksforGeeks')
print('End of String:', match)

# Any character represents any single character outside a baractred class
print('Any Character', re.search(r'p.th.n', 'python 3'))

# repetition allows to repeat the same character
print('Date{mm-dd-yyyy}:', re.search(r'[\d]{2}-[\d]{2}-[\d]{4}',
                                     '18-08-2020'))

# Ranges consider where only three digits and four digits are accepted
print('Three Digit:', re.search(r'[\d]{3,4}', '189'))
print('Four Digit:', re.search(r'[\d]{3,4}', '2145'))

# shorthand allow you to use + character to specify one or more and *
# to specify zero or more
print(re.search(r'[\d]+', '5th Floor, A-118,\
Sector-136, Noida, Uttar Pradesh - 201305'))

#Grouping is the process of separating an expression into groups by using parentheses, and it allows you to fetch each individual matching group.
grp = re.search(r'([\d]{2})-([\d]{2})-([\d]{4})', '26-08-2020')
print(grp)
#re module allows you to return the entire match using the group() method

grp = re.search(r'([\d]{2})-([\d]{2})-([\d]{4})','26-08-2020')
print(grp.group())
grp = re.search(r'([\d]{2})-([\d]{2})-([\d]{4})','26-08-2020')
print(grp.groups())

# upon passing the index to a group method you can retrieve just a single group
grp = re.search(r'([\d]{2})-([\d]{2})-([\d]{4})','26-08-2020')
print(grp.group(3))

# Name your group
match = re.search(r'(?P<dd>[\d]{2})-(?P<mm>[\d]{2})-(?P<yyyy>[\d]{4})',
                  '26-08-2020')
print(match.group('mm'))

# Individual match as a dictionary
match = re.search(r'(?P<dd>[\d]{2})-(?P<mm>[\d]{2})-(?P<yyyy>[\d]{4})',
                  '26-08-2020')
print(match.groupdict())

# substitution
print(re.sub(r'([\d]{4})-([\d]{4})-([\d]{4})-([\d]{4})',r'\1\2\3\4',
             '1111-2222-3333-4444'))
# If you are using Windows, and getting errors about the character encoding, you may need to set the environment variable set PYTHONUTF8=1 from the command line first.
import re

# Open language-specific config file

configfile = input("Language-specific config file:")
print("Language-specific config file is: " + configfile)

with open(configfile) as letsdothis:
    exec(letsdothis.read())

# Clean up text:  Remove punctuation and numerals, upper/lower case distinction, double consonants/vowels-> single, voiced/voiceless distinction 

delete_this = re.compile(r'\/|\{|\}|\[|\]|\?|\|\<|\>|\!|[0-9]|°|\'|\+|\"|\;|§|\.|\,|”|\-|“|’|\%|‘|\(|\)|′|•|\:|¿|¡|“||"|„|«|»') 
text=re.sub(delete_this, '', text)

for i in range(len(uppercase)):
    ff = re.compile(uppercase[i]) 
    text=re.sub(ff, lowercase[i], text)

p = f'({vowels}|{consonants})\\1'
pattern = re.compile(p)
matches = pattern.findall(text)
for match in matches:
	text = text.replace(match[0]+match[0], match[0])
    
for i in range(len(voiced)):
    ff = re.compile(voiced[i]) 
    text=re.sub(ff, voiceless[i], text)

# Convert to syllabic spelling

# First handle the consonant clusters

# I didn't want to go to the trouble of digging through all the scholarship at this point (my notes are in a box), so I relied on Volume 3 of A Companion to Linear B, whose discussion wasn't as complete as I would have liked.  In the interest of getting this show on the road, here's what I'm assuming in the way of spelling rules, whether both elements are written (Y) or only the second (N):
# S+S	Y
# S+N	Y
# S+F	Y
# S+L	Y
# N+S	N
# N+N	Y
# N+F	N (either not written, or 2 CL has taken place, but if N+S is not written, N+F likely won't be, either)
# N+L	Y (impossible to tell because nr -> ndr and mr -> mbr cf. a-re-ka-sa-da-ra-qe.  But if they wrote N+G, I'm going to assume N+L as well.)
# F+S	N
# F+N	Y
# F+F	Y (Does not appear in Greek but if NN and SS are Y I'm assuming this is Y also)
# F+L	Y (1CL took care of this in Greek but I'm assuming if they wrote out sequences F+G they would also write F+L.)
# L+S	N
# L+N	N
# L+F	N (Again 1CL, but I assume if they're not writing L+S they're not writing L+F)
# L+G	N
# G+L	N

# FINAL STOPS ARE WRITTEN, I assume from examples such as wa-na-ka.  Final fricatives, liquids, and nasals are not.

clusters = \
['({nasals})({stops}|{affrics})', 
'({nasals})({frics})', 
'({frics})({stops}|{affrics})',
'({liquids})({stops}|{affrics})',
'({liquids})({nasals})',
'({liquids})({frics})',
'({liquids})({glides})',
'({glides})({liquids})']

# This was my attempt at a for loop and it didn't work.  If you troubelshoot, you'll see that the problem is that it's defining 'pattern' as the entire string 're.compile(p)' and I do not know why

for i in range(len(clusters)):
    print(clusters[i])
    p = f'{clusters[i]}'
    pattern = re.compile(p) 
    print(pattern)
    matches = pattern.findall(text)
    print(matches)
    for match in matches:
        text = text.replace(match[0]+match[1], match[1])

# Second attempt at a for loop and tis doesn't work either
        
# for i in range(len(clusters)):
    # print(clusters[i])
    # ff = re.compile(clusters[i])
    # print(ff)
    # matches = ff.findall(text)
    # print(matches)
    # for match in matches:
        # text = text.replace(match[0]+match[1], match[1])

# I attempted to define a function so we at least don't have the repetition, but this also doesn't work?  I keep getting the error "TypeError:  'set' object is not callable
# def clusterdelete(cons):
    # p = f'cons'
    # pattern = re.compile(p)
    # matches = pattern.findall(text)
    # for match in matches:
        # text = text.replace(match[0]+match[1], match[1])

# w = ({nasals})({stops}|{affrics})
# clusterdelete(w)

# p = f'({nasals})({stops}|{affrics})'
# pattern = re.compile(p)
# matches = pattern.findall(text)
# for match in matches:
	# text = text.replace(match[0]+match[1], match[1])
    
# p = f'({nasals})({frics})'
# pattern = re.compile(p)
# matches = pattern.findall(text)
# for match in matches:
	# text = text.replace(match[0]+match[1], match[1])
    
# p = f'({frics})({stops}|{affrics})'
# pattern = re.compile(p)
# matches = pattern.findall(text)
# for match in matches:
	# text = text.replace(match[0]+match[1], match[1])
    
# p = f'({liquids})({stops}|{affrics})'
# pattern = re.compile(p)
# matches = pattern.findall(text)
# for match in matches:
	# text = text.replace(match[0]+match[1], match[1])
    
# p = f'({liquids})({nasals})'
# pattern = re.compile(p)
# matches = pattern.findall(text)
# for match in matches:
	# text = text.replace(match[0]+match[1], match[1])
    
# p = f'({liquids})({frics})'
# pattern = re.compile(p)
# matches = pattern.findall(text)
# for match in matches:
	# text = text.replace(match[0]+match[1], match[1])
    
# p = f'({liquids})({glides})'
# pattern = re.compile(p)
# matches = pattern.findall(text)
# for match in matches:
	# text = text.replace(match[0]+match[1], match[1])
    
# p = f'({glides})({liquids})'
# pattern = re.compile(p)
# matches = pattern.findall(text)
# for match in matches:
	# text = text.replace(match[0]+match[1], match[1])
    
#  Delete final consonants


myfile = open('OutputFile.txt', 'w')
myfile.write(text)
print('Output file written')
myfile.close()

# Next:  add dummy vowels where appropriate-- between consonant clusters and at word end.

# p = f'({vowels})({stops}|{affrics})({whitespace})'
# pattern = re.compile(p)
# matches = pattern.findall(text)
# print(matches)
# for match in matches:
    # text = text.replace(match[2], match[0]+match[2])



# Convert to Akkadian Cuneiform spelling
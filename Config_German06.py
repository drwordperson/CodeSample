import re
with open('deu_news_2023_10K-sentences.txt', encoding='utf8') as f:
    text = f.read()
    
myfile = open('OutputFile.txt', 'w')
myfile.write(text)
print('Input file opened')
myfile.close()

uppercase = ['A', 'Ä', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'Ö', 'P', 'Q', 'R', 'S', 'ẞ', 'T', 'U', 'Ü', 'V', 'W', 'X', 'Y', 'Z']
lowercase = ['a', 'ä', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'q', 'r', 's', 'ß', 't', 'u', 'ü', 'v', 'w', 'x', 'y', 'z']

vowels = 'a|ä|e|i|o|ö|u|ü|y'

diphs = ['ai', 'oi']  #Only diphthongs not in u

consonants = 'b|c|d|f|g|h|j|k|l|m|n|p|q|r|s|t|v|w|x|z|φ|χ|ʃ'

stops = 'p|b|t|d|k|g|q'
affrics = 'z|φ'
frics = 'f|s|v|h|w|χ|ʃ'
nasals = 'n|m'
liquids = 'l|r'
glides = 'j'
whitespace = r'\n|\s'

voiceless = ['p', 't', 'k', 'f']
voiced = ['b', 'd', 'g', 'v']

ff = re.compile('ẞ|ß') #Letter not realized as a consonant/vowel, so deleted.
text=re.sub(ff, 's', text)

ff = re.compile('PF|pf') #Can't do digraphs and this is as good a symbol as any
text=re.sub(ff, 'φ', text)

ff = re.compile('Ä|ä') #Whether or not these are separate in German, no Linear B scribe would write them as different vowel series
text=re.sub(ff, 'e', text)

ff = re.compile('X|x') #Underlying ks.
text=re.sub(ff, 'ks', text)

ff = re.compile('W|w') #These all need to end up voiceless anyway
text=re.sub(ff, 'f', text)

ff = re.compile('Sch|sch') #digraph
text=re.sub(ff, 'ʃ', text)

ff = re.compile('Ck|ck') #Trigraph
text=re.sub(ff, 'k', text)

ff = re.compile('Ch|ch') #Can't do digraphs and this is as good a symbol as any
text=re.sub(ff, 'χ', text)

ff = re.compile('Qu|qu') 
text=re.sub(ff, 'kv', text)

ff = re.compile('Q|q') 
text=re.sub(ff, 'k', text)

ff = re.compile('Ei|ei') 
text=re.sub(ff, 'ai', text) 

ff = re.compile('Ie|ie') 
text=re.sub(ff, 'i', text) 

ff = re.compile('Eu|eu') 
text=re.sub(ff, 'oi', text) 

#  Get rid of diphthongs in i

for i in range(len(diphs)):
    diph = diphs[i]
    text = text.replace(diph[0]+diph[1], diph[0])


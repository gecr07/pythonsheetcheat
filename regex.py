#!/usr/bin/python3

import re


var=r"Quiero imprimir \n"

#print(var)


pattern = r"Cookie"
sequence = " Most alphabets and characters will match themselves, as you saw in the example. Cookie"

if re.match(pattern, sequence):# Si lo pones al inicio si lo hace si lo pones solo si lo hace
    print("Match!")
else: print("Not a match!")#Osea busca sencilla 

print("group y search")

if re.search(pattern, sequence).group():# Si lo pones al inicio si lo hace si lo pones solo si lo hace
    print("Match!")
    print(re.search(pattern, sequence).group())# t  grefresa lo que encontro en todo el string
else: 
	print("Not a match!")# busca atraves de todo el string con group te devuelve loq ue encontro



#USO del Punto . A period. Matches any single character except the newline character.

print(re.search(r'Co.k.e', 'Cookie').group())	

#USO del ^  A caret. Matches the start of the string.


print(re.search(r'^Eat', "Eat cake!").group())

print(re.search(r'^Eat', "Eat cake!"))# regresa un objeto re.Match

#USO del $ Matches the end of string.

print(re.search(r'cake$', "Cake! Let's eat cake").group())


#USO Rangos

#[abc] - Matches a or b or c.
#[a-zA-Z0-9] - Matches any letter from (a to z) or (A to Z) or (0 to 9).

#USO Rango Negado 

#[^A-Za-z] Match any character that is not in the set. osea hace match con numero espacios y caracteres especiales 


print(re.search(r'[0-6]', 'Number: 5').group())

print(re.search(r'Number: [^5]', 'Number: 0').group())

print(re.search(r'Number: [^5]', 'Number: 5'))# no regresa nada NONE 

#USO DE \ - Backslash

#(Scenario 1)
#If the character following the backslash is a recognized escape character, then the special meaning of the term is taken 

## (Scenario 1) This treats '\s' as an escape character, '\s' defines a space
print(re.search(r'Not a\sregular character', 'Not a regular character').group())

#'Not a regular character'

## (Scenario 2) '\' is treated as an ordinary character, because '\r' is not a recognized escape character
print("AQUI")
print(re.search(r'Just a \regular character', 'Just a \regular character').group())
#'Just a \regular character' si lo hace pero bash interpreta el r como retorno de carro


## (Scenario 3) '\s' is escaped using an extra `\` so its interpreted as a literal string '\s'
print(re.search(r'Just a \\sregular character', 'Just a \sregular character').group())

#PREDEFINED There is a predefined set of special sequences that begin with '\'

#\w - Lowercase 'w'. Matches any single letter, digit, or underscore.
#\W - Uppercase 'W'. Matches any character not part of \w (lowercase w).


print("Lowercase w:", re.search(r'Co\wk\we', 'Cookie').group())



## Matches any character except single letter, digit or underscore
print("Uppercase W:", re.search(r'C\Wke', 'C@ke').group())

print("Uppercase W:", re.search(r'C\Wke', 'C#ke').group())

## Uppercase W won't match single letter, digit
print("Uppercase W won't match, and return:", re.search(r'Co\Wk\We', 'Cookie'))


#\s - Lowercase 's'. Matches a single whitespace character like: space, newline, tab, return.
#\S - Uppercase 'S'. Matches any character not part of \s (lowercase s).

print("Lowercase s:", re.search(r'Eat\scake', 'Eat cake').group())
print("Uppercase S:", re.search(r'cook\Se', "Let's eat cookie").group())

# minusculas es los caracteres y mayuscula son las negaciones ejemplo \w y \W

# Example for \d
print("How many cookies do you want? ", re.search(r'\d+', '100 cookies').group())


#\t - Lowercase t. Matches tab.
#\n - Lowercase n. Matches newline.
#\r - Lowercase r. Matches return.
#\A - Uppercase a. Matches only at the start of the string. Works across multiple lines as well.
#\Z - Uppercase z. Matches only at the end of the string.
#TIP: ^ and \A are effectively the same, and so are $ and \Z. Except when dealing with MULTILINE mode. Learn more about it in the flags section.




#https://www.datacamp.com/community/tutorials/python-regular-expression-tutorial?utm_source=adwords_ppc&utm_medium=cpc&utm_campaignid=14989519638&utm_adgroupid=127836677279&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=332602034364&utm_targetid=aud-392016246653:dsa-473406579035&utm_loc_interest_ms=&utm_loc_physical_ms=1010043&gclid=CjwKCAiAm7OMBhAQEiwArvGi3MAXp9mzWh6yMYPjmp3DonczlROjyDPYZQNLjJJnSzNR-_AGR_GNnBoC3L4QAvD_BwE#table



#USO Repetitions The + and * qualifiers are said to be greedy


#+ - Checks if the preceding character appears one or more times starting from that position.

#re.search(r'Co+kie', 'Cooookie').group() # 'Cooookie'


#* - Checks if the preceding character appears zero or more times starting from that position.

# re.search(r'Ca*o*kie', 'Cookie').group()#'Cookie'

#? - Checks if the preceding character appears exactly zero or one time starting from that position.

## Checks for exactly zero or one occurrence of a or o or both in the given sequence

#re.search(r'Colou?r', 'Color').group()#'Color'


#NUMERO DE REPETICIONES ( como una IP de 0 a 255) {1,3}

#{x} - Repeat exactly x number of times.
#{x,} - Repeat at least x times or more.
#{x, y} - Repeat at least x times but no more than y times.



print("REPETICION")
print(re.search(r'\d{9,10}', '098765432').group())

#USO GRUPOS trabajaste con grupos con la funcion group() 


statement = 'Please contact us at: support@datacamp.com'
match = re.search(r'([\w\.-]+)@([\w\.-]+)', statement)
if statement:
  print("Email address:", match.group()) # The whole matched text
  print("Username:", match.group(1)) # The username (group 1)
  print("Host:", match.group(2)) # The host (group 2)



#USO de Nombres en los grupos (?P<name> todo lo demas de la regex)



#The square brackets [] denote a character class. A character class will match any of the things inside it.
#
#\w is a special class called "word characters". It is shorthand for [a-zA-Z0-9_], so it will match:
#
#a-z (all lowercase letters)
#A-Z (all uppercase letters)
#0-9 (all digits)
#_ (an underscore)
#The class you are asking about, [\w-], is a class consisting of \w and -. So it will match the above list, plus hyphens (-).
#
#Exactly as written, [\w-], this regex would match a single character, as long as it's in the above list, or is a dash.


statement = 'Please contact us at: support@datacamp.com'
match = re.search(r'(?P<email>(?P<username>[\w\.-]+)@(?P<host>[\w\.-]+))', statement)
if statement:
  print("Email address:", match.group('email'))
  print("Username:", match.group('username'))
  print("Host:", match.group('host'))

#TIP: You can always access the named groups using numbers instead of the name. But as the number of groups increases,
# it gets harder to handle them using numbers alone. 
#So, always make it a habit to use named groups instead


#USO Emparejamiento codicioso versus no codicioso Greedy vs. Non-Greedy Matching


pattern = "cookie"
sequence = "Cake and cookie"

heading  = r'<h1>TITLEakshklahdlkjsafd </h1>'
print(re.match(r'<.*>', heading).group())
print("ATENCION")

print(re.match(r'(?P<email>(?P<username><.*?>)(?P<text>.*)(?P<username2><.*?>))', heading).group())
print(re.match(r'(?P<email>(?P<username><.*?>)(?P<text>.*)(?P<username2><.*?>))', heading).group(3))#LOGRO solo lo de adentro del <h1> esto </h1>

#'<h1>TITLE</h1>'
# *?  Adding ? after the qualifier makes it perform the match in a non-greedy or minimal fashion; 
#That is, as few characters as possible will be matched. When you run <.*>, you will only get a match with <h1>.

heading  = r'<h1>TITLE</h1>'
re.match(r'<.*?>', heading).group()

#'<h1>'

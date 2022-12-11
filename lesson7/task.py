this_is_string = 'Hi there'
the_same_string = 'Hi there'

print(this_is_string == the_same_string)


text = """
Привіт мене звати Саша 
Я займаюсь програмуванням протягом 2-х років
"""

# \n \f \r \t \v

jingle_bells = "Jingle bells, jingle bells\nJingle bells, jingle bells"
print(jingle_bells)
start = 0
end = 7
print(this_is_string.find('er', start, end))
print(this_is_string.find('q'))

s = 'I am learning strings in Python. Some new methods got how. I have some skills'
sentences = s.split('. ')
print(sentences[0])
print(sentences[1])
print(sentences[2])
text = '. '.join(sentences)
print(text)


clean_string = '   hello   '.strip()
print('   hello   ')
print(clean_string)

print('TestHook'.removeprefix('Test'))
print('TestHook'.removeprefix('Hook'))

print('TestHook'.removesuffix('Hook'))
print('TestHook'.removesuffix('Test'))

dogs_text = 'All dogs back like dogs'
cats_text = dogs_text.replace('dogs', 'cats')
print(cats_text)

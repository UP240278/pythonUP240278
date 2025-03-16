#01 Find the length of the set it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))

#02 Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

#03 Insert multiple IT companies at once to the set it_companies
it_companies.update(['Instagram', 'LinkedIn'])
print(it_companies)

#04 Remove one of the companies from the set it_companies
it_companies.remove('IBM')

#05 What is the difference between remove and discard
#Si no se encuentra el elemento, el método remove() generará errores, 
#por lo que es bueno verificar si el elemento existe en el conjunto dado.
#Sin embargo, el método discard() no genera ningún error.
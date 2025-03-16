#01 Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age = [22, 19, 24, 25, 26, 24, 25, 24]
age_set=set(age)
if len(age)==len(age_set):
    print('Las longiudes son iguales.')
else:
    print('Las longitudes son diferentes.')

#02 Explain the difference between the following data types: string, list, tuple and set
#Un string es una secuencia inmutable de caracteres utilizada para almacenar texto,
#mientras que una lista es una colección ordenada y mutable que permite elementos duplicados de cualquier tipo de dato. 
#Por otro lado, una tupla es como una lista, pero es inmutable y su contenido no puede cambiarse,
#aunque también mantiene el orden y permite duplicados. Finalmente,
#un conjunto (o set) es una colección desordenada de elementos únicos,
#que es mutable en cuanto a añadir o eliminar elementos, 
#pero no permite duplicados ni mantiene un orden fijo.

#03 I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence='I am a teacher and I love to inspire and teach people'
oracion=set(sentence.split())
print(len(oracion))
import timeit

SETUP_CODE = """
from horspool import naive_search, search, shift
roman_file = open("le_meilleur_des_mondes.txt","r",encoding='utf8')
roman = roman_file.read()
data = roman.replace('\\n', ' ')
pattern = "Personne n’aurait cru, dans les dernières années du dix-neuvième siècle,"
"""

TEST_NAIVE_CODE = """
naive_search(data, pattern, case_sensitive=False)"""

TEST_HORSPOOL_CODE = """
search(data, pattern, case_sensitive=False)"""

number = 10
naive_delay = timeit.timeit(setup=SETUP_CODE,
                          stmt=TEST_NAIVE_CODE,
                          number=number)


horspool_delay = timeit.timeit(setup=SETUP_CODE,
                          stmt=TEST_HORSPOOL_CODE,
                          number=number)

print(f'Naive search time: {naive_delay}')
print(f'Horspool search time: {horspool_delay}')
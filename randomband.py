import random

articles_list=("The","These","That", "This", "Those")
adj_list=("cool", "sick", "dope", "fun", "awesome")
nouns_list=("rabbit", "cow", "ducks", "dog", "snakes")

random_index= random.randint(0,4)
print(articles_list[random_index], adj_list[random_index], nouns_list[random_index])
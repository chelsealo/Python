import random

firstfive_list= ["Gabi has cool hair.", "Gabi plays soccer.", "Gabi can steam milk."]
seven_list= ["Rhae is in love with Harper.", "Rhae likes to eat cereal.", "Rhae likes to wrestle and run."]
secondfive_list= ["Sam gets lost at Bart.", "Sam has a sunburn.", "Sam likes to speak French."]

random_index= random.randint(0,2)
random_in= random.randint(0,2)
random_ind= random.randint(0,2)


print(firstfive_list[random_index], seven_list[random_in], secondfive_list[random_ind])
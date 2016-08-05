import random
adj_list= ["spicy", "zesty", "tangy", "creamy", "sweet", "sour", "salty", "peppery", "marinated", "tasty"]

cooked_list=["baked", "fried", "sauteed", "roasted", "seared", "broiled", "boiled", "grilled", "steamed", "barbecued"]

food_list=["chicken breast", "rib-eye steak", "scallops", "lamb", "veal", "broccoli", "salmon", "turkey leg", "pork chop", "shrimp"]


random_index= random.randint(0,9)
print(adj_list[random_index], cooked_list[random_index], food_list[random_index])
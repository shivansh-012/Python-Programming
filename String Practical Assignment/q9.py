string ="Everyone loves data science"
listy = [word[::-1] for word in string.split()]
res_list = " ".join(listy)
print(res_list)
def add_tags(tag,word):
    result = f"<{tag}>{word}</{tag}>"
    return result

res1 = add_tags("i","Python")
res2 = add_tags("b","Python Tutorial")

print(res1)
print(res2)

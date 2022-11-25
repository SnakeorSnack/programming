from collections import Counter

massive ='маша маша леша кошка суп картошка блоша пирог чипсики чипсики маша леша чипсики шерсть нитки иголки чипсики чипсики чипсики'


# split() без аргументов делит по пробельным символам, в том числе и по переносам строк
massive_split = massive.split()
# один проход с подсчетом в словаре - примерно O(n)
x = Counter(massive_split)
# нахождение максимума - О(n)
max_encounters = max(x.values())
# нахождение минимального из максимально частых слов O(n*m) (m - количество самых частых слов)
most_common_word = min(word for word, count in x.items() if count == max_encounters)
print(most_common_word)






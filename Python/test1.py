from collections import Counter

massive ='маша маша леша кошка суп картошка блоша пирог чипсики чипсики маша леша чипсики шерсть нитки иголки чипсики чипсики чипсики'

massive_split = massive.split()
x = Counter(massive_split)
max_encounters = max(x.values())
most_common_word = min(word for word, count in x.items() if count == max_encounters)
print(most_common_word)













# (myLine = text.split()  # split() без аргументов делит по пробельным символам, в том числе и по переносам строк
# d = Counter(myLine)  # один проход с подсчетом в словаре - примерно O(n)
# max_encounters = max(d.values())  # нахождение максимума - О(n)
# most_common_word = min(word for word, count in d.items() if count == max_encounters)  # нахождение минимального из максимально частых слов O(n*m) (m - количество самых частых слов)
# print(most_common_word) 
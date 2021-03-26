{% tabs %}
{% tab title='KT_prva.md' %}

* Output the lexicographically smallest word with <1 character in the crossword.

{% endtab %}
{% tab title='KT_prva.py' %}

```py
n, m = map(int, input().split())
G = []
for _ in range(n):
  G.append(input() + "#")
G.append('#' * (m + 1))
words = []
for i in range(n + 1):
  word = ""
  for j in range(m + 1):
    if G[i][j] == '#':
      if len(word) > 1:
        words.append(word)
      word = ""
    else:
      word += G[i][j]

for j in range(m + 1):
  word = ""
  for i in range(n + 1):
    if G[i][j] == '#':
      if len(word) > 1:
        words.append(word)
      word = ""
    else:
      word += G[i][j]
print(sorted(words)[0])
```

{% endtab %}
{% endtabs %}
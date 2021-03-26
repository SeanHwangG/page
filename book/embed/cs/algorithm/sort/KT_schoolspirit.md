{% tabs %}
{% tab title='KT_schoolspirit.md' %}
$$ \frac{1}{5} \sum_{i=0}^{n-1} s_{i} \cdot\left(\frac{4}{5}\right)^{i} $$
* What is the average value of gi over all all n students?

{% endtab %}
{% tab title='KT_schoolspirit.py' %}

```py
n_team = int(input())
li = list(sorted([int(input()) for _ in range(n_team)], reverse=True))
score = 0
for i, n in enumerate(li):
  score += n * (0.8 ** i)
print(score / 5)
score = 0
for i, n in enumerate(li):
  up = i
  stay = (n_team - 1 - i)
  score += n * (up * (0.8 ** (i - 1)) + stay * (0.8 ** i))
print(score / 5 / n_team)
```

{% endtab %}
{% endtabs %}
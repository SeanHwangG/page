{% tabs %}
{% tab title='KT_symmetricorder.md' %}

* Print name in symetric order respect to name length

{% endtab %}
{% tab title='KT_symmetricorder.py' %}

```py
si = 0
while True:
  si += 1
  n = int(input())

  if n == 0:
    break

  print(f"SET {si}")
  li = [input() for _ in range(n)]
  for i in range(0, n, 2):
    print(li[i])
  for i in range(1, n, 2):
    print(li[i])
```

{% endtab %}
{% endtabs %}
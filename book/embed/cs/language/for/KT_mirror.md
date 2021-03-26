{% tabs %}
{% tab title='KT_mirror.md' %}

* Print mirrored string

{% endtab %}
{% tab title='KT_mirror.py' %}

```py
n_test = int(input())
for test in range(1, n_test + 1):
  R, C = map(int, input().split())
  G = [input() for _ in range(R)]
  print(f"Test {test}")
  for st in reversed(G):
    print("".join(reversed(st)))
```

{% endtab %}
{% endtabs %}
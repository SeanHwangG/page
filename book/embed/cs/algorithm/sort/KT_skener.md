{% tabs %}
{% tab title='KT_skener.md' %}

* print magnified picture with r, c factor

{% endtab %}
{% tab title='KT_skener.py' %}

```py
N, M, a, b = map(int, input().split())
G = [input() for _ in range(N)]
for i in range(N):
  for _ in range(a):
    for j in range(M):
      for _ in range(b):
        print(G[i][j], end='')
    print()
```

{% endtab %}
{% endtabs %}
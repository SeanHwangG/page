{% tabs %}
{% tab title='KT_dicecup.md' %}

* 두 주사위에 a와 b개의 면이 있다. 이때 두 주사위를 굴렸을 때 가장 높은 확률로 나오는 합을 출력하라.

{% endtab %}
{% tab title='KT_dicecup.py' %}

```py
a, b = map(int, input().split())
for i in range(min(a, b) + 1, max(a, b) + 2):
  print(i)
```

{% endtab %}
{% endtabs %}
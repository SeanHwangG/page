{% tabs %}
{% tab title='KT_detaileddifferences.md' %}

* 두 문자가 주어질 때 그 문자를 출력하고
* 같은 자리는 . 다른 자리는 *를 아래에 출력하라.

{% endtab %}
{% tab title='KT_detaileddifferences.py' %}

```py
N = int(input())
for _ in range(N):
  st1 = input()
  st2 = input()
  print(st1)
  print(st2)
  for c1, c2 in zip(st1, st2):
    if c1 == c2:
      print('.', end='')
    else:
      print('*', end='')
  print()
```

{% endtab %}
{% endtabs %}
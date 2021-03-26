{% tabs %}
{% tab title='BJ_5063.md' %}

* r is the expected revenue if you do not advertise, e, is the expected revenue if you do advertise, c, is the cost of advertising

{% endtab %}
{% tab title='BJ_5063.py' %}

```py
for _ in range(int(input())):
  r, e, c = map(int, input().split())
  if r > e - c:
    print('do not advertise')
  elif r == e - c:
    print('does not matter')
  else:
    print('advertise')
```

{% endtab %}
{% endtabs %}
{% tabs %}
{% tab title='KT_apaxiaaans.md' %}

* 문자를 받아서, 연속된 문자는 한번만 출력하라.

{% endtab %}
{% tab title='KT_apaxiaaans.py' %}

```py
st = input()
for i in range(len(st)):
  if i == 0 or st[i - 1] != st[i]:
    print(st[i], end='')
```

{% endtab %}
{% endtabs %}
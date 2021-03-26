{% tabs %}
{% tab title='KT_modulo.md' %}

* 10개의 수가 주어지는데 이 때 42의 나머지의 가짓수를 구하라.

{% endtab %}
{% tab title='KT_modulo.py' %}

```py
st = set()
for i in range(10):
  st.add(int(input()) % 42)
print(len(st))
```

{% endtab %}
{% endtabs %}
{% tabs %}
{% tab title='KT_tri.md' %}

* a, b, c 가 주어질 때 사칙연산으로 a ? b = c가 되거나 a = b ? c가 되는 경우중 한가지를 출력하라

{% endtab %}
{% tab title='KT_tri.py' %}

```py
a, b, c = input().split()
for op in ['+', '-', '*', '/']:
  if eval(a + op + b) == int(c):
    print(a + op + b + '=' + c)
    break
  if int(a) == eval(b + op + c):
    print(a + '=' + b + op + c)
    break
```

{% endtab %}
{% endtabs %}
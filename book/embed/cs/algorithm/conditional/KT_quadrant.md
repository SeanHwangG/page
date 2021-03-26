{% tabs %}
{% tab title='KT_quadrant.md' %}

* a, b는 0이 아닌 정수이다.
* a, b가 주어졌을때 몇 사분면(Quadrant)에 있는지 구하여라.

{% endtab %}
{% tab title='KT_quadrant.py' %}

```py
a = int(input())
b = int(input())
if a > 0 and b > 0:
    print(1)
elif a < 0 and b > 0:
    print(2)
elif a < 0 and b < 0:
    print(3)
else:
    print(4)
```

{% endtab %}
{% endtabs %}
{% tabs %}
{% tab title='KT_numberfun.md' %}

* a, b, c가 주어 질 때, a, b와 +, -, *, / 로 c를 만들 수 있으면 Possible 불가능 하면 Impossible을 출력하라

{% endtab %}
{% tab title='KT_numberfun.py' %}

```py
n_test = int(input())
for _ in range(n_test):
  a, b, c = map(int, input().split())
  if a + b == c or a - b == c or b - a == c or a * b == c or a / b == c or b / a == c:
    print("Possible")
  else:
    print("Impossible")
```

{% endtab %}
{% endtabs %}
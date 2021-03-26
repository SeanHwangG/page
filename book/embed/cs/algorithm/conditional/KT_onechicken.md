{% tabs %}
{% tab title='KT_onechicken.md' %}

* a, b가 주어진다.
* a 가 b 보다 크면 Dr. Chaz needs a - b more pieces of chicken!
* b 가 a 보다 크면 Dr. Chaz will have b - a pieces of chicken left over! 를 출력하라. (이 때 차이가 1이면 s는 pieces를 piece로 대체한다.)

{% endtab %}
{% tab title='KT_onechicken.py' %}

```py
a, b = map(int, input().split())
if a < b:
  print(f"Dr. Chaz will have {b - a} piece{'' if b - a == 1 else 's'} of chicken left over!")
else:
  print(f"Dr. Chaz needs {a - b} more piece{'' if a - b == 1 else 's'} of chicken!")
```

{% endtab %}
{% endtabs %}
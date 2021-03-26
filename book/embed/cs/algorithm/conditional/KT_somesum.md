{% tabs %}
{% tab title='KT_somesum.md' %}

* 1부터 100까지 연속된 n개의 수를 뽑는다.
* 이 때 수의 합이 짝수이면 Even 홀수이면, Odd, 둘다 가능하면 Either을 출력하라.

{% endtab %}
{% tab title='KT_somesum.py' %}

```py
n = int(input())
if n % 4 == 0:
    print('Even')
elif n % 2 == 0:
    print('Odd')
else:
    print('Either')
```

{% endtab %}
{% endtabs %}
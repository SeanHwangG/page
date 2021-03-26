{% tabs %}
{% tab title='KT_judgingmoose.md' %}

* 왼쪽과 오른쪽의 뿔의 개수가 주어진다.
* 왼쪽과 오른쪽의 뿔의 개수가 같을 때, Even 총_뿔수
* 다를 시, Odd 더_많은_뿔수 * 2
* 뿔이 하나도 없을 시, Not a Moose를 출력한다.

{% endtab %}
{% tab title='KT_judgingmoose.py' %}

```py
a, b = map(int, input().split())
if a == b == 0:
    print("not a moose")
elif a == b:
    print(f"Even {a * 2}")
else:
    print(f"Odd {max(a, b) * 2}")
```

{% endtab %}
{% endtabs %}
{% tabs %}
{% tab title='KT_savingforretirement.md' %}

* Alice 는 은퇴 후에 Bob 보다 돈이 많았으면 좋겠다.
* 첫줄에 Bob이 일의 시작 나이, 은퇴 나이, 연봉, Alice가 일을 시작하는 나이, Alice의 연봉이 주어진다.
* 이 때 Alice가 은퇴를 해야되는 나이를 출력하라.

{% endtab %}
{% tab title='KT_savingforretirement.py' %}

```py
a, b, c, d, e = map(int, input().split())
print(d + (b - a) * c // e + 1)
```

{% endtab %}
{% endtabs %}
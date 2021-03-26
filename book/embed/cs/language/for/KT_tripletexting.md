{% tabs %}
{% tab title='KT_tripletexting.md' %}

* 띄어쓰기 없이 같은 문자를 3번 보내는데 그중 하나는 오타이다. 원래 보내려는 문자를 출력하라.

{% endtab %}
{% tab title='KT_tripletexting.py' %}

```py
s = input()
chunk = len(s) // 3
a = s[:chunk]
b = s[chunk:chunk * 2]
c = s[chunk * 2:]
if b == c:
    print(b)
else:
    print(a)
```

{% endtab %}
{% endtabs %}
{% tabs %}
{% tab title='KT_aaah.md' %}

* 두 문자가 각 줄에 주어진다
* 이 때 첫 문자가 길면 no 두번째 길이가 같거나, 두번째 문자가 길 때는 go를 출력하라.

{% endtab %}
{% tab title='KT_aaah.py' %}

```py
a = input()
b = input()
if len(b) > len(a):
    print("no")
else:
    print('go')
```

{% endtab %}
{% endtabs %}
{% tabs %}
{% tab title='KT_avion.md' %}

* 5개 줄에 차량 문자가 주어진다.
* 이 문자에 'FBI'가 포함 되어 있는 라인 숫자를 출력하라.
* 하나도 없을 시 'HE GOT AWAY'를 출력하라.

{% endtab %}
{% tab title='KT_avion.py' %}

```py
seen = False
for i in range(1, 6):
    st = input()
    if 'FBI' in st:
        print(i, end=' ')
        seen = True

if not seen:
    print("HE GOT AWAY!")
```

{% endtab %}
{% endtabs %}
{% tabs %}
{% tab title='KT_quickbrownfox.md' %}

* N개의 문장에 영어 알파벳 a-z까지 없는 알파벳을 출력하라. 모두 있을 시 pangram을 출력하라.

{% endtab %}
{% tab title='KT_quickbrownfox.py' %}

```py
N = int(input())
for _ in range(N):
    sentence = input().lower()
    missings = []
    for ch in 'abcdefghijklmnopqrstuvwxyz':
        if ch not in sentence:
            missings.append(ch)
    if len(missings) == 0:
        print("pangram")
    else:
        print("missing " + "".join(missings))
```

{% endtab %}
{% endtabs %}
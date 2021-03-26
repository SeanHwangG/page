{% tabs %}
{% tab title='KT_nodup.md' %}

* 문장이 주어지는데, 문장에서 같은 단어가 두번 이상 등장하면 no 모든 단어가 한번 등장하면 yes를 출력하라.

{% endtab %}
{% tab title='KT_nodup.py' %}

```py
li = input().split()
print("yes" if len(set(li)) == len(li) else "no")
```

{% endtab %}
{% endtabs %}
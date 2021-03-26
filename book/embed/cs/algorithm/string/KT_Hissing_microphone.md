{% tabs %}
{% tab title='KT_Hissing_microphone.md' %}

* input에 ss, 즉 연속된 s가 있을 시 'hiss' 그렇지 않으면 'no hiss'를 출력한다.

{% endtab %}
{% tab title='KT_Hissing_microphone.py' %}

```py
s = input()
if s.find('ss') == -1:
    print('no hiss')
else:
    print('hiss')
```

{% endtab %}
{% endtabs %}
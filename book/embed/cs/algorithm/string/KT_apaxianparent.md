{% tabs %}
{% tab title='KT_apaxianparent.md' %}

* 문자 Y, P가 주어진다. print
  * Y가 ex로 끝날 시 Y + P
  * Y가 e로 끝날 시 Y + 'e' + P
  * Y가 aiou 로 끝날 시 그 모음을 제거하고 Y + 'ex' + P
  * 위에 어느 것도 아닐 시 Y + 'ex' + P

{% endtab %}
{% tab title='KT_apaxianparent.py' %}

```py
a, b = input().split()
if a[-1] == 'e':
  print(a, 'x', b, sep='')
elif a[-2:] == 'ex':
  print(a, b, sep='')
elif a[-1] in 'aiou':
  print(a[:-1], 'ex', b, sep='')
else:
  print(a, 'ex', b, sep='')
```

{% endtab %}
{% endtabs %}
{% tabs %}
{% tab title='KT_reverserot.md' %}

* 숫자 a, 문자 b가 매 줄마다 주어진다.
* 이 때 문자를 뒤집어서 a만큼 회전한 문자를 출력한다. (단 Z → _ → . → A 으로 순환된다)
* 마지막 줄에는 0만 나온다.

{% endtab %}
{% tab title='KT_reverserot.py' %}

```py
alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
while True:
  raw = input()
  if raw == '0':
    break
  shift, st = raw.split()
  shift = int(shift)
  for ch in reversed(st):
    print(alp[(alp.find(ch) + shift) % len(alp)], end='')
  print()
```

{% endtab %}
{% endtabs %}
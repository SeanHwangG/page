{% tabs %}
{% tab title='KT_securedoors.md' %}

* 첫줄에 N이 주어지고 그 다음 N줄에 방명록이 주어진다.
* 방명록은 입장 이름 / 퇴장 이름과 같은 형식으로 주어지는데,
* 이 때 퇴장 전 입장을 여러번 했거나 입장 하지 않았는데 퇴장 한 경우는 (ANOMALY)를 출력한다.

{% endtab %}
{% tab title='KT_securedoors.py' %}

```py
N = int(input())
se = set()
for _ in range(N):
  typ, name = input().split()
  if typ == 'entry':
    if name in se:
      print(name, 'entered', '(ANOMALY)')
    else:
      print(name, 'entered')
      se.add(name)
  else:
    if name in se:
      print(name, 'exited')
      se.remove(name)
    else:
      print(name, 'exited', ('(ANOMALY)' if name not in se else ''))
```

{% endtab %}
{% endtabs %}
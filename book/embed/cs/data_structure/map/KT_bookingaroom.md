{% tabs %}
{% tab title='KT_bookingaroom.md' %}

* 첫 줄에 a, b가 주어진다. 이 때 a는 총 방의 개수이다. (1...n)
* 다음 b 줄에 예약된 방 번호가 주어진다.
* 이때 아무 빈 방을 출력하라.
* 빈 방이 없을 시 too late을 출력하라.

{% endtab %}
{% tab title='KT_bookingaroom.py' %}

```py
a, b = map(int, input().split())
se = set()
for _ in range(b):
  se.add(int(input()))
for i in range(1, a + 1):
  if i not in se:
    print(i)
    break
else:
  print("too late")
```

{% endtab %}
{% endtabs %}
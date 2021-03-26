{% tabs %}
{% tab title='KT_hangingout.md' %}

* 첫줄에 테라스의 최대 인원 L과 x개의 이벤트가 주어진다.
* 각 x줄의 이벤트에는 ‘enter’/‘leave’ 사람수 가 주어지는데 최대 인원 이상으로는 들어올 수 없다.
* 이때 사람이 많아 거절 당한 이벤트의 개수를 출력하라. (거절 당할 시 enter 해도 추가가 되지 않음)

{% endtab %}
{% tab title='KT_hangingout.py' %}

```py
max_n, n_line = map(int, input().split())
cur, ret = 0, 0
for _ in range(n_line):
  st, n = input().split()
  n = int(n)
  if st == 'enter':
    if n + cur <= max_n:
      cur += n
    else:
      ret += 1
  else:
    cur -= n
print(ret)
```

{% endtab %}
{% endtabs %}
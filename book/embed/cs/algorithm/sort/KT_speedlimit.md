{% tabs %}
{% tab title='KT_speedlimit.md' %}

* 첫줄에 N 그 다음 N개의 줄에 speed / hour 와 달린 시간이 나온다. 이때 평균 속력을 출력하라.

{% endtab %}
{% tab title='KT_speedlimit.py' %}

```py
n_line = int(input())
def total_miles(speeds, times):
  total_miles = 0
  prev_time = 0
  for speed, time in zip(speeds, times):
    total_miles += (time - prev_time) * speed
    prev_time = time
  return total_miles

while n_line != -1:
  speeds, times = [], []
  for _ in range(n_line):
    speed, time = map(int, input().split())
    speeds.append(speed)
    times.append(time)
  print(f'{total_miles(speeds, times)} miles')
  n_line = int(input())
```

{% endtab %}
{% endtabs %}
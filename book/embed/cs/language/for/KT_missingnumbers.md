{% tabs %}
{% tab title='KT_missingnumbers.md' %}

* 첫 줄에 n이 주어진다.
* 다음 n줄에 숫자가 주어지는데, 이 때 띄어 넘은 수를 모든 수를 출력하라.
* 만약 1, 2, 3 과 같이 띄어 넘는 숫자가 없을 시는 good job을 출력하라.

{% endtab %}
{% tab title='KT_missingnumbers.py' %}

```py
n = int(input())
gap = False
prev = 0
for i in range(n):
  a = int(input())
  for j in range(prev + 1, a):
    print(j)
    gap = True
  prev = a
if not gap:
  print('good job')
```

{% endtab %}
{% endtabs %}
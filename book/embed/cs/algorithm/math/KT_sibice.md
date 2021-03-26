{% tabs %}
{% tab title='KT_sibice.md' %}

* 첫 줄에 N, w, h이 주어진다.
* 다음 N줄에 성냥의 길이가 주어지는데, 가로 세로가 w, h 인 상자에 들어가면 DA, 들어가지 않으면 DE를 출력하라.

{% endtab %}
{% tab title='KT_sibice.py' %}

```py
n_match, w, h = map(int, input().split())
mx = (w ** 2 + h ** 2) ** 0.5
for _ in range(n_match):
  x = int(input())
  if x <= mx:
    print('DA')
  else:
    print('NE')
```

{% endtab %}
{% endtabs %}
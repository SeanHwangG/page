{% tabs %}
{% tab title='KT_whatdoesthefoxsay.md' %}

* 한 테스트 마다, 띄어쓰기로 나누어진 울음 소리 / animal says ~ / what does the fox say? 가 나온다.
* 이때 다른 동물이 내지 않은 울음소리를 모두 출력하라.

{% endtab %}
{% tab title='KT_whatdoesthefoxsay.py' %}

```py
n_test = int(input())
for _ in range(n_test):
  li = input().split()
  s = input()
  ignore = set()
  while s != 'what does the fox say?':
    ignore.add(s.split()[-1])
    s = input()
  for e in li:
    if e not in ignore:
      print(e, end=' ')
```

{% endtab %}
{% endtabs %}
{% tabs %}
{% tab title='KT_Heartrate.md' %}

* 첫줄에 N이 주어지고 N줄에 b,p가 차례로 주어진다
* ABPM최솟값, BPM값, ABPM최댓값을 한 줄에 출력하라. (BPM은 60b/p로 계산)

{% endtab %}
{% tab title='KT_Heartrate.py' %}

```py
n_test = int(input())
for _ in range(n_test):
  beat, sec = map(float, input().split())
  print((beat - 1) / sec * 60, beat / sec * 60, (beat + 1) / sec * 60)
```

{% endtab %}
{% endtabs %}
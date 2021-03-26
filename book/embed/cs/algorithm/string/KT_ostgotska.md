{% tabs %}
{% tab title='KT_ostgotska.md' %}

* 문장에 ae가 포함 된 단어가 40% 이상이면 스웨덴 어이다.
* 첫 줄에 문장이 주어질 때 스웨덴 어이면 dae ae ju traeligt va 아니면 haer talar vi rikssvenska 을 출력하라.

{% endtab %}
{% tab title='KT_ostgotska.py' %}

```py
li = input().split()
n = len(li) * 0.4
count = 0
for st in li:
  if "ae" in st:
    count += 1
if n <= count:
  print("dae ae ju traeligt va")
else:
  print("haer talar vi rikssvenska")
```

{% endtab %}
{% endtabs %}
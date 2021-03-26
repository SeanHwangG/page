{% tabs %}
{% tab title='KT_provincesandgold.md' %}

* 골드는 3, 실버는 2, 쿠퍼는 1의 값어치를 한다.
* 한 턴에 victory 카드와 treasure 카드 중 하나를 선택 할 수 있는데 비용은 아래와 같다.
* Province (costs 8)
* Duchy (costs 5)
* Estate (costs 2)
* Gold (costs 6)
* Silver (costs 3)
* Copper (costs 0)
* 골드 실버 쿠퍼의 개수가 주어질 때 고를 수 있는 최고의 victory or treasure 카드를 출력하라.

{% endtab %}
{% tab title='KT_provincesandgold.py' %}

```py
g, s, c = map(int, input().split())
tot = g * 3 + s * 2 + c
if tot >= 8:
  print("Province or Gold")
elif tot >= 6:
  print("Duchy or Gold")
elif tot >= 5:
  print("Duchy or Silver")
elif tot >= 3:
  print("Estate or Silver")
elif tot >= 2:
  print("Estate or Copper")
else:
  print("Copper")
```

{% endtab %}
{% endtabs %}
{% tabs %}
{% tab title='KT_twostones.md' %}

* a개의 돌이 다음과 같이 1열로 나열되어 있다. 1 2 3 … a
* Alice 와 Bob 이 번갈아 가며 2개의 연속된 번호의 돌을 가져간다.
* 더 이상 가져갈 수 있는 돌이 없을때, 남은 돌의 개수가 홀수이면 Alice가 이기고 짝수면 Bob이 이긴다.
* 예를들어 돌 1 2 3 4 로 시작해 Alice 가 2, 3 을 가져가면 Bob은 더 이상 가져갈 수 있는 연속된 돌이 없고,
* 남은 돌의 개수는 1, 4, 총 2개이므로 Bob이 승리한다.
* Alice가 항상 먼저 시작 가져가고 두 명은 항상 최적의 수를 둔다.
* a가 주어질때 승자를 구하여라.

{% endtab %}
{% tab title='KT_twostones.py' %}

```py
a = int(input())
if a % 2 == 1:
  print("Alice")
else:
  print("Bob")
```

{% endtab %}
{% endtabs %}

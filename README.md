Для того, чтобы выигрывать в покер, Джон поставил камеру с распознаванием
карт сзади игрока. Камера распознает карты,
после чего программа определяет какая комбинация в покере у
игрока-соперника и присылает Джону на телефон сообщение с кодом комбинации.
А если у него одинаковые карты, значит он жульничает и об этом тоже надо сообщить.
Напишите эту программу.
####Комбинации покера:
0-нет ни одной комбинации
1-one pair - две карты одного достоинства, например, 9s и 9h
2-two pair - две пары карт, например,  9s, 9h, 6c, 6h
3-three of a kind - три карты одного достоинства
4-straight - пять карт по порядку любых мастей, например, 6s, 7h, 8c, 9d, 10c
5-flush - пять карт одной масти, например, 6s, 8s, 11s, 13s, 7s
6-full house - одна тройка и одна пара, например, 9s, 9h, 6c, 6h, 6d
7-four of a kind - четыре карты одного достоинства
8-straight flush - любые пять карт  одной масти по порядку, например, 6s, 7s, 8s, 9s, 10s
####На входе:
card - массив из пяти строк - карт соперника в виде nnm,
где nn - вид карты (06, 07, 08, 09, 10, валет - 11, дама - 12, король - 13, туз - 14);
m - масть (пики (♠) - s, червы (♥) - h, бубны (♦) - d, трефы (♣) - c).
####На выходе:
число - номер комбинации покера у соперника
<p>
(-1 - 0-null, 1-one pair, 2-two pair, 3-three of a kind,
4-straight, 5-flush, 6-full house, 7-four of a kind, 8-straight flush)

####Пример:
card=["07s", "09s", "08s", "10s", "11s"]
<p>
get_result(card) → 8

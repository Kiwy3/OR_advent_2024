## Variables
$n = 100$ : number of cities<br>
$m = 955$ : number of connections <br>
$C = 73$ : fuel budget <br>
$s_{i} \text{ with } i \in \{0 \dots m\}$ : starting point of connection $i$ <br>
$d_{i} \text{ with } i \in \{0 \dots m\}$ : ending point of connection $i$  <br>
$d_{i} \text{ with } i \in \{0 \dots m\}$ : distance between cities $s_i$ and $e_i$ <br>
$c_{i}\text{ with } i \in \{0 \dots m\}$ : cost between between cities $s_i$ and $e_i$

## Parameters
$x_{i}\text{ with } i \in \{0 \dots m\}, \text{binary}$ : 1 if the path goes from $s_i$ to $e_i$, 0 else. <br>

## Objective function

$\text{min } z = \sum_i d_{i}*x_{i}$ : minimize the distance

## Constraints
(1) : $\sum_i c_{i}*x_i<=C $ : max cost <br>
(2) : $\sum_{i \in \{0 \dots m|s_i = 1 \}}x_i=1$ : starting from Madrid <br>
(3) : $\sum_{i \in \{0 \dots m|e_i = n \}}x_i=1$ : end at Copenhagen <br>
(4) : $\forall j \in \{1 \dots n\},   \sum_{i \in \{0 \dots m|s_i = j \}}x_i=\sum_{i \in \{0 \dots m|e_i = j \}}x_i$ : flow conservation <br>

## Variables
$n = 100$ : number of cities<br>
$C = 73$ : max cost
$i \in \{0 \dots n\}$ : index of cities. <br> 
$d_{i,j} \text{ with } i,j \in \{0 \dots n\} $ : distance between 2 cities <br>
$c_{i,j}\text{ with } i,j \in \{0 \dots n\} $ : cost between 2 cities

## Parameters
$x_{i,j}\text{ with } i,j \in \{0 \dots n\}, \text{binary} $ : 1 if the path goes from $i$ to $j$, 0 else. <br>

## Objective function

$ \text{min } z = \sum_i \sum_j d_{i,j}*x_{i,j} $

## Constraints
(1) : $ \forall j \in \{0 ,\dots, n-1\}, \sum_i  x_{ij}<=1  $ : max once to a cities <br>
(2) : $ \forall i \in \{1 ,\dots, n\}, \sum_j  x_{ij}<=1  $ : max once from a cities <br>
(3) : $ \sum_j x_{0,j} = \sum_i x_{i,100} = 1 $ : start from madrid and finish to copenhagen <br
(4) : $ \sum_i \sum_j  c_{ij}<=C  $ : max cost <br>


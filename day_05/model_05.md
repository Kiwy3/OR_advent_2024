## Variables
$n = 16$ : number of warehouses (index $i$)<br>
$m=50$ : number of clients (index $j$) <br>
$C_{i}\text{ with } i \in \{0 \dots n\}$ : Capacity of warehouse $i$.<br>
$f_{i}\text{ with } i \in \{0 \dots n\}$ : fixed cost of warehouse $i$.<br>
$d_{j}\text{ with } j \in \{0 \dots m\}$ : demand of client $j$.<br>
$c_{i,j}\text{ with } i \in \{0 \dots n\},j \in \{0 \dots m\} $ : cost for warehouse $i$ to handle client $j$ demand.<br>

## Parameters
$x_{i,j} \in \{0,1\}  \text{ with } i \in \{0 \dots n\},j \in \{0 \dots m\} $ : 1 if client $j$ demand is in warehouse $i$, 0 otherwise<br>
$y_{i}\in \{0,1\} \text{ with } i \in \{0 \dots n\}$ : 1 if warehouse $i$ is used, 0 otherwise.<br>

## Objective function
fixed cost : $\sum_i  f_{i}*y_{i}$ <br>
variable cost : $\sum_i \sum_j c_{i,j}*x_{i,j} $ <br><br>
$ \text{min } z =\sum_i  f_{i}*y_{i} + \sum_i \sum_j c_{i,j}*x_{i,j} $

## Constraints
(1) : $ \forall j \in \{0 ,\dots, m\}, \sum_i  x_{ij}=1  $ : each client $j$ is handled by a warehouse <br>
(2) : $\forall i \in \{1 ,\dots, n\}, \sum_j  d_{j}*x_{i,j} \leq C_i$ : respect max capacity of warehouses <br>
(3) : $\forall i \in \{1 ,\dots, n\},\sum_j x_{i,j} \leq y_i*m$ : link $y_i$ and $x_{ij}$.<br>


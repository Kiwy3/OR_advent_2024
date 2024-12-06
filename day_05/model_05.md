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
$\text{min } z =\sum_i  f_{i}*y_{i} + \sum_i \sum_j c_{i,j}*x_{i,j}$

## Constraints
(1) : $\forall j \in \{0 ,\dots, m\}, \sum_i  x_{ij}=1$ : each client $j$ is handled by a warehouse <br>
(2) : $\forall i \in \{1 ,\dots, n\}, \sum_j  d_{j}*x_{i,j} \leq C_i$ : respect max capacity of warehouses <br>
(3) : $\forall i \in \{1 ,\dots, n\},\sum_j x_{i,j} \leq y_i*m$ : link $y_i$ and $x_{ij}$.<br>


**Warning** : one client ask for 12.912 units, more than the maximum capacity of one warehouse. To deal with this, one client must be handled with multiple warehouses. 

## Corrected model

To change this : <br>
$x_{i,j}  \text{ with } i \in \{0 \dots n\},j \in \{0 \dots m\}$ : quantity of unit client $i$ is handled by warehouse $j$<br>

### Variables
$n = 16$ : number of warehouses (index $i$)<br>
$m=50$ : number of clients (index $j$) <br>
$C_{i}\text{ with } i \in \{0 \dots n\}$ : Capacity of warehouse $i$.<br>
$f_{i}\text{ with } i \in \{0 \dots n\}$ : fixed cost of warehouse $i$.<br>
$d_{j}\text{ with } j \in \{0 \dots m\}$ : demand of client $j$.<br>
$c_{i,j}\text{ with } i \in \{0 \dots n\},j \in \{0 \dots m\}$ : cost for warehouse $i$ to handle client $j$ demand.<br><br>
*new* : <br> 
$uc_{i,j} = c_{i,j}/d_j  \text{ with } i \in \{0 \dots n\},j \in \{0 \dots m\}$ : unit cost of one product of client $i$ in warehouse $j$. <br>
$M=\sum_j d_j$ : big M, scalar used to link $x_{ij}$ and $y_j$.

### Parameters
$x_{i,j}  \text{ with } i \in \{0 \dots n\},j \in \{0 \dots m\}$ : quantity of unit client $i$ is handled by warehouse $j$<br>
$y_{i}\in \{0,1\} \text{ with } i \in \{0 \dots n\}$ : 1 if warehouse $i$ is used, 0 otherwise.<br>

### Objective function
fixed cost : $\sum_i  f_{i}*y_{i}$ <br>
variable cost : $\sum_i \sum_j uc_{i,j}*x_{i,j} $ <br><br>
$\text{min } z =\sum_i  f_{i}*y_{i} + \sum_i \sum_j uc_{i,j}*x_{i,j}$

### Constraints
(1) : $\forall j \in \{0 ,\dots, m\}, \sum_i  x_{ij}=d_j$ : each client $j$  demand is handled  <br>
(2) : $\forall i \in \{1 ,\dots, n\}, \sum_j  x_{i,j} \leq C_i$ : respect max capacity of warehouses <br>
(3) : $\forall i \in \{1 ,\dots, n\},\sum_j x_{i,j} \leq y_i*M$ : link $y_i$ and $x_{ij}$.<br>
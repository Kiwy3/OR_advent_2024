## Variables
$n = 100$ : number of employes (index $i$)<br>
$m=100$ : number of tasks (index $j$) <br>
$c_{i,j}\text{ with } i \in \{0 \dots n\},j \in \{0 \dots m\}$ : cost for employees $i$ to do task $j$.

## Parameters
$x_{i,j} \in \{0,1\}  \text{ with } i \in \{0 \dots n\},j \in \{0 \dots m\}$ : 1 if the employee $i$ is doing task $j$ <br>

## Objective function

$\text{min } z = \sum_i \sum_j c_{i,j}*x_{i,j}$

## Constraints
(1) : $\forall j \in \{0 ,\dots, m\}, \sum_i  x_{ij}=1$ : one employee for each task <br>
(2) : $\forall i \in \{1 ,\dots, n\}, \sum_j  x_{ij}=1$ : one task for each employee <br>


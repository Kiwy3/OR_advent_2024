## Variables
$n = 4$ : number of classes (index $i$)<br>
$m=4$ : number of teachers (index $j$) <br>
$r=4$ : number of room (index $k$) <br>
$p=4$ : number of periods (index $t$) <br>
$o=120$ : number of requirements (index $l$) <br>
$q=20$ : number of subjects (index $s$) <br>

$M_{i,j,k}$ : number of times class $i$ needs to meet teacher $j$ in room $k$.<br>
$class_l,sub_l,room_l,times_l$ : requirements table <br>

## Parameters
$x_{i,j,k,t,s} \in \{0,1\}  \text{ with } i \in \{0 \dots n\},j \in \{0 \dots m\} $ : 1 if class $i$ meet teacher $j$ in room $k$ on period $t$ with subject $s$, 0 otherwise.<br>

## Objective function

## Constraints
(1) : $\forall i,j,k, \sum_t \sum_s x_{i,j,k,t,s}= M_{i,j,k}$ : respect matrix of global needs <br>
(2) : $\forall l, \sum_s \sum_t x_{i=class_l,j=teach_l,k=room_l} = times_l$ : respect requirements
(3) : $\forall i,t, \sum_j \sum_k \sum_s x_{i,j,k,t,s} \leq 1$ : max one attribution by class by period <br>
(4) : $\forall j,t, \sum_i \sum_k \sum_s x_{i,j,k,t,s} \leq 1$ : max one attribution by teacher by period <br>
(5) : $\forall k,t, \sum_i \sum_j \sum_s x_{i,j,k,t,s} \leq 1 $ : max one attribution by room by period <br>



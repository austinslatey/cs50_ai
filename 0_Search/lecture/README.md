* [Search](#search)
  * [Agent](#agent)
  * [Inital state](#inital-state)
  * [Actions](#actions)
  * [Transition model](#transition-model)
  * [State Space](#state-space)
  * [Goal Test](#goal-test)
  * [Path Cost](#path-cost)
* [Solving Search Problems](#solving-search-problems)
  * [Solution](#solution)
  * [Node](#node)
  * [Approach](#approach)
  * [Stack](#stack)
  * [Depth-first search](#depth-first-search)
  * [Breatdth-first search](#breatdth-first-search)
  * [Queue](#queue)
  * [Uninformed search](#uninformed-search)
  * [Informed search](#informed-search)
  * [Greedy best-first search(gfs)](#greedy-best-first-search-gfs)
  * [A* search](#a-search)
* [Adversarial search](#adversarial-search)
  * [Minimax](#minimax)
  * [Game](#game)
* [Optimizations](#optimizations)
  * [Alpha-Beta pruning](#alpha-beta-pruning)
  * [Depth-Limited Minima](#depth-limited-minima)
  * [Evalutation Function](#evalutation-function)

# Search

## Agent
entity that perceives its environment and acts upon that environment

## Inital state
the state in which the agent begins

## Actions
choices that can be made in a state

ACTIONS(s) returns the set of actions that can be executed in state (s)

## Transition model
A description of what state results from performing any applicable action in any state

RESULT(s, a) returns the state resulting from performing action (a) in state (s)

## State Space
The set of all states reachable from the inital state by any sequence of actions

## Goal Test
The condition that determines whether a given state is a goal state

Whether the current location of the agent is at the destination

```
// If condition met
    // solved
// Else
    // continue search
```

## Path Cost
A numerical cost associated with a given path

An application does not simply bring you to your goal; it does so while minimizing the path cost, finding the quickest path possible to achieve the goal state

# Solving Search Problems

## Solution
Sequential actions leading from the inital state to the goal state
    - Optimal Solution
    the lowest path cost amongst solutions

## Node
a data structure that keeps track of
- a state
- a parent (node that generated this node)
- an action (action applied to parent to get the node)
- a path cost (from inital state to node)

## Approach
Start with a frontier that contains the inital state
1.) Repeat:
- if the frontier is empty, then no solution
- remove the node from the frontier
- if the node contains the goal state, return the solution
- expand the node, add resulting nodes to the frontier
- add the node to the explored set
- expand the node, add resulting nodes to the frontier if they aren't already in the frontier or the expored set

```
                     (C) -> (E)
          (A) <-> (B) ^ --> (D) -> (F)
```

## Stack
last in, first out data type

```
                     (C) -> (E)
          (A) <-> (B) ^ --> (D) -> (F)
```

## Depth-first search
search algorithm that always expands the deepest node in the frontier

## Breatdth-first search
search algorithm that always expands the shallowest node in the frontier

## Queue
first in, last out data type

```
                     (C) -> (E)
          (A) <-> (B) ^ --> (D) -> (F)
```

## Uninformed search
search strategy that uses no-problem specific knowledge

## Informed search
search strategy that uses problem specific knowledge to find solutions more efficiently

## Greedy best-first search(gfs)
search algorigthm that expands the node that is closest to the goal, as estimated by a heuristic function h(n)

## A* search
search algorigthm that expands node with lowest value of g(n) + h(n)

g(n) = cost to reach node
h(n) = estimated cost to goal

#### Optimal if
- h(n) is admissable (never overestimates the true cost), and
- h(n) is consistant (for every node n and successor n' with step cost c)

`h(n) <= h(n') + c`


# Adversaial search
Whereas, previously, we have discussed algorithms that need to find an answer to a question, in adversarial search the algorithm faces an opponent that tries to achieve the opposite goal. Often, AI that uses adversarial search is encountered in games, such as tic tac toe.

## Minimax
A type of algorithm in adversarial search, Minimax represents winning conditions as (-1) for one side and (+1) for the other side. Further actions will be driven by these conditions, with the minimizing side trying to get the lowest score, and the maximizer trying to get the highest score.

- MAX (X) aims to maximize search
- MIN (O) aims to minimize search

Given a state in *s*
- MAX picks action *a* in *ACTIONS(s)* that produces highest value of *Min-Value(result(s, a))*
- MIN picks action *a* in *ACTIONS(s)* that produces lowest value of *Max-Value(result(s, a))*


#### Get Max-value
```
function Max-Value(state):
    if Terminal(state):
        return Utility(state)
    v = -∞
    for *action* in *Actions(state)*:
        v = Max(v, Min-Value(result(s, a)))
    return v
```

#### Get Max-value
```
function Min-Value(state):
    if Terminal(state):
        return Utility(state)
    v = -∞
    for *action* in *Actions(state)*:
        v = Min(v, Min-Value(result(s, a)))
    return v
```

## Game
- S<sub>0</sub> : inital state
- Player(s) returns which player to move in states *s*
- Actions(s) returns which legal moves in states *s*
- Player(s, a) returns state after action *a* taken in state *s*
- Terminal(s) checks if state *s* is a terminal state
- Utility(s) final numerical value for terminal state

# Optimizations

## Alpha-Beta pruning

## Depth-Limited Minima

## Evalutation Function
function that estimates the expected utility of the game from a given state

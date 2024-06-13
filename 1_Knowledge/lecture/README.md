# Knowledge


### Knowledge-Based Agents
Agents that reason by operating on internal representations of knowledge

```
If it didn't rain, Harry visited hagrid today.

Harry visited Hagrid or Dumbledore today, but not both.

Harry visited Dumbledore today.

*Harry did not visit Hagrid today*
```

#### Sentence
an assertion about the world in a knowledge representation language

## Propositional Logic
Based on propositions, statements about the world that can be either true or false

| P | Q | R |
|------|------|------|

### Propositional Symbols
| ¬ | ∧ | ∨ |  → | ↔ |
|------|------|------|------|------|
| not | and | or |  implication | biconditional |

### Logic Connectives

- Not (¬)

 P        | Q     |
|--------------|-----------|
| false  | true      |
| true  | false      |


- And (∧)

| P        | Q     | P ∧ Q      |
|--------------|-----------|------------|
| false  | false      | false        |
| false  | true     | false        |
| true  | false      | false        |
| true  | true      | true        |



- Or (∨)

| P        | Q     | P  ∨  Q |
|--------------|-----------|------------|
| false  | false      | false        |
| false  | true     | true       |
| true | false      | true        |
| true  | true      | true        |

#### Side notes
- Sometimes an example helps understand inclusive versus exclusive Or. Inclusive Or: “in order to eat dessert, you have to clean your room or mow the lawn.” In this case, if you do both chores, you will still get the cookies. Exclusive Or: “For dessert, you can have either cookies or ice cream.” In this case, you can’t have both.

- If you are curious, the exclusive Or is often shortened to XOR and a common symbol for it is ⊕).

#### Implication
| P        | Q     | P  ∨  Q |
|--------------|-----------|------------|
| false  | false      | true        |
| false  | true      | true        |
| true  | false      | true        |
| true  | true      | true        |

- #### Bicondtional
| P        | Q     | P  ∨  Q |
|--------------|-----------|------------|
| false  | false      | true        |
| false  | true      | false        |
| true  | false      | false        |
| true  | true      | true        |


### Model
assignment of a truth value to every proposition, statements about the world that can be either true, or false
```
if P: “It is raining.” and Q: “It is Tuesday.”,
a model could be the following truth-value assignment:
{P = True, Q = False}
```



### Knowledge Base (KB)
a set of sentences known by a knowledge-based agent

### Entailment (⊨)
`α ⊨ β`

If α ⊨ β (α entails β), then in any world where α is true, β is true, too.

```
If it didnt rain, Harry visited Hagrid today.
Harry visited Hagrid or Dumbledore today, but not both
Harry visited Dumbledore today
```
1. *Harry did not visit Hagrid today*

2. *It rained today*

## Inference
the process of deriving new sentences from old ones

`P: It is a Tuesday. | Q: It is raining. | R: Harry will go for a run.`

`KB: (P ∧ ¬Q) → R `

Does KB ⊨ R?


| P        | Q     | R      |     KB    |
|--------------|-----------|------------|------------|
| false  | false      | false        |            |
| false  | false      | false        |            |
| false  | true       | false        |            |
| false  | true       | true         |            |
| true   | false      | false        |            |
| true   | false      | true         |            |
| true   | true       | false        |            |
| true   | true       | true         |            |







| P        | Q     | R      |     KB    |
|--------------|-----------|------------|------------|
| false  | false      | false        |    false        |
| false  | false      | false        |    false        |
| false  | true       | false        |    false        |
| false  | true       | true         |    false        |
| true   | false      | false        |                 |
| true   | false      | true         |                 |
| true   | true       | false        |                 |
| true   | true       | true         |                 |






| P        | Q     | R      |     KB    |
|--------------|-----------|------------|------------|
| false  | false      | false        |    false        |
| false  | false      | false        |    false        |
| false  | true       | false        |    false        |
| false  | true       | true         |    false        |
| true   | false      | false        |                 |
| true   | false      | true         |                 |
| true   | true       | false        |    false        |
| true   | true       | true         |    false        |


| P        | Q     | R      |     KB    |
|--------------|-----------|------------|------------|
| false  | false      | false        |    false        |
| false  | false      | false        |    false        |
| false  | true       | false        |    false        |
| false  | true       | true         |    false        |
| true   | false      | false        |    false        |
| true   | false      | true         |    true         |
| true   | true       | false        |    false        |
| true   | true       | true         |    false        |



## Knowledge Engineering
the process of figuring out how to represent propositions and logic in AI

## Inference Rules
*Model Checking* is not an efficient algorith, it has to consider every possible model before giving the answer (a reminder: a query R is true if under all the models (truth assignments) where the KB is true, R is true as well)

*Inference rules* allows us to generate new information based on existing knowledge without considering every possible model

#### Example
If it is raining, then Harry is inside.
- It is raining.

Based on this, most can conclude that
- Harry is inside

### Modus Ponens
The type of inference rule we use in this example is *Modus Ponens* which is a way of saying:

We know an implication and its antecedent to be true, then the consequent is true as well

### And Elimination
If an And proposition is true, then any one atomic proposition within it is true as well. For example, if we know that Harry is friends with Ron and Hermione, we can conclude that Harry is friends with Hermione.

### Double Negation Elimination
A proposition that is negated twice is true. For example, consider the proposition “It is not true that Harry did not pass the test”. We can parse it the following way: “It is not true that (Harry did not pass the test)”, or “¬(Harry did not pass the test)”, and, finally “¬(¬(Harry passed the test)).” The two negations cancel each other, marking the proposition “Harry passed the test” as true.

### Implication Elimination
An implication is equivalent to an Or relation between the negated antecedent and the consequent. As an example, the proposition “If it is raining, Harry is inside” is equivalent to the proposition “(it is not raining) or (Harry is inside).”


P | Q |  P → Q | ¬P ∨ Q |
|--------------|-----------|------------|------------|
| false | false | true  | true  |
| false	| true	| true	| true  |
| true	| false	| false	| false |
| true	| true	| true	| true  |

Since P → Q and ¬P ∨ Q have the same truth-value assignment, they are equivalent logically.

An implication is true if either of two possible conditions is met: first, if the antecedent is false, the implication is trivially true.

Represented by the negated antecedent P in ¬P ∨ Q, meaning, the proposition is always true if P is false.

Second, the implication is true when the antecedent is true only when the consequent is true as well. That is, if P and Q are both true, then ¬P ∨ Q is true.

However, if P is true and Q is not, then ¬P ∨ Q is false.


### Biconditional Elimination
equivalent to an implication and its inverse with an And connective.

For example, “It is raining if and only if Harry is inside” is equivalent to (“If it is raining, Harry is inside” And “If Harry is inside, it is raining”).

### De Morgan’s Law
It is possible to turn an And connective into an Or connective.

Consider the following proposition: “It is not true that both Harry and Ron passed the test.”

From this, it is possible to conclude that “It is not true that Harry passed the test” Or “It is not true that Ron passed the test.” That is, for the And proposition earlier to be true, at least one of the propositions in the Or propositions must be true.

### Distributive Property
A proposition with two elements that are grouped with And or Or connectives can be distributed, or broken down into, smaller units consisting of And and Or.

### Knowledge and Search Problems
Inference can be viewed as a search problem with the following properties:

- Initial state: starting knowledge base
- Actions: inference rules
- Transition model: new knowledge base after inference
- Goal test: checking whether the statement that we are trying to prove is in the KB
- Path cost function: the number of steps in the proof

## Resolution
 Powerful inference rule that states that if one of two atomic propositions in an Or proposition is false, the other has to be true.

 For example, given the proposition “Ron is in the Great Hall” Or “Hermione is in the library”, in addition to the proposition “Ron is not in the Great Hall,” we can conclude that “Hermione is in the library.”

 Resolution relies on *Complementary Literals*, two of the same atomic propositions where one is negated and the other is not, such as P and ¬P.

 Complementary literals allow us to generate new sentences through inferences by resolution. Thus, inference algorithms locate complementary literals to generate new knowledge.

## First Order Logic
First order logic is another type of logic that allows us to express more complex ideas more succinctly than propositional logic. First order logic uses two types of symbols: Constant Symbols and Predicate Symbols. Constant symbols represent objects, while predicate symbols are like relations or functions that take an argument and return a true or false value.

### Universal Quantification
Quantification is a tool that can be used in first order logic to represent sentences without using a specific constant symbol. Universal quantification uses the symbol ∀ to express “for all.” So, for example, the sentence ∀x. BelongsTo(x, Gryffindor) → ¬BelongsTo(x, Hufflepuff) expresses the idea that it is true for every symbol that if this symbol belongs to Gryffindor, it does not belong to Hufflepuff.

### Existential Quantification
Existential quantification is an idea parallel to universal quantification. However, while universal quantification was used to create sentences that are true for all x, existential quantification is used to create sentences that are true for at least one x. It is expressed using the symbol ∃. For example, the sentence ∃x. House(x) ∧ BelongsTo(Minerva, x) means that there is at least one symbol that is both a house and that Minerva belongs to it. In other words, this expresses the idea that Minerva belongs to a house.

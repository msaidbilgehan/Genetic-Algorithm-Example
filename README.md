Genetic Algorithm
=================

This code implements a genetic algorithm to solve a problem of finding a target sequence. The algorithm starts with a random population of sequences and then evolves the population through a series of selection, crossover, and mutation operations, until the target sequence is found.

Classes
-------

### Genetic

The `Genetic` class is the main class of the genetic algorithm. It takes the following parameters in the constructor:

- `target`: the target sequence to be found
- `population_number`: the size of the population
- `gene_pool`: the set of genes that can be used to create the sequences

It has the following methods:

- `reset_Genetic()`: resets the genetic algorithm to its initial state
- `random_Gene()`: returns a random gene from the gene pool
- `create_Chromosome(unique:bool) -> list`: creates a chromosome (sequence) either with or without unique genes
- `create_Population(unique:bool)`: creates the initial population of sequences
- `get_Population() -> list`: returns the current population
- `calculate_Fitness(member)`: calculates the fitness of a given member (sequence) of the population
- `calculate_Fitness_For_Population()`: calculates the fitness of all members of the population
- `get_Best_Member()`: returns the member with the highest fitness score
- `sort_Population()`: sorts the population in descending order of fitness scores
- `get_Best_Member_Fitness() -> int`: returns the fitness score of the best member
- `get_Best_Member_Chromosome()`: returns the chromosome of the best member
- `crossover(unique: bool = True, best_percentage=0.1, evolve_probability=0.1) -> int`: performs crossover operations on the population to create the next generation. The `unique` parameter determines if the chromosomes should have unique genes or not, the `best_percentage` determines the percentage of the best members to include in the next generation, and the `evolve_probability` determines the probability of evolving a gene rather than doing a regular crossover.

### Member

The `Member` class represents a member (sequence) of the population. It has the following methods:

- `get_Chromosome() -> int`: returns the chromosome of the member
- `get_Fitness() -> int`: returns the fitness score of the member

Example Usage
-------------

Here's an example of how to use the genetic algorithm to find a target sequence:

scssCopy code

`target = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
population_number = 100
gene_pool = list(range(10))

g = Genetic(target, population_number, gene_pool)
g.create_Population(unique=True)

while g.get_Best_Member_Fitness() < len(target):
  g.calculate_Fitness_For_Population()
  g.crossover(unique=True, best_percentage=0.1, evolve_probability=0.1)

print("Found target sequence after", g.generation_count, "generations.")
print("Target sequence:", g.get_Best_Member_Chromosome())`

In this example, the target sequence is a list of numbers from 0 to 9, the population size is 100, and the gene pool is the same as the target sequence. The algorithm creates a population of unique sequences, calculates their fitness scores, and then performs crossover operations on the population until the target sequence is found. The `best_percentage` parameter is set to 0.1, which means that the top 10% of the population will be preserved in each generation, and the `evolve_probability` parameter is set to 0.1, which means that there is a 10% chance of a gene mutating during crossover.

The calculate_Fitness_For_Population() method calculates the fitness score for each member of the population. In this case, the fitness score is simply the number of elements in the member's chromosome that match the target sequence. For example, if a member's chromosome is [1, 2, 3, 4, 5, 6, 7, 8, 9, 0], its fitness score will be 9, since all but the last element match the target sequence.

The crossover() method performs crossover operations on the population. Crossover is a genetic operator that takes two parent chromosomes and produces one or two offspring chromosomes that inherit genetic information from both parents. In this case, the algorithm uses a type of crossover called "partially matched crossover" (PMX). PMX takes two parent chromosomes and produces two offspring chromosomes. The offspring chromosomes are constructed by randomly selecting a section of one parent chromosome and copying it to the corresponding section of the first offspring chromosome. The second offspring chromosome is constructed by swapping the corresponding sections of the two parent chromosomes.

The unique parameter in the create_Population() and crossover() methods ensures that all members of the population and offspring chromosomes are unique. This is important because the algorithm relies on the diversity of the population to explore different regions of the search space.

The get_Best_Member_Fitness() method returns the fitness score of the member with the highest fitness score in the population, and the get_Best_Member_Chromosome() method returns the chromosome of the member with the highest fitness score in the population. The algorithm continues to iterate until the fitness score of the best member in the population is equal to the length of the target sequence, indicating that the target sequence has been found.

Overall, the genetic algorithm in this example demonstrates the use of crossover and mutation operators to explore and exploit the search space, and the importance of maintaining a diverse population to avoid premature convergence.

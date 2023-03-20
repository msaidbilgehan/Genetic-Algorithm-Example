from Genetic import Genetic

gene_pool = [i for i in range(100)]
target = gene_pool[-5]

print("Target: ", target)
print("Gene Pool: ", gene_pool)

genetic_class = Genetic(
    target=target,
    population_number=100,
    gene_pool=gene_pool
)
# print("Example Chromosome:", genetic_class.create_Chromosome())

genetic_class.create_Population(unique=True)
genetic_class.calculate_Fitness_For_Population()
# population = genetic_class.get_Population()
# population_fitnesses = [member.get_Fitness() for member in population]
# print("Fitness Values of Population:", population_fitnesses)

# best_path = [member.get_Chromosome() for member in population if member.get_Fitness() == max(population_fitnesses)]
# print(f"Best Fitness ({max(population_fitnesses)}) Path:", best_path)
generation_count = genetic_class.crossover()

print("Generation Count:", generation_count)
print(f"Best Fitness ({genetic_class.get_Best_Member_Fitness()}) Member:",
      genetic_class.get_Best_Member().get_Chromosome())

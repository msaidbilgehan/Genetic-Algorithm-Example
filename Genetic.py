import random
import time

class Genetic():
    def __init__(self, target, population_number, gene_pool):
      self.target = target
      self.gene_pool = gene_pool
      self.population_number = population_number
      self.population = list()
      self.next_generation = list()
      self.generation_count = 0
      self.population_history = list()
      
    def reset_Genetic(self):
      self.population = list()
      self.next_generation = list()
      self.generation_count = 0
      self.population_history = list()
      
    def random_Gene(self):
      return random.choice(self.gene_pool)
      
    def __random_Gene(self):
      # https://stackoverflow.com/questions/6494508/how-do-you-pick-x-number-of-unique-numbers-from-a-list-in-python
      return random.sample(self.gene_pool, len(self.gene_pool))
    
    def create_Chromosome(self, unique:bool) -> list:
      if unique:
        chromosome = list()
        for _ in range(len(self.gene_pool)):
          gene = self.random_Gene()
          if gene not in chromosome:
            chromosome.append(gene)
          else:
            chromosome.append(None)
        return chromosome
      else:
        return [
            self.random_Gene()
            for _ in range(len(self.gene_pool))
        ]
      
    def create_Population(self, unique:bool):
      self.population = [
          Member(self.create_Chromosome(unique))
          for _ in range(self.population_number)
        ]
      
    def get_Population(self) -> list:
      return self.population
      
    def calculate_Fitness(self, member):
      fitness = 0
      for gene in member.chromosome:
        if gene == self.target:
          fitness += 10
        else:
          fitness -= 1
      member.fitness = fitness
      
    def calculate_Fitness_For_Population(self):
      for member in self.population:
        self.calculate_Fitness(member)
        
    def get_Best_Member(self):
      return max(self.population, key=lambda member: member.fitness)
    
    def sort_Population(self):
      self.population.sort(key=lambda member: member.fitness, reverse=True)
    
    def get_Best_Member_Fitness(self) -> int:
      return self.get_Best_Member().get_Fitness()
    
    def get_Best_Member_Chromosome(self):
      return self.get_Best_Member().get_Chromosome()
    
    def crossover(self, unique: bool = True, best_percentage=0.1, evolve_probability=0.1) -> int:
      self.sort_Population()

      self.next_generation = list()
      
      # Add the best members to the next generation
      best_members = self.population[
        :int(self.population_number * best_percentage)
      ]
      self.next_generation.extend(best_members)
      
      # Add the rest of the members to the next generation
      while self.next_generation.__len__() < self.population_number:
        parent1 = random.choice(best_members)
        parent2 = random.choice(best_members)
        
        # Crossover
        child = self.__crossover(
          parent1.get_Chromosome(), 
          parent2.get_Chromosome(), 
          unique=unique,
          evolve=True, 
          evolve_probability=evolve_probability
        )
        self.next_generation.append(Member(child))
        self.generation_count += 1
        
      self.population_history.append(self.population)
      self.population = self.next_generation
      return self.generation_count
      
    def __crossover(self, parent1, parent2, unique:bool, evolve:bool, evolve_probability:float):
      child = list()
      
      # Evolve or Crossover
      for i in range(len(parent1)):
        # Evolve
        if evolve:
          # Evolve Probability
          e_probability = random.random()
          if e_probability < evolve_probability:
            # Evolve Gene
            while unique:
              gene = self.random_Gene()
              if gene not in child:
                child.append(gene)
                break
            else:
              child.append(self.random_Gene())
          elif e_probability < evolve_probability * 2:
            child.append(parent1[i])
          else:
            child.append(parent2[i])
        else:
          # Crossover
          for i in range(len(parent1)):
            if i % 2 == 0:
              child.append(parent1[i])
            else:
              child.append(parent2[i])
      return child

      
      
class Member():
  def __init__(self, chromosome):
    self.chromosome = chromosome
    self.fitness = 0
  
  def get_Chromosome(self) -> int:
    return self.chromosome
  
  def get_Fitness(self) -> int:
    return self.fitness
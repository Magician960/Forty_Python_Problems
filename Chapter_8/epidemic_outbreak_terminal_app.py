#You will be responsible for writing a program that simulates the spread of an infectious disease
#throughout a population. Using classes, you will model an individual person’s and an entire
#population’s attributes and behaviors. Your program will allow users to set various initial
#conditions in regards to the infection such as population size, infection rate, mortality rate, and
#infection duration. The program will then simulate the interaction of people within a population
#and spread the disease. Each iteration of spreading the disease will result in a summary
#displaying statistics of the population.

#Import required libraries
import random

##CLASSES

#Simulation class
class Simulation():
    def __init__(self):
        self.day_number = 1
        #Set pop size parameter
        print("To simulate an epidemic outbreak, we must know the population size.")
        self.population_size = int(input("---Enter the population size: "))
        
        #Set initial infection %
        print("\nWe must first start by infecting a poriton of the population.")
        self.initial_infection = int(input("--Enter the percentage(0-100) of the population to initially infect: ")) / 100
        
        #Set infection risk
        print("\nWe must know the risk a person has to contract the disease when exposed.")
        self.infection_risk = int(input("--Enter the probability (0-100) that a person gets infected when exposed to the disease: "))
        
        #Set duration of infection
        print("\nWe must know how long the infection will last when exposed.")
        self.infection_duration = int(input("--Enter the duration (in days) of the infection: "))
        
        #Set mortality rate
        print("\nWe must know the mortality rate of those infected.")
        self.mortality_rate = int(input("--Enter the mortality rate (0-100) of the infection: "))
        
        #Set simulation duration
        print("\nWe must know how long to run the simulation.")     
        self.sim_duration_days = int(input("--Enter the number of days to simulate: "))

#Person class
class Person():
    def __init__(self):
        self.is_infected = False
        self.is_dead = False
        self.days_infected = 0
    
    #Method for person to get infected
    def infect(self, sim_param):
        random_infection = random.randint(0,100)
        #Set person as infected based on probability
        if random_infection < sim_param.infection_risk:
            self.is_infected = True

    #Method for person to recover
    def recover(self):
        self.is_infected = False
        self.days_infected = 0

    #Method for person to die
    def die(self):
        self.is_dead = True

    #Method to update the person's condition
    def update(self, sim_param):
        if self.is_dead == False:
            #Chance for infected person to die
            if self.is_infected == True:
                self.days_infected += 1
                random_die = random.randint(0,100)
                if random_die < sim_param.mortality_rate:
                    self.die()
                #Chance for infected person to recover
                elif self.is_dead == False:
                    if self.days_infected == sim_param.infection_duration:
                        self.recover()

#Population class
class Population():
    def __init__(self, sim_param):
        self.population = []
        #Populate the simulation
        for i in range(sim_param.population_size):
            new_person = Person()
            self.population.append(new_person)

    #Method to initialise the infection according to parameters
    def initial_infection(self, sim_param):
        infected_count = int(round(sim_param.initial_infection * sim_param.population_size))
        #Initialise infection
        for i in range(infected_count):
            self.population[i].is_infected = True
            self.population[i].days_infected = 1
        #Spread infection throughout list
        random.shuffle(self.population)

    #Method to spread infection
    def spread_infection(self, sim_param):
        for i in range(len(self.population)):
            if self.population[i].is_dead == False:
                if i == 0:
                    if self.population[i+1].is_infected == True:
                        self.population[i].infect(sim_param)
                elif i < len(self.population) - 1:
                    if self.population[i-1].is_infected == True or self.population[i+1].is_infected == True:
                        self.population[i].infect(sim_param)
                elif i == len(self.population) - 1:
                    if self.population[i-1].is_infected == True:
                        self.population[i].infect(sim_param)

    #Method to update the every person in the population
    def update(self, sim_param):
        sim_param.day_number += 1
        for i in range(len(self.population)):
            self.population[i].update(sim_param)

    #Method to display population statistics
    def display_statistics(self, sim_param):
        total_infected_count = 0
        total_death_count = 0
        #Update total counts by looping through each person
        for i in range(len(self.population)):
            if self.population[i].is_infected == True:
                total_infected_count += 1
                if self.population[i].is_dead == True:
                    total_death_count += 1
        #Calculate percentage of population infected
        infected_percent = round(total_infected_count/len(self.population) * 100,4)
        #Calculate percentage of population dead
        dead_percent = round(total_death_count/len(self.population) * 100,4)

        #Print summary statistics with formatting
        print(f"\n-----Day # {sim_param.day_number}-----")
        print(f"Percentage of Population Infected: {infected_percent}%")
        print(f"Percentage of Population Dead: {dead_percent}%")
        print(f"Total People Infected: {total_infected_count} / {sim_param.population_size}")
        print(f"Total Deaths: {total_death_count} / {sim_param.population_size}")

    #Method to display graphic of population
    def graphics(self):
        status = []
        for i in range(len(self.population)):
            if self.population[i].is_dead == True:
                char = "X"
            else:
                if self.population[i].is_infected == True:
                    char = "I"
                else:
                    char = "O"
            #Add graphic of person to list
            status.append(char)
        #Print status
        for person in status:
            print(person, end="-")

##MAIN PROGRAM

#Initialise simulation
simulation = Simulation()
#Initialise population
pop = Population(simulation)

#Display 1st day of infection
pop.initial_infection(simulation)
pop.display_statistics(simulation)
pop.graphics()
input("\nPress Enter to begin the simulation.")

for day in range(simulation.sim_duration_days - 1):
    pop.spread_infection(simulation)
    pop.update(simulation)
    pop.display_statistics(simulation)
    pop.graphics()
    if day != simulation.sim_duration_days - 2:
        input("\nPress Enter to advance to the next day.")
#You will be responsible for writing a program that simulates the spread of an infectious disease
#throughout a population similar to the previous program. Using classes, you will model an
#individual person’s and an entire population’s attributes and behaviors. Your program will allow
#users to set various initial conditions in regards to the infection such as population size, infection
#rate, mortality rate, and infection duration. The program will then simulate the interaction of
#people within a population and spread the disease. Each iteration of spreading the disease will
#result in a summary displaying statistics of the population. This time however, rather than storing
#the population in a list and checking if the person to the left or right of the current person is
#infected, we will store the population in a two dimensional list using nested for loops. This will
#allow us to check for infections both to the left and right and above and below. This added
#feature will help allow the program to create a Graphical User Interface or GUI (goo-e) to
#visually show the spread of the infection. Rather than representing the spread of the infection
#using O, I, and X in the terminal, each person in the population will be represented by a color
#square in a GUI; green being healthy, yellow being infected, and red being dead.

#Import required libraries
import random
import math
import tkinter

##CLASSES

#Simulation class
class Simulation():
    def __init__(self):
        self.day_number = 1
        #Set pop size parameter
        print("To simulate an epidemic outbreak, we must know the population size.")
        self.population_size = int(input("---Enter the population size: "))
        root = math.sqrt(self.population_size)
        #Check if pop size is perfect square, convert to one if not
        if int(root + .5)**2 != self.population_size:
            round(root, 0)
            self.grid_size = int(root)
            self.population_size = self.grid_size ** 2
            print(f"Rounding population size to {self.population_size} for visual purposes.")
        else:
            self.grid_size = int(math.sqrt(self.population_size))
        
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
        #Populate the simulation in a N by N grid
        for i in range(sim_param.grid_size):
            row = []
            for j in range(sim_param.grid_size):
                new_person = Person()
                row.append(new_person)
            self.population.append(row)

    #Method to initialise the infection according to parameters
    def initial_infection(self, sim_param):
        infected_count = int(round(sim_param.initial_infection * sim_param.population_size))
        infections = 0
        #Initialise infection
        while infections < infected_count:
            random_x = random.randint(0, sim_param.grid_size - 1)
            random_y = random.randint(0, sim_param.grid_size - 1)
            if self.population[random_x][random_y].is_infected == False:
                self.population[random_x][random_y].is_infected = True
                self.population[random_x][random_y].days_infected = 1
                infections += 1

    #Method to spread infection
    def spread_infection(self, sim_param):
        for i in range(sim_param.grid_size):
            for j in range(sim_param.grid_size):
                #Check if current person isn't already dead
                if self.population[i][j].is_dead == False:
                    #Check first row
                    if i == 0:
                        #check first column of first row
                        if j == 0:
                            if self.population[i+1][j].is_infected == True or self.population[i][j+1].is_infected == True:
                                self.population[i][j].infect(sim_param)
                        #Check last column of first row
                        elif j == sim_param.grid_size - 1:
                            if self.population[i+1][j].is_infected == True or self.population[i][j-1].is_infected == True:
                                self.population[i][j].infect(sim_param)
                        #Check rest of first row
                        else:
                            if self.population[i+1][j].is_infected == True or self.population[i][j+1].is_infected == True or self.population[i][j-1].is_infected == True:
                                self.population[i][j].infect(sim_param)
                    #Check last row
                    elif i == sim_param.grid_size - 1:
                        #Check first column of last row
                        if j == 0:
                            if self.population[i-1][j].is_infected == True or self.population[i][j+1].is_infected == True:
                                self.population[i][j].infect(sim_param)
                        #Check last column of last row
                        elif j == sim_param.grid_size - 1:
                            if self.population[i-1][j].is_infected == True or self.population[i][j-1].is_infected == True:
                                self.population[i][j].infect(sim_param)
                        #Check rest of last row
                        else:
                            if self.population[i-1][j].is_infected == True or self.population[i][j-1].is_infected == True or self.population[i][j+1].is_infected == True:
                                self.population[i][j].infect(sim_param)
                    #Check rest of rows
                    else:
                        #Check first column of rest of rows
                        if j == 0:
                            if self.population[i-1][j].is_infected == True or self.population[i+1][j].is_infected == True or self.population[i][j+1].is_infected == True:
                                self.population[i][j].infect(sim_param)
                        #Check last column of rest of rows
                        elif j == sim_param.grid_size - 1:
                            if self.population[i-1][j].is_infected == True or self.population[i+1][j].is_infected == True or self.population[i][j-1].is_infected == True:
                                self.population[i][j].infect(sim_param)
                        #Check rest of columns of rest of rwows
                        else:
                            if self.population[i-1][j].is_infected == True or self.population[i+1][j].is_infected == True or self.population[i][j-1].is_infected == True or self.population[i][j+1].is_infected == True:
                                self.population[i][j].infect(sim_param)
                        

    #Method to update the every person in the population
    def update(self, sim_param):
        sim_param.day_number += 1
        for row in self.population:
            for person in row:
                person.update(sim_param)

    #Method to display population statistics
    def display_statistics(self, sim_param):
        total_infected_count = 0
        total_death_count = 0
        #Update total counts by looping through each person
        for row in self.population:
            for person in row:
                if person.is_infected == True:
                    total_infected_count += 1
                    if person.is_dead == True:
                        total_death_count += 1
        #Calculate percentage of population infected
        infected_percent = round(total_infected_count/len(self.population),4)
        #Calculate percentage of population dead
        dead_percent = round(total_death_count/len(self.population),4)

        #Print summary statistics with formatting
        print(f"\n-----Day # {sim_param.day_number}-----")
        print(f"Percentage of Population Infected: {infected_percent}%")
        print(f"Percentage of Population Dead: {dead_percent}%")
        print(f"Total People Infected: {total_infected_count} / {sim_param.population_size}")
        print(f"Total Deaths: {total_death_count} / {sim_param.population_size}")

#Helper function to display graphic of population
def graphics(sim_param, population, canvas):
    square_dimension = 600 // sim_param.grid_size
    #Get square coordinates for each person
    for i in range(sim_param.grid_size):
        y = i * square_dimension
        for j in range(sim_param.grid_size):
            x = j * square_dimension
            #Colour in each square based on person's status
            if population.population[i][j].is_dead == True:
                canvas.create_rectangle(x,y,x+square_dimension,y+square_dimension, fill="red")
            else:
                if population.population[i][j].is_infected == True:
                    canvas.create_rectangle(x,y,x+square_dimension,y+square_dimension, fill="yellow")
                else:
                    canvas.create_rectangle(x,y,x+square_dimension,y+square_dimension,fill="green")


##MAIN PROGRAM

#Initialise simulation
simulation = Simulation()
#Initialise population
pop = Population(simulation)

#Set pop-up window variables
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

#Create tinker object
sim_window = tkinter.Tk()
sim_window.title("Epidemic Outbreak")

#Create canvas
sim_canvas = tkinter.Canvas(sim_window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="lightblue")
sim_canvas.pack(side=tkinter.LEFT)

#Display 1st day of infection
pop.initial_infection(simulation)
pop.display_statistics(simulation)
input("\nPress Enter to begin the simulation.")

for day in range(simulation.sim_duration_days - 1):
    pop.spread_infection(simulation)
    pop.update(simulation)
    pop.display_statistics(simulation)
    graphics(simulation, pop, sim_canvas)
    sim_window.update()
    if day != simulation.sim_duration_days - 2:
        sim_canvas.delete("all")
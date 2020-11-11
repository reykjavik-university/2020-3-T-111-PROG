import random

from island import Island
from animal import Animal
from prey import Prey
from predator import Predator

def put_animals_at_random(island, animal_type, animal_count):
    '''Puts animal_count instances of animal_type randomly on the island'''
    count = 0
    size = island.size()

    while count < animal_count:
        x = random.randint(0, size-1)
        y = random.randint(0, size-1)
        if island.animal(x,y) == Island.UNOCCUPIED:
            new_animal = animal_type(island, x, y)  # calling the constructor for the specific animal
            island.register(new_animal)
            count += 1

def main(predator_breed_time=6, predator_starve_time=3, initial_predators=10, prey_breed_time=3, initial_prey=50, size=10, ticks=10):
    '''Initialization of the simulation'''

    # Initialize class variables
    Predator.set_breed_time(predator_breed_time) 
    Predator.set_starve_time(predator_starve_time)
    Prey.set_breed_time(prey_breed_time)

    seed = int(input("Enter seed for randomness: "))
    random.seed(seed)

    isle = Island(size)
    put_animals_at_random(isle, Prey, initial_prey)
    put_animals_at_random(isle, Predator, initial_predators)
    print(isle)

    # The simulation is carried out 'ticks' times
    for _ in range(ticks):
        for x in range(size):
            for y in range(size):
                animal = isle.animal(x,y)
                if isinstance(animal, Animal):
                    if isinstance(animal, Predator): # a predator can eat
                        animal.eat()
                    animal.move()
                    animal.breed()
                    animal.clock_tick()

        isle.clear_all_moved_flags()
        print(isle)

#main(initial_predators=2, initial_prey=5, ticks=3, size=5)
main()
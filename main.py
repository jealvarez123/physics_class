# Train information
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# function for converting fahrenheit to celsius
def f_to_c(f_temp):
  return (f_temp - 32) * 5/9

f100_in_celsius = f_to_c(100)

# function for converting celsius to fahrenheit
def c_to_f(c_temp):
  return (c_temp * 9/5) + 32

c0_in_fahrenheit = c_to_f(0)

# Function used to find force
def get_force(mass, acceleration):
  return mass * acceleration
get_force(train_mass, train_acceleration)

train_force = get_force(train_mass, train_acceleration)

print("The GE train supplies " + str(train_force) + " Newtons of force")
# function to find energy
def get_energy(mass, c=3*10**8):
  return mass * c**2

bomb_energy = get_energy(bomb_mass)

print("A 1kg bomb supplies " + str(bomb_energy) + " Joules")

# function that returns force and distance
def get_work(mass, acceleration, distance):
  return train_force * train_distance

train_work = get_work(train_mass, train_acceleration, train_distance)
print(train_work)

print("the GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters")
from Procedures.CrossoverMethods import *
from Objects.BenchmarkFunctions import *
print("ih rapaiz")


crossoverChance = 0.80
mutationChance = 0.02
standartDeviation = 3  # Will be used in the Gaussian Mutation
iterations = 10000
function = Cross()  # Eggholder(), Sphere(), Bukin6() or Cross()
chromossomesNumber = 50
crossoverMethod = arithmetic  # blx or arithmetic
animationVelocity = 20  # In millisecond's

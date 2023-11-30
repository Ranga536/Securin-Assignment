#Total Combinations
total_combinations = 6 * 6

#Distribution of Combinations
distribution_matrix = [[0] * 6 for i in range(6)]

for die_a in range(6):
    for die_b in range(6):
        distribution_matrix[die_a][die_b] = die_a + die_b + 2

for row in distribution_matrix:
    print(row)

#Probability of Sums
probabilities = [row.count(i) / total_combinations for i in range(2, 13)]

#Undoom Dice Transformation
def undoom_dice(die_a, die_b):
    new_die_a = [min(4, spots) for spots in die_a]
    new_die_b = [spots for spots in die_b]
    return new_die_a, new_die_b

#Example input
Die_A = [1, 2, 3, 4, 5, 6]
Die_B = Die_A
New_Die_A, New_Die_B = undoom_dice(Die_A, Die_B)

#Displaying Results
print("Undoom Dice Transformation:")
print("New Die A:", New_Die_A)
print("New Die B:", New_Die_B)

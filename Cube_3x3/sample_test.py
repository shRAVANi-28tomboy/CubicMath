from basic_structure import RubiksCube3x3

test_cube = RubiksCube3x3()
ideal_cube = test_cube.cube
scramble_sequence = test_cube.scramble_ideal_cube()
print(scramble_sequence)
# test_cube.rotate_layer('d', -90)
# test_cube.display_cube()
# test_cube.rotate_layer('l', -90)
fig = test_cube.display_cube()
fig.show()
print('')
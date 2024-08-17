def repr_point(point):
  # point is an (x, y) tuple
	match point:
		case (0, 0):
			print("Origin")
		case (0, y):
			print(f"Y={y}")
		case (x, 0):
			print(f"X={x}")
		case (x, y):
			print(f"X={x}, Y={y}")
		case _:
			raise ValueError("Not a point")
repr_point((0,2))
repr_point((2,2))
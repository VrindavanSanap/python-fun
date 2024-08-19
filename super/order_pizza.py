def order_pizza(size, *toppings, **details):
  print(f"Ordered a {size} pizza with the following toppings:")
  for topping in toppings:
    print(f"- {topping}")
  if details.items():
    print(f"Detials:")
    for k, v in details.items():
      print(f"{k}: {v}")


order_pizza("Large", "pineapple", "anchovi", delivery=True, tip=5)

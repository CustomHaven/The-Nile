from nile import get_distance, format_price, SHIPPING_PRICES
from test import test_function

# Define calculate_shipping_cost() here:
# Q1 Q2 Q3 Q4 Q5 Q6 Q7
def calculate_shipping_cost(from_coords, to_coords, shipping_type='Overnight'):
  # Latitude
  from_lat, from_long = from_coords
  # Longitude
  to_lat, to_long = to_coords
  # we send them as *args in as they are 2 tuples each
  distance = get_distance(*from_coords, *to_coords)
  shipping_rate = SHIPPING_PRICES[shipping_type]

  price = distance * shipping_rate

  return format_price(price)

# Test the function by calling 
# Q8
test_function(calculate_shipping_cost)

# Define calculate_driver_cost() here
# Q9 Q10 Q11 Q12 Q13 Q14 Q15 Q16
def calculate_driver_cost(distance, *drivers):
  cheapest_driver = None
  cheapest_driver_price = None
  for driver in drivers:
    driver_time = driver.speed * distance
    price_for_driver = driver.salary * driver_time
    if cheapest_driver == None:
      cheapest_driver = driver
      cheapest_driver_price = price_for_driver
    elif price_for_driver < cheapest_driver_price:
      cheapest_driver = driver
      cheapest_driver_price = price_for_driver
  return cheapest_driver_price, cheapest_driver

# Test the function by calling
# Q16 
test_function(calculate_driver_cost)

# Define calculate_money_made() here
# Q17 Q18 Q19 Q20 Q21 Q22
def calculate_money_made(**trips):
  total_money_made = 0
  for trip_id, trip in trips.items():
    trip_revenue = trip.cost - trip.driver.cost
    total_money_made += trip_revenue
  return total_money_made

# Test the function by calling 
# Q23
test_function(calculate_money_made)


# OK! calculate_shipping_cost() passes tests
# OK! calculate_driver_cost() passes tests
# OK! calculate_money_made() passes tests
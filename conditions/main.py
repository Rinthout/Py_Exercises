# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line
def farm_action(
    weather,
    time_of_day, 
    cow_need_milking, 
    locations_cows, 
    season, 
    full_slurry_tank, 
    long_grass
):
    if time_of_day == "night" and weather == "rainy" and locations_cows == "pasture" :
        # print("Take cows to cowshed")
        return "Take cows to cowshed"
    elif cow_need_milking == True and locations_cows == "cowshed" :
        # print("milk cows")
        return "milk cows"
    elif cow_need_milking == True and locations_cows == "pasture" :
        # print("take cows to cowshed\nmilk cows\ntake cows back to pasture")
        return "take cows to cowshed\nmilk cows\ntake cows back to pasture"
    elif full_slurry_tank == True and locations_cows == "cowshed" and (weather == "rainy" or weather == "neutral") :
        # print("fertilize pasture")
        return "fertilize pasture"
    elif long_grass == True and season == "spring" and weather == "sunny" and locations_cows != "pasture" :
        # print("mow grass")
        return "mow grass"
    else: 
        # print("wait")
        return "wait"
# 1.
farm_action('rainy', 'night', False, 'cowshed', 'winter', True, True)
# 'fertilize pasture'

# 2.
farm_action('rainy', 'night', False, 'cowshed', 'winter', False, True)
# 'wait'

# 3.
farm_action('windy', 'night', True, 'cowshed', 'winter', True, True)
# 'milk cows'

# 4.
farm_action('sunny', 'day', True, 'pasture', 'spring', False, True)
# """take cows to cowshed
# milk cows
# take cows back to pasture"""

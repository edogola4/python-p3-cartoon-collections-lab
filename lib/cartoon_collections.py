def roll_call_dwarves(dwarves):
    for i, dwarf in enumerate(dwarves):
        print(f"{i + 1}. {dwarf}")
    pass

def summon_captain_planet(calls):
    return [call.capitalize() + "!" for call in calls]

    pass

def long_planeteer_calls(calls):
    return any(len(call) > 4 for call in calls)
    pass

def find_the_cheese(foods):
    cheeses = {"cheddar", "gouda", "camembert"}
    for food in foods:
        if food in cheeses:
            return food
    return None
    pass

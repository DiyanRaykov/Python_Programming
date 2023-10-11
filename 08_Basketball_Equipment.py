cost_of_training_for_a_year = int(input())

price_of_basketball_shoes = cost_of_training_for_a_year * 0.6
price_of_a_basketball_team = price_of_basketball_shoes * 0.8
cost_of_a_basketball = price_of_a_basketball_team * 0.25
price_of_basketball_accessories = cost_of_a_basketball * 0.20
total_price_for_the_equipment = (price_of_basketball_shoes
                                 + price_of_a_basketball_team
                                 + cost_of_a_basketball
                                 + price_of_basketball_accessories
                                 + cost_of_training_for_a_year)

print(total_price_for_the_equipment)

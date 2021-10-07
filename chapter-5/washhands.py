# Follow the instructions for what to code in this file.
mortality_rate = [18.1, 15.4, 19.0, 13.4, 10.2, 13.1, 18.1, 14.4, 15.0,
                  10.8, 5.4, 12.2, 0.7, 0.0, 0.7, 1.0, 1.1, 0.4, 0.0, 1.0, 2.3, 2.9, 1.3]

before_wash_hands = mortality_rate[0:12]
after_wash_hands = mortality_rate[12:]
#bwh_years = len(before_wash_hands)
#awh_years = len(after_wash_hands)

print(
    f"This is the avg death rate before washing hands {sum(before_wash_hands)/len(before_wash_hands)}")


print(
    f"This is the avg death rate after washing hands {sum(after_wash_hands)/len(after_wash_hands)}")

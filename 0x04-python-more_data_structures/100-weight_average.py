#!/usr/bin/python3i
def weight_average(my_list=[]):
    if not my_list:
        return 0
 
    total_weighted_score = 0
    total_weight = 0

    for score, weight in my_list:
        total_weighted_score += score * weight
        total_weight += weight

    weighted_average = total_weighted_score / total_weight
    return weighted_average

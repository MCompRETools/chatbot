def update_impact(total, choice_impact):
    for k in total:
        total[k] += choice_impact.get(k, 0)
    return total

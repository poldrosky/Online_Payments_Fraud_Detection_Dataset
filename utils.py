def cost_function_amount(y_true, y_score, amount, threshold=0.5):
    y_pred = [1 if prob>= threshold else 0 for prob in y_score]
    cost = 0
    for i in range(0, len(y_true)):
        if (y_true[i] == 0) and (y_pred[i] == 0):
            cost += (amount[i] * 0.2)
        elif (y_true[i] == 0) and (y_pred[i] == 1):
            cost -= (amount[i] * 0.2)
        elif (y_true[i] == 1) and (y_pred[i] == 0):
            cost -= amount[i]
        else:
            pass
    return cost
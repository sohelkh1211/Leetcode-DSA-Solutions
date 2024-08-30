def solution(weights, profits, m):
    profit_per_weight = [(w, p, p/w) for p, w in zip(profits, weights)]
    profit_per_weight.sort(reverse=True, key=lambda x: x[2])

    max_profit = 0
    print("Weight\tProfit\tProfit per weight\tSize of Bag")
    
    for weight, profit, ppw in profit_per_weight:
        if weight <= m:
            m -= weight
            max_profit += profit
        else:
            max_profit += (m / weight) * profit
            m = 0

            print(f"{weight}\t{profit}\t{ppw:.2f}\t\t\t{m}")
            return max_profit
        
        print(f"{weight}\t{profit}\t{ppw:.2f}\t\t\t{m}")

    return max_profit

weights = [2, 3, 5, 7, 1, 4, 1]
profits = [10, 5, 15, 7, 6, 18, 3]
m = 15
ans = solution(weights, profits, m)
print('%.2f' % ans)
# Stock Price Analyzer
# This program analyzes stock price data entered by the user.
# It calculates important statistics such as average price,
# highest price, lowest price, and displays the price trend.
# This type of analysis is commonly used in financial markets
# to evaluate stock performance over a period of time.

def analyze_prices(prices):

    average_price = sum(prices) / len(prices)
    highest_price = max(prices)
    lowest_price = min(prices)

    print("\n========== STOCK ANALYSIS ==========")
    print("Average Price :", round(average_price, 2))
    print("Highest Price :", highest_price)
    print("Lowest Price  :", lowest_price)

    if prices[-1] > prices[0]:
        print("Trend         : Upward 📈")
    elif prices[-1] < prices[0]:
        print("Trend         : Downward 📉")
    else:
        print("Trend         : Stable")

    print("====================================\n")


def main():

    print("========= STOCK PRICE ANALYZER =========")

    n = int(input("Enter number of days: "))

    prices = []

    for i in range(n):
        price = float(input(f"Enter price for day {i+1}: "))
        prices.append(price)

    analyze_prices(prices)


main()
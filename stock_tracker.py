import csv

# Hardcoded stock prices dictionary
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 185,
    "MSFT": 420
}

def show_available_stocks():
    print("\n📈 Available Stocks:")
    print(f"{'Stock':<10} {'Price (USD)'}")
    print("-" * 25)
    for stock, price in STOCK_PRICES.items():
        print(f"{stock:<10} ${price}")

def get_portfolio():
    portfolio = {}
    print("\n💼 Enter your stock holdings (type 'done' to finish):")

    while True:
        stock = input("Enter stock name (e.g., AAPL): ").upper().strip()

        if stock == "DONE":
            break

        if stock not in STOCK_PRICES:
            print(f"❌ '{stock}' not found. Available: {', '.join(STOCK_PRICES.keys())}")
            continue

        try:
            quantity = int(input(f"Enter quantity for {stock}: "))
            if quantity <= 0:
                print("❌ Quantity must be a positive number.")
                continue
            portfolio[stock] = portfolio.get(stock, 0) + quantity
        except ValueError:
            print("❌ Please enter a valid number.")

    return portfolio

def calculate_and_display(portfolio):
    if not portfolio:
        print("⚠️  No stocks in portfolio.")
        return

    print("\n📊 Portfolio Summary:")
    print(f"{'Stock':<10} {'Qty':<8} {'Price':<12} {'Total Value'}")
    print("-" * 45)

    grand_total = 0
    for stock, qty in portfolio.items():
        price = STOCK_PRICES[stock]
        total = price * qty
        grand_total += total
        print(f"{stock:<10} {qty:<8} ${price:<11} ${total}")

    print("-" * 45)
    print(f"{'TOTAL INVESTMENT':<30} ${grand_total}")
    return grand_total, portfolio

def save_to_file(portfolio, grand_total):
    choice = input("\nDo you want to save results? (csv/txt/no): ").lower().strip()

    if choice == "csv":
        with open("portfolio_result.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Stock", "Quantity", "Price (USD)", "Total Value (USD)"])
            for stock, qty in portfolio.items():
                price = STOCK_PRICES[stock]
                writer.writerow([stock, qty, price, price * qty])
            writer.writerow(["", "", "Grand Total", grand_total])
        print("✅ Saved to portfolio_result.csv")

    elif choice == "txt":
        with open("portfolio_result.txt", "w") as f:
            f.write("Stock Portfolio Summary\n")
            f.write("=" * 40 + "\n")
            for stock, qty in portfolio.items():
                price = STOCK_PRICES[stock]
                f.write(f"{stock}: {qty} shares x ${price} = ${price * qty}\n")
            f.write("=" * 40 + "\n")
            f.write(f"Total Investment: ${grand_total}\n")
        print("✅ Saved to portfolio_result.txt")

    else:
        print("Results not saved.")

def main():
    print("=" * 45)
    print("    💰 Stock Portfolio Tracker")
    print("=" * 45)

    show_available_stocks()
    portfolio = get_portfolio()
    result = calculate_and_display(portfolio)

    if result:
        grand_total, portfolio = result
        save_to_file(portfolio, grand_total)

if __name__ == "__main__":
    main()

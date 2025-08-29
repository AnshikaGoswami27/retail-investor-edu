import random

# Mock translation function (replace with real API calls e.g. googletrans)
def translate(text, target_lang):
    translations = {
        "hi": {
            "Welcome to the Stock Market Education App!": "स्टॉक मार्केट शिक्षा ऐप में आपका स्वागत है!",
            "Choose a tutorial to start learning:": "सीखना शुरू करने के लिए एक ट्यूटोरियल चुनें:",
            "1. Stock Market Basics": "1. स्टॉक मार्केट की मूल बातें",
            "2. Risk Assessment": "2. जोखिम मूल्यांकन",
            "3. Algorithmic Trading": "3. एल्गोरिदमिक ट्रेडिंग",
            "4. Portfolio Diversification": "4. पोर्टफोलियो विविधीकरण",
            "Enter your choice (1-4): ": "अपना विकल्प दर्ज करें (1-4): ",
            "Correct!": "सही!",
            "Incorrect.": "गलत।",
            "Your score:": "आपका स्कोर:",
            "Start Virtual Trading? (yes/no): ": "वर्चुअल ट्रेडिंग शुरू करें? (हाँ/नहीं): ",
            "You bought": "आपने खरीदा",
            "You sold": "आपने बेचा",
            "Current Portfolio Value:": "वर्तमान पोर्टफोलियो मूल्य:",
            "Thank you for using the app!": "ऐप का उपयोग करने के लिए धन्यवाद!",
        }
    }
    return translations.get(target_lang, {}).get(text, text)

# Tutorials content
tutorials = {
    1: {
        "title": "Stock Market Basics",
        "content": "Stocks represent ownership in a company. Prices fluctuate based on demand and company performance."
    },
    2: {
        "title": "Risk Assessment",
        "content": "Assess risk by diversifying investments and understanding market volatility."
    },
    3: {
        "title": "Algorithmic Trading",
        "content": "Algorithmic trading uses computer programs to execute trades at high speed based on predefined criteria."
    },
    4: {
        "title": "Portfolio Diversification",
        "content": "Diversify your portfolio to reduce risk by investing in different asset classes."
    }
}

# Quiz questions for each tutorial
quizzes = {
    1: [
        {"q": "What does owning a stock represent?", "a": "ownership in a company"},
        {"q": "Stock prices fluctuate based on?", "a": "demand and company performance"},
    ],
    2: [
        {"q": "What helps reduce investment risk?", "a": "diversification"},
        {"q": "Market volatility affects?", "a": "risk"},
    ],
    3: [
        {"q": "Algorithmic trading uses?", "a": "computer programs"},
        {"q": "Trades are executed at?", "a": "high speed"},
    ],
    4: [
        {"q": "Diversification reduces?", "a": "risk"},
        {"q": "Investing in different asset classes is called?", "a": "portfolio diversification"},
    ]
}

# Virtual trading mock data
stock_prices = {
    "ABC": 100,
    "XYZ": 200,
    "DEF": 50,
}

def run_tutorial(lang):
    print(translate("Choose a tutorial to start learning:", lang))
    for i in range(1, 5):
        print(f"{i}. {translate(tutorials[i]['title'], lang)}")
    choice = int(input(translate("Enter your choice (1-4): ", lang)))
    tutorial = tutorials.get(choice)
    if not tutorial:
        print("Invalid choice.")
        return
    print("\n" + translate(tutorial['title'], lang))
    print(translate(tutorial['content'], lang))

    # Quiz
    score = 0
    for q in quizzes[choice]:
        answer = input(translate(q['q'], lang) + " ").strip().lower()
        if q['a'] in answer:
            print(translate("Correct!", lang))
            score += 1
        else:
            print(translate("Incorrect.", lang))
    print(f"{translate('Your score:', lang)} {score}/{len(quizzes[choice])}")

def virtual_trading(lang):
    portfolio = {}
    cash = 10000  # virtual cash
    print(translate("Start Virtual Trading? (yes/no): ", lang))
    start = input().strip().lower()
    if start not in ['yes', 'हाँ', 'y']:
        return
    while True:
        print("\nStocks available:")
        for stock, price in stock_prices.items():
            print(f"{stock}: ₹{price}")
        action = input(translate("Buy or Sell? (buy/sell/exit): ", lang)).strip().lower()
        if action == "exit":
            break
        stock = input(translate("Enter stock symbol: ", lang)).strip().upper()
        if stock not in stock_prices:
            print("Invalid stock symbol.")
            continue
        qty = int(input(translate("Enter quantity: ", lang)))
        price = stock_prices[stock]
        if action == "buy":
            cost = price * qty
            if cost > cash:
                print("Insufficient cash.")
                continue
            cash -= cost
            portfolio[stock] = portfolio.get(stock, 0) + qty
            print(f"{translate('You bought', lang)} {qty} shares of {stock} at ₹{price} each.")
        elif action == "sell":
            if portfolio.get(stock, 0) < qty:
                print("Insufficient shares.")
                continue
            portfolio[stock] -= qty
            cash += price * qty
            print(f"{translate('You sold', lang)} {qty} shares of {stock} at ₹{price} each.")
        else:
            print("Invalid action.")
        # Show portfolio value
        value = cash + sum(stock_prices[s] * q for s, q in portfolio.items())
        print(f"{translate('Current Portfolio Value:', lang)} ₹{value:.2f}")
    print(translate("Thank you for using the app!", lang))

def main():
    print("Welcome to the Stock Market Education App!")
    lang = input("Choose language (en/hi): ").strip().lower()
    if lang not in ['en', 'hi']:
        lang = 'en'
    run_tutorial(lang)
    virtual_trading(lang)

if __name__ == "__main__":
    main()

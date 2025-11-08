# 1.1 Terminology and Trading Floors

### General Terms

- **Bid**: The highest price for which someone is willing to buy something 
- **Offer**: The lowest price at which someone is willing to sell something. Also known as the ask price. 
- **Size**: The number of contracts that one is willing to trade at a given price
    - Size is higher when the trader is more confident. For example, if a Bid and Offer both had a four degree cushion, you could trade more contracts on the offer if you were more confident in it. 
- **Make A Market**: To provide a bid and ask price and a quantity/size 
    - "I'm 60 at 68, 4 by 10."
    - Bid is 60, offer is 68, trading 4 bid contracts, and 10 offer contracts. 
- **Spread**: The difference between the bid and the ask price
    - Spread for the example above is 8. 
- **Hedge**: A trade or investment to reduce the risks of another transaction. A second bet that offsets risks associated with a first bet. 
    - Example: "$100 bet - Chicago Bulls to win tonight" 
    - Hedge #1: Bulls will score < 120 points tonight. --> You're reducing the risk of our first bet because the more points the Bulls score, the higher their chance of winning. 
    - Hedge #2: Score is 40-40 at halftime, you sell them winning at 55%. --> Betting against them at half time offsets the initial bet. 
    - Hedge #3: Bulls shoot < 30% from 3 point range. --> Betting against them scoring a high percentage of their 3 pointers because there's a high correlation between number of 3 pointers and victory. 
- **Index**: An instrument that tracks the performance of a market. Generally, an index will track the performance of many stocks. Examples include the Nasdaq, S&P 500, and Down Jones Industrial Average. 
- **ETF**: Marketable security that tracks a stock index, commodity, or other basket of assets. Behaves and trades very much like a stock. 
- **Commodity**: A raw material (oil, gold) or agricultural product (soybeans, corn) that can be bought and sold, normally at one prevailing price. 

### Market Participants 

- **Trader**: Can define any active market participant. Traders can work for trading firms, as well as hedge funds, banks, etc. 
- **Market Maker**: A specific trader willing to buy or sell an asset at a specific price at all times. Market makers constantly buy and sell related securities, with their primary responsibilities being to collect edge and manage risk. 
- **Local**: General term for market makers. Term comes from pit trading days, as locals stood in the pit every day. 
- **Broker**: A person or company that acts as an intermediary between buyers and sellers. 
- **Paper**: The interested parties trading against Akuna (or other market makers). Term comes from the pit trading days as customer orders came via paper. 
- **Hedge Fund/Institution/Bank**: Financial institutions that, for a variety of reasons, are active market participants. These groups are generally the largest paper customers. 
- **Retail Client**: Smaller "paper" customers. For example, an individual trading at home. 

### Option Specific Terms: 

- **Option**: An option is a contract giving the buyer the right, but no the obligation, to buy or sell an underlying asset at a specific price (the strike price) on or before a certin date (the expiration date). These contracts are a type of derivative, meaning their value is derived from another asset like a stock, index, or ETF. 
- **Fill**: Another term for the completion of a trade. If a market maker trades on their bid or offer, the market maker may claim he/she "got filled." 
- **Tick size, tick increment**: The increment between one price level. Different producst have different tick sizes. 
    - Ex: The USD tick size is 0.01. 
    - Another example would be a future where the gap between "prices" is 0.125. A future is a standardized legal contract ot buy or sell an asset at a predetermined price on a specified future date. 
- **Queue Priority**: For markets that are determined by "price-time," if multiple orders are entered for the same price, the participant who entered his/her order or quote first will trade first. This person is said to have queue priority. 
- **Settlement time**: The specific time of days options expire, and futures "settle" for the day. These values are used to calculate daily P&L and mark to market. 
- **Immediate or Cancel (IOC)**: A type of order that requires all or part of the order to be executed immediately. Unfilled parts of order are cancelled- sometimes referred to as Fill and Kill (FAK) orders. 
    - Ex: 100 bid for 24 contracts (price --> 100, quantity --> 24)
    - Enter an IOC order to Sell 50 at 100 
    - If we entered this order, 24 contracts will be sold at 100 and the remaining 26 will be cancelled. 
    - Your order is only "alive" to execute with any price at or above your offer, for a quantity up to your size. 
- **Good for Day (GFD) order**: A type of order that will remain active until executed (in part or full) or until the end of the trading day. It is then cancelled.
- **Good-till-cancelled (GTC):** A type of order that will remain active until completed or cancelled by the entering party.
- **Fill or Kill (FOK):** an order type that must be executed immediately in its entirety, otherwise the order is cancelled; often with floor trading—market makers have a few seconds to decide to make a trade and can also do a partial order. Sometimes brokers will use this interchangeably with Fill and Kill and will fill partial FOK orders.
- **All-or-None**: An order type that must be executed in its entirety, or not executed at all. 
- **OCO (one cancels the other)**: when one order is executed, the other order is automatically cancelled. This is usually invoked to protect someone from gaining too much exposure (or how much the trader is open to loss) in one direction.
    - Market A: Temp in NYC: 60 - 65
    - Market B: Temp in Connectict: 58 - 63 
    - Making these orders OCO means if someone buys 65 degrees in the NYC market, you don't want them to buy 63 degrees in the Connecticut market (the temperatures are connected because the states border each other).
- **Contract Size:** The multiplier attached to an option or future. Options on stock generally have a multiplier of 100 shares. Options on futures have a multiplier of 1 future. The multiplier on options on a future and the multiplier on the future can vary.
- **Vol bid, catching a bid, ripping/exploding:** Variety of terms for vol going up.
- **Vol offered, vol smashed/smoked:** Variety of terms for vol going down.
- **Teenie:** lowest priced options. Generally traded for movement risk purposes.
- **Theoretical Value (Theo):** based on all inputs, the current value a market maker believes an option is worth.
- **Sheets (or fair value):** same as above, but generally when referring to where something traded.
- **Liquidity:** how easy/hard it is to trade close to fair value. Generally determined by the number on contracts on the bid/offer, along with the width of the market.
- **Clearing houses**: Record keeper for trades

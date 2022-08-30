Project Description

When you assess whether to invest in an asset, you want to look not only at how much money you could make but also at how much risk you are taking. The Sharpe Ratio, developed by Nobel Prize winner William Sharpe some 50 years ago, does precisely this: it compares the return of an investment to that of an alternative and relates the relative return to the risk of the investment, measured by the standard deviation of returns.

In this project, you will apply the Sharpe ratio to real financial data using pandas.


Project Tasks

    1. Meet Professor William Sharpe
    2. A first glance at the data
    3. Plot & summarize daily prices for Amazon and Facebook
    4. Visualize & summarize daily values for the S&P 500
    5. The inputs for the Sharpe Ratio: Starting with Daily Stock Returns
    6. Daily S&P 500 returns
    7. Calculating Excess Returns for Amazon and Facebook vs. S&P 500
    8. The Sharpe Ratio, Step 1: The Average Difference in Daily Returns Stocks vs S&P 500
    9. The Sharpe Ratio, Step 2: Standard Deviation of the Return Difference
    10. Putting it all together
    11. Conclusion


Meet Professor William Sharpe
An investment may make sense if we expect it to return more money than it costs. But returns are only part of the story because they are risky - there may be a range of possible outcomes. How does one compare different investments that may deliver similar results on average, but exhibit different levels of risks?

The Sharpe ratio is usually calculated for a portfolio and uses the risk-free interest rate as benchmark. We will simplify our example and use stocks instead of a portfolio. We will also use a stock index as benchmark rather than the risk-free interest rate because both are readily available at daily frequencies and we do not have to get into converting interest rates from annual to daily frequency. Just keep in mind that you would run the same calculation with portfolio returns and your risk-free rate of choice, e.g, the 3-month Treasury Bill Rate. 

So let's learn about the Sharpe ratio by calculating it for the stocks of the two tech giants Facebook and Amazon. As benchmark we'll use the S&P 500 that measures the performance of the 500 largest stocks in the US. When we use a stock index instead of the risk-free rate, the result is called the Information Ratio and is used to benchmark the return on active portfolio management because it tells you how much more return for a given unit of risk your portfolio manager earned relative to just putting your money into a low-cost index fund.


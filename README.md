# Mean Reversion Pairs Backtester

This backtester identifies mean-reversion trading opportunities within equity pairs by using a rolling Augmented Dickney-Fuller test and obtaining trading signals when the rolling hedged spread significantly deviates from its mean.

## 📊 Performance Overview
The following results were generated using a 100-day rolling ADF window and a Z-score entry threshold of ±2.0.

| Pair | Sector | Sharpe Ratio | Annualized Returns| Max Drawdown |
| :--- | :--- | :--- | :--- | :---|
| **MU/NVDA** | Semiconductors | 1.29 | 9.25%| -5.34% |
| **BIIB/LLY** | Biotech | 0.93 | 5.26% | -3.79% |

## 📈 Top Performer: MU vs. NVDA
![MU vs NVDA Chart](results/MU_vs_NVDA.png)
*Figure 1: Equity curve and Z-score signals for the Semiconductor pair.*

## 🔬 Methodology
1. **Spread Formation:** The bot uses **Ordinary Least Squares** Regression over a set rolling window to find the optimal hedge ratio ($\beta$). I do this twice within the backtester for validation of a cointegrated relationship, and execution of trading signals. The formula I used for this is: $$\text{Spread}_t = \text{Price}_{A,t} - (\beta \times \text{Price}_{B,t})$$Where $\beta$ represents the relationship between the two assets.

2. **Cointegration:** The backtester uses a **100-day** lookback window to create a spread on which it performs an **Augmented Dickey-Fuller test**, in turn generating a p-value for cointegration between the two stocks. Since the ADF test evaluates the **stationarity** of the pair, we are looking for low p-values, which indicate that the spread's mean and variance are stable over time. This is repeated for each day in the market to ensure that the relationship holds.

3. **Signal:** A second, shorter lookback window of **30 days** is used to calculate more recent $\beta$ values, creating a more responsive spread. A **rolling Z-score** is then calculated, using a lookback window of 20 days. This is calculated by subtracting the rolling mean ($\mu$) from the current spread and then dividing by the rolling standard deviation ($\sigma$): $$Z = \frac{x - \mu}{\sigma}$$

4. **Position Generation:** The backtester has 2 main conditions for entry. Namely, the **p-value of the rolling ADF test must be < 0.1**, and the **correlation between the two stocks must be > 0.8**. If both conditions are met, the backtester then **shorts the spread whenever the Z-score is > 2**, and goes **long when the z-score is < -2**. It then maintains this position until the **z-score crosses 0**, as this maximizes profits from reversion.

5. **Exit Signals:** Outside of the z-score switching sign, the backtester will also choose to exit a trade if the **ADF p-value exceeds 0.15** or if the **correlation between the stocks falls below 0.5**, as these are indicators that the cointegration is weakening. Additionally, any **Z-score > |4|** will also cause the backtester to exit, as it is another indicator that the stocks are not cointegrated anymore. Finally, if the length of a trade exceeds **50 days**, the backtester will also stop trading, as the spread should have reverted to the mean within that time period.

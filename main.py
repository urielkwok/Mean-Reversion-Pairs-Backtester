import src.data_loader as dl
import src.analysis as an
import src.visualizer as vz
import src.backtester as bt

START_DATE, END_DATE = dl.get_dates()
STOCK_1 = "DASH"
STOCK_2 = "GRAB"
ADF_WINDOW = 252
BETA_WINDOW = 50
Z_WINDOW = 20

df = dl.get_data(STOCK_1, STOCK_2, START_DATE, END_DATE)
rolling_beta = an.rolling_beta(df, STOCK_1, STOCK_2, BETA_WINDOW)
df["spread"] = df[STOCK_2] - (rolling_beta.abs() * df[STOCK_1])
df["z-score"] = an.rolling_z_score(df["spread"], Z_WINDOW)
df["adf_p_value"] = an.rolling_adf_test(df["spread"], ADF_WINDOW)
bt.get_positions(df)
investment_price = (df[STOCK_2] + (rolling_beta * df[STOCK_1]))
df["cum_returns"] = bt.cum_returns(df, STOCK_1, STOCK_2, rolling_beta, ADF_WINDOW)
spy_returns = df["SPY"].pct_change().fillna(0)
spy_returns = spy_returns.iloc[ADF_WINDOW:]
df["cum_SPY"] = spy_returns.cumsum()
vz.plot_values(df)
bt.get_measurements(df, ADF_WINDOW)

import src.data_loader as dl
import src.analysis as an
import src.visualizer as vz
import src.backtester as bt

START_DATE, END_DATE = dl.get_dates()
STOCK_1 = "MU"
STOCK_2 = "NVDA"

# Separate rolling windows for each calculation,
# ADF test needs longer periods for accuracy.
ADF_WINDOW = 100
BETA_WINDOW = 30
Z_WINDOW = 20

# Create a dataframe with necessary entries to get positions
df = dl.get_data(STOCK_1, STOCK_2, START_DATE, END_DATE)
rolling_beta = an.rolling_beta(df, STOCK_1, STOCK_2, BETA_WINDOW)
df["spread"] = df[STOCK_2] - (rolling_beta.abs() * df[STOCK_1])
df["z-score"] = an.rolling_z_score(df["spread"], Z_WINDOW)
df["adf_p_value"] = an.rolling_adf_test(df, STOCK_1, STOCK_2, ADF_WINDOW)
df["correlation"] = df[STOCK_1].rolling(ADF_WINDOW).corr(df[STOCK_2])

# Convert all of our calculated measurements into positions
bt.get_positions(df)

# Cut off the largest window(ADF_WINDOW) from return calculations
# since data is still being gathered within that time period
df["cum_returns"] = bt.cum_returns(df, STOCK_1, STOCK_2, rolling_beta, ADF_WINDOW)
spy_returns = df["SPY"].pct_change().fillna(0)
spy_returns = spy_returns.iloc[ADF_WINDOW:]
df["cum_SPY"] = spy_returns.cumsum()

# Also start measurements after initial data gathering
vz.plot_values(df)
bt.get_measurements(df, ADF_WINDOW)

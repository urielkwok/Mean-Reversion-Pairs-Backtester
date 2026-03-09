import src.data_loader as dl
import src.analysis as an
import src.visualizer as vz
import src.backtester as bt

START_DATE, END_DATE = dl.get_dates()
STOCK_1 = "GRAB"
STOCK_2 = "DASH"
ROLLING_WINDOW = 30

stock_df = dl.get_data(STOCK_1, STOCK_2, START_DATE, END_DATE)
alpha, beta = an.OLS_regression(stock_df[STOCK_1], stock_df[STOCK_2])
stock_df["spread"] = stock_df[STOCK_2] - (alpha + beta * stock_df[STOCK_1])
stationary = an.adf_test(stock_df["spread"])
if stationary is True:
    print("Spread is stationary")
    z_scores = an.rolling_z_score(stock_df["spread"], ROLLING_WINDOW)
    stock_df["z-score"] = z_scores
    bt.get_positions(stock_df)
    stock_df["cumulative_returns"] = bt.cumulative_returns(stock_df["spread"], stock_df["position"])
    stock_df["cumulative_SPY"] = bt.cumulative_returns(stock_df["SPY"], stock_df["spy_position"])
    vz.plot_values(stock_df)
else:
    print("Spread is not stationary.")

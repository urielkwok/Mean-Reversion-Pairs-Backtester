import src.data_loader as dl
import src.analysis as an
import src.visualizer as vz

START_DATE, END_DATE = dl.get_dates()
STOCK_1 = "KO"
STOCK_2 = "PEP"
ROLLING_WINDOW = 30

stock_df = dl.get_data(STOCK_1, STOCK_2, START_DATE, END_DATE)
alpha, beta = an.OLS_regression(stock_df[STOCK_1], stock_df[STOCK_2])
spread = stock_df[STOCK_2] - (alpha + beta * stock_df[STOCK_1])
stationary = an.adf_test(spread)
if stationary is True:
    print("Spread is stationary")
    z_score = an.rolling_z_score(spread, ROLLING_WINDOW)
    vz.plot_z_values(z_score.dropna())
else:
    print("Spread is not stationary.")

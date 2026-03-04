import src.data_loader as dl
import src.analysis as an

START_DATE, END_DATE = dl.get_dates()
STOCK_1 = "KO"
STOCK_2 = "PEP"

stock_df = dl.get_data(STOCK_1, STOCK_2, START_DATE, END_DATE)
spread = stock_df[STOCK_1] - stock_df[STOCK_2]
stationary = an.adf_test(spread)
if stationary is True:
    print("Spread is stationary")
    print(an.z_score(spread))
else:
    print("Spread is not stationary.")

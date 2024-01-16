import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from TeamDataHistorical.get_rating import final_data

def fit_regression_line(result_list, slope_, y_intercept):
    return_list = []
    temp_list = []
    for x_value in result_list:
        predicted_y_value = x_value[1]*(slope_) +  y_intercept
        temp_list.append(predicted_y_value)
        print(predicted_y_value*82)
        temp_list.append(x_value[1])
        return_list.append(temp_list)
        temp_list = []

    return return_list


def plot_linear_regression(team_data, plot_regression_line):
    data = np.array(team_data)
    win_percentage = data[:, 0].reshape(-1, 1)
    net_rating = data[:, 1].reshape(-1, 1)

    model = LinearRegression()

    model.fit(net_rating, win_percentage)

    win_percentage_pred = model.predict(net_rating)

    plt.scatter(net_rating, win_percentage, color='blue', label='Data')
    if(plot_regression_line):
        plt.plot(net_rating, win_percentage_pred, color='red', linewidth=2, label='Linear Regression Line')


    rsqaured = r2_score(win_percentage, win_percentage_pred)
    print(rsqaured)

    slope = model.coef_[0][0]
    intercept = model.intercept_[0]

    print(slope)
    print(intercept)

    '''
    plot specific points of teams I want from past
    '''
    '''
    plt.scatter(10.11647, 0.87805, color='black', label='Bulls Win') #95-96 bulls
    plt.scatter(5.7326, 0.69512, color='black', label='Bulls Win') #92-93 bulls
    plt.scatter(8.63303, 0.817, color='black', label='Bulls Win') #91-92 bulls
    plt.scatter(7.49095, 0.7439, color='black', label='Bulls Win') #90-91 bulls
    '''
    plt.xlabel('Formulated ELO')
    plt.ylabel('Win Percentage')
    plt.title('Linear Regression: Formulated ELO vs Win Percentage')
    plt.legend()
    plt.show()

def get_regressed_data_historic():
    predicted_data = fit_regression_line(final_data, 0.0410576989, 0.4894025)
    plot_linear_regression(predicted_data, False)

def get_raw_data_historic():
    plot_linear_regression(final_data, True)
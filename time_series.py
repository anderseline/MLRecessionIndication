import pandas as pd
import numpy as np
import datetime
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification


def timeSeries(x_train, y_train, endSeries, x, y, model):
    model.fit(x_train, y_train)
    output = []
    for end in range(len(x_train), endSeries):
        model.fit(
            x[:end], y[:end]
        )
        try:
            step_data = [
                model.predict(x[:end + 1]),
                model.coef_
            ]
        except AttributeError:
            step_data = [
                model.predict(x[:end + 1]),
                model.feature_importances_
            ]
        output.append(step_data)
    return output

def sendToDF(output, x_train, x_time_series, y_time_series, model='nonlogit'):
    # get the weights of each indicator
    cci_coefs = []
    copper_coefs = []
    copper_pct_coefs = []
    gdp_coefs = []
    alc_coefs = []
    alc_pct_coefs = []
    spread_coefs = []
    emp_coefs = []
    emp_pct_coefs = []
    infl_coefs = []
    for i in range(len(output)):
        if model == 'nonlogit':
            coefs = output[i][1]
        #is logit
        else:
            coefs = output[i][1][0]
        cci_coefs.append(coefs[0])
        copper_coefs.append(coefs[1])
        copper_pct_coefs.append(coefs[2])
        gdp_coefs.append(coefs[3])
        alc_coefs.append(coefs[4])
        alc_pct_coefs.append(coefs[5])
        spread_coefs.append(coefs[6])
        emp_coefs.append(coefs[7])
        emp_pct_coefs.append(coefs[8])
        infl_coefs.append(coefs[9])

    # get all the predictions 
    preds = []
    for i in range(len(x_train), len(x_time_series)):
        step = i - len(x_train)
        preds.append(
            output[step][0][i]
        )

    # then add the dates
    dates = x_time_series['date']
    date_list = []
    for i in range(len(x_train), len(dates)):
        date_list.append(dates.loc[i])

    # and put all into a dataframe
    results = pd.DataFrame(list(zip(
        date_list, preds, cci_coefs, copper_coefs, copper_pct_coefs,
        gdp_coefs, alc_coefs, alc_pct_coefs, spread_coefs,
        emp_coefs, emp_pct_coefs, infl_coefs
        )),
        columns = [
            'date', 'pred', 'cci', 'copper', 'copper_pct', 'gdp',
            'alc', 'alc_pct', 'spread', 'emp', 'emp_pct',
            'inflation'
        ]
    )
    results['date'] = pd.to_datetime(results['date'])
    
    # now get the actual results, and combine predictions and date to make a dataframe ready for classifcation reporting
    actual = y_time_series.loc[len(x_train):len(x_time_series)]
    class_rep = pd.DataFrame(list(zip(
        date_list, preds, actual
    )),
    columns = [
        'date', 'pred', 'actual'
    ]
    )

    return results, class_rep


def factorWeightings(factors, values):
    most_neg = 1
    most_pos = -1
    least_imp = 1
    neg_ind = 0
    pos_ind = 0
    least_ind = 0
    ind = 0
    for i in values:
        abs_i = abs(i)
        if i < most_neg:
            most_neg = i
            neg_ind = ind
        elif i > most_pos:
            most_pos = i
            pos_ind = ind
        elif abs_i < least_imp:
            least_imp = i
            least_ind = ind
        ind += 1
    return factors[pos_ind], most_pos, factors[neg_ind], most_neg, factors[least_ind], least_imp
from sklearn.externals import joblib
import pandas as pd
import subprocess



def run_cmd(args_list):
    print('Running system command: {0}'.format(' '.join(args_list)))
    proc = subprocess.Popen(args_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    s_output, s_err = proc.communicate()
    s_return =  proc.returncode
    return s_return, s_output, s_err


def predict(data_frame):
    model_path = "/home/oleg/Стільниця/task/iris model/model/model.pkl"
    print(data_frame)
    with open(model_path, 'rb') as pickle_file:
        loaded_model = joblib.load(pickle_file)
        result = loaded_model.predict_proba(data_frame)
        return result


def convert_to_df(json):
    df = pd.DataFrame()
    df['petal_length'] = [json['petal_length']]
    df['petal_width'] = [json['petal_width']]
    df['sepal_length'] = [json['sepal_length']]
    df['sepal_width'] = [json['sepal_width']]
    return df

def deleteContent(fName):
    with open(fName, "w"):
        pass
    return 'success'

from app import predict, convert_to_df, run_cmd, deleteContent
from flask import Flask, request
import requests


app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def get_prediction():
    data = request.get_json()
    output = predict(convert_to_df(dict(data)))
    with open('output.csv', 'a+') as f:
        f.write(','.join(str(v) for v in output[0]) + "\n")
    return str(','.join(str(v) for v in output[0]))


@app.route("/put", methods=['GET'])
def import_to_hadoop():
    file = 'output.csv'
    hdfs_file_path = '/somedir'
    put = ['/home/oleg/hadoop/bin/hadoop', 'fs', '-appendToFile', file, hdfs_file_path + '/' + file]
    ret, out, err = run_cmd(put)
    deleteContent(file)
    print(ret, out, err)
    if ret == 0:
        output = "Success"
    else:
        output = err
    return "Result :%s" % output


@app.route("/get", methods=['Get'])
def get_from_hdfs():
    r = requests.get('http://127.0.0.1:50070/webhdfs/v1/somedir/output.csv?op=OPEN')
    return r.text


if __name__ == "__main__":
    app.run()

from flask import Flask, Response, render_template

import utils

#Flask handles HTTP requests
#pip install flask
#create text file in same path of script

app = Flask(__name__, template_folder='templates')

TEXT_FILE_PATH = utils.SCORES_FILE_NAME


@app.route('/content', methods=['GET'])
def score_server():
    try:
        with open(TEXT_FILE_PATH, 'r') as file:
            score_val = file.read()
            print(score_val)
            if score_val == str(utils.BAD_RETURN_CODE):
                return render_template('error_page.html', ERROR=score_val)
            else:
                return render_template('index.html', SCORE=score_val)
        #return Response(score_val,status=200,mimetype='text/plain')
    except FileNotFoundError:
        return Response("File not found", status=404, mimetype='text/plain')
    except Exception as e:
        return Response(f"An error occurred: {str(e)}", status=500, mimetype='text/plain')


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=8777, debug=True)

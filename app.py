'''
Created on Aug 1, 2022
Course work: 
@author: Vedha, Bagiya
Source:


    
'''

# Import necessary modules

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def start():

    return render_template('index.html')

@app.route('/result', methods = ['GET', "POST"])
def result():

    print ('1')

    cities = {
        'chennai': [ "Marina Beach", 'Guindy National Park'],
        'toronto': [ "Ontario Mall", 'CN Tower']
    }

    # if request.method == 'POST':

    city    = request.values.get("city")

    result = cities[city.lower()] 

    return render_template('index.html', result = result)

if __name__== "__main__":
    app.run(host="0.0.0.0", debug = True, port = 5003)
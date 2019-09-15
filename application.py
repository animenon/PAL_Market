from flask import Flask, render_template
import test
app = Flask(__name__)

paragraph = ''

@app.route("/")
def hello():
    #return "Yoho!"
    return render_template('index.html', paragraph='Welcome to PAL Market App!', pageType='index', title='Welcome to PAL Markets!')


@app.route('/data')
def dynamic_page():
    res = test.get_results()
    #return 'hello'
    #aragraph = 'Hello!\nPAL Markets is an app which can be used to predict Closing price for the day of any given stock.. ' \
    #'\nPredicted Closing price today: {}'.format(res)
    return render_template('index.html', paragraph='Hello! Welcome to PAL Market App!\nPAL Markets is an app which can be used to predict Closing price for the day of any given stock.. \nPredicted Closing price today: {}'.format(res), title='Results', pageType='results')


@app.route('/about')
def aboutpage():
    title = 'APL Market - About'
    pageType = 'about'
    #paragraph = 'Welcome to PAL Market App!' \
    #'nPAL Markets is an app which can be used to predict Closing price for the day of any given stock.. ' 
    return render_template('index.html', paragraph='Welcome to PAL Market App!\nPAL Markets is an app which can be used to predict Closing price for the day of any given stock.. ', pageType='about', title='About PAL Market')

#if __name__ == '__main__':
#    app.run(debug=True)


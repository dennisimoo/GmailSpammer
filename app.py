from flask import Flask, render_template, request
import spam

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        from_email = request.form['from_email']
        password = request.form['password']
        to_email = request.form['to_email']
        subject = request.form['subject']
        body = request.form['body']
        num_times = int(request.form['num_times'])
        
        result = spam.send_multiple_emails(subject, body, to_email, password, from_email, num_times)
        return render_template('index.html', result=result)

    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)

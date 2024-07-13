from flask import Flask, render_template
portfolio = Flask(__name__)
@portfolio.route('/')
def home():
    return render_template('portfolio.html')
@portfolio.route('/about')
def about():
    return render_template('about.html')
@portfolio.route('/contact')
def contact():
    return render_template('contact.html')

    l

@portfolio.route('/experience')
def experience():
    return render_template('experience.html')
@portfolio.route('/skill')
def skill():
    return render_template('skill.html')
@portfolio.route('/education')
def education():
    return render_template('education.html')
@portfolio.route('/project')
def project():
    return render_template('project.html')
if __name__ == "__main__":
    portfolio.run(debug=True)
from flask import Flask, render_template, request
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/<string:pagename>.html")
def router(pagename):
    return render_template(f"{pagename}.html")


@app.route("/submit_form",methods=['GET', 'POST'])
def submit_form():
    if request.method=='POST':
        data=request.form.to_dict()
        with open("form_data.txt","a") as cnt_file:
            cnt_file.write(f"{data}")
        return render_template("thankyou.html")


    else:
        return """Something Went Wrong
Please Try Again Later"""#return render_template("submit_form.html")

import os
import sys
from flask import Flask, render_template, request, redirect
from textSummarizer.pipeline.prediction import PredictionPipeline


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/train", methods=["GET", "POST"])
def training():
    if (request.method == "POST"):
        try:
            # Start training logic here
            os.system("python main.py")
            return render_template("train.html", message="Training started.")
        except Exception as e:
            return render_template("errors.html", error=e)
    return render_template("train.html")


# html file name and function must not be same. If they are same then it throws 
# `AssertionError: View function mapping is overwriting an existing endpoint function: train`
    
# @app.route("/predict", methods=['POST', 'GET'])
# def predict():
#     if request.method == "POST":
#         try:
#             # Get the input text from the form
#             text = request.form.get('text')
#             if not text:
#                 raise ValueError("No text provided for summarization")

#             # Use PredictionPipeline to generate the summary
#             obj = PredictionPipeline()
#             summary = obj.predict(text)

#             # Render the prediction result
#             return render_template("prediction.html", result=summary)
#         except Exception as e:
#             return render_template("errors.html", error=e)
#     else:
#         # If it's a GET request, render the input form
#         return render_template("prediction.html")

@app.route("/predict", methods=['POST', 'GET'])
def predict():
    if request.method == "POST":
        try:
            # Get the input text from the form
            input_text = request.form.get('text')
            if not input_text:
                raise ValueError("No text provided for summarization")

            # Use PredictionPipeline to generate the summary
            obj = PredictionPipeline()
            summary = obj.predict(input_text)

            # Send the entered text and summary back to the template
            return render_template("prediction.html", result=summary, input_text=input_text)
        except Exception as e:
            return render_template("error.html", error=e)
    else:
        # If it's a GET request, render the input form
        return render_template("prediction.html", input_text="")



if __name__=='__main__':
    app.run(debug=True)
from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])  # GET: website -> python, POST: python -> website
def main():
    """ Function that takes the input values, predicts the output and visualizes it on the website."""

    if request.method == 'POST':
        # Load the model
        with open('COMPO_model.pkl', 'rb') as f:
            model = pickle.load(f)

        # Denote inpute features
        input_features = [
            'density', 'modulus_elasticity', 'amount_hardener', 'content_epoxy_groups',
            'flash_point', 'surface_density', 'resin_consumption', 'stripe_angle', 
            'stripe_pitch', 'stripe_density', 'tensile_modulus_elasticity', 'tensile_strength'
        ]

        # Denote dataframe with input features
        df = pd.DataFrame(
            [
                [request.form.get(f) for f in input_features]
            ], columns=input_features
        )

        out = model.predict(df)[0]

    else:
        out = ''

    return render_template('main.html', output=out)

# Running the app
if __name__ == '__main__':
    app.run()
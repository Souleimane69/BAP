from flask import Flask, render_template, request, redirect, url_for
from produits import get_recommended_products 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/questionnaire', methods=['GET', 'POST'])
def questionnaire():
    if request.method == 'POST':
        symptoms = request.form.getlist('symptoms[]')
        intensite = request.form.get('intensite')
        duree = request.form.get('duree')
        frequence = request.form.get('frequence')
        allergies = request.form.getlist('allergies[]')
        traitements = request.form.getlist('traitements[]')

        recommended_products = get_recommended_products(symptoms, intensite, duree, frequence, allergies, traitements)

        el_mordjene = {
            'name': 'El Mordjene',
            'description': 'Un produit mystérieux aux bienfaits inconnus mais légendaires.',
            'image': 'images_product/elmorjene.png',
            'special': True 
        }

        recommended_products.append(el_mordjene)

        return render_template('produits.html', products=recommended_products)

    return render_template('questionnaire.html')

@app.route('/produits')
def produits():
    return render_template('produits.html', products=[])

if __name__ == '__main__':
    app.run(debug=True)

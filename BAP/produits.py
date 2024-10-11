def get_recommended_products(symptoms, intensite, duree, frequence, allergies, traitements):
    products = [
        {'name': 'Infusion de camomille', 'description': 'Soulage les troubles digestifs, calme l\'anxiété et favorise un meilleur sommeil.', 'image': 'images_product/camomille.png', 'symptoms': ['troubles_digestifs', 'stress_anxiete']},
        {'name': 'Huile essentielle de lavande', 'description': 'Apaise les douleurs musculaires, les maux de tête, et favorise la relaxation.', 'image': 'images_product/lavande.jpg', 'symptoms': ['douleurs_musculaires', 'maux_de_tete']},
        {'name': 'Tisane de menthe poivrée', 'description': 'Soulage les troubles digestifs et aide à réduire les maux de tête.', 'image': 'images_product/menthe_poivree.jpg', 'symptoms': ['maux_de_tete', 'troubles_digestifs']},
        {'name': 'Gingembre frais', 'description': 'Anti-inflammatoire naturel, soulage les nausées et améliore la digestion.', 'image': 'images_product/gingembre_frais.png', 'symptoms': ['troubles_digestifs']},
        {'name': 'Propolis', 'description': 'Renforce le système immunitaire et soulage les infections respiratoires légères.', 'image': 'images_product/propolis.png', 'symptoms': ['problemes_respiratoires']},
        {'name': 'Argile verte', 'description': 'Soulage les douleurs articulaires et les problèmes de peau.', 'image': 'images_product/argile_verte.jpg', 'symptoms': ['douleurs_articulaires', 'problemes_cutanes']},
        {'name': 'Curcuma', 'description': 'Anti-inflammatoire puissant, utile pour les douleurs articulaires et les troubles digestifs.', 'image': 'images_product/curcuma.png', 'symptoms': ['douleurs_articulaires', 'troubles_digestifs']},
        {'name': 'Huile de coco', 'description': 'Hydrate la peau et les cheveux, soulage les irritations cutanées.', 'image': 'images_product/huile_de_coco.jpg', 'symptoms': ['problemes_cutanes']},
        {'name': 'Ginseng', 'description': 'Tonique naturel, combat la fatigue et améliore la concentration.', 'image': 'images_product/ginseng.png', 'symptoms': ['fatigue_generale']},
        {'name': 'Thé vert', 'description': 'Riche en antioxydants, il aide à réduire le stress et améliore la digestion.', 'image': 'images_product/the_vert.png', 'symptoms': ['stress_anxiete', 'troubles_digestifs']},
        {'name': 'Tisane de fenouil', 'description': 'Aide à la digestion et réduit les ballonnements.', 'image': 'images_product/fenouil.png', 'symptoms': ['troubles_digestifs']},
        {'name': 'Huile essentielle d’eucalyptus', 'description': 'Soulage les congestions nasales et les affections respiratoires légères.', 'image': 'images_product/eucaliptus.jpg', 'symptoms': ['problemes_respiratoires']},
        {'name': 'Baume de calendula', 'description': 'Favorise la cicatrisation des plaies et apaise les irritations cutanées.', 'image': 'images_product/calendula.jpg', 'symptoms': ['problemes_cutanes']},
        {'name': 'Tisane de tilleul', 'description': 'Aide à réduire le stress, favorise un sommeil réparateur et calme les maux de tête légers.', 'image': 'images_product/tilleul.png', 'symptoms': ['stress_anxiete', 'maux_de_tete']},
        {'name': 'Aloe vera', 'description': 'Hydrate et apaise la peau, aide à la guérison des coups de soleil et des irritations.', 'image': 'images_product/aloe_vera.png', 'symptoms': ['problemes_cutanes']},
        {'name': 'Huile essentielle de tea tree', 'description': 'Antibactérienne et antifongique, idéale pour les infections cutanées mineures.', 'image': 'images_product/tea_tree.png', 'symptoms': ['problemes_cutanes']},
        {'name': 'Miel brut', 'description': 'Antibactérien naturel, soulage les maux de gorge et renforce le système immunitaire.', 'image': 'images_product/miel_brut.png', 'symptoms': ['problemes_respiratoires']},
        {'name': 'Millepertuis', 'description': 'Apaise les symptômes légers de dépression et d’anxiété.', 'image': 'images_product/millepertuis.png', 'symptoms': ['stress_anxiete']},
        {'name': 'Huile de ricin', 'description': 'Favorise la repousse des cheveux et hydrate en profondeur la peau.', 'image': 'images_product/huile_de_ricin.jpg', 'symptoms': ['problemes_cutanes']},
        {'name': 'Reine des prés', 'description': 'Anti-inflammatoire naturel, utile pour soulager les douleurs articulaires et les maux de tête.', 'image': 'images_product/reine_des_pres.png', 'symptoms': ['douleurs_articulaires', 'maux_de_tete']}
    ]

    recommended_products = []
    for product in products:
        for symptom in symptoms:
            if symptom in product['symptoms']:
                recommended_products.append(product)
                break

    return recommended_products

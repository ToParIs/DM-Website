import json

translations = {
    "en": {
        "nav": {
            "about": "About Us",
            "services": "Specialty & Services",
            "portfolio": "Portfolio",
            "team": "Our Team",
            "contact": "Contact Us",
            "lang_btn": "FR",
            "lang_label": "Français"
        },
        "hero": {
            "title_line1": "DAHL MARZIN INC.",
            "title_line2": "Structural Engineering Firm",
            "title_line3": "you can rely on",
            "btn_quote": "Tell Us About It",
            "scroll_down": "Scroll Down"
        },
        "about": {
            "title": "About Us",
            "p1": "DAHL MARZIN INC., is a structural engineering consulting firm since 1991 specializing in residential, commercial and industrial buildings. Our engineers are professionally trained in steel, concrete and wood structures.",
            "p2": "We design all types of structures and offer professional, optimal consultation, with efficient and simple solutions to help our clients meet their construction budget and timelines."
        },
        "services": {
            "title": "Our Services",
            "subtitle": "Specialty",
            "card1_title": "Design & Structures",
            "card1_items": [
                "Structures of Buildings",
                "Foundation Designs",
                "Steel & Concrete Structures",
                "Retaining Walls & Reservoirs",
                "Piles & Underpinning",
                "Restoration & Repair Existing Structures",
                "Timber Construction"
            ],
            "card2_title": "Building Types",
            "card2_items": [
                "Manufacturing & Warehouse facilities",
                "Underground Structures & Tunnels",
                "Multi-Story Residential Buildings",
                "Commercial & Industrial Buildings",
                "Hotels & Sport Centers",
                "Schools & Colleges",
                "Hospitals & Places of Worship"
            ],
            "card3_title": "Consulting & Inspection",
            "card3_items": [
                "Multi-level Parking",
                "Preliminary Studies & Cost Evaluations",
                "Technical Drawings & Specifications",
                "Feasibility Studies",
                "Analysis of Existing Structures",
                "Strength Assessment of Existing structures",
                "Full or Partial Surveillance"
            ],
            "bottom_text": "We provide solutions for new development projects and structural changes to existing structures. Every project is unique from minor implementations to major repairs, restorations & renovations. Our expert engineers and technicians will create, analyze designs, provide cost effective planning solutions while utilizing the latest technology during the design phase. Proudly servicing Canada & The United States of America."
        },
        "portfolio_teaser": {
            "tag": "PORTFOLIO",
            "title": "Projects",
            "desc": "With over 30 years of experience, our portfolio consists of thousands of projects. Here are some recently completed & some worth mentioning!",
            "btn": "View All Projects"
        },
        "team": {
            "title": "Our Team",
            "desc": "We are a group of dedicated Engineers & Technicians with over 30 years backed by industry experience. Our clients & partners are amongst North America's leading establishments.",
            "founder_badge": "Our Founder",
            "founder_name": "Silverio Marzin",
            "founder_title": "President & Founder of Dahl Marzin Inc. Since 1991"
        },
        "contact": {
            "badge": "Have a project you'd like to share with us?",
            "title": "Contact Us",
            "inquiries_title": "Inquiries",
            "inquiries_sub": "For inquiries or consultation please call or email us:",
            "phone_label": "Phone",
            "phone_val": "(514) 846-1040",
            "email_label": "Email",
            "email_val": "info@dahlmarzin.com",
            "careers_title": "Careers",
            "careers_desc": "To apply for a position at DAHL MARZIN, please send your resume and cover letter to:",
            "form_first_name": "First Name",
            "form_last_name": "Last Name",
            "form_email": "Email *",
            "form_phone": "Phone",
            "form_message": "Tell us about your project...",
            "form_submit": "Send Message",
            "form_success": "Thank you! Your message has been sent successfully.",
            "form_error": "Please fill in all required fields."
        },
        "footer": {
            "copyright": "© 2026 Dahl Marzin Inc. All Rights Reserved.",
            "tagline": "Professional Structural Engineering Consulting Since 1991"
        },
        "projects_page": {
            "title": "Projects Portfolio",
            "subtitle": "Selected Landmark Engineering Projects",
            "back_btn": "← Back to Home",
            "items": [
                {
                    "title": "M Sur la Montagne",
                    "category": "Heritage & Luxury Residential",
                    "desc": "Heritage building underwent transformation from College into a luxury living amid seven hundred thousand sq. foot private park in the heart of downtown Montreal. Structural designs for top floor units were added to the original building. In addition, a new development building was extended to the existing structure.",
                    "image": "assets/images/projects/M_SUR_LA_MONTAGNE.jpeg"
                },
                {
                    "title": "430 Sherbrooke St. E.",
                    "category": "Boutique Hotel & Historic Preservation",
                    "desc": "Located in Downtown Montreal. New development and structural design up to construction in accordance to preserving the existing front facade for this boutique hotel.",
                    "image": "assets/images/projects/430_Sherbroke_Est-Main.jpg"
                },
                {
                    "title": "Colisée Trois-Rivières",
                    "category": "Sports Center & Arena",
                    "desc": "Plans & specifications for a new development, in addition to inspection during the erection of the super structure. Projects included technical assistance for metalwork and concrete for interior seating staircase, support for curtain walls, bleacher guardrails, exterior ramp and concrete staircase at the main entrance.",
                    "image": "assets/images/projects/colisee_b.jpg"
                },
                {
                    "title": "Southam Lofts",
                    "category": "Industrial Heritage Loft Conversion",
                    "desc": "Conversion project featuring 10-story 'Tall & long' office building (built 1908-1916) into luxury loft living. Extensive restoration returning The Southam Building to its original state, fusing industrial elegance with modern minimalism.",
                    "image": "assets/images/projects/SOUTHAM_LOFTS.jpg"
                },
                {
                    "title": "U Building (Unity Building)",
                    "category": "Commercial & Residential",
                    "desc": "The historic Unity Building with a dynamic facade. Dahl Marzin provided structural design plans & specifications, converting a 14-storey apartment building into one-storey-high horizontal strips of mullion-free glazing while utilizing a commercial curtain wall system.",
                    "image": "assets/images/projects/U_BUILDING.jpg"
                },
                {
                    "title": "Albert Square Townhomes",
                    "category": "Prestigious Westmount Living",
                    "desc": "New development project preserving existing concrete structural frame and underpinning existing structure.",
                    "image": "assets/images/projects/ALBERT_SQUARE-2-main.png"
                },
                {
                    "title": "Tour des Canadiens 2",
                    "category": "High-Rise Tower",
                    "desc": "Montreal's most desirable living. Structural consulting, technical design assistance and inspections for high-density tower residence.",
                    "image": "assets/images/projects/Tour_de_Canadiens_2.jpeg"
                },
                {
                    "title": "Rooftop Structures Montreal",
                    "category": "Rooftop Expansion & Reinforcement",
                    "desc": "Structural engineering and load reinforcement designs for custom rooftop living, pools, and mechanical terraces across Montreal.",
                    "image": "assets/images/projects/Structural_Engineering_for_Montreal_Rooftop.png"
                }
            ]
        }
    },
    "fr": {
        "nav": {
            "about": "À Propos",
            "services": "Spécialités & Services",
            "portfolio": "Projets",
            "team": "Notre Équipe",
            "contact": "Contactez-nous",
            "lang_btn": "EN",
            "lang_label": "English"
        },
        "hero": {
            "title_line1": "DAHL MARZIN INC.",
            "title_line2": "Ingénierie structurelle",
            "title_line3": "sur laquelle vous pouvez compter",
            "btn_quote": "Parlez-nous en",
            "scroll_down": "Défiler vers le bas"
        },
        "about": {
            "title": "À Propos",
            "p1": "DAHL MARZIN INC. est une firme de consultation en ingénierie structurelle depuis 1991, spécialisée dans les bâtiments résidentiels, commerciaux et industriels. Nos ingénieurs sont professionnellement formés aux structures en acier, en béton et en bois.",
            "p2": "Nous concevons tous types de structures et offrons une consultation professionnelle et optimale, avec des solutions efficaces et simples pour aider nos clients à respecter leur budget et leurs délais de construction."
        },
        "services": {
            "title": "Nos Services",
            "subtitle": "Spécialités",
            "card1_title": "Conception & Structures",
            "card1_items": [
                "Structures de bâtiments",
                "Conceptions de fondation",
                "Structures en acier et en béton",
                "Murs de soutènement et réservoirs",
                "Pieux et sous-sol",
                "Restauration et réparation de structures existantes",
                "Construction en bois"
            ],
            "card2_title": "Types de Bâtiments",
            "card2_items": [
                "Installations de manufacture et entrepôts",
                "Structures souterraines et tunnels",
                "Bâtiments résidentiels à plusieurs étages",
                "Bâtiments commerciaux et industriels",
                "Hôtels & Centres sportifs",
                "Écoles et collèges",
                "Hôpitaux et lieux de culte"
            ],
            "card3_title": "Consultation & Surveillance",
            "card3_items": [
                "Stationnement à plusieurs niveaux",
                "Études préliminaires et évaluations des coûts",
                "Dessins techniques et spécifications",
                "Études de faisabilité",
                "Analyse des structures existantes",
                "Évaluation de la résistance des structures existantes",
                "Surveillance complète ou partielle"
            ],
            "bottom_text": "Nous fournissons des solutions pour des nouveaux projets de développement et des modifications structurelles de structures existantes. Chaque projet est unique, qu'il s'agisse de mises en œuvre mineures ou de réparations majeures, de restaurations et de rénovations. Nos ingénieurs et techniciens experts créeront et analyseront les conceptions, fourniront des solutions de planification rentables tout en utilisant les dernières technologies pendant la phase de conception. Nous sommes fiers d’offrir nos services au Canada et aux États-Unis d'Amérique."
        },
        "portfolio_teaser": {
            "tag": "PORTFOLIO",
            "title": "Projets",
            "desc": "Forts de plus de 30 ans d'expérience, notre portfolio compte des milliers de projets. Voici quelques réalisations récentes et d'envergure!",
            "btn": "Voir tous les projets"
        },
        "team": {
            "title": "Notre Équipe",
            "desc": "Nous sommes un groupe d'ingénieurs et de techniciens dévoués, forts d'une expérience de plus de 30 ans dans le secteur. Nos clients et partenaires comptent parmi les principales institutions d'Amérique du Nord.",
            "founder_badge": "Notre Fondateur",
            "founder_name": "Silverio Marzin",
            "founder_title": "Président & Fondateur de Dahl Marzin Inc. Depuis 1991"
        },
        "contact": {
            "badge": "Vous avez un projet que vous aimeriez partager avec nous ?",
            "title": "Contactez-nous",
            "inquiries_title": "Pour Informations",
            "inquiries_sub": "Pour toute demande de renseignements ou de consultation, appelez ou écrivez-nous :",
            "phone_label": "Téléphone",
            "phone_val": "(514) 846-1040",
            "email_label": "Courriel",
            "email_val": "info@dahlmarzin.com",
            "careers_title": "Carrières",
            "careers_desc": "Pour postuler chez DAHL MARZIN, veuillez envoyer votre lettre de motivation et curriculum vitae à :",
            "form_first_name": "Prénom",
            "form_last_name": "Nom",
            "form_email": "Courriel *",
            "form_phone": "Téléphone",
            "form_message": "Parlez-nous de votre projet...",
            "form_submit": "Envoyer le message",
            "form_success": "Merci! Votre message a été envoyé avec succès.",
            "form_error": "Veuillez remplir tous les champs obligatoires."
        },
        "footer": {
            "copyright": "© 2026 Dahl Marzin Inc. Tous droits réservés.",
            "tagline": "Firme conseil en ingénierie structurelle depuis 1991"
        },
        "projects_page": {
            "title": "Portfolio de Projets",
            "subtitle": "Sélection de Réalisations Majeures en Ingénierie",
            "back_btn": "← Retour à l'accueil",
            "items": [
                {
                    "title": "M Sur la Montagne",
                    "category": "Patrimoine & Résidentiel de Luxe",
                    "desc": "Transformation d'un collège patrimonial en résidences haut de gamme au cœur d'un parc privé de 700 000 pi² à Montréal. Conception structurale pour les unités de toit et agrandissement structural de l'immeuble existant.",
                    "image": "assets/images/projects/M_SUR_LA_MONTAGNE.jpeg"
                },
                {
                    "title": "430 Sherbrooke St. E.",
                    "category": "Hôtel Boutique & Préservation Historique",
                    "desc": "Au centre-ville de Montréal. Nouveau développement et conception structurale jusqu'à la construction, en préservant la façade existante pour cet hôtel boutique.",
                    "image": "assets/images/projects/430_Sherbroke_Est-Main.jpg"
                },
                {
                    "title": "Colisée Trois-Rivières",
                    "category": "Centre Sportif & Aréna",
                    "desc": "Plans et devis d'un nouveau complexe sportif et inspection lors du montage de la superstructure. Assistance technique métaux et béton pour gradins, murs rideaux, rampes extérieures et escaliers.",
                    "image": "assets/images/projects/colisee_b.jpg"
                },
                {
                    "title": "Southam Lofts",
                    "category": "Reconversion Industrielle en Lofts",
                    "desc": "Projet de conversion d'un immeuble de bureaux de 10 étages (bâti en 1908-1916) en lofts résidentiels haut de gamme, mariant authenticité industrielle et design moderne.",
                    "image": "assets/images/projects/SOUTHAM_LOFTS.jpg"
                },
                {
                    "title": "U Building (Édifice Unity)",
                    "category": "Commercial & Résidentiel",
                    "desc": "L'édifice historique Unity avec façade dynamique. Dahl Marzin a fourni les plans structuraux et devis pour transformer cet édifice de 14 étages avec système de murs-rideaux commerciaux.",
                    "image": "assets/images/projects/U_BUILDING.jpg"
                },
                {
                    "title": "Maisons de Ville Square Albert",
                    "category": "Prestigieux Projet Westmount",
                    "desc": "Projet de développement neuf préservant la charpente en béton existante et reprise en sous-œuvre de la structure existante.",
                    "image": "assets/images/projects/ALBERT_SQUARE-2-main.png"
                },
                {
                    "title": "Tour des Canadiens 2",
                    "category": "Tour Résidentielle de Grande Hauteur",
                    "desc": "L'une des plus prestigieuses tours résidentielles de Montréal. Consultation technique, assistance de conception et inspection.",
                    "image": "assets/images/projects/Tour_de_Canadiens_2.jpeg"
                },
                {
                    "title": "Structures de Toiture Montréal",
                    "category": "Aménagement et Renforcement Toit-Terrasse",
                    "desc": "Ingénierie structurale et renforcement de charges pour terrasses sur toit, piscines et équipements mécaniques à Montréal.",
                    "image": "assets/images/projects/Structural_Engineering_for_Montreal_Rooftop.png"
                }
            ]
        }
    }
}

with open('data/translations.json', 'w', encoding='utf-8') as f:
    json.dump(translations, f, indent=2, ensure_ascii=False)

print("translations.json created successfully!")

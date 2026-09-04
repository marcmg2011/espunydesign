# -*- coding: utf-8 -*-
import os
from string import Template

SITE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "https://espunydesign.com"

# ---------------------------------------------------------------
# Per-language content
# ---------------------------------------------------------------

COMMON = {
    "email": "manel@espunydesign.com",
    "phone_display": "+34 627 546 549",
    "phone_href": "+34627546549",
    "address_line1": "C/ Ramon Berenguer IV, 55, At. 2a",
    "address_line2": "TORTOSA",
    "facebook_url": "https://www.facebook.com/espunydesign",
    "instagram_url": "https://www.instagram.com/espunydesign",
    "form_action": "https://formsubmit.co/info@espunydesign.com",
}

LANGS = {
    "es": {
        "html_lang": "es",
        "path": "",  # root
        "meta_title": "EspunyDesign — Estudio de diseño y arquitectura del espacio",
        "meta_description": "Estudio de diseño y arquitectura del espacio. Especializados en diseño sostenible. Fundado por Manel Martínez Espuny en 1994.",
        "og_locale": "es_ES",
        "nav_projects": "proyectos.",
        "nav_services": "servicios.",
        "nav_about": "about.",
        "nav_contact": "contacto.",
        "nav_aria": "Menú principal",
        "nav_open_aria": "Abrir menú",
        "skip_link": "Ir al contenido",
        "form_subject": "Nuevo mensaje desde la web EspunyDesign",
        "hero_tagline": "Estudio de diseño y arquitectura del espacio",
        "hero_cta": "Ver proyectos",
        "hero_scroll": "scroll",
        "hero_logo_alt": "EspunyDesign 1963",
        "projects_title": "proyectos.",
        "projects_subtitle": "Una selección de nuestros trabajos recientes",
        "view_project": "Ver proyecto",
        "close_aria": "Cerrar",
        "project_salamandra_name": "Bar-Restaurante Salamandra",
        "project_salamandra_location": "Av. Generalitat 83, Tortosa",
        "project_castelldefels_name": "Castelldefels House",
        "project_castelldefels_location": "Castelldefels, Barcelona",
        "modal_lbl_location": "Ubicación",
        "modal_lbl_year": "Año",
        "modal_lbl_area": "Superficie",
        "modal_lbl_team": "Equipo",
        "modal_lbl_photo": "Fotografía",
        "team_salamandra": "ESPUNYDESIGN 1963",
        "team_castelldefels": "ESPUNYDESIGN 1963 (DISEÑO DE INTERIORES)",
        "photo_salamandra": "FREEINSTANTS",
        "photo_castelldefels": "CASA VIVA",
        "modal_desc_salamandra": "El proyecto parte de un reto atractivo y comprometido: mejorar el servicio para el confort de las personas. El bar-restaurante Salamandra ha sabido actualizarse sin perder jamás sus valores de origen: calidad, proximidad y bienestar. Por ello, el proyecto plantea una solución de arquitectura interior atemporal, capaz de ser elegante combinándola con la frescura y contemporaneidad requeridas. Elementos, iluminación y materiales dialogan desde el acceso para acompañar al usuario en los espacios.",
        "modal_desc_castelldefels": "En el proyecto de interiorismo, la selección de materiales, el color y la distribución del mobiliario aúnan las ideas claras del cliente con las propuestas innovadoras y contemporáneas del estudio showroom de diseño profesional y de interiores EspunyDesign de Tortosa, fuertemente vinculado a este proyecto y a su cliente. Materiales limpios y honestos definen la estética de la vivienda, muy enfocada a la practicidad del día a día para una familia numerosa. Ámbitos amplios y luminosos que se comunican visual o físicamente entre sí, o que se cierran para ofrecer privacidad al dormitorio principal. Un estudiado ejercicio de permeabilidad conecta el salón-comedor principal con la cocina y la zona de jardín/piscina, permitiendo a la propiedad disfrutar del espacio de planta baja casi sin barreras que obstaculicen su uso. Colores claros y objetos ligeros se combinan con detalles rotundos que dan fuerza al espacio en cada caso.",
        "more_work_title": "más trabajos.",
        "mw_dre": "Casa DRE",
        "mw_por": "Casa POR",
        "mw_terrassa": "Terrassa Ben",
        "mw_altres": "otros.",
        "services_title": "servicios.",
        "services_arch_title": "Arquitectura / Interiorismo",
        "services_arch_list": [
            "Redacción de Proyectos de edificación y Dirección de obra.",
            "Edificación nueva, rehabilitación y reforma.",
            "Vivienda unifamiliar, plurifamiliar.",
            "Proyectos de iluminación.",
            "Edificaciones industriales y comerciales.",
            "Equipamientos.",
            "Oficinas.",
        ],
        "services_other_title": "Otros Servicios",
        "services_other_list": [
            "Certificados e informes.",
            "Cédulas de habitabilidad.",
            "Certificados de eficiencia energética.",
            "Estudios y coordinación de seguridad y salud.",
            "Expedientes de actividad.",
            "Informe técnico del edificio.",
        ],
        "about_title": "about.",
        "about_p1": "espunydesign es un estudio de arquitectura, interiorismo, diseño y consultoría en creatividad con más de 60 años \u201cde experiencias\u201d 1963-2025.",
        "about_p2": "Compuesto por Manel Martínez Espuny, quien coordina el trabajo en equipo y el desarrollo de cada uno de los proyectos.",
        "about_image_alt": "Manel Martínez Espuny",
        "contact_title": "contacto.",
        "contact_lbl_email": "Email",
        "contact_lbl_phone": "Teléfono",
        "contact_lbl_address": "Dirección",
        "contact_form_name": "Nombre",
        "contact_ph_name": "Tu nombre",
        "contact_form_email": "Email",
        "contact_ph_email": "tu-correo@email.com",
        "contact_form_message": "Mensaje",
        "contact_ph_message": "Cuéntanos sobre tu proyecto...",
        "contact_btn_send": "Enviar mensaje",
        "contact_sending": "Enviando...",
        "footer_text": "© 2025 C/ Ramon Berenguer IV, 55, At. 2a. TORTOSA. / Tel. +34 627 546 549",
    },
    "ca": {
        "html_lang": "ca",
        "path": "ca/",
        "meta_title": "EspunyDesign — Estudi de disseny i arquitectura de l'espai",
        "meta_description": "Estudi de disseny i arquitectura de l'espai. Especialitzats en disseny sostenible. Fundat per Manel Martínez Espuny al 1994.",
        "og_locale": "ca_ES",
        "nav_projects": "projects.",
        "nav_services": "services.",
        "nav_about": "about.",
        "nav_contact": "contact.",
        "nav_aria": "Menú principal",
        "nav_open_aria": "Obrir menú",
        "skip_link": "Anar al contingut",
        "form_subject": "Nou missatge des de la web EspunyDesign",
        "hero_tagline": "Estudi de disseny i arquitectura de l'espai",
        "hero_cta": "Veure projectes",
        "hero_scroll": "scroll",
        "hero_logo_alt": "EspunyDesign 1963",
        "projects_title": "projects.",
        "projects_subtitle": "Una selecció dels nostres treballs recents",
        "view_project": "Veure projecte",
        "close_aria": "Tancar",
        "project_salamandra_name": "Bar-Restaurant Salamandra",
        "project_salamandra_location": "Av. Generalitat 83, Tortosa",
        "project_castelldefels_name": "Castelldefels House",
        "project_castelldefels_location": "Castelldefels, Barcelona",
        "modal_lbl_location": "Ubicació",
        "modal_lbl_year": "Any",
        "modal_lbl_area": "Superfície",
        "modal_lbl_team": "Equip",
        "modal_lbl_photo": "Fotografia",
        "team_salamandra": "ESPUNYDESIGN 1963",
        "team_castelldefels": "ESPUNYDESIGN 1963 (INTERIORISME)",
        "photo_salamandra": "FREEINSTANTS",
        "photo_castelldefels": "CASA VIVA",
        "modal_desc_salamandra": "El projecte parteix d'un repte atractiu i compromès: millorar el servei per a la comoditat de les persones. El bar-restaurant Salamandra ha sabut actualitzar-se sense perdre mai els seus valors d'origen: qualitat, proximitat i benestar. Per això, el projecte planteja una solució d'arquitectura interior atemporal, capaç de ser elegant combinant-la amb la frescor i contemporaneïtat requerides. Elements, il·luminació i materials dialoguen des de l'accés per acompanyar l'usuari en els espais.",
        "modal_desc_castelldefels": "En el projecte d'interiorisme, la selecció de materials, el color i la distribució del mobiliari conjuguen les idees clares del client amb les propostes innovadores i contemporànies de l'estudi showroom de disseny professional i d'interiors EspunyDesign de Tortosa, estretament vinculat a aquest projecte i al seu client. Materials nets i honestos defineixen l'estètica de la vivenda, molt enfocada a la practicitat del dia a dia per a una família nombrosa. Àmbits amplis i lluminosos que es comuniquen visual o físicament entre si, o que es tanquen per oferir privacitat al dormitori principal. Un estudiat exercici de permeabilitat connecta la sala d'estar i menjador principal amb la cuina i la zona de jardí/piscina, permetent a la propietat gaudir de l'espai de planta baixa gairebé sense barreres que n'obstaculitzin l'ús. Colors clars i objectes lleugers es combinen amb detalls rotunds que donen caràcter a l'espai en cada cas.",
        "more_work_title": "més treballs.",
        "mw_dre": "Casa DRE",
        "mw_por": "Casa POR",
        "mw_terrassa": "Terrassa Ben",
        "mw_altres": "altres.",
        "services_title": "services.",
        "services_arch_title": "Arquitectura / Interiorisme",
        "services_arch_list": [
            "Redacció de Projectes d'edificació i Direcció d'obra.",
            "Edificació nova, rehabilitació i reforma.",
            "Habitatge unifamiliar, plurifamiliar.",
            "Projectes d'il·luminació.",
            "Edificacions industrials i comercials.",
            "Equipaments.",
            "Oficines.",
        ],
        "services_other_title": "Altres Serveis",
        "services_other_list": [
            "Certificats i informes.",
            "Cèdules d'habitabilitat.",
            "Certificats d'eficencia energètica.",
            "Estudis i coordinació de seguretat i salut.",
            "Expedients d'activitat.",
            "Informe tècnic de l'edifici.",
        ],
        "about_title": "about.",
        "about_p1": "espunydesign es un estudi d'arquitectura, interiorisme, disseny i consultoria en creativitat amb més de 60 anys \u201cd'experiències\u201d 1963-2025.",
        "about_p2": "Composat per Manel Martínez Espuny, qui coordina el treball en equip i el desenvolupament de cada un dels projectes.",
        "about_image_alt": "Manel Martínez Espuny",
        "contact_title": "contact.",
        "contact_lbl_email": "Email",
        "contact_lbl_phone": "Telèfon",
        "contact_lbl_address": "Adreça",
        "contact_form_name": "Nom",
        "contact_ph_name": "El teu nom",
        "contact_form_email": "Email",
        "contact_ph_email": "el-teu@email.com",
        "contact_form_message": "Missatge",
        "contact_ph_message": "Explica'ns el teu projecte...",
        "contact_btn_send": "Enviar missatge",
        "contact_sending": "Enviant...",
        "footer_text": "© 2025 c/ Ramon Berenguer IV, 55, At. 2a. TORTOSA. / Telf. +34 627 546 549",
    },
    "en": {
        "html_lang": "en",
        "path": "en/",
        "meta_title": "EspunyDesign — Spatial Design & Architecture Studio",
        "meta_description": "Spatial design and architecture studio. Specialized in sustainable design. Founded by Manel Martínez Espuny in 1994.",
        "og_locale": "en_US",
        "nav_projects": "projects.",
        "nav_services": "services.",
        "nav_about": "about.",
        "nav_contact": "contact.",
        "nav_aria": "Main menu",
        "nav_open_aria": "Open menu",
        "skip_link": "Skip to content",
        "form_subject": "New message from the EspunyDesign website",
        "hero_tagline": "Spatial design and architecture studio",
        "hero_cta": "View projects",
        "hero_scroll": "scroll",
        "hero_logo_alt": "EspunyDesign 1963",
        "projects_title": "projects.",
        "projects_subtitle": "A selection of our recent work",
        "view_project": "View project",
        "close_aria": "Close",
        "project_salamandra_name": "Bar-Restaurant Salamandra",
        "project_salamandra_location": "Av. Generalitat 83, Tortosa",
        "project_castelldefels_name": "Castelldefels House",
        "project_castelldefels_location": "Castelldefels, Barcelona",
        "modal_lbl_location": "Location",
        "modal_lbl_year": "Year",
        "modal_lbl_area": "Area",
        "modal_lbl_team": "Team",
        "modal_lbl_photo": "Photography",
        "team_salamandra": "ESPUNYDESIGN 1963",
        "team_castelldefels": "ESPUNYDESIGN 1963 (INTERIOR DESIGN)",
        "photo_salamandra": "FREEINSTANTS",
        "photo_castelldefels": "CASA VIVA",
        "modal_desc_salamandra": "The project starts from an attractive yet committed challenge: improving the service for the comfort of people. The Salamandra bar-restaurant has managed to update itself without ever losing its original values: quality, proximity, and well-being. For this reason, the project proposes a timeless interior architecture solution, capable of being elegant while combining it with the freshness and contemporary feel required. Elements, lighting, and materials interact from the entrance to guide the user into the spaces.",
        "modal_desc_castelldefels": "In the interior design project, the selection of materials, color, and furniture layout combine the client's clear ideas with the innovative and contemporary proposals from the professional & interior design showroom studio EspunyDesign from Tortosa, strongly linked to this project and its client. Clean and honest materials define the aesthetic of the house, which is highly focused on the practicality of daily life for a large family. Spacious, bright areas that communicate visually or physically with each other, or are enclosed to offer privacy to the master bedroom. A studied exercise in permeability connects the main living and dining room with the kitchen and the garden/pool area, allowing the property to enjoy the ground floor space almost without barriers hindering its use. Light colors and lightweight objects are combined with bold details that add strength to the space in each case.",
        "more_work_title": "more work.",
        "mw_dre": "Casa DRE",
        "mw_por": "Casa POR",
        "mw_terrassa": "Terrassa Ben",
        "mw_altres": "other.",
        "services_title": "services.",
        "services_arch_title": "Architecture / Interior Design",
        "services_arch_list": [
            "Building project drafting and construction management.",
            "New construction, rehabilitation, and renovation.",
            "Single-family and multi-family housing.",
            "Lighting design projects.",
            "Industrial and commercial buildings.",
            "Public and private facilities.",
            "Offices.",
        ],
        "services_other_title": "Other Services",
        "services_other_list": [
            "Certificates and technical reports.",
            "Certificates of occupancy.",
            "Energy efficiency certificates.",
            "Health and safety studies and coordination.",
            "Activity and opening licenses.",
            "Building technical inspection reports (ITE).",
        ],
        "about_title": "about.",
        "about_p1": "espunydesign is an architecture, interior design, and creative consulting studio with more than 60 years of \u201cexperiences\u201d 1963\u20132025.",
        "about_p2": "Led by Manel Martínez Espuny, who coordinates teamwork and the comprehensive development of each project.",
        "about_image_alt": "Manel Martínez Espuny",
        "contact_title": "contact.",
        "contact_lbl_email": "Email",
        "contact_lbl_phone": "Phone",
        "contact_lbl_address": "Address",
        "contact_form_name": "Name",
        "contact_ph_name": "Your name",
        "contact_form_email": "Email",
        "contact_ph_email": "your-email@email.com",
        "contact_form_message": "Message",
        "contact_ph_message": "Tell us about your project...",
        "contact_btn_send": "Send message",
        "contact_sending": "Sending...",
        "footer_text": "© 2025 C/ Ramon Berenguer IV, 55, At. 2a. Tortosa (Spain). / Tel. +34 627 546 549",
    },
}

print("Loaded language dicts:", list(LANGS.keys()))

# ---------------------------------------------------------------
# HTML template (uses $identifier placeholders -> string.Template)
# ---------------------------------------------------------------

HEAD_TEMPLATE = Template("""<!DOCTYPE html>
<html lang="$html_lang">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>$meta_title</title>
    <meta name="description" content="$meta_description">
    <meta name="keywords" content="arquitectura, interiorisme, interiorismo, architecture, disseny, diseño, design, Tortosa, EspunyDesign, Manel Martínez Espuny">
    <meta name="author" content="EspunyDesign">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="$canonical">

    <!-- hreflang alternates -->
    <link rel="alternate" hreflang="es" href="$DOMAIN/">
    <link rel="alternate" hreflang="ca" href="$DOMAIN/ca/">
    <link rel="alternate" hreflang="en" href="$DOMAIN/en/">
    <link rel="alternate" hreflang="x-default" href="$DOMAIN/">

    <!-- Open Graph / Twitter -->
    <meta property="og:type" content="website">
    <meta property="og:title" content="$meta_title">
    <meta property="og:description" content="$meta_description">
    <meta property="og:url" content="$canonical">
    <meta property="og:image" content="$DOMAIN/assets/img/hero.jpg">
    <meta property="og:locale" content="$og_locale">
    <meta property="og:site_name" content="EspunyDesign">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="$meta_title">
    <meta name="twitter:description" content="$meta_description">
    <meta name="twitter:image" content="$DOMAIN/assets/img/hero.jpg">

    <!-- Icons -->
    <link rel="icon" href="/favicon.ico" sizes="any">
    <link rel="icon" href="/favicon-32.png" type="image/png" sizes="32x32">
    <link rel="icon" href="/favicon-16.png" type="image/png" sizes="16x16">
    <link rel="apple-touch-icon" href="/apple-touch-icon.png">
    <link rel="manifest" href="/site.webmanifest">
    <meta name="theme-color" content="#1a1a1a">

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,500;1,400&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/assets/css/style.css">

    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "ProfessionalService",
      "name": "EspunyDesign",
      "alternateName": "espunydesign 1963",
      "description": "$meta_description",
      "founder": {
        "@type": "Person",
        "name": "Manel Martínez Espuny"
      },
      "foundingDate": "1963",
      "email": "$email",
      "telephone": "$phone_display",
      "url": "$canonical",
      "image": "$DOMAIN/assets/img/hero.jpg",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "$address_line1",
        "addressLocality": "Tortosa",
        "addressRegion": "Tarragona",
        "addressCountry": "ES"
      },
      "sameAs": [
        "$facebook_url",
        "$instagram_url"
      ]
    }
    </script>
</head>
""")

BODY_TEMPLATE = Template("""<body>

    <a class="skip-link" href="#main">$skip_link</a>

    <!-- Navigation -->
    <header id="header" class="header">
        <nav class="nav" aria-label="$nav_aria">
            <a href="$home_path" class="nav__logo" id="nav-logo" aria-label="EspunyDesign">
                <img src="/assets/img/logo.png" alt="$hero_logo_alt" class="nav__logo-img" width="398" height="138">
            </a>

            <div class="nav__right">
                <ul class="nav__menu" id="nav-menu">
                    <li><a href="#projects" class="nav__link" data-section="projects">$nav_projects</a></li>
                    <li><a href="#services" class="nav__link" data-section="services">$nav_services</a></li>
                    <li><a href="#about" class="nav__link" data-section="about">$nav_about</a></li>
                    <li><a href="#contact" class="nav__link" data-section="contact">$nav_contact</a></li>
                    <li class="nav__lang-mobile">
                        <div class="lang-switch lang-switch--mobile">
                            $lang_links_mobile
                        </div>
                    </li>
                </ul>

                <div class="lang-switch lang-switch--desktop" id="lang-switch">
                    $lang_links_desktop
                </div>

                <button class="nav__toggle" id="nav-toggle" aria-label="$nav_open_aria" aria-controls="nav-menu" aria-expanded="false">
                    <span class="nav__toggle-line"></span>
                    <span class="nav__toggle-line"></span>
                    <span class="nav__toggle-line"></span>
                </button>
            </div>
        </nav>
    </header>

    <main id="main">
    <!-- Hero Section -->
    <section id="hero" class="hero">
        <div class="hero__bg">
            <picture>
                <source srcset="/assets/img/hero.webp" type="image/webp">
                <img src="/assets/img/hero.jpg" alt="" class="hero__bg-img" width="1898" height="1092" fetchpriority="high">
            </picture>
            <div class="hero__overlay"></div>
        </div>
        <div class="hero__content">
            <div class="hero__brand">
                <img src="/assets/img/logo.png" alt="$hero_logo_alt" class="hero__logo" width="398" height="138">
            </div>
            <p class="hero__tagline">$hero_tagline</p>
            <div class="hero__cta">
                <a href="#projects" class="btn btn--primary" id="hero-cta-projects">$hero_cta</a>
            </div>
        </div>
        <div class="hero__scroll">
            <span class="hero__scroll-text">$hero_scroll</span>
            <div class="hero__scroll-line"></div>
        </div>
    </section>

    <!-- Projects Section -->
    <section id="projects" class="section projects">
        <div class="container">
            <h1 class="section__title">$projects_title</h1>
            <p class="section__subtitle">$projects_subtitle</p>

            <div class="projects__grid">

                <article class="project-card" id="project-salamandra" data-modal="modal-salamandra" tabindex="0" role="button" aria-haspopup="dialog">
                    <div class="project-card__image-wrapper">
                        <picture>
                            <source srcset="/assets/img/projects/salamandra.webp" type="image/webp">
                            <img src="/assets/img/projects/salamandra.jpg" alt="$project_salamandra_name, Tortosa" class="project-card__image" loading="lazy" width="405" height="271">
                        </picture>
                        <div class="project-card__overlay">
                            <span class="project-card__view">$view_project</span>
                        </div>
                    </div>
                    <div class="project-card__info">
                        <h2 class="project-card__name">$project_salamandra_name</h2>
                        <div class="project-card__meta">
                            <span class="project-card__location">$project_salamandra_location</span>
                            <span class="project-card__divider">·</span>
                            <span class="project-card__year">2019</span>
                            <span class="project-card__divider">·</span>
                            <span class="project-card__area">140 m²</span>
                        </div>
                    </div>
                </article>

                <article class="project-card" id="project-castelldefels" data-modal="modal-castelldefels" tabindex="0" role="button" aria-haspopup="dialog">
                    <div class="project-card__image-wrapper">
                        <picture>
                            <source srcset="/assets/img/projects/castelldefels.webp" type="image/webp">
                            <img src="/assets/img/projects/castelldefels.jpg" alt="$project_castelldefels_name, Barcelona" class="project-card__image" loading="lazy" width="399" height="271">
                        </picture>
                        <div class="project-card__overlay">
                            <span class="project-card__view">$view_project</span>
                        </div>
                    </div>
                    <div class="project-card__info">
                        <h2 class="project-card__name">$project_castelldefels_name</h2>
                        <div class="project-card__meta">
                            <span class="project-card__location">$project_castelldefels_location</span>
                            <span class="project-card__divider">·</span>
                            <span class="project-card__year">2012</span>
                            <span class="project-card__divider">·</span>
                            <span class="project-card__area">300 m²</span>
                        </div>
                    </div>
                </article>

            </div>

            <div class="more-work">
                <p class="more-work__title">$more_work_title</p>
                <div class="more-work__grid">
                    <button type="button" class="more-work__item" data-name="$mw_dre" data-full="/assets/img/projects/casa-dre.jpg">
                        <picture>
                            <source srcset="/assets/img/projects/casa-dre.webp" type="image/webp">
                            <img src="/assets/img/projects/casa-dre.jpg" alt="$mw_dre" loading="lazy" width="900" height="675">
                        </picture>
                        <span class="more-work__name">$mw_dre</span>
                    </button>
                    <button type="button" class="more-work__item" data-name="$mw_por" data-full="/assets/img/projects/casa-por.jpg">
                        <picture>
                            <source srcset="/assets/img/projects/casa-por.webp" type="image/webp">
                            <img src="/assets/img/projects/casa-por.jpg" alt="$mw_por" loading="lazy" width="361" height="271">
                        </picture>
                        <span class="more-work__name">$mw_por</span>
                    </button>
                    <button type="button" class="more-work__item" data-name="$mw_terrassa" data-full="/assets/img/projects/terrassa-ben.jpg">
                        <picture>
                            <source srcset="/assets/img/projects/terrassa-ben.webp" type="image/webp">
                            <img src="/assets/img/projects/terrassa-ben.jpg" alt="$mw_terrassa" loading="lazy" width="405" height="271">
                        </picture>
                        <span class="more-work__name">$mw_terrassa</span>
                    </button>
                    <button type="button" class="more-work__item" data-name="$mw_altres" data-full="/assets/img/projects/altres.jpg">
                        <picture>
                            <source srcset="/assets/img/projects/altres.webp" type="image/webp">
                            <img src="/assets/img/projects/altres.jpg" alt="$mw_altres" loading="lazy" width="381" height="271">
                        </picture>
                        <span class="more-work__name">$mw_altres</span>
                    </button>
                </div>
            </div>
        </div>
    </section>

    <!-- Project Detail Modal: Salamandra -->
    <div class="modal" id="modal-salamandra" aria-hidden="true" role="dialog" aria-modal="true" aria-labelledby="modal-salamandra-title">
        <div class="modal__backdrop" data-close-modal></div>
        <div class="modal__content">
            <button class="modal__close" data-close-modal aria-label="$close_aria">&times;</button>
            <div class="modal__header">
                <h2 class="modal__title" id="modal-salamandra-title">$project_salamandra_name</h2>
            </div>
            <div class="modal__details">
                <div class="modal__detail-grid">
                    <div class="modal__detail">
                        <span class="modal__label">$modal_lbl_location</span>
                        <span class="modal__value">$project_salamandra_location</span>
                    </div>
                    <div class="modal__detail">
                        <span class="modal__label">$modal_lbl_year</span>
                        <span class="modal__value">2019</span>
                    </div>
                    <div class="modal__detail">
                        <span class="modal__label">$modal_lbl_area</span>
                        <span class="modal__value">140 m²</span>
                    </div>
                    <div class="modal__detail">
                        <span class="modal__label">$modal_lbl_team</span>
                        <span class="modal__value">$team_salamandra</span>
                    </div>
                    <div class="modal__detail">
                        <span class="modal__label">$modal_lbl_photo</span>
                        <span class="modal__value">$photo_salamandra</span>
                    </div>
                </div>
            </div>
            <p class="modal__description">$modal_desc_salamandra</p>
            <div class="modal__gallery">
                <picture>
                    <source srcset="/assets/img/projects/salamandra.webp" type="image/webp">
                    <img src="/assets/img/projects/salamandra.jpg" alt="$project_salamandra_name" loading="lazy" width="405" height="271">
                </picture>
            </div>
        </div>
    </div>

    <!-- Project Detail Modal: Castelldefels -->
    <div class="modal" id="modal-castelldefels" aria-hidden="true" role="dialog" aria-modal="true" aria-labelledby="modal-castelldefels-title">
        <div class="modal__backdrop" data-close-modal></div>
        <div class="modal__content">
            <button class="modal__close" data-close-modal aria-label="$close_aria">&times;</button>
            <div class="modal__header">
                <h2 class="modal__title" id="modal-castelldefels-title">$project_castelldefels_name</h2>
            </div>
            <div class="modal__details">
                <div class="modal__detail-grid">
                    <div class="modal__detail">
                        <span class="modal__label">$modal_lbl_location</span>
                        <span class="modal__value">$project_castelldefels_location</span>
                    </div>
                    <div class="modal__detail">
                        <span class="modal__label">$modal_lbl_year</span>
                        <span class="modal__value">2012</span>
                    </div>
                    <div class="modal__detail">
                        <span class="modal__label">$modal_lbl_area</span>
                        <span class="modal__value">300 m²</span>
                    </div>
                    <div class="modal__detail">
                        <span class="modal__label">$modal_lbl_team</span>
                        <span class="modal__value">$team_castelldefels</span>
                    </div>
                    <div class="modal__detail">
                        <span class="modal__label">$modal_lbl_photo</span>
                        <span class="modal__value">$photo_castelldefels</span>
                    </div>
                </div>
            </div>
            <p class="modal__description">$modal_desc_castelldefels</p>
            <div class="modal__gallery">
                <picture>
                    <source srcset="/assets/img/projects/castelldefels.webp" type="image/webp">
                    <img src="/assets/img/projects/castelldefels.jpg" alt="$project_castelldefels_name" loading="lazy" width="399" height="271">
                </picture>
            </div>
        </div>
    </div>

    <!-- Secondary gallery lightbox -->
    <div class="modal lightbox" id="lightbox" aria-hidden="true" role="dialog" aria-modal="true" aria-label="$view_project">
        <div class="modal__backdrop" data-close-modal></div>
        <div class="modal__content">
            <button class="modal__close" data-close-modal aria-label="$close_aria">&times;</button>
            <img class="lightbox__img" src="" alt="">
            <p class="lightbox__caption"></p>
        </div>
    </div>

    <!-- Services Section -->
    <section id="services" class="section services">
        <div class="container">
            <h2 class="section__title">$services_title</h2>

            <div class="services__grid">

                <div class="service-block" id="service-architecture">
                    <div class="service-block__icon">
                        <svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                            <rect x="8" y="20" width="48" height="36" rx="2"/>
                            <path d="M8 20L32 8L56 20"/>
                            <line x1="24" y1="36" x2="24" y2="56"/>
                            <line x1="40" y1="36" x2="40" y2="56"/>
                            <line x1="24" y1="36" x2="40" y2="36"/>
                        </svg>
                    </div>
                    <h3 class="service-block__title">$services_arch_title</h3>
                    <ul class="service-block__list">
$services_arch_items
                    </ul>
                </div>

                <div class="service-block" id="service-other">
                    <div class="service-block__icon">
                        <svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                            <rect x="12" y="8" width="40" height="48" rx="3"/>
                            <line x1="20" y1="20" x2="44" y2="20"/>
                            <line x1="20" y1="28" x2="44" y2="28"/>
                            <line x1="20" y1="36" x2="36" y2="36"/>
                            <path d="M38 44L42 48L50 40"/>
                        </svg>
                    </div>
                    <h3 class="service-block__title">$services_other_title</h3>
                    <ul class="service-block__list">
$services_other_items
                    </ul>
                </div>

            </div>
        </div>
    </section>

    <!-- About Section -->
    <section id="about" class="section about">
        <div class="container">
            <h2 class="section__title">$about_title</h2>
            <div class="about__content">
                <div class="about__image-wrapper">
                    <picture>
                        <source srcset="/assets/img/manel-espuny.webp" type="image/webp">
                        <img src="/assets/img/manel-espuny.jpg" alt="$about_image_alt" class="about__image" loading="lazy" width="147" height="98">
                    </picture>
                    <div class="about__image-label">$about_image_alt</div>
                </div>
                <div class="about__text">
                    <div class="about__logo">
                        <img src="/assets/img/logo-mark.png" alt="ed 1963" class="about__logo-img" width="192" height="192">
                    </div>
                    <p class="about__paragraph">$about_p1</p>
                    <p class="about__paragraph">$about_p2</p>
                    <div class="about__years">
                        <span class="about__year-start">1963</span>
                        <div class="about__year-line"></div>
                        <span class="about__year-end">2025</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="section contact">
        <div class="container">
            <h2 class="section__title">$contact_title</h2>

            <div class="contact__grid">

                <div class="contact__info" id="contact-info">
                    <div class="contact__info-item">
                        <span class="contact__info-label">$contact_lbl_email</span>
                        <a href="mailto:$email" class="contact__info-value">$email</a>
                    </div>
                    <div class="contact__info-item">
                        <span class="contact__info-label">$contact_lbl_phone</span>
                        <a href="tel:$phone_href" class="contact__info-value">$phone_display</a>
                    </div>
                    <div class="contact__info-item">
                        <span class="contact__info-label">$contact_lbl_address</span>
                        <span class="contact__info-value">$address_line1<br>$address_line2</span>
                    </div>
                    <div class="contact__social">
                        <a href="$facebook_url" target="_blank" rel="noopener noreferrer" class="contact__social-link" aria-label="Facebook">
                            <svg viewBox="0 0 24 24" fill="currentColor" width="22" height="22" aria-hidden="true"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
                        </a>
                        <a href="$instagram_url" target="_blank" rel="noopener noreferrer" class="contact__social-link" aria-label="Instagram">
                            <svg viewBox="0 0 24 24" fill="currentColor" width="22" height="22" aria-hidden="true"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg>
                        </a>
                    </div>
                </div>

                <form class="contact__form" id="contact-form" action="$form_action" method="POST">
                    <input type="hidden" name="_subject" value="$form_subject">
                    <input type="hidden" name="_captcha" value="false">
                    <input type="hidden" name="_next" value="$canonical#contact">
                    <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
                    <div class="form-group">
                        <label for="form-name" class="form-label">$contact_form_name</label>
                        <input type="text" id="form-name" name="name" class="form-input" required placeholder="$contact_ph_name">
                    </div>
                    <div class="form-group">
                        <label for="form-email" class="form-label">$contact_form_email</label>
                        <input type="email" id="form-email" name="email" class="form-input" required placeholder="$contact_ph_email">
                    </div>
                    <div class="form-group">
                        <label for="form-message" class="form-label">$contact_form_message</label>
                        <textarea id="form-message" name="message" class="form-input form-textarea" required placeholder="$contact_ph_message" rows="5"></textarea>
                    </div>
                    <button type="submit" class="btn btn--primary btn--full" id="form-submit" data-sending-text="$contact_sending">$contact_btn_send</button>
                </form>
            </div>
        </div>
    </section>
    </main>

    <!-- Footer -->
    <footer class="footer" id="footer">
        <div class="container">
            <div class="footer__content">
                <img src="/assets/img/logo.png" alt="$hero_logo_alt" class="footer__logo" width="398" height="138">
                <p class="footer__text">$footer_text</p>
            </div>
        </div>
    </footer>

    <script src="/assets/js/main.js" defer></script>
</body>
</html>
""")

def render_lang_links(current, style):
    """style: 'mobile' renders bigger buttons, 'desktop' compact with dividers"""
    order = ["ca", "es", "en"]
    hrefs = {"es": "/", "ca": "/ca/", "en": "/en/"}
    labels = {"es": "ES", "ca": "CA", "en": "EN"}
    parts = []
    for i, code in enumerate(order):
        active = " active" if code == current else ""
        parts.append(f'<a href="{hrefs[code]}" class="lang-btn{active}" aria-label="{labels[code]}"{" aria-current=\"page\"" if code == current else ""}>{labels[code]}</a>')
        if i < len(order) - 1:
            parts.append('<span class="lang-divider">/</span>')
    joiner = "\n                            " if style == "mobile" else "\n                    "
    return joiner.join(parts)

def render_list_items(items):
    return "\n".join(f"                        <li>{item}</li>" for item in items)

def build_page(lang_code, lang):
    ctx = dict(COMMON)
    ctx.update(lang)
    ctx["DOMAIN"] = DOMAIN
    ctx["canonical"] = f"{DOMAIN}/{lang['path']}"
    ctx["home_path"] = f"/{lang['path']}"
    ctx["lang_links_desktop"] = render_lang_links(lang_code, "desktop")
    ctx["lang_links_mobile"] = render_lang_links(lang_code, "mobile")
    ctx["services_arch_items"] = render_list_items(lang["services_arch_list"])
    ctx["services_other_items"] = render_list_items(lang["services_other_list"])

    head = HEAD_TEMPLATE.substitute(ctx)
    body = BODY_TEMPLATE.substitute(ctx)
    return head + body

for code, data in LANGS.items():
    html = build_page(code, data)
    out_dir = os.path.join(SITE, data["path"]) if data["path"] else SITE
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("Wrote", out_path, len(html), "bytes")

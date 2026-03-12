// Multi-language translation system for Hindi and Tamil
const translations = {
    en: {
        // Header
        app_title: "Government Construction Cost & Delay Predictor",
        app_subtitle: "AI-Powered Estimation System for Government Contractors",
        projects: "Projects",
        predictions: "Predictions",
        avg_risk: "Avg Risk",

        // Navigation tabs
        dashboard: "Dashboard",
        new_prediction: "New Prediction",
        live_rates: "Live Rates",
        projects_tab: "Projects",
        history: "History",
        compare: "Compare",
        analytics: "Analytics",

        // Dashboard
        overview_statistics: "Overview Statistics",
        residential: "Residential",
        commercial: "Commercial",
        industrial: "Industrial",
        infrastructure: "Infrastructure",
        project_distribution: "Project Distribution",
        risk_distribution: "Risk Distribution",
        recent_predictions: "Recent Predictions",
        quick_actions: "Quick Actions",
        new_cost_prediction: "New Cost Prediction",
        create_project: "Create Project",
        view_rates: "View Rates",
        view_analytics: "View Analytics",

        // Prediction Form - Basic Info
        basic_information: "Basic Information",
        project_type: "Project Type",
        location: "Location / Place Name",
        total_area: "Total Area (sq ft)",
        num_floors: "Number of Floors",
        start_typing: "Start typing district/city name...",

        // Resource Planning
        resource_planning: "Resource Planning",
        num_workers: "Number of Workers",
        planned_duration: "Planned Duration (days)",
        contractor_experience: "Contractor Experience (years)",
        num_supervisors: "Number of Supervisors",

        // Material & Quality
        material_quality: "Material Quality",
        economy: "Economy",
        standard: "Standard",
        premium: "Premium",
        complexity_level: "Complexity Level",
        low: "Low",
        medium: "Medium",
        high: "High",

        // Site Conditions
        site_conditions: "Site Conditions",
        weather_risk_zone: "Weather Risk Zone",
        soil_type: "Soil Type",
        normal: "Normal",
        rocky: "Rocky",
        sandy: "Sandy",
        clay: "Clay",
        marshy: "Marshy",
        seismic_zone: "Seismic Zone",
        site_accessibility: "Site Accessibility / Road Access",
        easy_access: "Easy (Wide road, crane accessible)",
        moderate_access: "Moderate (Standard road)",
        difficult_access: "Difficult (Narrow road, manual labor)",
        remote_access: "Remote Location (No proper road)",
        water_table: "Water Table Level",
        deep_water: "Deep (>10m) - No issue",
        moderate_water: "Moderate (5-10m)",
        shallow_water: "Shallow (2-5m) - Dewatering needed",
        high_water: "High (<2m) - Major dewatering",
        site_topography: "Site Topography",
        flat: "Flat Land",
        gentle_slope: "Gentle Slope",
        steep_slope: "Steep Slope (Retaining walls needed)",
        hilly: "Hilly Terrain",
        foundation_type: "Foundation Type",
        isolated: "Isolated Footing",
        strip: "Strip Foundation",
        raft: "Raft Foundation",
        pile: "Pile Foundation (Deep)",
        distance_city: "Distance from City (km)",

        // Building Specifications
        building_specifications: "Building Specifications",
        floor_height: "Floor Height (feet)",
        num_bathrooms: "Number of Bathrooms",
        electrical_load: "Electrical Load (kW)",
        finishing_level: "Finishing Level",
        basic: "Basic (Whitewash, cement floor)",
        standard_finish: "Standard (Paint, tiles)",
        premium_finish: "Premium (Designer, marble/granite)",
        luxury: "Luxury (Imported, high-end)",

        // Additional Features
        additional_features: "Additional Features",
        has_basement: "Has Basement",
        parking_structure: "Parking Structure",
        elevator_lift: "Elevator/Lift",
        swimming_pool: "Swimming Pool",
        central_hvac: "Central HVAC",
        fire_safety: "Fire Safety System",
        smart_building: "Smart Building Systems",
        requires_demolition: "Requires Demolition",

        // Buttons
        predict_cost: "Predict Cost & Delay",
        calculate: "Calculate",
        submit: "Submit",
        cancel: "Cancel",
        close: "Close",
        refresh: "Refresh",
        export_pdf: "Export PDF",
        save: "Save",
        delete: "Delete",

        // Results
        predicted_cost: "Predicted Cost",
        predicted_delay: "Predicted Delay",
        delay_probability: "Delay Probability",
        risk_score: "Risk Score",
        cost_range: "Cost Range",
        delay_range: "Delay Range",
        risk_factors: "Risk Factors",
        recommendations: "Recommendations",
        govt_estimate: "Government BOQ Estimate",
        cost_optimization: "Cost Optimization",

        // Live Rates
        live_material_rates: "Live Material & Labor Rates",
        report_local_price: "Report Local Price",
        community_prices: "Community Reported Prices",
        region: "Region",
        last_updated: "Last Updated",
        cement: "Cement",
        steel: "Steel",
        sand: "Sand",
        aggregate: "Aggregate",
        bricks: "Bricks",
        per_bag: "per bag (50kg)",
        per_kg: "per kg",
        per_cum: "per cum",
        all_material_rates: "All Material Rates",
        labor_rates: "Labor Rates",
        price_alerts: "Price Alerts",

        // Crowdsourced
        report_price_title: "Report Local Material Price",
        report_price_desc: "Help the community by sharing current prices in your area.",
        material_category: "Material Category",
        material_name: "Material Name",
        price: "Price (Rs.)",
        city: "City",
        brand: "Brand (optional)",
        you_are: "You are a",
        contractor: "Contractor",
        dealer: "Material Dealer",
        engineer: "Civil Engineer",
        homeowner: "Home Owner",
        your_name: "Your Name (optional)",
        notes: "Notes (optional)",
        submit_report: "Submit Price Report",
        thank_you: "Thank you!",
        report_submitted: "Your price report has been submitted. This helps everyone get accurate local rates.",
        recent_reports: "Recent Reports",
        no_reports: "No community reports yet. Be the first to report local prices!",

        // Projects
        all_projects: "All Projects",
        create_new_project: "Create New Project",
        project_name: "Project Name",
        no_projects: "No projects yet",
        actual_cost: "Actual Cost",
        actual_duration: "Actual Duration",
        status: "Status",
        active: "Active",
        completed: "Completed",

        // Dashboard extra
        cost_trends: "Cost Prediction Trends",
        export_data: "Export Data",
        prediction_results: "Prediction Results",

        // Common
        days: "days",
        loading: "Loading...",
        error: "Error",
        success: "Success",
        select: "Select",
        search: "Search",
        filter: "Filter",
        no_data: "No data available",
        per_sqft: "per sq ft",
    },

    hi: {
        // Header
        app_title: "सरकारी निर्माण लागत और देरी भविष्यवाणी",
        app_subtitle: "सरकारी ठेकेदारों के लिए AI-संचालित अनुमान प्रणाली",
        projects: "परियोजनाएं",
        predictions: "भविष्यवाणियां",
        avg_risk: "औसत जोखिम",

        // Navigation tabs
        dashboard: "डैशबोर्ड",
        new_prediction: "नया अनुमान",
        live_rates: "लाइव दरें",
        projects_tab: "परियोजनाएं",
        history: "इतिहास",
        compare: "तुलना",
        analytics: "विश्लेषण",

        // Dashboard
        overview_statistics: "अवलोकन सांख्यिकी",
        residential: "आवासीय",
        commercial: "व्यावसायिक",
        industrial: "औद्योगिक",
        infrastructure: "बुनियादी ढांचा",
        project_distribution: "परियोजना वितरण",
        risk_distribution: "जोखिम वितरण",
        recent_predictions: "हालिया भविष्यवाणियां",
        quick_actions: "त्वरित कार्रवाई",
        new_cost_prediction: "नया लागत अनुमान",
        create_project: "परियोजना बनाएं",
        view_rates: "दरें देखें",
        view_analytics: "विश्लेषण देखें",

        // Prediction Form - Basic Info
        basic_information: "मूल जानकारी",
        project_type: "परियोजना प्रकार",
        location: "स्थान / जगह का नाम",
        total_area: "कुल क्षेत्रफल (वर्ग फुट)",
        num_floors: "मंजिलों की संख्या",
        start_typing: "जिला/शहर का नाम टाइप करें...",

        // Resource Planning
        resource_planning: "संसाधन योजना",
        num_workers: "मजदूरों की संख्या",
        planned_duration: "नियोजित अवधि (दिन)",
        contractor_experience: "ठेकेदार का अनुभव (वर्ष)",
        num_supervisors: "पर्यवेक्षकों की संख्या",

        // Material & Quality
        material_quality: "सामग्री गुणवत्ता",
        economy: "किफायती",
        standard: "मानक",
        premium: "प्रीमियम",
        complexity_level: "जटिलता स्तर",
        low: "कम",
        medium: "मध्यम",
        high: "उच्च",

        // Site Conditions
        site_conditions: "साइट की स्थिति",
        weather_risk_zone: "मौसम जोखिम क्षेत्र",
        soil_type: "मिट्टी का प्रकार",
        normal: "सामान्य",
        rocky: "चट्टानी",
        sandy: "रेतीली",
        clay: "चिकनी मिट्टी",
        marshy: "दलदली",
        seismic_zone: "भूकंपीय क्षेत्र",
        site_accessibility: "साइट पहुंच / सड़क मार्ग",
        easy_access: "आसान (चौड़ी सड़क, क्रेन पहुंच)",
        moderate_access: "मध्यम (सामान्य सड़क)",
        difficult_access: "कठिन (संकरी सड़क, हाथ से काम)",
        remote_access: "दूरस्थ (कोई सड़क नहीं)",
        water_table: "भूजल स्तर",
        deep_water: "गहरा (>10m) - कोई समस्या नहीं",
        moderate_water: "मध्यम (5-10m)",
        shallow_water: "उथला (2-5m) - डीवाटरिंग जरूरी",
        high_water: "ऊंचा (<2m) - बड़ी डीवाटरिंग",
        site_topography: "भूमि की बनावट",
        flat: "समतल भूमि",
        gentle_slope: "हल्की ढलान",
        steep_slope: "तीव्र ढलान (रिटेनिंग वॉल जरूरी)",
        hilly: "पहाड़ी इलाका",
        foundation_type: "नींव का प्रकार",
        isolated: "आइसोलेटेड फुटिंग",
        strip: "स्ट्रिप नींव",
        raft: "राफ्ट नींव",
        pile: "पाइल नींव (गहरी)",
        distance_city: "शहर से दूरी (किमी)",

        // Building Specifications
        building_specifications: "भवन विनिर्देश",
        floor_height: "मंजिल की ऊंचाई (फीट)",
        num_bathrooms: "बाथरूम की संख्या",
        electrical_load: "विद्युत भार (kW)",
        finishing_level: "फिनिशिंग स्तर",
        basic: "बेसिक (सफेदी, सीमेंट फर्श)",
        standard_finish: "मानक (पेंट, टाइल्स)",
        premium_finish: "प्रीमियम (डिजाइनर, संगमरमर/ग्रेनाइट)",
        luxury: "लग्जरी (आयातित, उच्च श्रेणी)",

        // Additional Features
        additional_features: "अतिरिक्त सुविधाएं",
        has_basement: "बेसमेंट है",
        parking_structure: "पार्किंग",
        elevator_lift: "लिफ्ट",
        swimming_pool: "स्विमिंग पूल",
        central_hvac: "सेंट्रल AC",
        fire_safety: "अग्नि सुरक्षा प्रणाली",
        smart_building: "स्मार्ट बिल्डिंग",
        requires_demolition: "तोड़-फोड़ जरूरी",

        // Buttons
        predict_cost: "लागत और देरी का अनुमान लगाएं",
        calculate: "गणना करें",
        submit: "जमा करें",
        cancel: "रद्द करें",
        close: "बंद करें",
        refresh: "रीफ्रेश",
        export_pdf: "PDF डाउनलोड",
        save: "सहेजें",
        delete: "हटाएं",

        // Results
        predicted_cost: "अनुमानित लागत",
        predicted_delay: "अनुमानित देरी",
        delay_probability: "देरी की संभावना",
        risk_score: "जोखिम स्कोर",
        cost_range: "लागत सीमा",
        delay_range: "देरी सीमा",
        risk_factors: "जोखिम कारक",
        recommendations: "सुझाव",
        govt_estimate: "सरकारी BOQ अनुमान",
        cost_optimization: "लागत अनुकूलन",

        // Live Rates
        live_material_rates: "लाइव सामग्री और मजदूरी दरें",
        report_local_price: "स्थानीय कीमत दर्ज करें",
        community_prices: "समुदाय द्वारा रिपोर्ट की गई कीमतें",
        region: "क्षेत्र",
        last_updated: "अंतिम अपडेट",
        cement: "सीमेंट",
        steel: "स्टील / सरिया",
        sand: "रेत / बालू",
        aggregate: "गिट्टी",
        bricks: "ईंट",
        per_bag: "प्रति बोरी (50kg)",
        per_kg: "प्रति किलो",
        per_cum: "प्रति घन मीटर",
        all_material_rates: "सभी सामग्री दरें",
        labor_rates: "मजदूरी दरें",
        price_alerts: "कीमत अलर्ट",

        // Crowdsourced
        report_price_title: "स्थानीय सामग्री कीमत दर्ज करें",
        report_price_desc: "अपने क्षेत्र की वर्तमान कीमतें साझा करके समुदाय की मदद करें।",
        material_category: "सामग्री श्रेणी",
        material_name: "सामग्री का नाम",
        price: "कीमत (रु.)",
        city: "शहर",
        brand: "ब्रांड (वैकल्पिक)",
        you_are: "आप हैं",
        contractor: "ठेकेदार",
        dealer: "सामग्री विक्रेता",
        engineer: "सिविल इंजीनियर",
        homeowner: "घर मालिक",
        your_name: "आपका नाम (वैकल्पिक)",
        notes: "टिप्पणी (वैकल्पिक)",
        submit_report: "कीमत रिपोर्ट जमा करें",
        thank_you: "धन्यवाद!",
        report_submitted: "आपकी कीमत रिपोर्ट जमा हो गई है। इससे सभी को सही दरें मिलती हैं।",
        recent_reports: "हालिया रिपोर्ट",
        no_reports: "अभी कोई रिपोर्ट नहीं। स्थानीय कीमतें दर्ज करने वाले पहले बनें!",

        // Projects
        all_projects: "सभी परियोजनाएं",
        create_new_project: "नई परियोजना बनाएं",
        project_name: "परियोजना का नाम",
        no_projects: "अभी कोई परियोजना नहीं",
        actual_cost: "वास्तविक लागत",
        actual_duration: "वास्तविक अवधि",
        status: "स्थिति",
        active: "सक्रिय",
        completed: "पूर्ण",

        // Dashboard extra
        cost_trends: "लागत अनुमान रुझान",
        export_data: "डेटा डाउनलोड",
        prediction_results: "अनुमान परिणाम",

        // Common
        days: "दिन",
        loading: "लोड हो रहा है...",
        error: "त्रुटि",
        success: "सफल",
        select: "चुनें",
        search: "खोजें",
        filter: "फ़िल्टर",
        no_data: "कोई डेटा उपलब्ध नहीं",
        per_sqft: "प्रति वर्ग फुट",
    },

    ta: {
        // Header
        app_title: "அரசு கட்டுமான செலவு மற்றும் தாமத கணிப்பான்",
        app_subtitle: "அரசு ஒப்பந்ததாரர்களுக்கான AI-இயங்கும் மதிப்பீட்டு அமைப்பு",
        projects: "திட்டங்கள்",
        predictions: "கணிப்புகள்",
        avg_risk: "சராசரி ஆபத்து",

        // Navigation tabs
        dashboard: "டாஷ்போர்டு",
        new_prediction: "புதிய கணிப்பு",
        live_rates: "நேரடி விலைகள்",
        projects_tab: "திட்டங்கள்",
        history: "வரலாறு",
        compare: "ஒப்பிடு",
        analytics: "பகுப்பாய்வு",

        // Dashboard
        overview_statistics: "மேலோட்ட புள்ளிவிவரங்கள்",
        residential: "குடியிருப்பு",
        commercial: "வணிக",
        industrial: "தொழிற்சாலை",
        infrastructure: "உள்கட்டமைப்பு",
        project_distribution: "திட்ட விநியோகம்",
        risk_distribution: "ஆபத்து விநியோகம்",
        recent_predictions: "சமீபத்திய கணிப்புகள்",
        quick_actions: "விரைவு செயல்கள்",
        new_cost_prediction: "புதிய செலவு கணிப்பு",
        create_project: "திட்டம் உருவாக்கு",
        view_rates: "விலைகள் பார்",
        view_analytics: "பகுப்பாய்வு பார்",

        // Prediction Form - Basic Info
        basic_information: "அடிப்படை தகவல்",
        project_type: "திட்ட வகை",
        location: "இடம் / ஊர் பெயர்",
        total_area: "மொத்த பரப்பு (சதுர அடி)",
        num_floors: "மாடிகள் எண்ணிக்கை",
        start_typing: "மாவட்டம்/நகரம் பெயர் தட்டச்சு செய்யவும்...",

        // Resource Planning
        resource_planning: "வள திட்டமிடல்",
        num_workers: "தொழிலாளர் எண்ணிக்கை",
        planned_duration: "திட்டமிட்ட காலம் (நாட்கள்)",
        contractor_experience: "ஒப்பந்ததாரர் அனுபவம் (ஆண்டுகள்)",
        num_supervisors: "மேற்பார்வையாளர் எண்ணிக்கை",

        // Material & Quality
        material_quality: "பொருள் தரம்",
        economy: "சிக்கனம்",
        standard: "நிலையான",
        premium: "பிரீமியம்",
        complexity_level: "சிக்கல் நிலை",
        low: "குறைவு",
        medium: "நடுத்தரம்",
        high: "அதிகம்",

        // Site Conditions
        site_conditions: "தள நிலைமைகள்",
        weather_risk_zone: "வானிலை ஆபத்து மண்டலம்",
        soil_type: "மண் வகை",
        normal: "சாதாரண",
        rocky: "பாறை",
        sandy: "மணல்",
        clay: "களிமண்",
        marshy: "சதுப்பு",
        seismic_zone: "நில நடுக்க மண்டலம்",
        site_accessibility: "தள அணுகல் / சாலை வழி",
        easy_access: "எளிதான (அகலமான சாலை, கிரேன் அணுகல்)",
        moderate_access: "நடுத்தர (சாதாரண சாலை)",
        difficult_access: "கடினம் (குறுகிய சாலை, கைவேலை)",
        remote_access: "தொலைதூர (சாலை இல்லை)",
        water_table: "நிலத்தடி நீர் மட்டம்",
        deep_water: "ஆழம் (>10m) - பிரச்சனை இல்லை",
        moderate_water: "நடுத்தர (5-10m)",
        shallow_water: "ஆழமற்ற (2-5m) - நீர் அகற்றல் தேவை",
        high_water: "உயர்ந்த (<2m) - பெரிய நீர் அகற்றல்",
        site_topography: "நிலப்பரப்பு",
        flat: "சமதளம்",
        gentle_slope: "லேசான சரிவு",
        steep_slope: "செங்குத்தான சரிவு (தக்கவைப்பு சுவர் தேவை)",
        hilly: "மலைப்பகுதி",
        foundation_type: "அடித்தள வகை",
        isolated: "தனித்த அடித்தளம்",
        strip: "நீள் அடித்தளம்",
        raft: "ராஃப்ட் அடித்தளம்",
        pile: "குழி அடித்தளம் (ஆழம்)",
        distance_city: "நகரத்திலிருந்து தூரம் (கிமீ)",

        // Building Specifications
        building_specifications: "கட்டிட விவரக்குறிப்புகள்",
        floor_height: "மாடி உயரம் (அடி)",
        num_bathrooms: "குளியலறை எண்ணிக்கை",
        electrical_load: "மின் சுமை (kW)",
        finishing_level: "பூச்சு நிலை",
        basic: "அடிப்படை (சுண்ணாம்பு, சிமெண்ட் தரை)",
        standard_finish: "நிலையான (பெயிண்ட், டைல்ஸ்)",
        premium_finish: "பிரீமியம் (டிசைனர், மார்பிள்/கிரானைட்)",
        luxury: "ஆடம்பரம் (இறக்குமதி, உயர்தரம்)",

        // Additional Features
        additional_features: "கூடுதல் வசதிகள்",
        has_basement: "பேஸ்மெண்ட் உள்ளது",
        parking_structure: "பார்க்கிங்",
        elevator_lift: "லிஃப்ட்",
        swimming_pool: "நீச்சல் குளம்",
        central_hvac: "மத்திய ஏசி",
        fire_safety: "தீ பாதுகாப்பு அமைப்பு",
        smart_building: "ஸ்மார்ட் கட்டிடம்",
        requires_demolition: "இடிப்பு தேவை",

        // Buttons
        predict_cost: "செலவு மற்றும் தாமதத்தை கணிக்கவும்",
        calculate: "கணக்கிடு",
        submit: "சமர்ப்பி",
        cancel: "ரத்து",
        close: "மூடு",
        refresh: "புதுப்பி",
        export_pdf: "PDF பதிவிறக்கம்",
        save: "சேமி",
        delete: "நீக்கு",

        // Results
        predicted_cost: "கணிக்கப்பட்ட செலவு",
        predicted_delay: "கணிக்கப்பட்ட தாமதம்",
        delay_probability: "தாமத நிகழ்தகவு",
        risk_score: "ஆபத்து மதிப்பெண்",
        cost_range: "செலவு வரம்பு",
        delay_range: "தாமத வரம்பு",
        risk_factors: "ஆபத்து காரணிகள்",
        recommendations: "பரிந்துரைகள்",
        govt_estimate: "அரசு BOQ மதிப்பீடு",
        cost_optimization: "செலவு குறைப்பு",

        // Live Rates
        live_material_rates: "நேரடி பொருள் மற்றும் கூலி விலைகள்",
        report_local_price: "உள்ளூர் விலை தெரிவிக்கவும்",
        community_prices: "சமூகம் தெரிவித்த விலைகள்",
        region: "பகுதி",
        last_updated: "கடைசி புதுப்பிப்பு",
        cement: "சிமெண்ட்",
        steel: "எஃகு / சரிகம்பி",
        sand: "மணல்",
        aggregate: "ஜல்லி",
        bricks: "செங்கல்",
        per_bag: "ஒரு மூட்டை (50kg)",
        per_kg: "ஒரு கிலோ",
        per_cum: "ஒரு கன மீட்டர்",
        all_material_rates: "அனைத்து பொருள் விலைகள்",
        labor_rates: "கூலி விலைகள்",
        price_alerts: "விலை எச்சரிக்கைகள்",

        // Crowdsourced
        report_price_title: "உள்ளூர் பொருள் விலை தெரிவிக்கவும்",
        report_price_desc: "உங்கள் பகுதியின் தற்போதைய விலைகளை பகிர்ந்து சமூகத்திற்கு உதவுங்கள்.",
        material_category: "பொருள் வகை",
        material_name: "பொருள் பெயர்",
        price: "விலை (ரூ.)",
        city: "நகரம்",
        brand: "பிராண்ட் (விருப்பம்)",
        you_are: "நீங்கள்",
        contractor: "ஒப்பந்ததாரர்",
        dealer: "பொருள் விற்பனையாளர்",
        engineer: "சிவில் பொறியாளர்",
        homeowner: "வீட்டு உரிமையாளர்",
        your_name: "உங்கள் பெயர் (விருப்பம்)",
        notes: "குறிப்புகள் (விருப்பம்)",
        submit_report: "விலை அறிக்கை சமர்ப்பி",
        thank_you: "நன்றி!",
        report_submitted: "உங்கள் விலை அறிக்கை சமர்ப்பிக்கப்பட்டது. இது அனைவருக்கும் சரியான விலைகள் பெற உதவும்.",
        recent_reports: "சமீபத்திய அறிக்கைகள்",
        no_reports: "இன்னும் அறிக்கைகள் இல்லை. உள்ளூர் விலைகளை தெரிவிக்கும் முதல் நபராக இருங்கள்!",

        // Projects
        all_projects: "அனைத்து திட்டங்கள்",
        create_new_project: "புதிய திட்டம் உருவாக்கு",
        project_name: "திட்ட பெயர்",
        no_projects: "இன்னும் திட்டங்கள் இல்லை",
        actual_cost: "உண்மையான செலவு",
        actual_duration: "உண்மையான காலம்",
        status: "நிலை",
        active: "செயலில்",
        completed: "நிறைவு",

        // Dashboard extra
        cost_trends: "செலவு கணிப்பு போக்குகள்",
        export_data: "தரவு பதிவிறக்கம்",
        prediction_results: "கணிப்பு முடிவுகள்",

        // Common
        days: "நாட்கள்",
        loading: "ஏற்றுகிறது...",
        error: "பிழை",
        success: "வெற்றி",
        select: "தேர்வு",
        search: "தேடு",
        filter: "வடிகட்டு",
        no_data: "தரவு இல்லை",
        per_sqft: "ஒரு சதுர அடி",
    }
};

// Current language
let currentLang = localStorage.getItem('app_language') || 'en';

// Get translation
function t(key) {
    return (translations[currentLang] && translations[currentLang][key]) || translations.en[key] || key;
}

// Switch language
function switchLanguage(lang) {
    currentLang = lang;
    localStorage.setItem('app_language', lang);
    applyTranslations();

    // Update language selector
    const selector = document.getElementById('language-selector');
    if (selector) selector.value = lang;
}

// Apply translations to all elements with data-i18n attribute
function applyTranslations() {
    // Translate elements with data-i18n attribute
    document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        const translation = t(key);
        if (el.tagName === 'INPUT' && el.type === 'text') {
            el.placeholder = translation;
        } else if (el.tagName === 'OPTION') {
            el.textContent = translation;
        } else {
            // Preserve icons - only replace text content
            const icon = el.querySelector('i.fas, i.fab, i.far');
            if (icon) {
                el.innerHTML = icon.outerHTML + ' ' + translation;
            } else {
                el.textContent = translation;
            }
        }
    });

    // Update page title
    document.title = t('app_title');

    // Update HTML lang attribute
    document.documentElement.lang = currentLang === 'hi' ? 'hi' : currentLang === 'ta' ? 'ta' : 'en';
}

// Initialize language on page load
function initLanguage() {
    const saved = localStorage.getItem('app_language');
    if (saved) {
        currentLang = saved;
        const selector = document.getElementById('language-selector');
        if (selector) selector.value = saved;
    }
    applyTranslations();
}

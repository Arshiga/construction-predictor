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

        // Material Calculator
        material_calculator: "Material Calculator",
        calc_desc: "Calculate exact material quantities for any construction work based on IS code standards.",
        calc_construction_type: "Construction Type",
        calc_dimensions: "Dimensions",
        calc_length: "Length (meters)",
        calc_width: "Width (meters)",
        calc_height: "Height (meters)",
        calc_thickness: "Thickness (mm)",
        calc_mix_ratio: "Concrete Mix Ratio",
        calc_calculate: "Calculate Quantities",
        calc_clear: "Clear",
        calc_results: "Calculation Results",
        calc_cost_estimate: "Estimated Material Cost",
        calc_wastage_note: "Quantities include 5% wastage allowance. Rates based on current market prices.",
        calc_add_to_summary: "Add to Summary",
        calc_summary: "Material Summary (All Items)",

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

        // NEW: Regions
        north_india: "North India (Delhi, UP, Punjab)",
        south_india: "South India (TN, Kerala, Karnataka)",
        west_india: "West India (Maharashtra, Gujarat)",
        east_india: "East India (WB, Bihar, Odisha)",
        central_india: "Central India (MP, Chhattisgarh)",
        northeast_india: "North East India",

        // NEW: Material cards
        no_price_alerts: "No price alerts at this time",
        cement_opc43: "Cement (OPC 43)",
        tmt_steel_fe500: "TMT Steel (Fe500)",
        river_sand: "River Sand",
        aggregate_20mm: "Aggregate (20mm)",
        bricks_1st: "Bricks (1st Class)",
        mason_skilled: "Mason (Skilled)",
        per_bag_50kg: "per bag (50kg)",
        per_1000_nos: "per 1000 nos",
        per_day: "per day",

        // NEW: Material categories
        select_category: "Select category",
        cement_category: "Cement",
        steel_tmt: "Steel / TMT",
        sand_category: "Sand",
        aggregate_gravel: "Aggregate / Gravel",
        bricks_blocks: "Bricks / Blocks",
        wood_timber: "Wood / Timber",
        paint_category: "Paint",
        tiles_flooring: "Tiles / Flooring",
        pipes_plumbing: "Pipes / Plumbing",
        electrical_category: "Electrical",
        all_categories: "All Categories",
        search_materials: "Search materials...",

        // NEW: Price trends
        cement_price_trend: "Cement Price Trend",
        steel_price_trend: "Steel Price Trend",

        // NEW: Government form
        govt_project_params: "Government Project Parameters",
        work_name_label: "Work Name / Project Title *",
        work_name_hint: "Enter the exact work name as per tender/contract document",
        govt_contract_details: "Government Contract Details",
        tender_number: "Tender/Contract Number",
        department_agency: "Department/Agency *",
        select_department: "Select Department",
        pwd: "Public Works Department (PWD)",
        cpwd: "Central PWD (CPWD)",
        nhai: "National Highways Authority (NHAI)",
        railways: "Indian Railways",
        mes: "Military Engineering Services (MES)",
        irrigation: "Irrigation Department",
        rural_dev: "Rural Development",
        urban_dev: "Urban Development",
        panchayat: "Panchayati Raj",
        municipal: "Municipal Corporation",
        housing_board: "Housing Board",
        education_dept: "Education Department",
        health_dept: "Health Department",
        other_govt: "Other Government Body",

        // NEW: Schemes
        scheme_program: "Scheme/Program Name",
        select_scheme: "Select Scheme (if applicable)",
        pmay: "Pradhan Mantri Awas Yojana (PMAY)",
        pmgsy: "Pradhan Mantri Gram Sadak Yojana (PMGSY)",
        amrut: "AMRUT Mission",
        smart_city: "Smart City Mission",
        jal_jeevan: "Jal Jeevan Mission",
        swachh_bharat: "Swachh Bharat Mission",
        mgnrega: "MGNREGA",
        state_scheme: "State Government Scheme",
        other_scheme: "Other Scheme",
        no_scheme: "Not under any scheme",

        // NEW: Contractor & Bid
        contractor_class: "Contractor Class/Category",
        class_a: "Class A (Above 5 Cr)",
        class_b: "Class B (1-5 Cr)",
        class_c: "Class C (25L-1 Cr)",
        class_d: "Class D (Below 25L)",
        bid_percentage: "Bid Percentage (if applicable)",
        at_par: "At Par (0%)",
        above_bid: "Above (+)",
        below_bid: "Below (-)",

        // NEW: Form labels
        quality_complexity: "Quality & Complexity",
        design_type: "Design Type",
        green_building: "Green Building Certification",
        residential_housing: "Residential (Housing/Quarters)",
        commercial_offices: "Commercial (Offices/Buildings)",
        industrial_factories: "Industrial (Factories/Warehouses)",
        infrastructure_roads: "Infrastructure (Roads/Bridges)",
        infra_work_details: "Infrastructure Work Details",
        work_type: "Work Type *",
        road_drain_length: "Road/Drain Length (meters) *",
        road_drain_width: "Road/Drain Width (meters) *",
        road_surface_type: "Road Surface Type",
        drain_depth: "Drain Depth (meters)",
        drain_type_label: "Drain Type",
        permits_regulatory: "Permits & Regulatory",
        permit_status: "Permit Status",
        environmental_clearance: "Environmental Clearance",
        estimation_method: "Estimation Method",

        // NEW: Dashboard & misc
        no_predictions_yet: "No predictions yet. Make your first prediction!",
        view_all: "View All",
        avg_cost_sqft: "Average Cost per sqft",
        avg_delay_label: "Average Delay",
        high_risk_projects: "High Risk Projects",
        most_common_type: "Most Common Type",
        footer_for_contractors: "For Government Contractors | Predictions are estimates for tendering purposes only",
        footer_disclaimer: "This tool is meant for estimation purposes. Actual costs may vary based on site conditions and government rates.",
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

        // Material Calculator
        material_calculator: "सामग्री कैलकुलेटर",
        calc_desc: "IS कोड मानकों के आधार पर किसी भी निर्माण कार्य के लिए सटीक सामग्री मात्रा की गणना करें।",
        calc_construction_type: "निर्माण प्रकार",
        calc_dimensions: "माप / आकार",
        calc_length: "लंबाई (मीटर)",
        calc_width: "चौड़ाई (मीटर)",
        calc_height: "ऊंचाई (मीटर)",
        calc_thickness: "मोटाई (mm)",
        calc_mix_ratio: "कंक्रीट मिक्स अनुपात",
        calc_calculate: "मात्रा की गणना करें",
        calc_clear: "साफ करें",
        calc_results: "गणना परिणाम",
        calc_cost_estimate: "अनुमानित सामग्री लागत",
        calc_wastage_note: "मात्रा में 5% बर्बादी शामिल है। दरें वर्तमान बाजार मूल्य पर आधारित हैं।",
        calc_add_to_summary: "सारांश में जोड़ें",
        calc_summary: "सामग्री सारांश (सभी आइटम)",

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

        // NEW: Regions
        north_india: "उत्तर भारत (दिल्ली, उ.प्र., पंजाब)",
        south_india: "दक्षिण भारत (तमिलनाडु, केरल, कर्नाटक)",
        west_india: "पश्चिम भारत (महाराष्ट्र, गुजरात)",
        east_india: "पूर्वी भारत (प.बंगाल, बिहार, ओडिशा)",
        central_india: "मध्य भारत (म.प्र., छत्तीसगढ़)",
        northeast_india: "पूर्वोत्तर भारत",

        // NEW: Material cards
        no_price_alerts: "इस समय कोई कीमत अलर्ट नहीं",
        cement_opc43: "सीमेंट (OPC 43)",
        tmt_steel_fe500: "TMT सरिया (Fe500)",
        river_sand: "नदी की रेत",
        aggregate_20mm: "गिट्टी (20mm)",
        bricks_1st: "ईंट (प्रथम श्रेणी)",
        mason_skilled: "राज मिस्त्री (कुशल)",
        per_bag_50kg: "प्रति बोरी (50kg)",
        per_1000_nos: "प्रति 1000 नग",
        per_day: "प्रति दिन",

        // NEW: Material categories
        select_category: "श्रेणी चुनें",
        cement_category: "सीमेंट",
        steel_tmt: "स्टील / TMT",
        sand_category: "रेत",
        aggregate_gravel: "गिट्टी / बजरी",
        bricks_blocks: "ईंट / ब्लॉक",
        wood_timber: "लकड़ी / इमारती लकड़ी",
        paint_category: "पेंट",
        tiles_flooring: "टाइल्स / फर्श",
        pipes_plumbing: "पाइप / प्लंबिंग",
        electrical_category: "इलेक्ट्रिकल",
        all_categories: "सभी श्रेणियां",
        search_materials: "सामग्री खोजें...",

        // NEW: Price trends
        cement_price_trend: "सीमेंट मूल्य रुझान",
        steel_price_trend: "स्टील मूल्य रुझान",

        // NEW: Government form
        govt_project_params: "सरकारी परियोजना मापदंड",
        work_name_label: "कार्य का नाम / परियोजना शीर्षक *",
        work_name_hint: "टेंडर/अनुबंध दस्तावेज़ के अनुसार सही कार्य नाम दर्ज करें",
        govt_contract_details: "सरकारी अनुबंध विवरण",
        tender_number: "टेंडर/अनुबंध संख्या",
        department_agency: "विभाग/एजेंसी *",
        select_department: "विभाग चुनें",
        pwd: "लोक निर्माण विभाग (PWD)",
        cpwd: "केंद्रीय लोक निर्माण विभाग (CPWD)",
        nhai: "राष्ट्रीय राजमार्ग प्राधिकरण (NHAI)",
        railways: "भारतीय रेलवे",
        mes: "सैन्य अभियांत्रिकी सेवा (MES)",
        irrigation: "सिंचाई विभाग",
        rural_dev: "ग्रामीण विकास",
        urban_dev: "शहरी विकास",
        panchayat: "पंचायती राज",
        municipal: "नगर निगम",
        housing_board: "आवास बोर्ड",
        education_dept: "शिक्षा विभाग",
        health_dept: "स्वास्थ्य विभाग",
        other_govt: "अन्य सरकारी संस्था",

        // NEW: Schemes
        scheme_program: "योजना/कार्यक्रम का नाम",
        select_scheme: "योजना चुनें (यदि लागू हो)",
        pmay: "प्रधानमंत्री आवास योजना (PMAY)",
        pmgsy: "प्रधानमंत्री ग्राम सड़क योजना (PMGSY)",
        amrut: "अमृत मिशन",
        smart_city: "स्मार्ट सिटी मिशन",
        jal_jeevan: "जल जीवन मिशन",
        swachh_bharat: "स्वच्छ भारत मिशन",
        mgnrega: "मनरेगा",
        state_scheme: "राज्य सरकार की योजना",
        other_scheme: "अन्य योजना",
        no_scheme: "किसी योजना के तहत नहीं",

        // NEW: Contractor & Bid
        contractor_class: "ठेकेदार वर्ग/श्रेणी",
        class_a: "वर्ग A (5 करोड़ से ऊपर)",
        class_b: "वर्ग B (1-5 करोड़)",
        class_c: "वर्ग C (25 लाख - 1 करोड़)",
        class_d: "वर्ग D (25 लाख से नीचे)",
        bid_percentage: "बोली प्रतिशत (यदि लागू हो)",
        at_par: "बराबर (0%)",
        above_bid: "ऊपर (+)",
        below_bid: "नीचे (-)",

        // NEW: Form labels
        quality_complexity: "गुणवत्ता और जटिलता",
        design_type: "डिज़ाइन प्रकार",
        green_building: "ग्रीन बिल्डिंग प्रमाणन",
        residential_housing: "आवासीय (मकान/क्वार्टर)",
        commercial_offices: "व्यावसायिक (कार्यालय/भवन)",
        industrial_factories: "औद्योगिक (कारखाना/गोदाम)",
        infrastructure_roads: "बुनियादी ढांचा (सड़क/पुल)",
        infra_work_details: "बुनियादी ढांचा कार्य विवरण",
        work_type: "कार्य प्रकार *",
        road_drain_length: "सड़क/नाली की लंबाई (मीटर) *",
        road_drain_width: "सड़क/नाली की चौड़ाई (मीटर) *",
        road_surface_type: "सड़क की सतह का प्रकार",
        drain_depth: "नाली की गहराई (मीटर)",
        drain_type_label: "नाली का प्रकार",
        permits_regulatory: "अनुमति और नियामक",
        permit_status: "अनुमति की स्थिति",
        environmental_clearance: "पर्यावरण मंजूरी",
        estimation_method: "अनुमान विधि",

        // NEW: Dashboard & misc
        no_predictions_yet: "अभी कोई अनुमान नहीं। अपना पहला अनुमान लगाएं!",
        view_all: "सभी देखें",
        avg_cost_sqft: "प्रति वर्ग फुट औसत लागत",
        avg_delay_label: "औसत देरी",
        high_risk_projects: "उच्च जोखिम परियोजनाएं",
        most_common_type: "सबसे आम प्रकार",
        footer_for_contractors: "सरकारी ठेकेदारों के लिए | अनुमान केवल टेंडर उद्देश्यों के लिए हैं",
        footer_disclaimer: "यह उपकरण अनुमान के उद्देश्य से है। वास्तविक लागत साइट की स्थिति और सरकारी दरों के आधार पर भिन्न हो सकती है।",
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

        // Material Calculator
        material_calculator: "பொருள் கணிப்பான்",
        calc_desc: "IS குறியீடு தரநிலைகளின் அடிப்படையில் எந்த கட்டுமான வேலைக்கும் துல்லியமான பொருள் அளவைக் கணக்கிடுங்கள்.",
        calc_construction_type: "கட்டுமான வகை",
        calc_dimensions: "அளவுகள்",
        calc_length: "நீளம் (மீட்டர்)",
        calc_width: "அகலம் (மீட்டர்)",
        calc_height: "உயரம் (மீட்டர்)",
        calc_thickness: "தடிமன் (mm)",
        calc_mix_ratio: "கான்கிரீட் கலவை விகிதம்",
        calc_calculate: "அளவைக் கணக்கிடு",
        calc_clear: "அழி",
        calc_results: "கணக்கீட்டு முடிவுகள்",
        calc_cost_estimate: "மதிப்பிடப்பட்ட பொருள் செலவு",
        calc_wastage_note: "அளவுகளில் 5% விரயம் சேர்க்கப்பட்டுள்ளது. விலைகள் தற்போதைய சந்தை விலையை அடிப்படையாகக் கொண்டவை.",
        calc_add_to_summary: "சுருக்கத்தில் சேர்",
        calc_summary: "பொருள் சுருக்கம் (அனைத்து பொருட்கள்)",

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

        // NEW: Regions
        north_india: "வட இந்தியா (டெல்லி, உ.பி, பஞ்சாப்)",
        south_india: "தென் இந்தியா (தமிழ்நாடு, கேரளா, கர்நாடகா)",
        west_india: "மேற்கு இந்தியா (மகாராஷ்டிரா, குஜராத்)",
        east_india: "கிழக்கு இந்தியா (மே.வங்காளம், பீகார், ஒடிசா)",
        central_india: "மத்திய இந்தியா (ம.பி, சத்தீஸ்கர்)",
        northeast_india: "வடகிழக்கு இந்தியா",

        // NEW: Material cards
        no_price_alerts: "தற்போது விலை எச்சரிக்கைகள் இல்லை",
        cement_opc43: "சிமெண்ட் (OPC 43)",
        tmt_steel_fe500: "TMT எஃகு (Fe500)",
        river_sand: "ஆற்று மணல்",
        aggregate_20mm: "ஜல்லி (20mm)",
        bricks_1st: "செங்கல் (முதல் வகுப்பு)",
        mason_skilled: "கொத்தனார் (திறமையான)",
        per_bag_50kg: "ஒரு மூட்டை (50kg)",
        per_1000_nos: "1000 எண்ணிக்கைக்கு",
        per_day: "ஒரு நாளைக்கு",

        // NEW: Material categories
        select_category: "வகையைத் தேர்ந்தெடுக்கவும்",
        cement_category: "சிமெண்ட்",
        steel_tmt: "எஃகு / TMT",
        sand_category: "மணல்",
        aggregate_gravel: "ஜல்லி / சரளை",
        bricks_blocks: "செங்கல் / பிளாக்",
        wood_timber: "மரம் / மரக்கட்டை",
        paint_category: "பெயிண்ட்",
        tiles_flooring: "டைல்ஸ் / தரையோடு",
        pipes_plumbing: "குழாய் / பிளம்பிங்",
        electrical_category: "மின்சாரம்",
        all_categories: "அனைத்து வகைகள்",
        search_materials: "பொருட்களை தேடு...",

        // NEW: Price trends
        cement_price_trend: "சிமெண்ட் விலை போக்கு",
        steel_price_trend: "எஃகு விலை போக்கு",

        // NEW: Government form
        govt_project_params: "அரசு திட்ட அளவுருக்கள்",
        work_name_label: "பணியின் பெயர் / திட்ட தலைப்பு *",
        work_name_hint: "டெண்டர்/ஒப்பந்த ஆவணத்தின்படி சரியான பணி பெயரை உள்ளிடவும்",
        govt_contract_details: "அரசு ஒப்பந்த விவரங்கள்",
        tender_number: "டெண்டர்/ஒப்பந்த எண்",
        department_agency: "துறை/நிறுவனம் *",
        select_department: "துறையைத் தேர்ந்தெடுக்கவும்",
        pwd: "பொதுப்பணித் துறை (PWD)",
        cpwd: "மத்திய பொதுப்பணித் துறை (CPWD)",
        nhai: "தேசிய நெடுஞ்சாலை ஆணையம் (NHAI)",
        railways: "இந்திய ரயில்வே",
        mes: "ராணுவ பொறியியல் சேவை (MES)",
        irrigation: "நீர்ப்பாசனத் துறை",
        rural_dev: "ஊரக வளர்ச்சி",
        urban_dev: "நகர் வளர்ச்சி",
        panchayat: "பஞ்சாயத்து ராஜ்",
        municipal: "மாநகராட்சி",
        housing_board: "வீட்டு வசதி வாரியம்",
        education_dept: "கல்வித் துறை",
        health_dept: "சுகாதாரத் துறை",
        other_govt: "பிற அரசு அமைப்பு",

        // NEW: Schemes
        scheme_program: "திட்டம்/செயல்திட்டம் பெயர்",
        select_scheme: "திட்டத்தைத் தேர்ந்தெடுக்கவும் (பொருந்தினால்)",
        pmay: "பிரதம மந்திரி வீட்டு வசதி திட்டம் (PMAY)",
        pmgsy: "பிரதம மந்திரி கிராம சாலை திட்டம் (PMGSY)",
        amrut: "அம்ருத் திட்டம்",
        smart_city: "ஸ்மார்ட் சிட்டி திட்டம்",
        jal_jeevan: "ஜல் ஜீவன் திட்டம்",
        swachh_bharat: "சுவச் பாரத் திட்டம்",
        mgnrega: "மகாத்மா காந்தி வேலைவாய்ப்பு உறுதித் திட்டம்",
        state_scheme: "மாநில அரசு திட்டம்",
        other_scheme: "பிற திட்டம்",
        no_scheme: "எந்த திட்டத்திலும் இல்லை",

        // NEW: Contractor & Bid
        contractor_class: "ஒப்பந்ததாரர் வகுப்பு/பிரிவு",
        class_a: "வகுப்பு A (5 கோடிக்கு மேல்)",
        class_b: "வகுப்பு B (1-5 கோடி)",
        class_c: "வகுப்பு C (25 லட்சம் - 1 கோடி)",
        class_d: "வகுப்பு D (25 லட்சத்திற்கு கீழ்)",
        bid_percentage: "ஏல சதவீதம் (பொருந்தினால்)",
        at_par: "சம நிலையில் (0%)",
        above_bid: "மேல் (+)",
        below_bid: "கீழ் (-)",

        // NEW: Form labels
        quality_complexity: "தரம் & சிக்கலான தன்மை",
        design_type: "வடிவமைப்பு வகை",
        green_building: "பசுமை கட்டிட சான்றிதழ்",
        residential_housing: "குடியிருப்பு (வீடு/குடியிருப்பு)",
        commercial_offices: "வணிக (அலுவலகங்கள்/கட்டிடங்கள்)",
        industrial_factories: "தொழிற்சாலை (ஆலைகள்/கிடங்குகள்)",
        infrastructure_roads: "உள்கட்டமைப்பு (சாலைகள்/பாலங்கள்)",
        infra_work_details: "உள்கட்டமைப்பு பணி விவரங்கள்",
        work_type: "பணி வகை *",
        road_drain_length: "சாலை/வடிகால் நீளம் (மீட்டர்) *",
        road_drain_width: "சாலை/வடிகால் அகலம் (மீட்டர்) *",
        road_surface_type: "சாலை மேற்பரப்பு வகை",
        drain_depth: "வடிகால் ஆழம் (மீட்டர்)",
        drain_type_label: "வடிகால் வகை",
        permits_regulatory: "அனுமதிகள் & ஒழுங்குமுறை",
        permit_status: "அனுமதி நிலை",
        environmental_clearance: "சுற்றுச்சூழல் அனுமதி",
        estimation_method: "மதிப்பீட்டு முறை",

        // NEW: Dashboard & misc
        no_predictions_yet: "இன்னும் கணிப்புகள் இல்லை. உங்கள் முதல் கணிப்பை செய்யுங்கள்!",
        view_all: "அனைத்தையும் பார்",
        avg_cost_sqft: "சராசரி செலவு ஒரு சதுர அடிக்கு",
        avg_delay_label: "சராசரி தாமதம்",
        high_risk_projects: "அதிக ஆபத்து திட்டங்கள்",
        most_common_type: "மிகவும் பொதுவான வகை",
        footer_for_contractors: "அரசு ஒப்பந்ததாரர்களுக்கு | கணிப்புகள் டெண்டர் நோக்கங்களுக்கான மதிப்பீடுகள் மட்டுமே",
        footer_disclaimer: "இந்த கருவி மதிப்பீட்டு நோக்கங்களுக்கானது. உண்மையான செலவுகள் தள நிலைமைகள் மற்றும் அரசு விலைகளின் அடிப்படையில் மாறுபடலாம்.",
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

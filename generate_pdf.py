"""
Generate PDF documentation for the Construction Cost & Delay Prediction System
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
import os

def create_pdf():
    # Create PDF document
    pdf_path = os.path.join(os.path.dirname(__file__), "Project_Documentation.pdf")
    doc = SimpleDocTemplate(pdf_path, pagesize=A4,
                           rightMargin=50, leftMargin=50,
                           topMargin=50, bottomMargin=50)

    # Styles
    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=30,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#2c3e50')
    )

    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        spaceBefore=20,
        spaceAfter=10,
        textColor=colors.HexColor('#34495e')
    )

    subheading_style = ParagraphStyle(
        'CustomSubHeading',
        parent=styles['Heading3'],
        fontSize=13,
        spaceBefore=15,
        spaceAfter=8,
        textColor=colors.HexColor('#2980b9')
    )

    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=10,
        alignment=TA_JUSTIFY,
        leading=16
    )

    bullet_style = ParagraphStyle(
        'BulletStyle',
        parent=styles['Normal'],
        fontSize=11,
        leftIndent=20,
        spaceAfter=5,
        leading=14
    )

    # Build content
    content = []

    # ============ TITLE PAGE ============
    content.append(Spacer(1, 2*inch))
    content.append(Paragraph("AI-Powered Construction Cost &<br/>Delay Prediction System", title_style))
    content.append(Spacer(1, 0.5*inch))
    content.append(Paragraph("Project Documentation", ParagraphStyle(
        'Subtitle', parent=styles['Normal'], fontSize=16, alignment=TA_CENTER, textColor=colors.gray
    )))
    content.append(Spacer(1, 2*inch))

    # Project info table
    info_data = [
        ["Technology", "Python, Flask, Machine Learning"],
        ["ML Algorithms", "XGBoost, Gradient Boosting, Random Forest"],
        ["Database", "SQLite with SQLAlchemy ORM"],
        ["Frontend", "HTML, CSS, JavaScript, Chart.js"],
    ]
    info_table = Table(info_data, colWidths=[2*inch, 3.5*inch])
    info_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor('#2c3e50')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
    ]))
    content.append(info_table)
    content.append(PageBreak())

    # ============ TABLE OF CONTENTS ============
    content.append(Paragraph("Table of Contents", heading_style))
    toc_items = [
        "1. Project Overview",
        "2. Key Features",
        "3. Technology Stack",
        "4. System Architecture",
        "5. Machine Learning Models",
        "6. Input Parameters",
        "7. Prediction Output",
        "8. API Endpoints",
        "9. Database Schema",
        "10. How to Run the Application",
        "11. Project Structure",
        "12. Future Enhancements"
    ]
    for item in toc_items:
        content.append(Paragraph(item, bullet_style))
    content.append(PageBreak())

    # ============ 1. PROJECT OVERVIEW ============
    content.append(Paragraph("1. Project Overview", heading_style))
    overview_text = """
    The AI-Powered Construction Cost & Delay Prediction System is an intelligent web application
    designed for contractors, project managers, and construction companies. It uses machine learning
    algorithms to predict construction project costs and potential delays based on various project
    parameters.

    The system analyzes historical construction data and learns patterns to provide accurate
    predictions for new projects. It helps stakeholders make informed decisions by providing:
    """
    content.append(Paragraph(overview_text, body_style))

    overview_points = [
        "• Accurate cost estimation based on project parameters",
        "• Delay prediction with probability assessment",
        "• Comprehensive risk analysis with severity levels",
        "• AI-generated recommendations for risk mitigation",
        "• Scenario comparison for optimal planning"
    ]
    for point in overview_points:
        content.append(Paragraph(point, bullet_style))
    content.append(Spacer(1, 0.2*inch))

    # ============ 2. KEY FEATURES ============
    content.append(Paragraph("2. Key Features", heading_style))

    features = [
        ("Cost Prediction", "Estimates total project costs based on parameters like area, location, materials, number of floors, and complexity. Provides cost ranges with confidence intervals."),
        ("Delay Prediction", "Predicts potential delays in days and calculates the probability of delays occurring based on historical patterns and project parameters."),
        ("Risk Assessment", "Generates a comprehensive risk score (0-100) and identifies specific risk factors such as weather risks, understaffing, aggressive timelines, etc."),
        ("Scenario Comparison", "Allows users to compare different project configurations side-by-side to find the optimal approach for their construction project."),
        ("Project Management", "Save and track projects with full prediction history, update project status, and record actual costs/duration upon completion."),
        ("Analytics Dashboard", "Visual charts showing cost trends, delay patterns, risk distribution, and project type statistics."),
        ("Smart Detection", "Auto-detects project type from project name (e.g., 'Highway Construction' detects as Infrastructure)."),
        ("Export Options", "Export predictions and reports to PDF or Excel format for documentation and sharing.")
    ]

    for feature_name, feature_desc in features:
        content.append(Paragraph(f"<b>{feature_name}:</b> {feature_desc}", body_style))

    content.append(PageBreak())

    # ============ 3. TECHNOLOGY STACK ============
    content.append(Paragraph("3. Technology Stack", heading_style))

    content.append(Paragraph("Backend Technologies", subheading_style))
    backend_data = [
        ["Component", "Technology", "Purpose"],
        ["Web Framework", "Flask 3.0", "Lightweight Python web framework for REST APIs"],
        ["Database ORM", "SQLAlchemy", "Object-Relational Mapping for database operations"],
        ["Database", "SQLite", "Lightweight relational database for data storage"],
        ["CORS Support", "Flask-CORS", "Enable Cross-Origin Resource Sharing"],
    ]
    backend_table = Table(backend_data, colWidths=[1.5*inch, 1.5*inch, 3*inch])
    backend_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3498db')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.gray),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
    ]))
    content.append(backend_table)
    content.append(Spacer(1, 0.2*inch))

    content.append(Paragraph("Machine Learning Libraries", subheading_style))
    ml_data = [
        ["Library", "Version", "Purpose"],
        ["XGBoost", "Latest", "Cost prediction using gradient boosting"],
        ["Scikit-learn", "Latest", "Data preprocessing, model training, evaluation"],
        ["Pandas", "Latest", "Data manipulation and analysis"],
        ["NumPy", "Latest", "Numerical computations"],
        ["Joblib", "Latest", "Model serialization and persistence"],
    ]
    ml_table = Table(ml_data, colWidths=[1.5*inch, 1.5*inch, 3*inch])
    ml_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#27ae60')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.gray),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
    ]))
    content.append(ml_table)
    content.append(Spacer(1, 0.2*inch))

    content.append(Paragraph("Frontend Technologies", subheading_style))
    frontend_data = [
        ["Technology", "Purpose"],
        ["HTML5", "Structure and semantic markup"],
        ["CSS3", "Styling, animations, responsive design"],
        ["JavaScript (ES6+)", "Interactive functionality and API calls"],
        ["Chart.js", "Data visualization with interactive charts"],
        ["Font Awesome", "Icon library for UI elements"],
    ]
    frontend_table = Table(frontend_data, colWidths=[2*inch, 4*inch])
    frontend_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#9b59b6')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.gray),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
    ]))
    content.append(frontend_table)

    content.append(PageBreak())

    # ============ 4. SYSTEM ARCHITECTURE ============
    content.append(Paragraph("4. System Architecture", heading_style))

    arch_text = """
    The application follows a three-tier architecture pattern consisting of:
    """
    content.append(Paragraph(arch_text, body_style))

    content.append(Paragraph("Presentation Layer (Frontend)", subheading_style))
    content.append(Paragraph("""
    The frontend is a single-page application (SPA) built with HTML, CSS, and JavaScript.
    It provides an intuitive dashboard interface with multiple tabs for different functionalities:
    Dashboard, New Prediction, Projects, History, Compare, and Analytics. The UI communicates
    with the backend via REST API calls using the Fetch API.
    """, body_style))

    content.append(Paragraph("Application Layer (Backend)", subheading_style))
    content.append(Paragraph("""
    The Flask backend handles HTTP requests, processes data, and coordinates between the
    presentation layer and the data layer. It includes:
    • Route handlers for API endpoints
    • ML predictor module for making predictions
    • Business logic for risk assessment and recommendations
    • Data validation and error handling
    """, body_style))

    content.append(Paragraph("Data Layer", subheading_style))
    content.append(Paragraph("""
    SQLite database stores all persistent data including projects and prediction history.
    SQLAlchemy ORM provides an abstraction layer for database operations. Trained ML models
    are serialized using Joblib and stored as .joblib files for quick loading.
    """, body_style))

    # ============ 5. MACHINE LEARNING MODELS ============
    content.append(Paragraph("5. Machine Learning Models", heading_style))

    content.append(Paragraph("5.1 Cost Prediction Model", subheading_style))
    content.append(Paragraph("""
    <b>Algorithm:</b> XGBoost Regressor<br/>
    <b>Purpose:</b> Predicts the total cost of a construction project<br/>
    <b>Parameters:</b> n_estimators=100, max_depth=6, learning_rate=0.1<br/>
    <b>Input Features:</b> Project type, area, floors, workers, duration, materials, complexity, location
    """, body_style))

    content.append(Paragraph("5.2 Delay Prediction Model", subheading_style))
    content.append(Paragraph("""
    <b>Algorithm:</b> Gradient Boosting Regressor<br/>
    <b>Purpose:</b> Predicts the number of delay days expected<br/>
    <b>Parameters:</b> n_estimators=100, max_depth=5, learning_rate=0.1<br/>
    <b>Output:</b> Predicted delay in days (positive values indicate delay)
    """, body_style))

    content.append(Paragraph("5.3 Delay Probability Model", subheading_style))
    content.append(Paragraph("""
    <b>Algorithm:</b> Random Forest Classifier<br/>
    <b>Purpose:</b> Predicts the probability that a project will experience any delay<br/>
    <b>Parameters:</b> n_estimators=100, max_depth=6<br/>
    <b>Output:</b> Probability value between 0 and 1
    """, body_style))

    content.append(Paragraph("5.4 Feature Engineering", subheading_style))
    content.append(Paragraph("""
    The system processes three types of features:<br/>
    • <b>Numerical:</b> total_area_sqft, num_floors, num_workers, planned_duration_days, contractor_experience_years<br/>
    • <b>Categorical:</b> project_type, location, material_quality, complexity_level, weather_risk_zone<br/>
    • <b>Boolean:</b> has_basement<br/><br/>
    Categorical features are encoded using LabelEncoder, and all features are standardized using StandardScaler.
    """, body_style))

    content.append(Paragraph("5.5 Fallback Rule-Based System", subheading_style))
    content.append(Paragraph("""
    When ML models are not trained, the system uses a rule-based prediction engine with predefined
    cost rates per square foot for different project types (in Indian Rupees):
    • Residential: Rs. 1,800/sqft
    • Commercial: Rs. 2,500/sqft
    • Industrial: Rs. 2,200/sqft
    • Infrastructure: Rs. 3,000/sqft

    These base rates are adjusted by multipliers for material quality, complexity, floors, and other factors.
    """, body_style))

    content.append(PageBreak())

    # ============ 6. INPUT PARAMETERS ============
    content.append(Paragraph("6. Input Parameters", heading_style))

    params_data = [
        ["Parameter", "Type", "Description", "Example Values"],
        ["project_type", "String", "Type of construction project", "residential, commercial, industrial, infrastructure"],
        ["location", "String", "Project location (city/state)", "Mumbai, Delhi, Bangalore"],
        ["total_area_sqft", "Float", "Total construction area in sq ft", "1000 - 50000"],
        ["num_floors", "Integer", "Number of floors in building", "1 - 20"],
        ["num_workers", "Integer", "Workers assigned to project", "10 - 100"],
        ["planned_duration_days", "Integer", "Planned project timeline", "90 - 365"],
        ["material_quality", "String", "Quality grade of materials", "economy, standard, premium"],
        ["complexity_level", "String", "Project complexity level", "low, medium, high"],
        ["has_basement", "Boolean", "Whether project has basement", "True, False"],
        ["weather_risk_zone", "String", "Weather risk in location", "low, moderate, high"],
        ["contractor_experience_years", "Integer", "Contractor's experience", "1 - 20"],
    ]

    params_table = Table(params_data, colWidths=[1.4*inch, 0.8*inch, 1.8*inch, 2*inch])
    params_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2c3e50')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.gray),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    content.append(params_table)

    # ============ 7. PREDICTION OUTPUT ============
    content.append(Paragraph("7. Prediction Output", heading_style))

    content.append(Paragraph("The system returns a comprehensive prediction response:", body_style))

    output_data = [
        ["Field", "Description"],
        ["predicted_cost", "Estimated total project cost in Rupees"],
        ["predicted_delay_days", "Expected delay in number of days"],
        ["delay_probability", "Probability of experiencing any delay (0-1)"],
        ["risk_score", "Overall risk score from 0 (low) to 100 (high)"],
        ["cost_lower_bound", "Lower limit of 95% confidence interval for cost"],
        ["cost_upper_bound", "Upper limit of 95% confidence interval for cost"],
        ["delay_lower_bound", "Lower limit of 95% confidence interval for delay"],
        ["delay_upper_bound", "Upper limit of 95% confidence interval for delay"],
        ["risk_factors", "List of identified risk factors with severity"],
        ["recommendations", "AI-generated recommendations for risk mitigation"],
    ]

    output_table = Table(output_data, colWidths=[1.8*inch, 4.2*inch])
    output_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#e74c3c')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.gray),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
    ]))
    content.append(output_table)

    content.append(PageBreak())

    # ============ 8. API ENDPOINTS ============
    content.append(Paragraph("8. API Endpoints", heading_style))

    content.append(Paragraph("Prediction Endpoints", subheading_style))
    pred_api_data = [
        ["Method", "Endpoint", "Description"],
        ["POST", "/api/predictions/predict", "Get a full prediction for a project"],
        ["POST", "/api/predictions/quick-estimate", "Quick estimate without saving to DB"],
        ["POST", "/api/predictions/compare", "Compare multiple project scenarios"],
        ["GET", "/api/predictions/history", "Get all prediction history"],
        ["GET", "/api/predictions/<id>", "Get specific prediction by ID"],
    ]
    pred_api_table = Table(pred_api_data, colWidths=[0.8*inch, 2.2*inch, 3*inch])
    pred_api_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3498db')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.gray),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
    ]))
    content.append(pred_api_table)
    content.append(Spacer(1, 0.2*inch))

    content.append(Paragraph("Project Management Endpoints", subheading_style))
    proj_api_data = [
        ["Method", "Endpoint", "Description"],
        ["GET", "/api/projects", "List all saved projects"],
        ["POST", "/api/projects", "Create a new project"],
        ["GET", "/api/projects/<id>", "Get project details by ID"],
        ["PUT", "/api/projects/<id>", "Update an existing project"],
        ["DELETE", "/api/projects/<id>", "Delete a project"],
        ["POST", "/api/projects/<id>/complete", "Mark project complete with actual values"],
        ["GET", "/api/projects/stats", "Get overall project statistics"],
    ]
    proj_api_table = Table(proj_api_data, colWidths=[0.8*inch, 2.2*inch, 3*inch])
    proj_api_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#27ae60')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.gray),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
    ]))
    content.append(proj_api_table)

    # ============ 9. DATABASE SCHEMA ============
    content.append(Paragraph("9. Database Schema", heading_style))

    content.append(Paragraph("Projects Table", subheading_style))
    content.append(Paragraph("""
    Stores information about construction projects including all input parameters and actual values
    after project completion.
    """, body_style))

    projects_schema = [
        ["Column", "Type", "Description"],
        ["id", "Integer (PK)", "Unique project identifier"],
        ["name", "String(200)", "Project name"],
        ["project_type", "String(50)", "Type: residential/commercial/industrial/infrastructure"],
        ["location", "String(100)", "Project location"],
        ["total_area_sqft", "Float", "Total area in square feet"],
        ["num_floors", "Integer", "Number of floors"],
        ["num_workers", "Integer", "Number of workers"],
        ["planned_duration_days", "Integer", "Planned duration"],
        ["material_quality", "String(20)", "Material quality level"],
        ["complexity_level", "String(20)", "Project complexity"],
        ["has_basement", "Boolean", "Has basement flag"],
        ["weather_risk_zone", "String(20)", "Weather risk zone"],
        ["actual_cost", "Float (nullable)", "Actual cost after completion"],
        ["actual_duration_days", "Integer (nullable)", "Actual duration after completion"],
        ["created_at", "DateTime", "Creation timestamp"],
    ]

    proj_schema_table = Table(projects_schema, colWidths=[1.8*inch, 1.5*inch, 2.7*inch])
    proj_schema_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#34495e')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.gray),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
    ]))
    content.append(proj_schema_table)
    content.append(Spacer(1, 0.2*inch))

    content.append(Paragraph("Predictions Table", subheading_style))
    content.append(Paragraph("""
    Stores all predictions made by the system along with input snapshots and results.
    """, body_style))

    pred_schema = [
        ["Column", "Type", "Description"],
        ["id", "Integer (PK)", "Unique prediction identifier"],
        ["project_id", "Integer (FK)", "Associated project (nullable)"],
        ["input_data", "JSON", "Snapshot of input parameters"],
        ["predicted_cost", "Float", "Predicted total cost"],
        ["predicted_delay_days", "Float", "Predicted delay in days"],
        ["delay_probability", "Float", "Probability of delay (0-1)"],
        ["risk_score", "Float", "Risk score (0-100)"],
        ["cost_lower_bound", "Float", "Lower confidence bound for cost"],
        ["cost_upper_bound", "Float", "Upper confidence bound for cost"],
        ["risk_factors", "JSON", "List of identified risk factors"],
        ["created_at", "DateTime", "Prediction timestamp"],
    ]

    pred_schema_table = Table(pred_schema, colWidths=[1.8*inch, 1.5*inch, 2.7*inch])
    pred_schema_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#34495e')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.gray),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
    ]))
    content.append(pred_schema_table)

    content.append(PageBreak())

    # ============ 10. HOW TO RUN ============
    content.append(Paragraph("10. How to Run the Application", heading_style))

    content.append(Paragraph("Prerequisites", subheading_style))
    prereq_text = """
    • Python 3.8 or higher installed on your system
    • pip (Python package manager)
    • Web browser (Chrome, Firefox, Edge recommended)
    """
    content.append(Paragraph(prereq_text, body_style))

    content.append(Paragraph("Installation Steps", subheading_style))
    steps = [
        ("Step 1: Navigate to Project Directory", "cd construction_predictor"),
        ("Step 2: Create Virtual Environment (Optional)", "python -m venv venv"),
        ("Step 3: Activate Virtual Environment", "venv\\Scripts\\activate (Windows)\nsource venv/bin/activate (Linux/Mac)"),
        ("Step 4: Install Dependencies", "pip install -r requirements.txt"),
        ("Step 5: Train ML Models (Optional)", "python train_models.py"),
        ("Step 6: Run the Application", "python run.py"),
        ("Step 7: Open in Browser", "http://localhost:5000"),
    ]

    for step_name, step_cmd in steps:
        content.append(Paragraph(f"<b>{step_name}</b>", body_style))
        content.append(Paragraph(f"<font face='Courier' size='10'>{step_cmd}</font>", bullet_style))

    content.append(Paragraph("Quick Start (Windows)", subheading_style))
    content.append(Paragraph("""
    Simply double-click the <b>START_APP.bat</b> file in the project folder.
    This will automatically start the server and open your browser to the application.
    """, body_style))

    # ============ 11. PROJECT STRUCTURE ============
    content.append(Paragraph("11. Project Structure", heading_style))

    structure_text = """
    <font face='Courier' size='9'>
    construction_predictor/<br/>
    ├── app/<br/>
    │   ├── __init__.py          # Flask app factory<br/>
    │   ├── models/<br/>
    │   │   └── database.py      # SQLAlchemy models<br/>
    │   ├── routes/<br/>
    │   │   ├── main.py          # Main routes<br/>
    │   │   ├── predictions.py   # Prediction endpoints<br/>
    │   │   └── projects.py      # Project endpoints<br/>
    │   ├── ml/<br/>
    │   │   └── predictor.py     # ML prediction engine<br/>
    │   └── utils/<br/>
    ├── static/<br/>
    │   ├── css/style.css        # Dashboard styles<br/>
    │   └── js/main.js           # Frontend JavaScript<br/>
    ├── templates/<br/>
    │   └── index.html           # Dashboard template<br/>
    ├── data/<br/>
    │   └── sample_data.csv      # Training data<br/>
    ├── trained_models/          # Saved ML models<br/>
    ├── config.py                # Configuration<br/>
    ├── run.py                   # Entry point<br/>
    ├── train_models.py          # Model training<br/>
    └── requirements.txt         # Dependencies<br/>
    </font>
    """
    content.append(Paragraph(structure_text, body_style))

    content.append(PageBreak())

    # ============ 12. FUTURE ENHANCEMENTS ============
    content.append(Paragraph("12. Future Enhancements", heading_style))

    enhancements = [
        "Integration with real-time material price APIs for dynamic cost updates",
        "Weather API integration for accurate weather risk assessment",
        "Mobile application for on-site predictions and updates",
        "Multi-language support for wider accessibility",
        "Advanced ML models with deep learning for improved accuracy",
        "Integration with project management tools (MS Project, Primavera)",
        "Real-time collaboration features for team members",
        "Automated report generation and email scheduling",
        "Historical data import from existing systems",
        "GPS-based location auto-detection for site parameters"
    ]

    for i, enhancement in enumerate(enhancements, 1):
        content.append(Paragraph(f"{i}. {enhancement}", bullet_style))

    content.append(Spacer(1, 0.5*inch))

    # Footer
    content.append(Paragraph("---", ParagraphStyle('HR', alignment=TA_CENTER)))
    content.append(Paragraph(
        "Document generated for Construction Cost & Delay Prediction System",
        ParagraphStyle('Footer', parent=styles['Normal'], fontSize=10, alignment=TA_CENTER, textColor=colors.gray)
    ))

    # Build PDF
    doc.build(content)
    print(f"PDF generated successfully: {pdf_path}")
    return pdf_path


if __name__ == "__main__":
    create_pdf()

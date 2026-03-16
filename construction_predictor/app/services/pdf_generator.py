"""
PDF Report Generator for Construction Cost Predictor
Generates professional PDF reports with charts and branding
"""

from io import BytesIO
from datetime import datetime
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, Image, HRFlowable
)
from reportlab.graphics.shapes import Drawing, Rect, String, Wedge, Line
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics import renderPDF


class PDFReportGenerator:
    """Generates professional PDF reports for construction cost predictions"""

    def __init__(self):
        self.styles = getSampleStyleSheet()
        self._setup_custom_styles()

    def _setup_custom_styles(self):
        """Setup custom paragraph styles"""
        self.styles.add(ParagraphStyle(
            name='MainTitle',
            parent=self.styles['Heading1'],
            fontSize=18,
            textColor=colors.HexColor('#1a237e'),
            spaceAfter=12,
            alignment=1  # Center
        ))
        self.styles.add(ParagraphStyle(
            name='SectionTitle',
            parent=self.styles['Heading2'],
            fontSize=14,
            textColor=colors.HexColor('#1565c0'),
            spaceBefore=16,
            spaceAfter=8,
            borderPadding=4,
        ))
        self.styles.add(ParagraphStyle(
            name='CompanyName',
            parent=self.styles['Normal'],
            fontSize=16,
            textColor=colors.HexColor('#333333'),
            fontName='Helvetica-Bold'
        ))
        self.styles.add(ParagraphStyle(
            name='ContactInfo',
            parent=self.styles['Normal'],
            fontSize=10,
            textColor=colors.HexColor('#666666')
        ))
        self.styles.add(ParagraphStyle(
            name='RiskHigh',
            parent=self.styles['Normal'],
            textColor=colors.HexColor('#c62828'),
            fontSize=10
        ))
        self.styles.add(ParagraphStyle(
            name='RiskMedium',
            parent=self.styles['Normal'],
            textColor=colors.HexColor('#ef6c00'),
            fontSize=10
        ))
        self.styles.add(ParagraphStyle(
            name='RiskLow',
            parent=self.styles['Normal'],
            textColor=colors.HexColor('#2e7d32'),
            fontSize=10
        ))
        self.styles.add(ParagraphStyle(
            name='Footer',
            parent=self.styles['Normal'],
            fontSize=8,
            textColor=colors.HexColor('#888888'),
            alignment=1
        ))

    def generate_report(self, prediction_data, company_name=None, contact_info=None):
        """
        Generate a complete PDF report for a prediction.

        Args:
            prediction_data: Dictionary containing prediction results
            company_name: Optional company name for branding
            contact_info: Optional contact information

        Returns:
            BytesIO buffer containing the PDF
        """
        buffer = BytesIO()
        doc = SimpleDocTemplate(
            buffer,
            pagesize=A4,
            rightMargin=20*mm,
            leftMargin=20*mm,
            topMargin=20*mm,
            bottomMargin=20*mm
        )

        # Build the document elements
        elements = []

        # Header with branding
        elements.extend(self._create_header(
            company_name or "Construction Cost Predictor",
            contact_info,
            prediction_data.get('id')
        ))

        # Main title
        elements.append(Spacer(1, 10))
        elements.append(Paragraph(
            "CONSTRUCTION COST ESTIMATE REPORT",
            self.styles['MainTitle']
        ))
        elements.append(HRFlowable(
            width="100%",
            thickness=2,
            color=colors.HexColor('#1565c0'),
            spaceAfter=20
        ))

        # Project Details
        elements.extend(self._create_project_details(prediction_data))

        # Cost Summary
        elements.extend(self._create_cost_summary(prediction_data))

        # Cost Breakdown Chart
        elements.extend(self._create_cost_breakdown_chart(prediction_data))

        # Timeline & Delay Analysis
        elements.extend(self._create_timeline_section(prediction_data))

        # Risk Assessment
        elements.extend(self._create_risk_section(prediction_data))

        # Recommendations
        elements.extend(self._create_recommendations(prediction_data))

        # Footer
        elements.extend(self._create_footer(prediction_data.get('id')))

        # Build PDF
        doc.build(elements)
        buffer.seek(0)
        return buffer

    def _create_header(self, company_name, contact_info, prediction_id):
        """Create the header section with branding"""
        elements = []

        # Company info table
        header_data = []

        # Logo placeholder (gray box) and company info
        logo_drawing = Drawing(60, 60)
        logo_drawing.add(Rect(0, 0, 55, 55, fillColor=colors.HexColor('#e0e0e0'), strokeColor=colors.HexColor('#bdbdbd')))
        logo_drawing.add(String(10, 22, "LOGO", fontSize=12, fillColor=colors.HexColor('#757575')))

        company_text = f"<b>{company_name}</b>"
        if contact_info:
            company_text += f"<br/>{contact_info}"
        company_text += f"<br/>Date: {datetime.now().strftime('%d-%m-%Y')}"

        header_data = [[
            logo_drawing,
            Paragraph(company_text, self.styles['Normal'])
        ]]

        header_table = Table(header_data, colWidths=[70, 400])
        header_table.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ]))

        elements.append(header_table)
        return elements

    def _create_project_details(self, prediction_data):
        """Create the project details section"""
        elements = []
        elements.append(Paragraph("1. PROJECT DETAILS", self.styles['SectionTitle']))

        input_data = prediction_data.get('input_data', {})

        # Format project type
        project_type = input_data.get('project_type', 'Unknown')
        project_type_display = project_type.replace('_', ' ').title()

        # Format material quality
        material_quality = input_data.get('material_quality', 'standard')
        material_quality_display = material_quality.title()

        # Format complexity
        complexity = input_data.get('complexity_level', 'medium')
        complexity_display = complexity.title()

        details_data = [
            ['Project Type', project_type_display],
            ['Location', input_data.get('location', 'Not specified')],
            ['Total Area', f"{input_data.get('total_area_sqft', 0):,.0f} sqft"],
            ['Number of Floors', str(input_data.get('num_floors', 1))],
            ['Material Quality', material_quality_display],
            ['Complexity Level', complexity_display],
            ['Number of Workers', str(input_data.get('num_workers', 0))],
            ['Contractor Experience', f"{input_data.get('contractor_experience_years', 0)} years"],
        ]

        # Add optional fields
        if input_data.get('has_basement'):
            details_data.append(['Has Basement', 'Yes'])
        if input_data.get('weather_risk_zone'):
            details_data.append(['Weather Risk Zone', input_data['weather_risk_zone'].title()])

        table = Table(details_data, colWidths=[150, 300])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#e3f2fd')),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#333333')),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#bbdefb')),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]))

        elements.append(table)
        elements.append(Spacer(1, 15))
        return elements

    def _create_cost_summary(self, prediction_data):
        """Create the cost summary section"""
        elements = []
        elements.append(Paragraph("2. COST SUMMARY", self.styles['SectionTitle']))

        predicted_cost = prediction_data.get('predicted_cost', 0)
        cost_lower = prediction_data.get('cost_lower_bound', 0)
        cost_upper = prediction_data.get('cost_upper_bound', 0)

        input_data = prediction_data.get('input_data', {})
        area = input_data.get('total_area_sqft', 1)
        cost_per_sqft = predicted_cost / area if area > 0 else 0

        cost_data = [
            ['Metric', 'Amount'],
            ['Estimated Cost', f"Rs. {predicted_cost:,.0f}"],
            ['Lower Bound (Conservative)', f"Rs. {cost_lower:,.0f}"],
            ['Upper Bound (With Contingency)', f"Rs. {cost_upper:,.0f}"],
            ['Cost per Sq.Ft.', f"Rs. {cost_per_sqft:,.0f}"],
        ]

        table = Table(cost_data, colWidths=[200, 250])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1565c0')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('BACKGROUND', (0, 1), (-1, 1), colors.HexColor('#e8f5e9')),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTNAME', (0, 1), (-1, 1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('FONTSIZE', (0, 1), (-1, 1), 12),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#bbdefb')),
            ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]))

        elements.append(table)
        elements.append(Spacer(1, 15))
        return elements

    def _create_cost_breakdown_chart(self, prediction_data):
        """Create the cost breakdown pie chart section"""
        elements = []
        elements.append(Paragraph("3. COST BREAKDOWN", self.styles['SectionTitle']))

        predicted_cost = prediction_data.get('predicted_cost', 100)

        # Standard cost breakdown percentages
        breakdown = {
            'Materials': 0.40,
            'Labor': 0.35,
            'Overhead': 0.15,
            'Contingency': 0.10
        }

        # Create pie chart
        drawing = Drawing(400, 200)

        pie = Pie()
        pie.x = 100
        pie.y = 25
        pie.width = 150
        pie.height = 150
        pie.data = [v * 100 for v in breakdown.values()]
        pie.labels = list(breakdown.keys())

        pie.slices.strokeWidth = 0.5
        pie.slices.strokeColor = colors.white

        # Colors for pie slices
        pie_colors = [
            colors.HexColor('#FF6384'),  # Materials - red
            colors.HexColor('#36A2EB'),  # Labor - blue
            colors.HexColor('#FFCE56'),  # Overhead - yellow
            colors.HexColor('#4BC0C0'),  # Contingency - teal
        ]

        for i, color in enumerate(pie_colors):
            pie.slices[i].fillColor = color
            pie.slices[i].popout = 5 if i == 0 else 0

        drawing.add(pie)

        # Add legend on the right side
        legend_x = 280
        legend_y = 160
        for i, (name, value) in enumerate(breakdown.items()):
            # Color box
            drawing.add(Rect(legend_x, legend_y - i*25, 15, 15,
                           fillColor=pie_colors[i], strokeColor=None))
            # Label
            cost_amount = predicted_cost * value
            drawing.add(String(legend_x + 22, legend_y - i*25 + 3,
                              f"{name}: Rs. {cost_amount:,.0f} ({value*100:.0f}%)",
                              fontSize=9, fillColor=colors.HexColor('#333333')))

        elements.append(drawing)
        elements.append(Spacer(1, 15))
        return elements

    def _create_timeline_section(self, prediction_data):
        """Create the timeline and delay analysis section"""
        elements = []
        elements.append(Paragraph("4. TIMELINE & DELAY ANALYSIS", self.styles['SectionTitle']))

        input_data = prediction_data.get('input_data', {})
        planned_duration = input_data.get('planned_duration_days', 0)
        predicted_delay = prediction_data.get('predicted_delay_days', 0)
        delay_probability = prediction_data.get('delay_probability', 0)
        expected_completion = planned_duration + predicted_delay

        timeline_data = [
            ['Metric', 'Value'],
            ['Planned Duration', f"{planned_duration} days"],
            ['Predicted Delay', f"{predicted_delay:.1f} days"],
            ['Delay Probability', f"{delay_probability * 100:.0f}%"],
            ['Expected Total Duration', f"{expected_completion:.0f} days"],
        ]

        table = Table(timeline_data, colWidths=[200, 250])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1565c0')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#bbdefb')),
            ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]))

        elements.append(table)
        elements.append(Spacer(1, 15))
        return elements

    def _create_risk_section(self, prediction_data):
        """Create the risk assessment section with gauge visualization"""
        elements = []
        elements.append(Paragraph("5. RISK ASSESSMENT", self.styles['SectionTitle']))

        risk_score = prediction_data.get('risk_score', 0)
        risk_factors = prediction_data.get('risk_factors', [])

        # Determine risk level
        if risk_score < 40:
            risk_level = "LOW"
            risk_color = colors.HexColor('#2e7d32')
        elif risk_score < 70:
            risk_level = "MODERATE"
            risk_color = colors.HexColor('#ef6c00')
        else:
            risk_level = "HIGH"
            risk_color = colors.HexColor('#c62828')

        # Risk score display
        elements.append(Paragraph(
            f"<b>Risk Score: {risk_score:.1f}/100</b> [{risk_level}]",
            self.styles['Normal']
        ))
        elements.append(Spacer(1, 10))

        # Create risk gauge
        drawing = Drawing(400, 60)

        # Background bar
        drawing.add(Rect(50, 20, 300, 25,
                        fillColor=colors.HexColor('#e0e0e0'),
                        strokeColor=None))

        # Risk zones
        drawing.add(Rect(50, 20, 100, 25,
                        fillColor=colors.HexColor('#c8e6c9'),
                        strokeColor=None))
        drawing.add(Rect(150, 20, 100, 25,
                        fillColor=colors.HexColor('#fff3e0'),
                        strokeColor=None))
        drawing.add(Rect(250, 20, 100, 25,
                        fillColor=colors.HexColor('#ffcdd2'),
                        strokeColor=None))

        # Indicator line
        indicator_x = 50 + (risk_score / 100) * 300
        drawing.add(Line(indicator_x, 15, indicator_x, 50,
                        strokeColor=colors.black, strokeWidth=3))

        # Labels
        drawing.add(String(85, 5, "Low", fontSize=8, fillColor=colors.HexColor('#2e7d32')))
        drawing.add(String(180, 5, "Moderate", fontSize=8, fillColor=colors.HexColor('#ef6c00')))
        drawing.add(String(285, 5, "High", fontSize=8, fillColor=colors.HexColor('#c62828')))

        elements.append(drawing)
        elements.append(Spacer(1, 10))

        # Risk factors list
        if risk_factors:
            elements.append(Paragraph("<b>Risk Factors:</b>", self.styles['Normal']))
            elements.append(Spacer(1, 5))

            for factor in risk_factors:
                factor_name = factor.get('factor', factor) if isinstance(factor, dict) else str(factor)
                severity = factor.get('severity', 'medium') if isinstance(factor, dict) else 'medium'

                if severity == 'high':
                    style = self.styles['RiskHigh']
                    bullet = "●"
                elif severity == 'low':
                    style = self.styles['RiskLow']
                    bullet = "○"
                else:
                    style = self.styles['RiskMedium']
                    bullet = "◐"

                elements.append(Paragraph(f"{bullet} {factor_name} ({severity.title()} severity)", style))
        else:
            elements.append(Paragraph("No significant risk factors identified.", self.styles['Normal']))

        elements.append(Spacer(1, 15))
        return elements

    def _create_recommendations(self, prediction_data):
        """Create the recommendations section"""
        elements = []
        elements.append(Paragraph("6. RECOMMENDATIONS", self.styles['SectionTitle']))

        risk_factors = prediction_data.get('risk_factors', [])
        risk_score = prediction_data.get('risk_score', 0)
        input_data = prediction_data.get('input_data', {})

        recommendations = []

        # Generate recommendations based on risk factors and input data
        for factor in risk_factors:
            factor_name = factor.get('factor', factor) if isinstance(factor, dict) else str(factor)
            factor_lower = factor_name.lower()

            if 'overstaffing' in factor_lower or 'workforce' in factor_lower:
                recommendations.append("Review workforce allocation to optimize efficiency and reduce labor costs.")
            elif 'delay' in factor_lower or 'duration' in factor_lower:
                recommendations.append("Consider adding buffer time to the project schedule to account for potential delays.")
            elif 'weather' in factor_lower:
                recommendations.append("Plan for weather contingencies and consider seasonal factors in scheduling.")
            elif 'experience' in factor_lower:
                recommendations.append("Consider partnering with experienced contractors for technical guidance.")
            elif 'complexity' in factor_lower:
                recommendations.append("Break down complex tasks into manageable phases with clear milestones.")

        # Add general recommendations based on risk score
        if risk_score > 60:
            recommendations.append("High risk score detected - conduct detailed risk mitigation planning.")
        if input_data.get('material_quality') == 'economy':
            recommendations.append("Consider upgrading material quality for better long-term durability.")
        if input_data.get('num_floors', 1) > 3 and not input_data.get('has_elevator'):
            recommendations.append("Consider elevator installation for buildings with multiple floors.")

        # Default recommendation if none generated
        if not recommendations:
            recommendations.append("Project parameters are within normal ranges. Follow standard construction best practices.")
            recommendations.append("Maintain regular progress monitoring and quality control checkpoints.")

        for rec in recommendations:
            elements.append(Paragraph(f"• {rec}", self.styles['Normal']))
            elements.append(Spacer(1, 3))

        elements.append(Spacer(1, 15))
        return elements

    def _create_footer(self, prediction_id):
        """Create the footer section"""
        elements = []

        elements.append(HRFlowable(
            width="100%",
            thickness=1,
            color=colors.HexColor('#e0e0e0'),
            spaceBefore=20,
            spaceAfter=10
        ))

        footer_text = f"Generated by Construction Cost Predictor | Report ID: #{prediction_id or 'N/A'} | Generated: {datetime.now().strftime('%d-%m-%Y %H:%M')}"
        elements.append(Paragraph(footer_text, self.styles['Footer']))

        return elements


# Singleton instance
pdf_generator = PDFReportGenerator()

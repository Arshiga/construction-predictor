# API Routes for Live Material Rates & Crowdsourced Prices
from flask import Blueprint, request, jsonify
from app import db
from app.models.database import PriceReport
from app.services.material_rates import material_rate_service
from app.services.live_prices import live_price_service
from datetime import datetime, timedelta

bp = Blueprint('rates', __name__, url_prefix='/api/rates')

# City to region mapping
CITY_REGION_MAP = {
    'delhi': 'north', 'noida': 'north', 'gurgaon': 'north', 'faridabad': 'north',
    'jaipur': 'north', 'lucknow': 'north', 'chandigarh': 'north', 'amritsar': 'north',
    'ludhiana': 'north', 'agra': 'north', 'varanasi': 'north', 'kanpur': 'north',
    'dehradun': 'north', 'shimla': 'north', 'srinagar': 'north', 'jodhpur': 'north',
    'udaipur': 'north', 'meerut': 'north', 'bareilly': 'north', 'aligarh': 'north',
    'mumbai': 'west', 'pune': 'west', 'thane': 'west', 'navi mumbai': 'west',
    'ahmedabad': 'west', 'surat': 'west', 'vadodara': 'west', 'nagpur': 'west',
    'nashik': 'west', 'rajkot': 'west', 'goa': 'west', 'gandhinagar': 'west',
    'aurangabad': 'west',
    'chennai': 'south', 'bangalore': 'south', 'hyderabad': 'south', 'kochi': 'south',
    'coimbatore': 'south', 'madurai': 'south', 'mysore': 'south', 'mangalore': 'south',
    'visakhapatnam': 'south', 'vijayawada': 'south', 'trichy': 'south',
    'thiruvananthapuram': 'south', 'pondicherry': 'south', 'tirupati': 'south',
    'vellore': 'south', 'salem': 'south', 'hubli': 'south', 'warangal': 'south',
    'guntur': 'south', 'thrissur': 'south', 'thanjavur': 'south',
    'kolkata': 'east', 'patna': 'east', 'ranchi': 'east', 'bhubaneswar': 'east',
    'jamshedpur': 'east',
    'bhopal': 'central', 'indore': 'central', 'raipur': 'central', 'jabalpur': 'central',
    'guwahati': 'northeast',
}

MATERIAL_UNITS = {
    'cement': 'per bag (50kg)',
    'steel': 'per kg',
    'sand': 'per cum',
    'aggregate': 'per cum',
    'bricks': 'per 1000 nos',
    'wood': 'per cum',
    'paint': 'per liter',
    'tiles': 'per sqft',
    'pipes': 'per meter',
    'electrical': 'per unit',
}


@bp.route('/summary', methods=['GET'])
def get_rates_summary():
    """
    Get summary of all material and labor rates for a region.
    Query params: region (north, south, west, east, central, northeast)
    """
    region = request.args.get('region', 'west')
    summary = material_rate_service.get_rates_summary(region)
    return jsonify(summary), 200


@bp.route('/materials', methods=['GET'])
def get_all_materials():
    """Get all material rates"""
    materials = material_rate_service.get_all_materials()
    return jsonify(materials), 200


@bp.route('/materials/<material_id>', methods=['GET'])
def get_material_rate(material_id):
    """
    Get rate for a specific material.
    Query params: region
    """
    region = request.args.get('region', 'west')
    rate = material_rate_service.get_material_rate(material_id, region)

    if not rate:
        return jsonify({'error': 'Material not found'}), 404

    return jsonify(rate), 200


@bp.route('/materials/<material_id>', methods=['PUT'])
def update_material_rate(material_id):
    """
    Update a material rate.
    JSON body: { "rate": 400, "region": "west" (optional) }
    """
    data = request.get_json()
    if not data or 'rate' not in data:
        return jsonify({'error': 'Rate is required'}), 400

    result = material_rate_service.update_material_rate(
        material_id,
        float(data['rate']),
        data.get('region')
    )

    if not result.get('success'):
        return jsonify(result), 404

    return jsonify(result), 200


@bp.route('/labor', methods=['GET'])
def get_all_labor_rates():
    """Get all labor rates"""
    labor = material_rate_service.get_all_labor_rates()
    return jsonify(labor), 200


@bp.route('/labor/<labor_type>', methods=['GET'])
def get_labor_rate(labor_type):
    """
    Get rate for a specific labor type.
    Query params: region
    """
    region = request.args.get('region', 'west')
    rate = material_rate_service.get_labor_rate(labor_type, region)

    if not rate:
        return jsonify({'error': 'Labor type not found'}), 404

    return jsonify(rate), 200


@bp.route('/alerts', methods=['GET'])
def get_alerts():
    """
    Get price change alerts.
    Query params: unread_only (true/false)
    """
    unread_only = request.args.get('unread_only', 'false').lower() == 'true'
    alerts = material_rate_service.get_alerts(unread_only)
    return jsonify(alerts), 200


@bp.route('/alerts/<alert_id>/read', methods=['POST'])
def mark_alert_read(alert_id):
    """Mark an alert as read"""
    material_rate_service.mark_alert_read(alert_id)
    return jsonify({'success': True}), 200


@bp.route('/regions', methods=['GET'])
def get_regions():
    """Get list of regions"""
    return jsonify(material_rate_service.REGIONS), 200


@bp.route('/categories', methods=['GET'])
def get_categories():
    """Get list of material categories"""
    return jsonify(material_rate_service.CATEGORIES), 200


@bp.route('/region-from-location', methods=['GET'])
def get_region_from_location():
    """
    Get region from location string.
    Query params: location
    """
    location = request.args.get('location', '')
    region = material_rate_service.get_region_from_location(location)
    return jsonify({
        'location': location,
        'region': region,
        'region_name': material_rate_service.REGIONS.get(region, region)
    }), 200


# ============== LIVE PRICES ENDPOINTS ==============

@bp.route('/live', methods=['GET'])
def get_live_prices():
    """
    Get live material prices from market sources.
    Query params:
        region: north, south, west, east, central, northeast (default: west)
        refresh: true/false - force refresh cache (default: false)
    """
    region = request.args.get('region', 'west')
    force_refresh = request.args.get('refresh', 'false').lower() == 'true'

    try:
        prices = live_price_service.get_live_prices(region, force_refresh)
        return jsonify(prices), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'message': 'Failed to fetch live prices. Using cached data.'
        }), 500


@bp.route('/live/history/<material_id>', methods=['GET'])
def get_price_history(material_id):
    """
    Get price history for a material.
    Query params: days (default: 30)
    """
    try:
        days = int(request.args.get('days', 30))
    except (ValueError, TypeError):
        days = 30
    history = live_price_service.get_price_history(material_id, days)
    return jsonify({
        'material_id': material_id,
        'days': days,
        'history': history
    }), 200


@bp.route('/live/alerts', methods=['GET'])
def get_live_price_alerts():
    """
    Get materials with significant price changes.
    Query params: threshold (default: 5.0 percent)
    """
    try:
        threshold = float(request.args.get('threshold', 5.0))
    except (ValueError, TypeError):
        threshold = 5.0
    alerts = live_price_service.get_price_alerts(threshold)
    return jsonify({
        'threshold_percent': threshold,
        'alerts': alerts,
        'count': len(alerts)
    }), 200


# ============== CROWDSOURCED PRICE ENDPOINTS ==============

@bp.route('/crowdsourced/report', methods=['POST'])
def report_price():
    """
    Submit a crowdsourced price report.
    JSON body: {
        "material_name": "Cement OPC 43",
        "material_category": "cement",
        "price": 420,
        "city": "Chennai",
        "brand": "UltraTech" (optional),
        "reporter_name": "Ravi" (optional),
        "reporter_type": "contractor" (optional),
        "notes": "Price at local dealer" (optional)
    }
    """
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    required = ['material_name', 'material_category', 'price', 'city']
    missing = [f for f in required if f not in data]
    if missing:
        return jsonify({'error': f'Missing required fields: {missing}'}), 400

    # Validate price is positive
    try:
        price = float(data['price'])
        if price <= 0:
            return jsonify({'error': 'Price must be positive'}), 400
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid price value'}), 400

    # Determine region from city
    city = data['city'].strip()
    region = CITY_REGION_MAP.get(city.lower(), 'west')

    # Get unit from category
    category = data['material_category'].lower()
    unit = MATERIAL_UNITS.get(category, 'per unit')

    report = PriceReport(
        material_name=data['material_name'].strip(),
        material_category=category,
        price=price,
        unit=unit,
        city=city,
        region=region,
        brand=data.get('brand', '').strip() or None,
        reporter_name=data.get('reporter_name', '').strip() or None,
        reporter_type=data.get('reporter_type', '').strip() or None,
        notes=data.get('notes', '').strip() or None,
    )

    db.session.add(report)
    db.session.commit()

    return jsonify({
        'success': True,
        'message': 'Price report submitted successfully!',
        'report': report.to_dict()
    }), 201


@bp.route('/crowdsourced/prices', methods=['GET'])
def get_crowdsourced_prices():
    """
    Get crowdsourced average prices.
    Query params:
        city: filter by city
        region: filter by region
        category: filter by material category
        days: number of days to look back (default: 30)
    """
    city = request.args.get('city', '').strip() or None
    region = request.args.get('region', '').strip() or None
    category = request.args.get('category', '').strip() or None
    try:
        days = int(request.args.get('days', 30))
    except (ValueError, TypeError):
        days = 30

    cutoff = datetime.utcnow() - timedelta(days=days)
    query = PriceReport.query.filter(PriceReport.created_at >= cutoff)

    if city:
        query = query.filter(PriceReport.city.ilike(f'%{city}%'))
    if region:
        query = query.filter(PriceReport.region == region)
    if category:
        query = query.filter(PriceReport.material_category == category)

    reports = query.order_by(PriceReport.created_at.desc()).all()

    # Group by material category and calculate averages
    grouped = {}
    for r in reports:
        key = r.material_category
        if key not in grouped:
            grouped[key] = {
                'material_category': key,
                'reports': [],
                'prices': [],
                'cities': set(),
            }
        grouped[key]['reports'].append(r.to_dict())
        grouped[key]['prices'].append(r.price)
        grouped[key]['cities'].add(r.city)

    result = []
    for key, data in grouped.items():
        prices = data['prices']
        result.append({
            'material_category': key,
            'avg_price': round(sum(prices) / len(prices), 2),
            'min_price': min(prices),
            'max_price': max(prices),
            'report_count': len(prices),
            'cities_covered': list(data['cities']),
            'unit': MATERIAL_UNITS.get(key, 'per unit'),
            'recent_reports': data['reports'][:10],  # Last 10 reports
        })

    return jsonify({
        'success': True,
        'days': days,
        'total_reports': len(reports),
        'materials': result,
        'city_filter': city,
        'region_filter': region,
    }), 200


@bp.route('/crowdsourced/recent', methods=['GET'])
def get_recent_reports():
    """Get most recent price reports"""
    try:
        limit = int(request.args.get('limit', 20))
    except (ValueError, TypeError):
        limit = 20
    reports = PriceReport.query.order_by(
        PriceReport.created_at.desc()
    ).limit(limit).all()

    return jsonify({
        'success': True,
        'reports': [r.to_dict() for r in reports],
        'count': len(reports),
    }), 200


@bp.route('/crowdsourced/stats', methods=['GET'])
def get_crowdsourced_stats():
    """Get crowdsourced pricing statistics"""
    total = PriceReport.query.count()
    last_7_days = PriceReport.query.filter(
        PriceReport.created_at >= datetime.utcnow() - timedelta(days=7)
    ).count()
    cities = db.session.query(PriceReport.city).distinct().count()
    categories = db.session.query(PriceReport.material_category).distinct().count()

    return jsonify({
        'success': True,
        'total_reports': total,
        'reports_last_7_days': last_7_days,
        'cities_covered': cities,
        'categories_covered': categories,
    }), 200

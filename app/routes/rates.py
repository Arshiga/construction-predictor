# API Routes for Live Material Rates
from flask import Blueprint, request, jsonify
from app.services.material_rates import material_rate_service
from app.services.live_prices import live_price_service

bp = Blueprint('rates', __name__, url_prefix='/api/rates')


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
    days = int(request.args.get('days', 30))
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
    threshold = float(request.args.get('threshold', 5.0))
    alerts = live_price_service.get_price_alerts(threshold)
    return jsonify({
        'threshold_percent': threshold,
        'alerts': alerts,
        'count': len(alerts)
    }), 200

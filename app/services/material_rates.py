# Live Material Rate Service
# Provides current market rates, historical trends, and price alerts

import json
import os
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import random

# Path to rates database
RATES_DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'material_rates.json')


class MaterialRateService:
    """
    Service for managing live material rates with:
    - Current market prices by region
    - Historical price tracking
    - Trend analysis
    - Price change alerts
    """

    # Material Categories
    CATEGORIES = {
        'cement': 'Cement',
        'steel': 'Steel & Iron',
        'aggregates': 'Aggregates & Sand',
        'bricks': 'Bricks & Blocks',
        'wood': 'Wood & Timber',
        'paint': 'Paints & Finishes',
        'plumbing': 'Plumbing Materials',
        'electrical': 'Electrical Materials',
        'tiles': 'Tiles & Flooring',
        'labor': 'Labor Rates'
    }

    # Regions
    REGIONS = {
        'north': 'North India (Delhi, UP, Punjab, Haryana)',
        'south': 'South India (Tamil Nadu, Kerala, Karnataka, AP, Telangana)',
        'west': 'West India (Maharashtra, Gujarat, Rajasthan, MP)',
        'east': 'East India (West Bengal, Bihar, Odisha, Jharkhand)',
        'central': 'Central India (MP, Chhattisgarh)',
        'northeast': 'North East India'
    }

    def __init__(self):
        self.rates_db = self._load_rates_db()

    def _load_rates_db(self) -> Dict:
        """Load rates database from JSON file"""
        if os.path.exists(RATES_DB_PATH):
            try:
                with open(RATES_DB_PATH, 'r') as f:
                    return json.load(f)
            except:
                pass
        return self._create_default_rates_db()

    def _save_rates_db(self):
        """Save rates database to JSON file"""
        os.makedirs(os.path.dirname(RATES_DB_PATH), exist_ok=True)
        with open(RATES_DB_PATH, 'w') as f:
            json.dump(self.rates_db, f, indent=2)

    def _create_default_rates_db(self) -> Dict:
        """Create default rates database with current market rates"""
        today = datetime.now().strftime('%Y-%m-%d')

        db = {
            'last_updated': today,
            'version': '2024-25',
            'materials': {
                # CEMENT
                'cement_opc_43': {
                    'name': 'OPC 43 Grade Cement',
                    'category': 'cement',
                    'unit': 'Bag (50kg)',
                    'brand_rates': {
                        'UltraTech': 390,
                        'ACC': 385,
                        'Ambuja': 380,
                        'Shree': 370,
                        'Birla': 375,
                        'Average': 380
                    },
                    'regional_rates': {
                        'north': 375,
                        'south': 385,
                        'west': 390,
                        'east': 370,
                        'central': 365,
                        'northeast': 420
                    },
                    'history': [
                        {'date': '2024-01-01', 'rate': 360},
                        {'date': '2024-02-01', 'rate': 365},
                        {'date': '2024-03-01', 'rate': 368},
                        {'date': '2024-04-01', 'rate': 372},
                        {'date': '2024-05-01', 'rate': 375},
                        {'date': '2024-06-01', 'rate': 378},
                        {'date': '2024-07-01', 'rate': 380},
                        {'date': '2024-08-01', 'rate': 382},
                        {'date': '2024-09-01', 'rate': 380},
                        {'date': '2024-10-01', 'rate': 378},
                        {'date': '2024-11-01', 'rate': 380},
                        {'date': '2024-12-01', 'rate': 380}
                    ],
                    'alert_threshold': 5  # Alert if change > 5%
                },
                'cement_opc_53': {
                    'name': 'OPC 53 Grade Cement',
                    'category': 'cement',
                    'unit': 'Bag (50kg)',
                    'brand_rates': {
                        'UltraTech': 410,
                        'ACC': 405,
                        'Ambuja': 400,
                        'Shree': 390,
                        'Average': 400
                    },
                    'regional_rates': {
                        'north': 395,
                        'south': 405,
                        'west': 410,
                        'east': 390,
                        'central': 385,
                        'northeast': 440
                    },
                    'history': [
                        {'date': '2024-01-01', 'rate': 380},
                        {'date': '2024-06-01', 'rate': 390},
                        {'date': '2024-12-01', 'rate': 400}
                    ],
                    'alert_threshold': 5
                },
                'cement_ppc': {
                    'name': 'PPC (Portland Pozzolana Cement)',
                    'category': 'cement',
                    'unit': 'Bag (50kg)',
                    'brand_rates': {
                        'UltraTech': 375,
                        'ACC': 370,
                        'Ambuja': 365,
                        'Average': 370
                    },
                    'regional_rates': {
                        'north': 365,
                        'south': 375,
                        'west': 380,
                        'east': 360,
                        'central': 355,
                        'northeast': 410
                    },
                    'history': [
                        {'date': '2024-01-01', 'rate': 350},
                        {'date': '2024-06-01', 'rate': 360},
                        {'date': '2024-12-01', 'rate': 370}
                    ],
                    'alert_threshold': 5
                },

                # STEEL
                'steel_tmt_fe500': {
                    'name': 'TMT Steel Fe500 Grade',
                    'category': 'steel',
                    'unit': 'Kg',
                    'brand_rates': {
                        'TATA Tiscon': 75,
                        'SAIL': 72,
                        'JSW': 73,
                        'Jindal': 71,
                        'Kamdhenu': 70,
                        'Average': 72
                    },
                    'regional_rates': {
                        'north': 72,
                        'south': 74,
                        'west': 73,
                        'east': 70,
                        'central': 71,
                        'northeast': 78
                    },
                    'history': [
                        {'date': '2024-01-01', 'rate': 68},
                        {'date': '2024-02-01', 'rate': 69},
                        {'date': '2024-03-01', 'rate': 70},
                        {'date': '2024-04-01', 'rate': 71},
                        {'date': '2024-05-01', 'rate': 72},
                        {'date': '2024-06-01', 'rate': 73},
                        {'date': '2024-07-01', 'rate': 74},
                        {'date': '2024-08-01', 'rate': 73},
                        {'date': '2024-09-01', 'rate': 72},
                        {'date': '2024-10-01', 'rate': 71},
                        {'date': '2024-11-01', 'rate': 72},
                        {'date': '2024-12-01', 'rate': 72}
                    ],
                    'alert_threshold': 3
                },
                'steel_tmt_fe550': {
                    'name': 'TMT Steel Fe550 Grade',
                    'category': 'steel',
                    'unit': 'Kg',
                    'brand_rates': {
                        'TATA Tiscon': 82,
                        'SAIL': 78,
                        'JSW': 80,
                        'Average': 78
                    },
                    'regional_rates': {
                        'north': 78,
                        'south': 80,
                        'west': 79,
                        'east': 76,
                        'central': 77,
                        'northeast': 85
                    },
                    'history': [
                        {'date': '2024-01-01', 'rate': 74},
                        {'date': '2024-06-01', 'rate': 76},
                        {'date': '2024-12-01', 'rate': 78}
                    ],
                    'alert_threshold': 3
                },
                'steel_structural': {
                    'name': 'Structural Steel (Angles, Channels)',
                    'category': 'steel',
                    'unit': 'Kg',
                    'brand_rates': {
                        'SAIL': 75,
                        'JSW': 76,
                        'Average': 75
                    },
                    'regional_rates': {
                        'north': 75,
                        'south': 77,
                        'west': 76,
                        'east': 73,
                        'central': 74,
                        'northeast': 82
                    },
                    'history': [
                        {'date': '2024-01-01', 'rate': 72},
                        {'date': '2024-06-01', 'rate': 74},
                        {'date': '2024-12-01', 'rate': 75}
                    ],
                    'alert_threshold': 3
                },

                # AGGREGATES
                'aggregate_20mm': {
                    'name': 'Coarse Aggregate 20mm',
                    'category': 'aggregates',
                    'unit': 'Cubic Meter',
                    'brand_rates': {'Average': 1800},
                    'regional_rates': {
                        'north': 1700,
                        'south': 1900,
                        'west': 1850,
                        'east': 1600,
                        'central': 1550,
                        'northeast': 2200
                    },
                    'history': [
                        {'date': '2024-01-01', 'rate': 1700},
                        {'date': '2024-06-01', 'rate': 1750},
                        {'date': '2024-12-01', 'rate': 1800}
                    ],
                    'alert_threshold': 8
                },
                'aggregate_40mm': {
                    'name': 'Coarse Aggregate 40mm',
                    'category': 'aggregates',
                    'unit': 'Cubic Meter',
                    'brand_rates': {'Average': 1700},
                    'regional_rates': {
                        'north': 1600,
                        'south': 1800,
                        'west': 1750,
                        'east': 1500,
                        'central': 1450,
                        'northeast': 2100
                    },
                    'history': [
                        {'date': '2024-01-01', 'rate': 1600},
                        {'date': '2024-06-01', 'rate': 1650},
                        {'date': '2024-12-01', 'rate': 1700}
                    ],
                    'alert_threshold': 8
                },
                'river_sand': {
                    'name': 'River Sand (Fine Aggregate)',
                    'category': 'aggregates',
                    'unit': 'Cubic Meter',
                    'brand_rates': {'Average': 2200},
                    'regional_rates': {
                        'north': 2000,
                        'south': 2500,
                        'west': 2300,
                        'east': 1800,
                        'central': 1900,
                        'northeast': 2800
                    },
                    'history': [
                        {'date': '2024-01-01', 'rate': 2000},
                        {'date': '2024-06-01', 'rate': 2100},
                        {'date': '2024-12-01', 'rate': 2200}
                    ],
                    'alert_threshold': 10
                },
                'm_sand': {
                    'name': 'M-Sand (Manufactured Sand)',
                    'category': 'aggregates',
                    'unit': 'Cubic Meter',
                    'brand_rates': {'Average': 1500},
                    'regional_rates': {
                        'north': 1400,
                        'south': 1600,
                        'west': 1550,
                        'east': 1300,
                        'central': 1350,
                        'northeast': 1800
                    },
                    'history': [
                        {'date': '2024-01-01', 'rate': 1400},
                        {'date': '2024-06-01', 'rate': 1450},
                        {'date': '2024-12-01', 'rate': 1500}
                    ],
                    'alert_threshold': 8
                },

                # BRICKS
                'brick_first_class': {
                    'name': 'First Class Bricks',
                    'category': 'bricks',
                    'unit': 'Per 1000 Nos',
                    'brand_rates': {'Average': 8500},
                    'regional_rates': {
                        'north': 8000,
                        'south': 9000,
                        'west': 8500,
                        'east': 7500,
                        'central': 7000,
                        'northeast': 10000
                    },
                    'history': [
                        {'date': '2024-01-01', 'rate': 8000},
                        {'date': '2024-06-01', 'rate': 8200},
                        {'date': '2024-12-01', 'rate': 8500}
                    ],
                    'alert_threshold': 5
                },
                'fly_ash_brick': {
                    'name': 'Fly Ash Bricks',
                    'category': 'bricks',
                    'unit': 'Per 1000 Nos',
                    'brand_rates': {'Average': 5500},
                    'regional_rates': {
                        'north': 5200,
                        'south': 5800,
                        'west': 5500,
                        'east': 5000,
                        'central': 4800,
                        'northeast': 6500
                    },
                    'history': [
                        {'date': '2024-01-01', 'rate': 5200},
                        {'date': '2024-06-01', 'rate': 5400},
                        {'date': '2024-12-01', 'rate': 5500}
                    ],
                    'alert_threshold': 5
                },
                'aac_block': {
                    'name': 'AAC Blocks',
                    'category': 'bricks',
                    'unit': 'Cubic Meter',
                    'brand_rates': {
                        'Ultratech': 4200,
                        'Magicrete': 4000,
                        'Average': 4000
                    },
                    'regional_rates': {
                        'north': 3900,
                        'south': 4200,
                        'west': 4100,
                        'east': 3800,
                        'central': 3700,
                        'northeast': 4800
                    },
                    'history': [
                        {'date': '2024-01-01', 'rate': 3800},
                        {'date': '2024-06-01', 'rate': 3900},
                        {'date': '2024-12-01', 'rate': 4000}
                    ],
                    'alert_threshold': 5
                },

                # BITUMEN (for roads)
                'bitumen_vg30': {
                    'name': 'Bitumen VG-30',
                    'category': 'aggregates',
                    'unit': 'MT (Metric Ton)',
                    'brand_rates': {
                        'IOCL': 48000,
                        'BPCL': 47500,
                        'HPCL': 47800,
                        'Average': 47500
                    },
                    'regional_rates': {
                        'north': 47000,
                        'south': 48000,
                        'west': 47500,
                        'east': 46500,
                        'central': 46000,
                        'northeast': 52000
                    },
                    'history': [
                        {'date': '2024-01-01', 'rate': 45000},
                        {'date': '2024-06-01', 'rate': 46500},
                        {'date': '2024-12-01', 'rate': 47500}
                    ],
                    'alert_threshold': 5
                }
            },

            # LABOR RATES
            'labor': {
                'unskilled': {
                    'name': 'Unskilled Labor (Mazdoor/Beldar)',
                    'unit': 'Per Day',
                    'regional_rates': {
                        'north': 550,
                        'south': 600,
                        'west': 580,
                        'east': 500,
                        'central': 480,
                        'northeast': 520
                    },
                    'history': [
                        {'date': '2024-01-01', 'rate': 500},
                        {'date': '2024-06-01', 'rate': 530},
                        {'date': '2024-12-01', 'rate': 550}
                    ],
                    'min_wage_ref': 'Minimum Wages Act'
                },
                'mason': {
                    'name': 'Mason (Raj Mistri)',
                    'unit': 'Per Day',
                    'regional_rates': {
                        'north': 850,
                        'south': 900,
                        'west': 880,
                        'east': 750,
                        'central': 720,
                        'northeast': 780
                    },
                    'history': [
                        {'date': '2024-01-01', 'rate': 800},
                        {'date': '2024-06-01', 'rate': 830},
                        {'date': '2024-12-01', 'rate': 850}
                    ]
                },
                'carpenter': {
                    'name': 'Carpenter',
                    'unit': 'Per Day',
                    'regional_rates': {
                        'north': 850,
                        'south': 900,
                        'west': 880,
                        'east': 750,
                        'central': 720,
                        'northeast': 780
                    },
                    'history': [
                        {'date': '2024-01-01', 'rate': 800},
                        {'date': '2024-06-01', 'rate': 830},
                        {'date': '2024-12-01', 'rate': 850}
                    ]
                },
                'plumber': {
                    'name': 'Plumber',
                    'unit': 'Per Day',
                    'regional_rates': {
                        'north': 800,
                        'south': 850,
                        'west': 830,
                        'east': 700,
                        'central': 680,
                        'northeast': 750
                    },
                    'history': [
                        {'date': '2024-01-01', 'rate': 750},
                        {'date': '2024-06-01', 'rate': 780},
                        {'date': '2024-12-01', 'rate': 800}
                    ]
                },
                'electrician': {
                    'name': 'Electrician',
                    'unit': 'Per Day',
                    'regional_rates': {
                        'north': 850,
                        'south': 900,
                        'west': 880,
                        'east': 750,
                        'central': 720,
                        'northeast': 780
                    },
                    'history': [
                        {'date': '2024-01-01', 'rate': 800},
                        {'date': '2024-06-01', 'rate': 830},
                        {'date': '2024-12-01', 'rate': 850}
                    ]
                },
                'bar_bender': {
                    'name': 'Bar Bender (Sariya Mistri)',
                    'unit': 'Per Day',
                    'regional_rates': {
                        'north': 800,
                        'south': 850,
                        'west': 830,
                        'east': 700,
                        'central': 680,
                        'northeast': 750
                    },
                    'history': [
                        {'date': '2024-01-01', 'rate': 750},
                        {'date': '2024-06-01', 'rate': 780},
                        {'date': '2024-12-01', 'rate': 800}
                    ]
                },
                'painter': {
                    'name': 'Painter',
                    'unit': 'Per Day',
                    'regional_rates': {
                        'north': 750,
                        'south': 800,
                        'west': 780,
                        'east': 650,
                        'central': 630,
                        'northeast': 700
                    },
                    'history': [
                        {'date': '2024-01-01', 'rate': 700},
                        {'date': '2024-06-01', 'rate': 730},
                        {'date': '2024-12-01', 'rate': 750}
                    ]
                },
                'welder': {
                    'name': 'Welder',
                    'unit': 'Per Day',
                    'regional_rates': {
                        'north': 900,
                        'south': 950,
                        'west': 930,
                        'east': 800,
                        'central': 780,
                        'northeast': 850
                    },
                    'history': [
                        {'date': '2024-01-01', 'rate': 850},
                        {'date': '2024-06-01', 'rate': 880},
                        {'date': '2024-12-01', 'rate': 900}
                    ]
                },
                'helper': {
                    'name': 'Helper (Semi-skilled)',
                    'unit': 'Per Day',
                    'regional_rates': {
                        'north': 600,
                        'south': 650,
                        'west': 630,
                        'east': 550,
                        'central': 520,
                        'northeast': 580
                    },
                    'history': [
                        {'date': '2024-01-01', 'rate': 550},
                        {'date': '2024-06-01', 'rate': 580},
                        {'date': '2024-12-01', 'rate': 600}
                    ]
                }
            },

            # Price alerts
            'alerts': [],

            # Update log
            'update_log': [
                {'date': today, 'action': 'Database created', 'user': 'system'}
            ]
        }

        self._save_rates_db_data(db)
        return db

    def _save_rates_db_data(self, db):
        """Save specific database data"""
        os.makedirs(os.path.dirname(RATES_DB_PATH), exist_ok=True)
        with open(RATES_DB_PATH, 'w') as f:
            json.dump(db, f, indent=2)

    def get_all_materials(self) -> Dict:
        """Get all material rates"""
        return self.rates_db.get('materials', {})

    def get_all_labor_rates(self) -> Dict:
        """Get all labor rates"""
        return self.rates_db.get('labor', {})

    def get_material_rate(self, material_id: str, region: str = 'west') -> Dict:
        """Get rate for a specific material in a region"""
        material = self.rates_db.get('materials', {}).get(material_id)
        if not material:
            return None

        current_rate = material.get('regional_rates', {}).get(region,
                       material.get('brand_rates', {}).get('Average', 0))

        # Calculate trend
        history = material.get('history', [])
        trend = self._calculate_trend(history)

        return {
            'id': material_id,
            'name': material.get('name'),
            'category': material.get('category'),
            'unit': material.get('unit'),
            'current_rate': current_rate,
            'brand_rates': material.get('brand_rates', {}),
            'regional_rates': material.get('regional_rates', {}),
            'trend': trend,
            'history': history,
            'alert_threshold': material.get('alert_threshold', 5)
        }

    def get_labor_rate(self, labor_type: str, region: str = 'west') -> Dict:
        """Get labor rate for a specific type in a region"""
        labor = self.rates_db.get('labor', {}).get(labor_type)
        if not labor:
            return None

        current_rate = labor.get('regional_rates', {}).get(region, 0)
        history = labor.get('history', [])
        trend = self._calculate_trend(history)

        return {
            'id': labor_type,
            'name': labor.get('name'),
            'unit': labor.get('unit'),
            'current_rate': current_rate,
            'regional_rates': labor.get('regional_rates', {}),
            'trend': trend,
            'history': history
        }

    def _calculate_trend(self, history: List[Dict]) -> Dict:
        """Calculate price trend from history"""
        if len(history) < 2:
            return {'direction': 'stable', 'change_percent': 0, 'change_amount': 0}

        latest = history[-1]['rate']
        previous = history[-2]['rate']

        change_amount = latest - previous
        change_percent = ((latest - previous) / previous) * 100 if previous > 0 else 0

        if change_percent > 1:
            direction = 'up'
        elif change_percent < -1:
            direction = 'down'
        else:
            direction = 'stable'

        # Calculate 6-month trend
        if len(history) >= 6:
            six_month_ago = history[-6]['rate']
            six_month_change = ((latest - six_month_ago) / six_month_ago) * 100 if six_month_ago > 0 else 0
        else:
            six_month_change = change_percent

        return {
            'direction': direction,
            'change_percent': round(change_percent, 2),
            'change_amount': round(change_amount, 2),
            'six_month_change': round(six_month_change, 2)
        }

    def update_material_rate(self, material_id: str, new_rate: float, region: str = None) -> Dict:
        """Update a material rate and track history"""
        material = self.rates_db.get('materials', {}).get(material_id)
        if not material:
            return {'success': False, 'error': 'Material not found'}

        today = datetime.now().strftime('%Y-%m-%d')
        old_rate = material.get('brand_rates', {}).get('Average', 0)

        # Update rate
        if region:
            material['regional_rates'][region] = new_rate
        else:
            material['brand_rates']['Average'] = new_rate
            # Update all regional rates proportionally
            ratio = new_rate / old_rate if old_rate > 0 else 1
            for r in material['regional_rates']:
                material['regional_rates'][r] = round(material['regional_rates'][r] * ratio, 2)

        # Add to history
        material['history'].append({'date': today, 'rate': new_rate})

        # Check for alert
        alert = self._check_price_alert(material_id, old_rate, new_rate, material.get('alert_threshold', 5))

        # Update database
        self.rates_db['materials'][material_id] = material
        self.rates_db['last_updated'] = today
        self._save_rates_db()

        return {
            'success': True,
            'old_rate': old_rate,
            'new_rate': new_rate,
            'alert': alert
        }

    def _check_price_alert(self, material_id: str, old_rate: float, new_rate: float, threshold: float) -> Optional[Dict]:
        """Check if price change exceeds threshold and create alert"""
        if old_rate == 0:
            return None

        change_percent = abs((new_rate - old_rate) / old_rate) * 100

        if change_percent >= threshold:
            alert = {
                'id': f"alert_{datetime.now().strftime('%Y%m%d%H%M%S')}",
                'material_id': material_id,
                'type': 'price_increase' if new_rate > old_rate else 'price_decrease',
                'old_rate': old_rate,
                'new_rate': new_rate,
                'change_percent': round(change_percent, 2),
                'threshold': threshold,
                'date': datetime.now().strftime('%Y-%m-%d %H:%M'),
                'read': False
            }

            self.rates_db['alerts'].insert(0, alert)
            # Keep only last 50 alerts
            self.rates_db['alerts'] = self.rates_db['alerts'][:50]

            return alert

        return None

    def get_alerts(self, unread_only: bool = False) -> List[Dict]:
        """Get price change alerts"""
        alerts = self.rates_db.get('alerts', [])
        if unread_only:
            alerts = [a for a in alerts if not a.get('read', False)]
        return alerts

    def mark_alert_read(self, alert_id: str):
        """Mark an alert as read"""
        for alert in self.rates_db.get('alerts', []):
            if alert.get('id') == alert_id:
                alert['read'] = True
                self._save_rates_db()
                break

    def get_rates_summary(self, region: str = 'west') -> Dict:
        """Get summary of all rates for a region"""
        summary = {
            'region': region,
            'region_name': self.REGIONS.get(region, region),
            'last_updated': self.rates_db.get('last_updated'),
            'materials': {},
            'labor': {},
            'alerts_count': len([a for a in self.rates_db.get('alerts', []) if not a.get('read', False)])
        }

        # Materials summary
        for mat_id, material in self.rates_db.get('materials', {}).items():
            rate = material.get('regional_rates', {}).get(region,
                   material.get('brand_rates', {}).get('Average', 0))
            trend = self._calculate_trend(material.get('history', []))

            summary['materials'][mat_id] = {
                'name': material.get('name'),
                'category': material.get('category'),
                'unit': material.get('unit'),
                'rate': rate,
                'trend': trend['direction'],
                'change_percent': trend['change_percent']
            }

        # Labor summary
        for labor_id, labor in self.rates_db.get('labor', {}).items():
            rate = labor.get('regional_rates', {}).get(region, 0)
            trend = self._calculate_trend(labor.get('history', []))

            summary['labor'][labor_id] = {
                'name': labor.get('name'),
                'unit': labor.get('unit'),
                'rate': rate,
                'trend': trend['direction'],
                'change_percent': trend['change_percent']
            }

        return summary

    def get_region_from_location(self, location: str) -> str:
        """Determine region from location string"""
        location_lower = location.lower() if location else ''

        # North India
        north_states = ['delhi', 'uttar pradesh', 'punjab', 'haryana', 'himachal', 'uttarakhand', 'jammu', 'kashmir', 'chandigarh']
        if any(state in location_lower for state in north_states):
            return 'north'

        # South India
        south_states = ['tamil nadu', 'kerala', 'karnataka', 'andhra', 'telangana', 'chennai', 'bangalore', 'hyderabad', 'kochi']
        if any(state in location_lower for state in south_states):
            return 'south'

        # West India
        west_states = ['maharashtra', 'gujarat', 'rajasthan', 'goa', 'mumbai', 'pune', 'ahmedabad', 'jaipur']
        if any(state in location_lower for state in west_states):
            return 'west'

        # East India
        east_states = ['west bengal', 'bihar', 'odisha', 'jharkhand', 'kolkata', 'patna']
        if any(state in location_lower for state in east_states):
            return 'east'

        # Central India
        central_states = ['madhya pradesh', 'chhattisgarh', 'bhopal', 'raipur']
        if any(state in location_lower for state in central_states):
            return 'central'

        # Northeast
        ne_states = ['assam', 'meghalaya', 'manipur', 'mizoram', 'tripura', 'nagaland', 'arunachal', 'sikkim', 'guwahati']
        if any(state in location_lower for state in ne_states):
            return 'northeast'

        return 'west'  # Default


# Singleton instance
material_rate_service = MaterialRateService()

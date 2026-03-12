"""
Generate 5000 realistic synthetic construction project data
using actual CPWD/PWD SOR rates and Indian market conditions.
"""

import csv
import random
import math

random.seed(42)

# ============================================
# REALISTIC PARAMETERS
# ============================================

CITIES = {
    # Metro cities (higher costs)
    'Mumbai': {'factor': 1.25, 'weather': 'high', 'region': 'west'},
    'Delhi': {'factor': 1.20, 'weather': 'high', 'region': 'north'},
    'Bangalore': {'factor': 1.15, 'weather': 'low', 'region': 'south'},
    'Chennai': {'factor': 1.10, 'weather': 'high', 'region': 'south'},
    'Kolkata': {'factor': 1.05, 'weather': 'high', 'region': 'east'},
    'Hyderabad': {'factor': 1.10, 'weather': 'moderate', 'region': 'south'},

    # Tier 1
    'Pune': {'factor': 1.12, 'weather': 'moderate', 'region': 'west'},
    'Ahmedabad': {'factor': 1.08, 'weather': 'moderate', 'region': 'west'},
    'Jaipur': {'factor': 1.05, 'weather': 'high', 'region': 'north'},
    'Lucknow': {'factor': 1.02, 'weather': 'moderate', 'region': 'north'},
    'Chandigarh': {'factor': 1.10, 'weather': 'moderate', 'region': 'north'},
    'Kochi': {'factor': 1.08, 'weather': 'high', 'region': 'south'},
    'Gurgaon': {'factor': 1.18, 'weather': 'high', 'region': 'north'},
    'Noida': {'factor': 1.15, 'weather': 'high', 'region': 'north'},
    'Thane': {'factor': 1.20, 'weather': 'high', 'region': 'west'},
    'Navi Mumbai': {'factor': 1.22, 'weather': 'high', 'region': 'west'},

    # Tier 2
    'Indore': {'factor': 1.00, 'weather': 'moderate', 'region': 'central'},
    'Bhopal': {'factor': 0.98, 'weather': 'moderate', 'region': 'central'},
    'Nagpur': {'factor': 0.98, 'weather': 'moderate', 'region': 'west'},
    'Vadodara': {'factor': 1.02, 'weather': 'moderate', 'region': 'west'},
    'Surat': {'factor': 1.05, 'weather': 'high', 'region': 'west'},
    'Coimbatore': {'factor': 1.00, 'weather': 'low', 'region': 'south'},
    'Visakhapatnam': {'factor': 0.98, 'weather': 'high', 'region': 'south'},
    'Mysore': {'factor': 0.95, 'weather': 'low', 'region': 'south'},
    'Nashik': {'factor': 0.97, 'weather': 'moderate', 'region': 'west'},
    'Rajkot': {'factor': 0.96, 'weather': 'moderate', 'region': 'west'},
    'Madurai': {'factor': 0.93, 'weather': 'moderate', 'region': 'south'},
    'Vijayawada': {'factor': 0.95, 'weather': 'moderate', 'region': 'south'},
    'Mangalore': {'factor': 1.00, 'weather': 'high', 'region': 'south'},
    'Trichy': {'factor': 0.90, 'weather': 'moderate', 'region': 'south'},

    # Tier 3
    'Patna': {'factor': 0.90, 'weather': 'high', 'region': 'east'},
    'Ranchi': {'factor': 0.88, 'weather': 'moderate', 'region': 'east'},
    'Bhubaneswar': {'factor': 0.92, 'weather': 'high', 'region': 'east'},
    'Guwahati': {'factor': 0.95, 'weather': 'high', 'region': 'northeast'},
    'Raipur': {'factor': 0.90, 'weather': 'moderate', 'region': 'central'},
    'Dehradun': {'factor': 1.05, 'weather': 'high', 'region': 'north'},
    'Shimla': {'factor': 1.12, 'weather': 'high', 'region': 'north'},
    'Jodhpur': {'factor': 0.92, 'weather': 'moderate', 'region': 'north'},
    'Udaipur': {'factor': 0.94, 'weather': 'low', 'region': 'north'},
    'Amritsar': {'factor': 0.95, 'weather': 'moderate', 'region': 'north'},
    'Varanasi': {'factor': 0.90, 'weather': 'moderate', 'region': 'north'},
    'Agra': {'factor': 0.93, 'weather': 'high', 'region': 'north'},
    'Kanpur': {'factor': 0.88, 'weather': 'moderate', 'region': 'north'},
    'Goa': {'factor': 1.08, 'weather': 'high', 'region': 'west'},
    'Pondicherry': {'factor': 1.02, 'weather': 'high', 'region': 'south'},
    'Srinagar': {'factor': 1.15, 'weather': 'high', 'region': 'north'},
    'Jamshedpur': {'factor': 0.88, 'weather': 'moderate', 'region': 'east'},
    'Ludhiana': {'factor': 0.95, 'weather': 'moderate', 'region': 'north'},
    'Faridabad': {'factor': 1.12, 'weather': 'high', 'region': 'north'},
    'Gandhinagar': {'factor': 1.05, 'weather': 'moderate', 'region': 'west'},
    'Thiruvananthapuram': {'factor': 1.05, 'weather': 'high', 'region': 'south'},
    'Thrissur': {'factor': 1.02, 'weather': 'high', 'region': 'south'},
    'Aurangabad': {'factor': 0.92, 'weather': 'moderate', 'region': 'west'},
    'Hubli': {'factor': 0.90, 'weather': 'low', 'region': 'south'},
    'Warangal': {'factor': 0.88, 'weather': 'moderate', 'region': 'south'},
    'Guntur': {'factor': 0.87, 'weather': 'moderate', 'region': 'south'},
    'Jabalpur': {'factor': 0.88, 'weather': 'moderate', 'region': 'central'},
    'Dehradun': {'factor': 1.05, 'weather': 'high', 'region': 'north'},
    'Meerut': {'factor': 0.92, 'weather': 'moderate', 'region': 'north'},
    'Bareilly': {'factor': 0.85, 'weather': 'moderate', 'region': 'north'},
    'Aligarh': {'factor': 0.85, 'weather': 'moderate', 'region': 'north'},
    'Salem': {'factor': 0.88, 'weather': 'low', 'region': 'south'},
    'Tirupati': {'factor': 0.90, 'weather': 'moderate', 'region': 'south'},
    'Vellore': {'factor': 0.88, 'weather': 'moderate', 'region': 'south'},
    'Thanjavur': {'factor': 0.87, 'weather': 'moderate', 'region': 'south'},
}

# Base cost per sqft (SOR-derived realistic rates)
BASE_COST_PER_SQFT = {
    'residential': {
        'economy': {'min': 1400, 'max': 1800},
        'standard': {'min': 1800, 'max': 2400},
        'premium': {'min': 2400, 'max': 3800},
    },
    'commercial': {
        'economy': {'min': 1800, 'max': 2400},
        'standard': {'min': 2400, 'max': 3200},
        'premium': {'min': 3200, 'max': 5000},
    },
    'industrial': {
        'economy': {'min': 1200, 'max': 1800},
        'standard': {'min': 1800, 'max': 2600},
        'premium': {'min': 2600, 'max': 3500},
    },
    'infrastructure': {
        'economy': {'min': 2000, 'max': 2800},
        'standard': {'min': 2800, 'max': 3800},
        'premium': {'min': 3800, 'max': 5500},
    },
}

# Area ranges by project type (sqft)
AREA_RANGES = {
    'residential': {'min': 800, 'max': 8000},
    'commercial': {'min': 3000, 'max': 50000},
    'industrial': {'min': 5000, 'max': 80000},
    'infrastructure': {'min': 2000, 'max': 25000},
}

# Floor ranges
FLOOR_RANGES = {
    'residential': {'min': 1, 'max': 4},
    'commercial': {'min': 1, 'max': 8},
    'industrial': {'min': 1, 'max': 3},
    'infrastructure': {'min': 1, 'max': 2},
}

# Workers per 1000 sqft (approximate)
WORKERS_PER_1000SQFT = {
    'residential': {'min': 4, 'max': 8},
    'commercial': {'min': 3, 'max': 6},
    'industrial': {'min': 2, 'max': 5},
    'infrastructure': {'min': 4, 'max': 8},
}

# Duration per 1000 sqft in days
DURATION_PER_1000SQFT = {
    'residential': {'min': 30, 'max': 55},
    'commercial': {'min': 20, 'max': 40},
    'industrial': {'min': 15, 'max': 30},
    'infrastructure': {'min': 25, 'max': 45},
}


def generate_project():
    """Generate one realistic construction project record"""

    # Pick project type with realistic distribution
    # More residential projects in India
    project_type = random.choices(
        ['residential', 'commercial', 'industrial', 'infrastructure'],
        weights=[45, 25, 15, 15],
        k=1
    )[0]

    # Pick city
    city = random.choice(list(CITIES.keys()))
    city_info = CITIES[city]

    # Pick material quality with realistic distribution
    material_quality = random.choices(
        ['economy', 'standard', 'premium'],
        weights=[30, 50, 20],
        k=1
    )[0]

    # Pick complexity
    complexity = random.choices(
        ['low', 'medium', 'high'],
        weights=[25, 50, 25],
        k=1
    )[0]

    # Weather risk (based on city)
    weather_risk = city_info['weather']
    # Some randomness — same city can have different seasons
    if random.random() < 0.15:
        weather_risk = random.choice(['low', 'moderate', 'high'])

    # Area
    area_range = AREA_RANGES[project_type]
    total_area = random.randint(area_range['min'], area_range['max'])
    # Round to nearest 100
    total_area = round(total_area / 100) * 100

    # Floors
    floor_range = FLOOR_RANGES[project_type]
    num_floors = random.randint(floor_range['min'], floor_range['max'])

    # Basement (more likely in commercial/premium)
    basement_prob = {
        'residential': 0.15 if material_quality == 'premium' else 0.05,
        'commercial': 0.40 if material_quality == 'premium' else 0.20,
        'industrial': 0.10,
        'infrastructure': 0.05,
    }
    has_basement = random.random() < basement_prob[project_type]

    # Contractor experience
    experience = random.randint(1, 25)
    # Weighted toward 3-15 years (most common)
    experience = max(1, min(25, int(random.gauss(8, 4))))

    # Workers (based on area)
    worker_range = WORKERS_PER_1000SQFT[project_type]
    base_workers = (total_area / 1000) * random.uniform(worker_range['min'], worker_range['max'])
    num_workers = max(5, int(base_workers))
    # Add floor factor
    num_workers = int(num_workers * (1 + (num_floors - 1) * 0.15))

    # Planned duration (based on area and floors)
    dur_range = DURATION_PER_1000SQFT[project_type]
    base_duration = (total_area / 1000) * random.uniform(dur_range['min'], dur_range['max'])
    planned_duration = max(60, int(base_duration))
    # Add floor factor
    planned_duration = int(planned_duration * (1 + (num_floors - 1) * 0.12))
    # Cap at reasonable limits
    planned_duration = min(730, planned_duration)

    # ============================================
    # NEW DETAILED FIELDS
    # ============================================

    # Soil type
    soil_type = random.choices(
        ['normal', 'rocky', 'sandy', 'clay', 'marshy'],
        weights=[40, 15, 20, 15, 10],
        k=1
    )[0]

    # Water table level
    water_table_level = random.choices(
        ['deep', 'moderate', 'shallow', 'high'],
        weights=[35, 30, 20, 15],
        k=1
    )[0]

    # Distance from city (km)
    distance_from_city_km = max(0, int(random.gauss(15, 20)))
    distance_from_city_km = min(150, distance_from_city_km)

    # Site accessibility (correlated with distance)
    if distance_from_city_km > 50:
        site_accessibility = random.choices(['moderate', 'difficult', 'remote'], weights=[20, 40, 40], k=1)[0]
    elif distance_from_city_km > 20:
        site_accessibility = random.choices(['easy', 'moderate', 'difficult'], weights=[20, 50, 30], k=1)[0]
    else:
        site_accessibility = random.choices(['easy', 'moderate', 'difficult'], weights=[60, 30, 10], k=1)[0]

    # Floor height (feet)
    floor_height_ft = random.choices(
        [9, 10, 10.5, 11, 12, 14, 16, 18],
        weights=[10, 30, 20, 15, 10, 8, 5, 2],
        k=1
    )[0]
    if project_type == 'commercial':
        floor_height_ft = random.choices([10, 11, 12, 14, 16], weights=[15, 25, 30, 20, 10], k=1)[0]
    elif project_type == 'industrial':
        floor_height_ft = random.choices([12, 14, 16, 18, 20], weights=[15, 25, 30, 20, 10], k=1)[0]

    # Foundation type (correlated with soil, floors, project type)
    if soil_type in ('marshy', 'clay') or num_floors > 4:
        foundation_type = random.choices(['raft', 'pile', 'strip'], weights=[40, 40, 20], k=1)[0]
    elif soil_type == 'rocky':
        foundation_type = random.choices(['isolated', 'strip', 'raft'], weights=[50, 30, 20], k=1)[0]
    elif num_floors > 2:
        foundation_type = random.choices(['isolated', 'strip', 'raft'], weights=[30, 40, 30], k=1)[0]
    else:
        foundation_type = random.choices(['isolated', 'strip', 'raft', 'pile'], weights=[50, 30, 15, 5], k=1)[0]

    # Number of bathrooms (based on area and project type)
    if project_type == 'residential':
        num_bathrooms = max(1, int(total_area / 600))
    elif project_type == 'commercial':
        num_bathrooms = max(2, int(total_area / 800))
    elif project_type == 'industrial':
        num_bathrooms = max(2, int(total_area / 2000))
    else:
        num_bathrooms = max(1, int(total_area / 1500))
    num_bathrooms = min(50, num_bathrooms + random.randint(-1, 2))
    num_bathrooms = max(1, num_bathrooms)

    # Electrical load (kW) - based on area and project type
    if project_type == 'residential':
        electrical_load_kw = max(3, int(total_area * random.uniform(0.003, 0.008)))
    elif project_type == 'commercial':
        electrical_load_kw = max(10, int(total_area * random.uniform(0.008, 0.02)))
    elif project_type == 'industrial':
        electrical_load_kw = max(20, int(total_area * random.uniform(0.015, 0.05)))
    else:
        electrical_load_kw = max(5, int(total_area * random.uniform(0.002, 0.006)))

    # Finishing level (correlated with material quality)
    if material_quality == 'premium':
        finishing_level = random.choices(['standard', 'premium', 'luxury'], weights=[10, 50, 40], k=1)[0]
    elif material_quality == 'economy':
        finishing_level = random.choices(['basic', 'standard'], weights=[60, 40], k=1)[0]
    else:
        finishing_level = random.choices(['basic', 'standard', 'premium'], weights=[15, 60, 25], k=1)[0]

    # Site topography
    site_topography = random.choices(
        ['flat', 'gentle_slope', 'steep_slope', 'hilly'],
        weights=[55, 25, 12, 8],
        k=1
    )[0]
    # Hilly regions more likely to have slopes
    if city in ('Shimla', 'Dehradun', 'Srinagar', 'Goa', 'Kochi', 'Mangalore'):
        site_topography = random.choices(
            ['flat', 'gentle_slope', 'steep_slope', 'hilly'],
            weights=[20, 30, 30, 20],
            k=1
        )[0]

    # ============================================
    # CALCULATE ACTUAL COST (SOR-based)
    # ============================================

    cost_range = BASE_COST_PER_SQFT[project_type][material_quality]
    base_cost_per_sqft = random.uniform(cost_range['min'], cost_range['max'])

    actual_cost = total_area * base_cost_per_sqft

    # Location factor
    actual_cost *= city_info['factor']

    # Floor premium (10-15% per additional floor)
    floor_premium = 1 + (num_floors - 1) * random.uniform(0.08, 0.15)
    actual_cost *= floor_premium

    # Basement adds 12-20%
    if has_basement:
        actual_cost *= random.uniform(1.12, 1.20)

    # Complexity factor
    complexity_factor = {'low': 0.90, 'medium': 1.0, 'high': 1.25}
    actual_cost *= complexity_factor[complexity]

    # Soil type impact
    soil_cost_factor = {'normal': 1.0, 'rocky': 1.20, 'sandy': 1.05, 'clay': 1.10, 'marshy': 1.25}
    actual_cost *= soil_cost_factor[soil_type]

    # Water table impact
    water_cost_factor = {'deep': 1.0, 'moderate': 1.04, 'shallow': 1.10, 'high': 1.18}
    actual_cost *= water_cost_factor[water_table_level]

    # Distance from city (transport costs)
    if distance_from_city_km > 50:
        actual_cost *= random.uniform(1.10, 1.18)
    elif distance_from_city_km > 20:
        actual_cost *= random.uniform(1.05, 1.10)
    elif distance_from_city_km > 10:
        actual_cost *= random.uniform(1.02, 1.06)

    # Road access impact
    access_cost_factor = {'easy': 1.0, 'moderate': 1.04, 'difficult': 1.12, 'remote': 1.22}
    actual_cost *= access_cost_factor[site_accessibility]

    # Floor height impact (taller = more scaffolding, materials)
    if floor_height_ft > 14:
        actual_cost *= random.uniform(1.08, 1.15)
    elif floor_height_ft > 12:
        actual_cost *= random.uniform(1.03, 1.08)

    # Foundation type impact
    foundation_cost_factor = {'isolated': 1.0, 'strip': 1.06, 'raft': 1.15, 'pile': 1.35}
    actual_cost *= foundation_cost_factor[foundation_type]

    # Bathroom costs (plumbing fixtures: Rs.50K-1.5L each)
    bathroom_cost_per = {'basic': 50000, 'standard': 75000, 'premium': 120000, 'luxury': 180000}
    actual_cost += num_bathrooms * bathroom_cost_per.get(finishing_level, 75000) * random.uniform(0.9, 1.1)

    # Electrical load impact
    if electrical_load_kw > 100:
        actual_cost += electrical_load_kw * random.uniform(600, 1000)
    elif electrical_load_kw > 50:
        actual_cost += electrical_load_kw * random.uniform(400, 700)
    else:
        actual_cost += electrical_load_kw * random.uniform(200, 400)

    # Finishing level impact
    finishing_cost_factor = {'basic': 0.85, 'standard': 1.0, 'premium': 1.30, 'luxury': 1.75}
    actual_cost *= finishing_cost_factor[finishing_level]

    # Topography impact
    topo_cost_factor = {'flat': 1.0, 'gentle_slope': 1.06, 'steep_slope': 1.18, 'hilly': 1.28}
    actual_cost *= topo_cost_factor[site_topography]

    # Experience discount
    if experience > 15:
        actual_cost *= random.uniform(0.92, 0.97)
    elif experience > 10:
        actual_cost *= random.uniform(0.95, 0.99)
    elif experience < 3:
        actual_cost *= random.uniform(1.05, 1.15)

    # Add overhead charges
    actual_cost *= random.uniform(1.05, 1.15)
    actual_cost *= random.uniform(1.13, 1.19)

    # Random market variation (+/- 8%)
    actual_cost *= random.uniform(0.92, 1.08)

    actual_cost = round(actual_cost, -3)

    # ============================================
    # CALCULATE ACTUAL DURATION (with delays)
    # ============================================

    actual_duration = planned_duration

    # Start with some projects finishing early or on time
    actual_duration += random.uniform(-15, 5)

    # Weather delays (only sometimes)
    if random.random() < 0.5:
        weather_delay = {'low': random.uniform(0, 3), 'moderate': random.uniform(0, 8), 'high': random.uniform(3, 18)}
        actual_duration += weather_delay[weather_risk]

    # Complexity delays (only for medium/high)
    if complexity == 'high' and random.random() < 0.6:
        actual_duration += random.uniform(5, 20)
    elif complexity == 'medium' and random.random() < 0.3:
        actual_duration += random.uniform(2, 10)

    # Experience impact on delays
    if experience < 3:
        actual_duration += random.uniform(5, 15)
    elif experience > 15:
        actual_duration -= random.uniform(5, 15)
    elif experience > 10:
        actual_duration -= random.uniform(2, 8)

    # Worker shortage/surplus impact
    optimal_workers = (total_area / 1000) * 5 * (1 + (num_floors - 1) * 0.15)
    worker_ratio = num_workers / max(1, optimal_workers)
    if worker_ratio < 0.7:
        actual_duration += random.uniform(5, 15)
    elif worker_ratio > 1.3:
        actual_duration -= random.uniform(3, 10)

    # Basement adds time
    if has_basement:
        actual_duration += random.uniform(5, 15)

    # Soil & topography delays (only when bad conditions)
    if soil_type in ('rocky', 'marshy') and random.random() < 0.6:
        actual_duration += random.uniform(3, 10)
    if site_topography in ('steep_slope', 'hilly') and random.random() < 0.5:
        actual_duration += random.uniform(3, 12)
    if water_table_level in ('shallow', 'high') and random.random() < 0.5:
        actual_duration += random.uniform(2, 8)
    if site_accessibility in ('difficult', 'remote') and random.random() < 0.5:
        actual_duration += random.uniform(3, 10)
    if foundation_type == 'pile' and random.random() < 0.5:
        actual_duration += random.uniform(5, 12)
    elif foundation_type == 'raft' and random.random() < 0.3:
        actual_duration += random.uniform(2, 6)

    # Random variation
    actual_duration += random.uniform(-8, 5)

    actual_duration = max(planned_duration - 15, int(actual_duration))
    actual_duration = max(45, actual_duration)

    return {
        'project_type': project_type,
        'location': city,
        'total_area_sqft': total_area,
        'num_floors': num_floors,
        'num_workers': num_workers,
        'planned_duration_days': planned_duration,
        'material_quality': material_quality,
        'complexity_level': complexity,
        'has_basement': has_basement,
        'weather_risk_zone': weather_risk,
        'contractor_experience_years': experience,
        'soil_type': soil_type,
        'water_table_level': water_table_level,
        'distance_from_city_km': distance_from_city_km,
        'site_accessibility': site_accessibility,
        'floor_height_ft': floor_height_ft,
        'foundation_type': foundation_type,
        'num_bathrooms': num_bathrooms,
        'electrical_load_kw': electrical_load_kw,
        'finishing_level': finishing_level,
        'site_topography': site_topography,
        'actual_cost': actual_cost,
        'actual_duration_days': actual_duration,
    }


def main():
    print("Generating 5000 synthetic construction project records...")

    fieldnames = [
        'project_type', 'location', 'total_area_sqft', 'num_floors',
        'num_workers', 'planned_duration_days', 'material_quality',
        'complexity_level', 'has_basement', 'weather_risk_zone',
        'contractor_experience_years',
        'soil_type', 'water_table_level', 'distance_from_city_km',
        'site_accessibility', 'floor_height_ft', 'foundation_type',
        'num_bathrooms', 'electrical_load_kw', 'finishing_level',
        'site_topography',
        'actual_cost', 'actual_duration_days'
    ]

    records = []
    for i in range(5000):
        records.append(generate_project())

    # Write to CSV
    output_path = 'data/sample_data.csv'
    with open(output_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)

    # Print statistics
    costs = [r['actual_cost'] for r in records]
    durations = [r['actual_duration_days'] for r in records]
    delays = [r['actual_duration_days'] - r['planned_duration_days'] for r in records]
    types = [r['project_type'] for r in records]

    print(f"\nGenerated {len(records)} records -> {output_path}")
    print(f"\n--- Statistics ---")
    print(f"Project types: residential={types.count('residential')}, "
          f"commercial={types.count('commercial')}, "
          f"industrial={types.count('industrial')}, "
          f"infrastructure={types.count('infrastructure')}")
    print(f"Cost range: Rs.{min(costs):,.0f} - Rs.{max(costs):,.0f}")
    print(f"Avg cost: Rs.{sum(costs)/len(costs):,.0f}")
    print(f"Duration range: {min(durations)} - {max(durations)} days")
    print(f"Avg delay: {sum(delays)/len(delays):.1f} days")
    print(f"Projects with delay: {sum(1 for d in delays if d > 0)} ({sum(1 for d in delays if d > 0)/len(delays)*100:.1f}%)")
    print(f"Cities covered: {len(set(r['location'] for r in records))}")


if __name__ == '__main__':
    main()

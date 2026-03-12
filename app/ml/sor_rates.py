# Schedule of Rates (SOR) Based Cost Estimation
# Based on CPWD/PWD Standard Rates (2024-25 approximate)
# Rates are in Indian Rupees (INR)

"""
Government Construction Cost Estimation System
Based on:
- CPWD Delhi Schedule of Rates (DSR)
- State PWD Schedule of Rates (SOR)
- Current Market Rates Analysis

Note: These rates should be updated periodically based on actual SOR publications
"""

# ============================================
# MATERIAL RATES (Per Unit) - Update these regularly
# ============================================
MATERIAL_RATES = {
    # Cement (per bag of 50 kg)
    'cement_opc_43': 380,
    'cement_opc_53': 400,
    'cement_ppc': 370,

    # Steel (per kg)
    'steel_tmt_fe500': 72,
    'steel_tmt_fe550': 78,
    'steel_structural': 75,

    # Aggregates (per cubic meter)
    'coarse_aggregate_20mm': 1800,
    'coarse_aggregate_40mm': 1700,
    'fine_aggregate_sand': 2200,
    'stone_dust': 1200,

    # Bricks (per 1000 nos)
    'brick_first_class': 8500,
    'brick_second_class': 6500,
    'fly_ash_brick': 5500,
    'concrete_block': 4500,

    # Wood (per cubic meter)
    'wood_teak': 85000,
    'wood_sal': 55000,
    'wood_deodar': 45000,
    'plywood_commercial': 65,  # per sqft
    'plywood_marine': 120,     # per sqft

    # Tiles (per sqft)
    'tile_ceramic_floor': 45,
    'tile_vitrified': 65,
    'tile_granite': 120,
    'tile_marble': 180,
    'tile_kota': 55,

    # Paint (per liter)
    'paint_distemper': 45,
    'paint_acrylic': 180,
    'paint_enamel': 280,
    'primer': 120,
    'putty': 45,  # per kg

    # Pipes (per running meter)
    'pipe_pvc_4inch': 180,
    'pipe_pvc_6inch': 320,
    'pipe_gi_1inch': 250,
    'pipe_cpvc_1inch': 120,

    # Electrical (per unit)
    'wire_1.5sqmm': 18,  # per meter
    'wire_2.5sqmm': 28,  # per meter
    'wire_4sqmm': 45,    # per meter
    'switch_modular': 85,
    'socket_modular': 120,
    'mcb_sp': 180,
    'mcb_dp': 350,

    # Miscellaneous
    'water_per_kl': 50,
    'bitumen_per_kg': 65,
    'polythene_sheet': 12,  # per sqm
}

# ============================================
# LABOR RATES (Per Day) - Skilled & Unskilled
# ============================================
LABOR_RATES = {
    # Unskilled Labor
    'mazdoor': 550,
    'beldar': 550,
    'coolie': 500,

    # Semi-skilled Labor
    'helper': 600,
    'bhisti': 580,

    # Skilled Labor
    'mason': 850,
    'carpenter': 850,
    'plumber': 800,
    'electrician': 850,
    'painter': 750,
    'welder': 900,
    'bar_bender': 800,
    'tile_layer': 850,

    # Highly Skilled
    'foreman': 1200,
    'supervisor': 1500,
    'site_engineer': 2500,
}

# ============================================
# ITEM-WISE SOR RATES (Per Unit)
# Based on CPWD DSR 2024
# ============================================
SOR_RATES = {
    # ----------------------------------------
    # EARTHWORK
    # ----------------------------------------
    'earthwork': {
        'excavation_ordinary_soil': {
            'unit': 'cum',
            'rate': 185,
            'description': 'Excavation in ordinary soil (0-1.5m depth)'
        },
        'excavation_hard_soil': {
            'unit': 'cum',
            'rate': 280,
            'description': 'Excavation in hard soil/murrum'
        },
        'excavation_rock': {
            'unit': 'cum',
            'rate': 850,
            'description': 'Excavation in soft rock'
        },
        'backfilling': {
            'unit': 'cum',
            'rate': 120,
            'description': 'Backfilling with excavated earth'
        },
        'sand_filling': {
            'unit': 'cum',
            'rate': 2800,
            'description': 'Sand filling in foundation'
        },
        'anti_termite': {
            'unit': 'sqm',
            'rate': 45,
            'description': 'Anti-termite treatment'
        }
    },

    # ----------------------------------------
    # CONCRETE WORK
    # ----------------------------------------
    'concrete': {
        'pcc_1_4_8': {
            'unit': 'cum',
            'rate': 4850,
            'description': 'PCC 1:4:8 (M7.5) - Bed concrete'
        },
        'pcc_1_3_6': {
            'unit': 'cum',
            'rate': 5250,
            'description': 'PCC 1:3:6 (M10)'
        },
        'pcc_1_2_4': {
            'unit': 'cum',
            'rate': 5850,
            'description': 'PCC 1:2:4 (M15)'
        },
        'rcc_m20': {
            'unit': 'cum',
            'rate': 6500,
            'description': 'RCC M20 grade (excluding steel)'
        },
        'rcc_m25': {
            'unit': 'cum',
            'rate': 7200,
            'description': 'RCC M25 grade (excluding steel)'
        },
        'rcc_m30': {
            'unit': 'cum',
            'rate': 7800,
            'description': 'RCC M30 grade (excluding steel)'
        },
        'steel_reinforcement': {
            'unit': 'kg',
            'rate': 85,
            'description': 'Steel reinforcement (TMT Fe500) including cutting, bending, binding'
        }
    },

    # ----------------------------------------
    # MASONRY WORK
    # ----------------------------------------
    'masonry': {
        'brick_work_cm_1_6': {
            'unit': 'cum',
            'rate': 6200,
            'description': 'Brick masonry in CM 1:6 in foundation'
        },
        'brick_work_cm_1_4': {
            'unit': 'cum',
            'rate': 6800,
            'description': 'Brick masonry in CM 1:4 in superstructure'
        },
        'brick_work_9inch': {
            'unit': 'sqm',
            'rate': 850,
            'description': '9 inch (230mm) brick wall'
        },
        'brick_work_4.5inch': {
            'unit': 'sqm',
            'rate': 480,
            'description': '4.5 inch (115mm) brick wall'
        },
        'aac_block_work': {
            'unit': 'cum',
            'rate': 5800,
            'description': 'AAC block masonry'
        },
        'stone_masonry': {
            'unit': 'cum',
            'rate': 4500,
            'description': 'Random rubble stone masonry'
        }
    },

    # ----------------------------------------
    # PLASTERING
    # ----------------------------------------
    'plastering': {
        'plaster_cm_1_6_12mm': {
            'unit': 'sqm',
            'rate': 185,
            'description': '12mm thick cement plaster 1:6'
        },
        'plaster_cm_1_4_15mm': {
            'unit': 'sqm',
            'rate': 225,
            'description': '15mm thick cement plaster 1:4'
        },
        'plaster_cm_1_4_20mm': {
            'unit': 'sqm',
            'rate': 275,
            'description': '20mm thick cement plaster 1:4'
        },
        'neeru_finish': {
            'unit': 'sqm',
            'rate': 85,
            'description': 'Neeru (lime) finish'
        },
        'pop_punning': {
            'unit': 'sqm',
            'rate': 120,
            'description': 'POP punning on walls'
        }
    },

    # ----------------------------------------
    # FLOORING
    # ----------------------------------------
    'flooring': {
        'cement_concrete_floor': {
            'unit': 'sqm',
            'rate': 450,
            'description': '40mm cement concrete flooring 1:2:4'
        },
        'ips_flooring': {
            'unit': 'sqm',
            'rate': 380,
            'description': 'IPS flooring with cement'
        },
        'ceramic_tile': {
            'unit': 'sqm',
            'rate': 850,
            'description': 'Ceramic tile flooring'
        },
        'vitrified_tile': {
            'unit': 'sqm',
            'rate': 1100,
            'description': 'Vitrified tile flooring 600x600'
        },
        'granite_flooring': {
            'unit': 'sqm',
            'rate': 2200,
            'description': 'Granite flooring 18mm thick'
        },
        'marble_flooring': {
            'unit': 'sqm',
            'rate': 2800,
            'description': 'Marble flooring 18mm thick'
        },
        'kota_stone': {
            'unit': 'sqm',
            'rate': 950,
            'description': 'Kota stone flooring 25mm'
        }
    },

    # ----------------------------------------
    # DOORS & WINDOWS
    # ----------------------------------------
    'doors_windows': {
        'wooden_door_frame': {
            'unit': 'cum',
            'rate': 65000,
            'description': 'Wooden door frame (Sal wood)'
        },
        'flush_door_35mm': {
            'unit': 'sqm',
            'rate': 2800,
            'description': '35mm flush door shutter'
        },
        'panel_door': {
            'unit': 'sqm',
            'rate': 4500,
            'description': 'Panel door (teak wood)'
        },
        'steel_door_frame': {
            'unit': 'kg',
            'rate': 95,
            'description': 'MS door frame'
        },
        'upvc_window': {
            'unit': 'sqm',
            'rate': 650,
            'description': 'UPVC sliding window'
        },
        'aluminum_window': {
            'unit': 'sqm',
            'rate': 750,
            'description': 'Aluminum sliding window'
        },
        'ms_grill': {
            'unit': 'kg',
            'rate': 110,
            'description': 'MS grill for windows'
        }
    },

    # ----------------------------------------
    # PAINTING
    # ----------------------------------------
    'painting': {
        'whitewash_2coat': {
            'unit': 'sqm',
            'rate': 28,
            'description': 'Whitewashing 2 coats'
        },
        'distemper_2coat': {
            'unit': 'sqm',
            'rate': 65,
            'description': 'Distemper 2 coats'
        },
        'acrylic_paint_2coat': {
            'unit': 'sqm',
            'rate': 125,
            'description': 'Acrylic emulsion paint 2 coats'
        },
        'enamel_paint_2coat': {
            'unit': 'sqm',
            'rate': 145,
            'description': 'Enamel paint 2 coats on wood/steel'
        },
        'exterior_paint': {
            'unit': 'sqm',
            'rate': 155,
            'description': 'Exterior weather coat paint'
        },
        'primer': {
            'unit': 'sqm',
            'rate': 45,
            'description': 'Primer coat'
        },
        'putty_2coat': {
            'unit': 'sqm',
            'rate': 75,
            'description': 'Wall putty 2 coats'
        }
    },

    # ----------------------------------------
    # PLUMBING & SANITARY
    # ----------------------------------------
    'plumbing': {
        'pvc_pipe_110mm': {
            'unit': 'rm',
            'rate': 380,
            'description': 'PVC pipe 110mm dia'
        },
        'pvc_pipe_75mm': {
            'unit': 'rm',
            'rate': 280,
            'description': 'PVC pipe 75mm dia'
        },
        'cpvc_pipe_25mm': {
            'unit': 'rm',
            'rate': 165,
            'description': 'CPVC pipe 25mm dia (hot/cold)'
        },
        'gi_pipe_25mm': {
            'unit': 'rm',
            'rate': 450,
            'description': 'GI pipe 25mm dia'
        },
        'wc_indian': {
            'unit': 'nos',
            'rate': 3500,
            'description': 'Indian WC with flushing'
        },
        'wc_ewc': {
            'unit': 'nos',
            'rate': 8500,
            'description': 'EWC with seat cover and flush'
        },
        'wash_basin': {
            'unit': 'nos',
            'rate': 2800,
            'description': 'Wash basin with pedestal'
        },
        'water_tank_500l': {
            'unit': 'nos',
            'rate': 4500,
            'description': 'Plastic water tank 500L'
        },
        'water_tank_1000l': {
            'unit': 'nos',
            'rate': 7500,
            'description': 'Plastic water tank 1000L'
        }
    },

    # ----------------------------------------
    # ELECTRICAL WORK
    # ----------------------------------------
    'electrical': {
        'conduit_pvc_25mm': {
            'unit': 'rm',
            'rate': 85,
            'description': 'PVC conduit 25mm with wiring point'
        },
        'wiring_point_light': {
            'unit': 'point',
            'rate': 450,
            'description': 'Wiring for light point'
        },
        'wiring_point_power': {
            'unit': 'point',
            'rate': 650,
            'description': 'Wiring for power point (5A/15A)'
        },
        'wiring_point_ac': {
            'unit': 'point',
            'rate': 1200,
            'description': 'Wiring for AC point'
        },
        'db_4way': {
            'unit': 'nos',
            'rate': 2500,
            'description': 'Distribution board 4 way'
        },
        'db_8way': {
            'unit': 'nos',
            'rate': 4500,
            'description': 'Distribution board 8 way'
        },
        'earthing': {
            'unit': 'nos',
            'rate': 3500,
            'description': 'Earthing with GI pipe'
        },
        'led_light_18w': {
            'unit': 'nos',
            'rate': 450,
            'description': 'LED panel light 18W'
        }
    },

    # ----------------------------------------
    # ROAD WORK (Infrastructure)
    # ----------------------------------------
    'road_work': {
        'gsb_200mm': {
            'unit': 'sqm',
            'rate': 280,
            'description': 'GSB (Granular Sub Base) 200mm'
        },
        'wbm_75mm': {
            'unit': 'sqm',
            'rate': 185,
            'description': 'WBM (Water Bound Macadam) 75mm'
        },
        'wet_mix_macadam': {
            'unit': 'sqm',
            'rate': 220,
            'description': 'Wet Mix Macadam 100mm'
        },
        'prime_coat': {
            'unit': 'sqm',
            'rate': 35,
            'description': 'Prime coat with bitumen'
        },
        'tack_coat': {
            'unit': 'sqm',
            'rate': 18,
            'description': 'Tack coat'
        },
        'dbm_50mm': {
            'unit': 'sqm',
            'rate': 450,
            'description': 'Dense Bituminous Macadam 50mm'
        },
        'bc_40mm': {
            'unit': 'sqm',
            'rate': 380,
            'description': 'Bituminous Concrete 40mm'
        },
        'cc_pavement_150mm': {
            'unit': 'sqm',
            'rate': 850,
            'description': 'CC Pavement M30 grade 150mm'
        },
        'kerb_stone': {
            'unit': 'rm',
            'rate': 450,
            'description': 'Precast cement concrete kerb stone'
        },
        'interlocking_paver': {
            'unit': 'sqm',
            'rate': 750,
            'description': 'Interlocking paver blocks 80mm'
        }
    },

    # ----------------------------------------
    # DRAINAGE & CULVERT
    # ----------------------------------------
    'drainage': {
        'rcc_pipe_300mm': {
            'unit': 'rm',
            'rate': 850,
            'description': 'RCC NP3 pipe 300mm dia'
        },
        'rcc_pipe_450mm': {
            'unit': 'rm',
            'rate': 1250,
            'description': 'RCC NP3 pipe 450mm dia'
        },
        'rcc_pipe_600mm': {
            'unit': 'rm',
            'rate': 1850,
            'description': 'RCC NP3 pipe 600mm dia'
        },
        'manhole_1m': {
            'unit': 'nos',
            'rate': 18000,
            'description': 'Brick masonry manhole 1m depth'
        },
        'box_culvert': {
            'unit': 'cum',
            'rate': 8500,
            'description': 'RCC box culvert'
        },
        'open_drain': {
            'unit': 'rm',
            'rate': 1200,
            'description': 'Open pucca drain'
        }
    },

    # ----------------------------------------
    # COMPOUND WALL & MISC
    # ----------------------------------------
    'boundary': {
        'compound_wall_brick': {
            'unit': 'rm',
            'rate': 2800,
            'description': 'Compound wall 1.8m height brick'
        },
        'compound_wall_rcc': {
            'unit': 'rm',
            'rate': 3500,
            'description': 'RCC precast compound wall'
        },
        'chain_link_fencing': {
            'unit': 'rm',
            'rate': 850,
            'description': 'Chain link fencing with MS posts'
        },
        'main_gate_ms': {
            'unit': 'sqm',
            'rate': 4500,
            'description': 'MS main gate fabricated'
        },
        'retaining_wall': {
            'unit': 'cum',
            'rate': 5500,
            'description': 'Stone masonry retaining wall'
        }
    }
}

# ============================================
# PROJECT TYPE CONFIGURATIONS
# ============================================
PROJECT_CONFIGS = {
    'residential': {
        'building': {
            'rcc_percentage': 0.08,      # 8% of plinth area in cum
            'steel_kg_per_cum': 100,     # Steel per cum of RCC
            'brick_percentage': 0.12,    # Brick work as % of plinth
            'plaster_multiplier': 2.5,   # Wall area multiplier
            'flooring_rate': 'vitrified_tile',
            'paint_type': 'acrylic_paint_2coat',
            'door_rate': 'flush_door_35mm',
        }
    },
    'commercial': {
        'building': {
            'rcc_percentage': 0.10,
            'steel_kg_per_cum': 120,
            'brick_percentage': 0.10,
            'plaster_multiplier': 2.8,
            'flooring_rate': 'granite_flooring',
            'paint_type': 'acrylic_paint_2coat',
            'door_rate': 'panel_door',
        }
    },
    'industrial': {
        'building': {
            'rcc_percentage': 0.06,
            'steel_kg_per_cum': 80,
            'brick_percentage': 0.08,
            'plaster_multiplier': 2.2,
            'flooring_rate': 'ips_flooring',
            'paint_type': 'distemper_2coat',
            'door_rate': 'flush_door_35mm',
        }
    },
    'infrastructure': {
        'road': {
            'layers': ['gsb_200mm', 'wbm_75mm', 'prime_coat', 'dbm_50mm', 'tack_coat', 'bc_40mm'],
            'shoulder_percentage': 0.15,
            'drainage_percentage': 0.10,
        },
        'drain': {
            'base_rate': 'open_drain',
            'manhole_per_30m': True,
        },
        'culvert': {
            'base_rate': 'box_culvert',
            'wing_wall': True,
        }
    }
}

# ============================================
# OVERHEAD & CHARGES
# ============================================
OVERHEAD_CHARGES = {
    'contractor_profit': 0.10,          # 10% contractor profit
    'overhead_charges': 0.05,           # 5% overhead
    'contingency': 0.03,                # 3% contingency
    'gst': 0.18,                        # 18% GST (can be 12% for some works)
    'labour_cess': 0.01,                # 1% labour cess
    'quality_control': 0.01,            # 1% quality control
    'insurance': 0.005,                 # 0.5% insurance
}

# GST rates for different categories
GST_RATES = {
    'works_contract': 0.12,             # 12% for works contract
    'material_supply': 0.18,            # 18% for material supply
    'composite_supply': 0.18,           # 18% for composite
    'government_works': 0.12,           # 12% for government works
}

# ============================================
# LOCATION FACTORS (Cost adjustment by region)
# ============================================
LOCATION_FACTORS = {
    # Metro Cities
    'Mumbai': 1.25,
    'Delhi': 1.20,
    'Bangalore': 1.15,
    'Chennai': 1.10,
    'Kolkata': 1.05,
    'Hyderabad': 1.10,

    # Tier 1 Cities
    'Pune': 1.12,
    'Ahmedabad': 1.08,
    'Jaipur': 1.05,
    'Lucknow': 1.02,
    'Chandigarh': 1.10,
    'Kochi': 1.08,

    # Tier 2 Cities
    'Indore': 1.00,
    'Bhopal': 0.98,
    'Nagpur': 0.98,
    'Vadodara': 1.02,
    'Surat': 1.05,
    'Coimbatore': 1.00,

    # Tier 3 & Rural
    'default': 0.95,
    'rural': 0.90,
    'hilly_terrain': 1.15,
    'remote_area': 1.20,
}

# ============================================
# LEAD & LIFT CHARGES
# ============================================
def get_lead_charges(distance_km):
    """Calculate lead charges based on distance"""
    if distance_km <= 1:
        return 0
    elif distance_km <= 5:
        return 50 * (distance_km - 1)  # Rs 50 per km after 1 km
    elif distance_km <= 10:
        return 200 + 80 * (distance_km - 5)
    else:
        return 600 + 100 * (distance_km - 10)

def get_lift_charges(height_m):
    """Calculate lift charges based on height"""
    if height_m <= 3:
        return 0
    elif height_m <= 6:
        return 15  # Rs 15 per cum/sqm
    elif height_m <= 9:
        return 30
    elif height_m <= 12:
        return 50
    else:
        return 75 + 10 * ((height_m - 12) // 3)

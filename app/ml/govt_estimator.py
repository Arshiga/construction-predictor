# Government Construction Cost Estimator
# Generates BOQ and estimates based on SOR rates

import math
from .sor_rates import (
    SOR_RATES, MATERIAL_RATES, LABOR_RATES,
    OVERHEAD_CHARGES, GST_RATES, LOCATION_FACTORS,
    PROJECT_CONFIGS, get_lead_charges, get_lift_charges
)


class GovtCostEstimator:
    """
    Government Construction Cost Estimator
    Generates item-wise BOQ based on SOR/DSR rates
    """

    def __init__(self):
        self.sor_rates = SOR_RATES
        self.material_rates = MATERIAL_RATES
        self.overhead = OVERHEAD_CHARGES

    def estimate_building(self, params):
        """
        Estimate cost for building construction (residential/commercial/industrial)
        """
        # Extract parameters
        plinth_area = params.get('total_area_sqft', 1000) * 0.0929  # Convert to sqm
        num_floors = params.get('num_floors', 1)
        project_type = params.get('project_type', 'residential')
        material_quality = params.get('material_quality', 'standard')
        complexity = params.get('complexity_level', 'medium')
        location = params.get('location', 'default')
        has_basement = params.get('has_basement', False)

        # Get location factor
        location_factor = self._get_location_factor(location)

        # Quality multipliers
        quality_multipliers = {'economy': 0.85, 'standard': 1.0, 'premium': 1.25}
        quality_factor = quality_multipliers.get(material_quality, 1.0)

        # Complexity multipliers
        complexity_multipliers = {'low': 0.90, 'medium': 1.0, 'high': 1.15}
        complexity_factor = complexity_multipliers.get(complexity, 1.0)

        # Initialize BOQ
        boq = []
        total_cost = 0

        # Calculate total built-up area
        total_built_area = plinth_area * num_floors
        if has_basement:
            total_built_area += plinth_area * 0.8  # 80% of plinth for basement

        # ============================================
        # 1. EARTHWORK
        # ============================================
        # Foundation excavation (assuming 1m depth, 1.2m width around perimeter)
        perimeter = 4 * math.sqrt(plinth_area)  # Approximate perimeter
        excavation_volume = perimeter * 1.2 * 1.0  # Length x Width x Depth

        if has_basement:
            excavation_volume += plinth_area * 2.5  # Basement depth

        boq.append({
            'sno': 1,
            'item': 'Earthwork in excavation in foundation',
            'description': SOR_RATES['earthwork']['excavation_ordinary_soil']['description'],
            'unit': 'cum',
            'quantity': round(excavation_volume, 2),
            'rate': SOR_RATES['earthwork']['excavation_ordinary_soil']['rate'],
            'amount': round(excavation_volume * SOR_RATES['earthwork']['excavation_ordinary_soil']['rate'], 2)
        })
        total_cost += boq[-1]['amount']

        # Sand filling
        sand_volume = plinth_area * 0.15  # 150mm sand filling
        boq.append({
            'sno': 2,
            'item': 'Sand filling in foundation and plinth',
            'description': SOR_RATES['earthwork']['sand_filling']['description'],
            'unit': 'cum',
            'quantity': round(sand_volume, 2),
            'rate': SOR_RATES['earthwork']['sand_filling']['rate'],
            'amount': round(sand_volume * SOR_RATES['earthwork']['sand_filling']['rate'], 2)
        })
        total_cost += boq[-1]['amount']

        # Anti-termite treatment
        boq.append({
            'sno': 3,
            'item': 'Anti-termite treatment',
            'description': SOR_RATES['earthwork']['anti_termite']['description'],
            'unit': 'sqm',
            'quantity': round(plinth_area, 2),
            'rate': SOR_RATES['earthwork']['anti_termite']['rate'],
            'amount': round(plinth_area * SOR_RATES['earthwork']['anti_termite']['rate'], 2)
        })
        total_cost += boq[-1]['amount']

        # ============================================
        # 2. CONCRETE WORK
        # ============================================
        # PCC for foundation bed
        pcc_volume = plinth_area * 0.075  # 75mm PCC
        boq.append({
            'sno': 4,
            'item': 'PCC (1:4:8) in foundation',
            'description': SOR_RATES['concrete']['pcc_1_4_8']['description'],
            'unit': 'cum',
            'quantity': round(pcc_volume, 2),
            'rate': SOR_RATES['concrete']['pcc_1_4_8']['rate'],
            'amount': round(pcc_volume * SOR_RATES['concrete']['pcc_1_4_8']['rate'], 2)
        })
        total_cost += boq[-1]['amount']

        # RCC Work (footings, columns, beams, slabs)
        rcc_percentage = 0.08 + (num_floors - 1) * 0.02  # Increases with floors
        if project_type == 'commercial':
            rcc_percentage += 0.02
        if complexity == 'high':
            rcc_percentage += 0.01

        rcc_volume = total_built_area * rcc_percentage
        rcc_grade = 'rcc_m25' if material_quality == 'premium' else 'rcc_m20'

        boq.append({
            'sno': 5,
            'item': f'RCC work in foundation, columns, beams, slabs',
            'description': SOR_RATES['concrete'][rcc_grade]['description'],
            'unit': 'cum',
            'quantity': round(rcc_volume, 2),
            'rate': SOR_RATES['concrete'][rcc_grade]['rate'],
            'amount': round(rcc_volume * SOR_RATES['concrete'][rcc_grade]['rate'], 2)
        })
        total_cost += boq[-1]['amount']

        # Steel reinforcement
        steel_kg_per_cum = 100 if project_type == 'residential' else 120
        if complexity == 'high':
            steel_kg_per_cum += 20

        steel_quantity = rcc_volume * steel_kg_per_cum
        boq.append({
            'sno': 6,
            'item': 'Steel reinforcement TMT Fe500',
            'description': SOR_RATES['concrete']['steel_reinforcement']['description'],
            'unit': 'kg',
            'quantity': round(steel_quantity, 2),
            'rate': SOR_RATES['concrete']['steel_reinforcement']['rate'],
            'amount': round(steel_quantity * SOR_RATES['concrete']['steel_reinforcement']['rate'], 2)
        })
        total_cost += boq[-1]['amount']

        # ============================================
        # 3. MASONRY WORK
        # ============================================
        # Brick work - External walls (230mm)
        external_wall_area = perimeter * 3.0 * num_floors  # 3m height per floor
        # Deduct 15% for openings
        external_wall_area *= 0.85

        boq.append({
            'sno': 7,
            'item': 'Brick work in superstructure (230mm thick)',
            'description': SOR_RATES['masonry']['brick_work_9inch']['description'],
            'unit': 'sqm',
            'quantity': round(external_wall_area, 2),
            'rate': SOR_RATES['masonry']['brick_work_9inch']['rate'],
            'amount': round(external_wall_area * SOR_RATES['masonry']['brick_work_9inch']['rate'], 2)
        })
        total_cost += boq[-1]['amount']

        # Internal walls (115mm)
        internal_wall_area = total_built_area * 0.5  # Approximate
        internal_wall_area *= 0.85  # Deduct openings

        boq.append({
            'sno': 8,
            'item': 'Brick work in partition walls (115mm thick)',
            'description': SOR_RATES['masonry']['brick_work_4.5inch']['description'],
            'unit': 'sqm',
            'quantity': round(internal_wall_area, 2),
            'rate': SOR_RATES['masonry']['brick_work_4.5inch']['rate'],
            'amount': round(internal_wall_area * SOR_RATES['masonry']['brick_work_4.5inch']['rate'], 2)
        })
        total_cost += boq[-1]['amount']

        # ============================================
        # 4. PLASTERING
        # ============================================
        # Total plaster area (internal + external both sides)
        total_plaster_area = (external_wall_area * 2) + (internal_wall_area * 2)
        # Add ceiling
        total_plaster_area += total_built_area * 0.9

        boq.append({
            'sno': 9,
            'item': 'Cement plaster 12mm thick (1:6)',
            'description': SOR_RATES['plastering']['plaster_cm_1_6_12mm']['description'],
            'unit': 'sqm',
            'quantity': round(total_plaster_area, 2),
            'rate': SOR_RATES['plastering']['plaster_cm_1_6_12mm']['rate'],
            'amount': round(total_plaster_area * SOR_RATES['plastering']['plaster_cm_1_6_12mm']['rate'], 2)
        })
        total_cost += boq[-1]['amount']

        # ============================================
        # 5. FLOORING
        # ============================================
        flooring_type = 'vitrified_tile' if material_quality != 'economy' else 'ceramic_tile'
        if project_type == 'industrial':
            flooring_type = 'ips_flooring'
        elif material_quality == 'premium':
            flooring_type = 'granite_flooring'

        boq.append({
            'sno': 10,
            'item': f'Flooring ({flooring_type.replace("_", " ").title()})',
            'description': SOR_RATES['flooring'][flooring_type]['description'],
            'unit': 'sqm',
            'quantity': round(total_built_area, 2),
            'rate': SOR_RATES['flooring'][flooring_type]['rate'],
            'amount': round(total_built_area * SOR_RATES['flooring'][flooring_type]['rate'], 2)
        })
        total_cost += boq[-1]['amount']

        # ============================================
        # 6. DOORS & WINDOWS
        # ============================================
        # Estimate doors: 1 door per 15 sqm
        num_doors = max(4, int(total_built_area / 15))
        door_area = num_doors * 1.8  # Average 1.8 sqm per door

        boq.append({
            'sno': 11,
            'item': 'Flush door shutters with frame',
            'description': SOR_RATES['doors_windows']['flush_door_35mm']['description'],
            'unit': 'sqm',
            'quantity': round(door_area, 2),
            'rate': SOR_RATES['doors_windows']['flush_door_35mm']['rate'],
            'amount': round(door_area * SOR_RATES['doors_windows']['flush_door_35mm']['rate'], 2)
        })
        total_cost += boq[-1]['amount']

        # Windows: 1 window per 20 sqm
        num_windows = max(4, int(total_built_area / 20))
        window_area = num_windows * 1.5  # Average 1.5 sqm per window

        boq.append({
            'sno': 12,
            'item': 'Aluminum sliding windows with glass',
            'description': SOR_RATES['doors_windows']['aluminum_window']['description'],
            'unit': 'sqm',
            'quantity': round(window_area, 2),
            'rate': SOR_RATES['doors_windows']['aluminum_window']['rate'],
            'amount': round(window_area * SOR_RATES['doors_windows']['aluminum_window']['rate'], 2)
        })
        total_cost += boq[-1]['amount']

        # MS Grill
        grill_weight = window_area * 8  # ~8 kg per sqm
        boq.append({
            'sno': 13,
            'item': 'MS safety grill for windows',
            'description': SOR_RATES['doors_windows']['ms_grill']['description'],
            'unit': 'kg',
            'quantity': round(grill_weight, 2),
            'rate': SOR_RATES['doors_windows']['ms_grill']['rate'],
            'amount': round(grill_weight * SOR_RATES['doors_windows']['ms_grill']['rate'], 2)
        })
        total_cost += boq[-1]['amount']

        # ============================================
        # 7. PAINTING
        # ============================================
        paint_type = 'acrylic_paint_2coat' if material_quality != 'economy' else 'distemper_2coat'

        # Interior painting
        interior_paint_area = total_plaster_area * 0.7  # 70% interior
        boq.append({
            'sno': 14,
            'item': 'Interior wall painting with putty',
            'description': f"Wall putty 2 coats + {SOR_RATES['painting'][paint_type]['description']}",
            'unit': 'sqm',
            'quantity': round(interior_paint_area, 2),
            'rate': SOR_RATES['painting'][paint_type]['rate'] + SOR_RATES['painting']['putty_2coat']['rate'],
            'amount': round(interior_paint_area * (SOR_RATES['painting'][paint_type]['rate'] + SOR_RATES['painting']['putty_2coat']['rate']), 2)
        })
        total_cost += boq[-1]['amount']

        # Exterior painting
        exterior_paint_area = external_wall_area
        boq.append({
            'sno': 15,
            'item': 'Exterior weather coat painting',
            'description': SOR_RATES['painting']['exterior_paint']['description'],
            'unit': 'sqm',
            'quantity': round(exterior_paint_area, 2),
            'rate': SOR_RATES['painting']['exterior_paint']['rate'],
            'amount': round(exterior_paint_area * SOR_RATES['painting']['exterior_paint']['rate'], 2)
        })
        total_cost += boq[-1]['amount']

        # ============================================
        # 8. PLUMBING & SANITARY
        # ============================================
        # Estimate based on built-up area
        plumbing_points = max(10, int(total_built_area / 10))

        # WC/toilets: 1 per 50 sqm
        num_wc = max(2, int(total_built_area / 50))
        wc_type = 'wc_ewc' if material_quality != 'economy' else 'wc_indian'

        boq.append({
            'sno': 16,
            'item': 'WC with flushing cistern complete',
            'description': SOR_RATES['plumbing'][wc_type]['description'],
            'unit': 'nos',
            'quantity': num_wc,
            'rate': SOR_RATES['plumbing'][wc_type]['rate'],
            'amount': num_wc * SOR_RATES['plumbing'][wc_type]['rate']
        })
        total_cost += boq[-1]['amount']

        # Wash basins
        num_basins = num_wc
        boq.append({
            'sno': 17,
            'item': 'Wash basin with pedestal and fittings',
            'description': SOR_RATES['plumbing']['wash_basin']['description'],
            'unit': 'nos',
            'quantity': num_basins,
            'rate': SOR_RATES['plumbing']['wash_basin']['rate'],
            'amount': num_basins * SOR_RATES['plumbing']['wash_basin']['rate']
        })
        total_cost += boq[-1]['amount']

        # Internal plumbing (lump sum based on area)
        plumbing_lumpsum = total_built_area * 250  # Rs 250 per sqm
        boq.append({
            'sno': 18,
            'item': 'Internal plumbing work complete',
            'description': 'CPVC/PVC pipes, fittings, valves complete',
            'unit': 'LS',
            'quantity': 1,
            'rate': plumbing_lumpsum,
            'amount': plumbing_lumpsum
        })
        total_cost += boq[-1]['amount']

        # ============================================
        # 9. ELECTRICAL WORK
        # ============================================
        # Light points: 1 per 8 sqm
        light_points = max(10, int(total_built_area / 8))
        boq.append({
            'sno': 19,
            'item': 'Wiring for light points with accessories',
            'description': SOR_RATES['electrical']['wiring_point_light']['description'],
            'unit': 'point',
            'quantity': light_points,
            'rate': SOR_RATES['electrical']['wiring_point_light']['rate'],
            'amount': light_points * SOR_RATES['electrical']['wiring_point_light']['rate']
        })
        total_cost += boq[-1]['amount']

        # Power points: 1 per 12 sqm
        power_points = max(8, int(total_built_area / 12))
        boq.append({
            'sno': 20,
            'item': 'Wiring for power points (5A/15A)',
            'description': SOR_RATES['electrical']['wiring_point_power']['description'],
            'unit': 'point',
            'quantity': power_points,
            'rate': SOR_RATES['electrical']['wiring_point_power']['rate'],
            'amount': power_points * SOR_RATES['electrical']['wiring_point_power']['rate']
        })
        total_cost += boq[-1]['amount']

        # Distribution boards
        num_db = max(1, num_floors)
        boq.append({
            'sno': 21,
            'item': 'Distribution board with MCBs',
            'description': SOR_RATES['electrical']['db_8way']['description'],
            'unit': 'nos',
            'quantity': num_db,
            'rate': SOR_RATES['electrical']['db_8way']['rate'],
            'amount': num_db * SOR_RATES['electrical']['db_8way']['rate']
        })
        total_cost += boq[-1]['amount']

        # Earthing
        boq.append({
            'sno': 22,
            'item': 'Earthing with GI pipe',
            'description': SOR_RATES['electrical']['earthing']['description'],
            'unit': 'nos',
            'quantity': 2,
            'rate': SOR_RATES['electrical']['earthing']['rate'],
            'amount': 2 * SOR_RATES['electrical']['earthing']['rate']
        })
        total_cost += boq[-1]['amount']

        # ============================================
        # 10. MISCELLANEOUS
        # ============================================
        # Water tank
        tank_size = 'water_tank_1000l' if total_built_area > 200 else 'water_tank_500l'
        boq.append({
            'sno': 23,
            'item': 'Overhead water tank',
            'description': SOR_RATES['plumbing'][tank_size]['description'],
            'unit': 'nos',
            'quantity': max(1, num_floors),
            'rate': SOR_RATES['plumbing'][tank_size]['rate'],
            'amount': max(1, num_floors) * SOR_RATES['plumbing'][tank_size]['rate']
        })
        total_cost += boq[-1]['amount']

        # Apply factors
        total_cost *= location_factor
        total_cost *= quality_factor
        total_cost *= complexity_factor

        # Calculate overhead and charges
        subtotal = total_cost
        contractor_profit = subtotal * self.overhead['contractor_profit']
        overhead_charges = subtotal * self.overhead['overhead_charges']
        contingency = subtotal * self.overhead['contingency']

        amount_before_gst = subtotal + contractor_profit + overhead_charges + contingency
        gst = amount_before_gst * GST_RATES['government_works']
        labour_cess = amount_before_gst * self.overhead['labour_cess']

        grand_total = amount_before_gst + gst + labour_cess

        return {
            'boq': boq,
            'subtotal': round(subtotal, 2),
            'contractor_profit': round(contractor_profit, 2),
            'overhead_charges': round(overhead_charges, 2),
            'contingency': round(contingency, 2),
            'amount_before_gst': round(amount_before_gst, 2),
            'gst': round(gst, 2),
            'gst_rate': GST_RATES['government_works'] * 100,
            'labour_cess': round(labour_cess, 2),
            'grand_total': round(grand_total, 2),
            'cost_per_sqft': round(grand_total / (plinth_area / 0.0929 * num_floors), 2),
            'cost_per_sqm': round(grand_total / total_built_area, 2),
            'location_factor': location_factor,
            'quality_factor': quality_factor,
            'complexity_factor': complexity_factor,
            'total_built_area_sqm': round(total_built_area, 2),
            'total_built_area_sqft': round(total_built_area / 0.0929, 2)
        }

    def estimate_road(self, params):
        """
        Estimate cost for road construction
        """
        # Extract parameters
        length_m = params.get('road_length_m', 1000)
        width_m = params.get('road_width_m', 7)
        road_type = params.get('road_type', 'bituminous')  # bituminous, concrete, wbm
        location = params.get('location', 'default')
        complexity = params.get('complexity_level', 'medium')

        location_factor = self._get_location_factor(location)

        # Complexity multipliers
        complexity_multipliers = {'low': 0.90, 'medium': 1.0, 'high': 1.15}
        complexity_factor = complexity_multipliers.get(complexity, 1.0)

        road_area = length_m * width_m
        boq = []
        total_cost = 0
        sno = 0

        # ============================================
        # 1. EARTHWORK
        # ============================================
        sno += 1
        # Excavation for road bed
        excavation_vol = road_area * 0.3  # 300mm depth
        boq.append({
            'sno': sno,
            'item': 'Earthwork in excavation for road formation',
            'description': SOR_RATES['earthwork']['excavation_ordinary_soil']['description'],
            'unit': 'cum',
            'quantity': round(excavation_vol, 2),
            'rate': SOR_RATES['earthwork']['excavation_ordinary_soil']['rate'],
            'amount': round(excavation_vol * SOR_RATES['earthwork']['excavation_ordinary_soil']['rate'], 2)
        })
        total_cost += boq[-1]['amount']

        # ============================================
        # 2. SUB-BASE & BASE COURSE
        # ============================================
        sno += 1
        # GSB (Granular Sub Base)
        boq.append({
            'sno': sno,
            'item': 'GSB (Granular Sub Base) 200mm thick',
            'description': SOR_RATES['road_work']['gsb_200mm']['description'],
            'unit': 'sqm',
            'quantity': round(road_area, 2),
            'rate': SOR_RATES['road_work']['gsb_200mm']['rate'],
            'amount': round(road_area * SOR_RATES['road_work']['gsb_200mm']['rate'], 2)
        })
        total_cost += boq[-1]['amount']

        sno += 1
        # WBM
        boq.append({
            'sno': sno,
            'item': 'WBM (Water Bound Macadam) 75mm thick',
            'description': SOR_RATES['road_work']['wbm_75mm']['description'],
            'unit': 'sqm',
            'quantity': round(road_area, 2),
            'rate': SOR_RATES['road_work']['wbm_75mm']['rate'],
            'amount': round(road_area * SOR_RATES['road_work']['wbm_75mm']['rate'], 2)
        })
        total_cost += boq[-1]['amount']

        # ============================================
        # 3. SURFACE COURSE
        # ============================================
        if road_type == 'bituminous':
            sno += 1
            # Prime coat
            boq.append({
                'sno': sno,
                'item': 'Prime coat with bitumen emulsion',
                'description': SOR_RATES['road_work']['prime_coat']['description'],
                'unit': 'sqm',
                'quantity': round(road_area, 2),
                'rate': SOR_RATES['road_work']['prime_coat']['rate'],
                'amount': round(road_area * SOR_RATES['road_work']['prime_coat']['rate'], 2)
            })
            total_cost += boq[-1]['amount']

            sno += 1
            # DBM
            boq.append({
                'sno': sno,
                'item': 'Dense Bituminous Macadam (DBM) 50mm',
                'description': SOR_RATES['road_work']['dbm_50mm']['description'],
                'unit': 'sqm',
                'quantity': round(road_area, 2),
                'rate': SOR_RATES['road_work']['dbm_50mm']['rate'],
                'amount': round(road_area * SOR_RATES['road_work']['dbm_50mm']['rate'], 2)
            })
            total_cost += boq[-1]['amount']

            sno += 1
            # Tack coat
            boq.append({
                'sno': sno,
                'item': 'Tack coat',
                'description': SOR_RATES['road_work']['tack_coat']['description'],
                'unit': 'sqm',
                'quantity': round(road_area, 2),
                'rate': SOR_RATES['road_work']['tack_coat']['rate'],
                'amount': round(road_area * SOR_RATES['road_work']['tack_coat']['rate'], 2)
            })
            total_cost += boq[-1]['amount']

            sno += 1
            # BC
            boq.append({
                'sno': sno,
                'item': 'Bituminous Concrete (BC) 40mm',
                'description': SOR_RATES['road_work']['bc_40mm']['description'],
                'unit': 'sqm',
                'quantity': round(road_area, 2),
                'rate': SOR_RATES['road_work']['bc_40mm']['rate'],
                'amount': round(road_area * SOR_RATES['road_work']['bc_40mm']['rate'], 2)
            })
            total_cost += boq[-1]['amount']

        elif road_type == 'concrete':
            sno += 1
            boq.append({
                'sno': sno,
                'item': 'CC Pavement M30 grade 150mm thick',
                'description': SOR_RATES['road_work']['cc_pavement_150mm']['description'],
                'unit': 'sqm',
                'quantity': round(road_area, 2),
                'rate': SOR_RATES['road_work']['cc_pavement_150mm']['rate'],
                'amount': round(road_area * SOR_RATES['road_work']['cc_pavement_150mm']['rate'], 2)
            })
            total_cost += boq[-1]['amount']

        # ============================================
        # 4. KERB STONE
        # ============================================
        sno += 1
        kerb_length = length_m * 2  # Both sides
        boq.append({
            'sno': sno,
            'item': 'Precast cement concrete kerb stone',
            'description': SOR_RATES['road_work']['kerb_stone']['description'],
            'unit': 'rm',
            'quantity': round(kerb_length, 2),
            'rate': SOR_RATES['road_work']['kerb_stone']['rate'],
            'amount': round(kerb_length * SOR_RATES['road_work']['kerb_stone']['rate'], 2)
        })
        total_cost += boq[-1]['amount']

        # ============================================
        # 5. DRAINAGE
        # ============================================
        sno += 1
        drain_length = length_m * 2  # Both sides
        boq.append({
            'sno': sno,
            'item': 'Side drain (open pucca drain)',
            'description': SOR_RATES['drainage']['open_drain']['description'],
            'unit': 'rm',
            'quantity': round(drain_length, 2),
            'rate': SOR_RATES['drainage']['open_drain']['rate'],
            'amount': round(drain_length * SOR_RATES['drainage']['open_drain']['rate'], 2)
        })
        total_cost += boq[-1]['amount']

        # Apply factors
        total_cost *= location_factor
        total_cost *= complexity_factor

        # Calculate overhead and charges
        subtotal = total_cost
        contractor_profit = subtotal * self.overhead['contractor_profit']
        overhead_charges = subtotal * self.overhead['overhead_charges']
        contingency = subtotal * self.overhead['contingency']

        amount_before_gst = subtotal + contractor_profit + overhead_charges + contingency
        gst = amount_before_gst * GST_RATES['government_works']
        labour_cess = amount_before_gst * self.overhead['labour_cess']

        grand_total = amount_before_gst + gst + labour_cess

        return {
            'boq': boq,
            'subtotal': round(subtotal, 2),
            'contractor_profit': round(contractor_profit, 2),
            'overhead_charges': round(overhead_charges, 2),
            'contingency': round(contingency, 2),
            'amount_before_gst': round(amount_before_gst, 2),
            'gst': round(gst, 2),
            'gst_rate': GST_RATES['government_works'] * 100,
            'labour_cess': round(labour_cess, 2),
            'grand_total': round(grand_total, 2),
            'cost_per_sqm': round(grand_total / road_area, 2),
            'cost_per_km': round(grand_total / (length_m / 1000), 2),
            'location_factor': location_factor,
            'complexity_factor': complexity_factor,
            'road_area_sqm': round(road_area, 2),
            'road_length_m': length_m,
            'road_width_m': width_m
        }

    def estimate_drain(self, params):
        """
        Estimate cost for drain/nala construction
        """
        length_m = params.get('drain_length_m', 500)
        width_m = params.get('drain_width_m', 1.0)
        depth_m = params.get('drain_depth_m', 0.6)
        drain_type = params.get('drain_type', 'open')  # open, covered, pipe
        location = params.get('location', 'default')

        location_factor = self._get_location_factor(location)

        boq = []
        total_cost = 0
        sno = 0

        # Excavation
        sno += 1
        excavation_vol = length_m * (width_m + 0.3) * (depth_m + 0.15)
        boq.append({
            'sno': sno,
            'item': 'Earthwork excavation for drain',
            'description': SOR_RATES['earthwork']['excavation_ordinary_soil']['description'],
            'unit': 'cum',
            'quantity': round(excavation_vol, 2),
            'rate': SOR_RATES['earthwork']['excavation_ordinary_soil']['rate'],
            'amount': round(excavation_vol * SOR_RATES['earthwork']['excavation_ordinary_soil']['rate'], 2)
        })
        total_cost += boq[-1]['amount']

        if drain_type == 'open':
            sno += 1
            boq.append({
                'sno': sno,
                'item': 'Open pucca drain construction',
                'description': SOR_RATES['drainage']['open_drain']['description'],
                'unit': 'rm',
                'quantity': round(length_m, 2),
                'rate': SOR_RATES['drainage']['open_drain']['rate'],
                'amount': round(length_m * SOR_RATES['drainage']['open_drain']['rate'], 2)
            })
            total_cost += boq[-1]['amount']

        elif drain_type == 'pipe':
            pipe_dia = 'rcc_pipe_450mm' if width_m >= 0.45 else 'rcc_pipe_300mm'
            sno += 1
            boq.append({
                'sno': sno,
                'item': f'RCC NP3 pipe laying',
                'description': SOR_RATES['drainage'][pipe_dia]['description'],
                'unit': 'rm',
                'quantity': round(length_m, 2),
                'rate': SOR_RATES['drainage'][pipe_dia]['rate'],
                'amount': round(length_m * SOR_RATES['drainage'][pipe_dia]['rate'], 2)
            })
            total_cost += boq[-1]['amount']

        # Manholes every 30m
        sno += 1
        num_manholes = max(2, int(length_m / 30))
        boq.append({
            'sno': sno,
            'item': 'Brick masonry manholes',
            'description': SOR_RATES['drainage']['manhole_1m']['description'],
            'unit': 'nos',
            'quantity': num_manholes,
            'rate': SOR_RATES['drainage']['manhole_1m']['rate'],
            'amount': num_manholes * SOR_RATES['drainage']['manhole_1m']['rate']
        })
        total_cost += boq[-1]['amount']

        # Apply factors
        total_cost *= location_factor

        # Calculate overhead and charges
        subtotal = total_cost
        contractor_profit = subtotal * self.overhead['contractor_profit']
        overhead_charges = subtotal * self.overhead['overhead_charges']
        contingency = subtotal * self.overhead['contingency']

        amount_before_gst = subtotal + contractor_profit + overhead_charges + contingency
        gst = amount_before_gst * GST_RATES['government_works']
        labour_cess = amount_before_gst * self.overhead['labour_cess']

        grand_total = amount_before_gst + gst + labour_cess

        return {
            'boq': boq,
            'subtotal': round(subtotal, 2),
            'contractor_profit': round(contractor_profit, 2),
            'overhead_charges': round(overhead_charges, 2),
            'contingency': round(contingency, 2),
            'amount_before_gst': round(amount_before_gst, 2),
            'gst': round(gst, 2),
            'gst_rate': GST_RATES['government_works'] * 100,
            'labour_cess': round(labour_cess, 2),
            'grand_total': round(grand_total, 2),
            'cost_per_rm': round(grand_total / length_m, 2),
            'location_factor': location_factor,
            'drain_length_m': length_m
        }

    def _get_location_factor(self, location):
        """Get location-based cost adjustment factor"""
        # Check exact match
        if location in LOCATION_FACTORS:
            return LOCATION_FACTORS[location]

        # Check partial match
        location_lower = location.lower() if location else ''
        for city, factor in LOCATION_FACTORS.items():
            if city.lower() in location_lower or location_lower in city.lower():
                return factor

        return LOCATION_FACTORS['default']


# Create singleton instance
govt_estimator = GovtCostEstimator()

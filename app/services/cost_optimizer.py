"""
AI Cost Optimizer Service for Construction Cost Predictor
Analyzes project parameters and suggests cost-saving optimizations
"""

from typing import Dict, List, Any
from dataclasses import dataclass
from enum import Enum


class OptimizationCategory(Enum):
    MATERIAL = "material"
    LABOR = "labor"
    SCHEDULING = "scheduling"
    DESIGN = "design"
    PROCUREMENT = "procurement"


@dataclass
class Optimization:
    """Represents a single optimization suggestion"""
    id: str
    category: str
    title: str
    description: str
    savings_amount: float
    savings_percent: float
    impact: str  # low, medium, high
    trade_off: str
    applicable: bool = True

    def to_dict(self) -> Dict:
        return {
            'id': self.id,
            'category': self.category,
            'title': self.title,
            'description': self.description,
            'savings_amount': self.savings_amount,
            'savings_percent': self.savings_percent,
            'impact': self.impact,
            'trade_off': self.trade_off,
            'applicable': self.applicable
        }


class CostOptimizer:
    """AI-powered cost optimization engine"""

    # Material substitution options with savings percentages
    MATERIAL_SUBSTITUTIONS = {
        'fly_ash_bricks': {
            'title': 'Use Fly Ash Bricks instead of Clay Bricks',
            'description': 'Fly ash bricks are 30% cheaper, eco-friendly, and have better insulation properties.',
            'savings_percent': 0.035,  # 3.5% of total cost
            'impact': 'low',
            'trade_off': 'Slightly different appearance, requires curing time'
        },
        'm_sand': {
            'title': 'Use M-Sand instead of River Sand',
            'description': 'Manufactured sand is 25-30% cheaper and more consistent in quality.',
            'savings_percent': 0.025,  # 2.5% of total cost
            'impact': 'low',
            'trade_off': 'May require slight mix design adjustment'
        },
        'aac_blocks': {
            'title': 'Use AAC Blocks for non-load bearing walls',
            'description': 'Autoclaved Aerated Concrete blocks reduce wall construction cost by 20%.',
            'savings_percent': 0.03,  # 3% of total cost
            'impact': 'low',
            'trade_off': 'Requires special adhesive, not suitable for wet areas'
        },
        'ppc_cement': {
            'title': 'Use PPC Cement instead of OPC for non-structural work',
            'description': 'Portland Pozzolana Cement is 5-8% cheaper for plastering and flooring.',
            'savings_percent': 0.015,  # 1.5% of total cost
            'impact': 'low',
            'trade_off': 'Slightly longer setting time'
        },
        'steel_optimization': {
            'title': 'Optimize steel design with Fe500D grade',
            'description': 'Higher grade steel allows 10-15% less quantity with same strength.',
            'savings_percent': 0.04,  # 4% of total cost
            'impact': 'medium',
            'trade_off': 'Requires structural engineer review'
        }
    }

    # Workforce optimization thresholds
    WORKER_EFFICIENCY = {
        'residential': {'sqft_per_worker_per_day': 15, 'optimal_ratio': 0.008},
        'commercial': {'sqft_per_worker_per_day': 12, 'optimal_ratio': 0.006},
        'industrial': {'sqft_per_worker_per_day': 20, 'optimal_ratio': 0.005},
        'infrastructure': {'sqft_per_worker_per_day': 25, 'optimal_ratio': 0.004}
    }

    # Seasonal factors (monsoon months have higher costs)
    MONSOON_MONTHS = [6, 7, 8, 9]  # June to September

    def __init__(self):
        pass

    def analyze(self, input_data: Dict, predicted_cost: float) -> Dict[str, Any]:
        """
        Analyze project parameters and generate optimization suggestions.

        Args:
            input_data: Project input parameters
            predicted_cost: The predicted total cost

        Returns:
            Dictionary with optimizations and summary
        """
        optimizations = []

        # 1. Material optimizations
        optimizations.extend(self._analyze_materials(input_data, predicted_cost))

        # 2. Labor optimizations
        optimizations.extend(self._analyze_labor(input_data, predicted_cost))

        # 3. Scheduling optimizations
        optimizations.extend(self._analyze_scheduling(input_data, predicted_cost))

        # 4. Design optimizations
        optimizations.extend(self._analyze_design(input_data, predicted_cost))

        # 5. Procurement optimizations
        optimizations.extend(self._analyze_procurement(input_data, predicted_cost))

        # Filter applicable optimizations and sort by savings
        applicable = [opt for opt in optimizations if opt.applicable]
        applicable.sort(key=lambda x: x.savings_amount, reverse=True)

        # Calculate totals
        total_savings = sum(opt.savings_amount for opt in applicable)
        total_savings_percent = (total_savings / predicted_cost * 100) if predicted_cost > 0 else 0
        optimized_cost = predicted_cost - total_savings

        return {
            'original_cost': predicted_cost,
            'optimized_cost': optimized_cost,
            'total_savings': total_savings,
            'total_savings_percent': round(total_savings_percent, 1),
            'optimization_count': len(applicable),
            'optimizations': [opt.to_dict() for opt in applicable[:8]],  # Top 8 suggestions
            'summary': self._generate_summary(applicable, total_savings, predicted_cost)
        }

    def _analyze_materials(self, input_data: Dict, predicted_cost: float) -> List[Optimization]:
        """Analyze material-related optimizations"""
        optimizations = []
        material_quality = input_data.get('material_quality', 'standard')
        project_type = input_data.get('project_type', 'commercial')

        # Fly ash bricks suggestion
        if project_type in ['residential', 'commercial']:
            savings = predicted_cost * self.MATERIAL_SUBSTITUTIONS['fly_ash_bricks']['savings_percent']
            optimizations.append(Optimization(
                id='fly_ash_bricks',
                category='material',
                title=self.MATERIAL_SUBSTITUTIONS['fly_ash_bricks']['title'],
                description=self.MATERIAL_SUBSTITUTIONS['fly_ash_bricks']['description'],
                savings_amount=round(savings),
                savings_percent=round(self.MATERIAL_SUBSTITUTIONS['fly_ash_bricks']['savings_percent'] * 100, 1),
                impact=self.MATERIAL_SUBSTITUTIONS['fly_ash_bricks']['impact'],
                trade_off=self.MATERIAL_SUBSTITUTIONS['fly_ash_bricks']['trade_off'],
                applicable=True
            ))

        # M-Sand suggestion
        savings = predicted_cost * self.MATERIAL_SUBSTITUTIONS['m_sand']['savings_percent']
        optimizations.append(Optimization(
            id='m_sand',
            category='material',
            title=self.MATERIAL_SUBSTITUTIONS['m_sand']['title'],
            description=self.MATERIAL_SUBSTITUTIONS['m_sand']['description'],
            savings_amount=round(savings),
            savings_percent=round(self.MATERIAL_SUBSTITUTIONS['m_sand']['savings_percent'] * 100, 1),
            impact=self.MATERIAL_SUBSTITUTIONS['m_sand']['impact'],
            trade_off=self.MATERIAL_SUBSTITUTIONS['m_sand']['trade_off'],
            applicable=True
        ))

        # AAC Blocks for multi-floor buildings
        num_floors = input_data.get('num_floors', 1)
        if num_floors >= 2 and project_type in ['residential', 'commercial']:
            savings = predicted_cost * self.MATERIAL_SUBSTITUTIONS['aac_blocks']['savings_percent']
            optimizations.append(Optimization(
                id='aac_blocks',
                category='material',
                title=self.MATERIAL_SUBSTITUTIONS['aac_blocks']['title'],
                description=self.MATERIAL_SUBSTITUTIONS['aac_blocks']['description'],
                savings_amount=round(savings),
                savings_percent=round(self.MATERIAL_SUBSTITUTIONS['aac_blocks']['savings_percent'] * 100, 1),
                impact=self.MATERIAL_SUBSTITUTIONS['aac_blocks']['impact'],
                trade_off=self.MATERIAL_SUBSTITUTIONS['aac_blocks']['trade_off'],
                applicable=True
            ))

        # PPC Cement suggestion
        savings = predicted_cost * self.MATERIAL_SUBSTITUTIONS['ppc_cement']['savings_percent']
        optimizations.append(Optimization(
            id='ppc_cement',
            category='material',
            title=self.MATERIAL_SUBSTITUTIONS['ppc_cement']['title'],
            description=self.MATERIAL_SUBSTITUTIONS['ppc_cement']['description'],
            savings_amount=round(savings),
            savings_percent=round(self.MATERIAL_SUBSTITUTIONS['ppc_cement']['savings_percent'] * 100, 1),
            impact=self.MATERIAL_SUBSTITUTIONS['ppc_cement']['impact'],
            trade_off=self.MATERIAL_SUBSTITUTIONS['ppc_cement']['trade_off'],
            applicable=True
        ))

        # Steel optimization for larger projects
        total_area = input_data.get('total_area_sqft', 0)
        if total_area > 5000:
            savings = predicted_cost * self.MATERIAL_SUBSTITUTIONS['steel_optimization']['savings_percent']
            optimizations.append(Optimization(
                id='steel_optimization',
                category='material',
                title=self.MATERIAL_SUBSTITUTIONS['steel_optimization']['title'],
                description=self.MATERIAL_SUBSTITUTIONS['steel_optimization']['description'],
                savings_amount=round(savings),
                savings_percent=round(self.MATERIAL_SUBSTITUTIONS['steel_optimization']['savings_percent'] * 100, 1),
                impact=self.MATERIAL_SUBSTITUTIONS['steel_optimization']['impact'],
                trade_off=self.MATERIAL_SUBSTITUTIONS['steel_optimization']['trade_off'],
                applicable=True
            ))

        # Premium to Standard material suggestion
        if material_quality == 'premium':
            savings = predicted_cost * 0.08  # 8% savings
            optimizations.append(Optimization(
                id='quality_downgrade',
                category='material',
                title='Use Standard quality for non-visible areas',
                description='Use premium materials only for visible/high-traffic areas. Standard quality for utility areas, storage, etc.',
                savings_amount=round(savings),
                savings_percent=8.0,
                impact='medium',
                trade_off='Slightly lower finish quality in some areas',
                applicable=True
            ))

        return optimizations

    def _analyze_labor(self, input_data: Dict, predicted_cost: float) -> List[Optimization]:
        """Analyze labor-related optimizations"""
        optimizations = []

        project_type = input_data.get('project_type', 'commercial')
        num_workers = input_data.get('num_workers', 0)
        total_area = input_data.get('total_area_sqft', 0)
        planned_duration = input_data.get('planned_duration_days', 0)

        if num_workers <= 0 or total_area <= 0 or planned_duration <= 0:
            return optimizations

        # Calculate optimal worker count
        efficiency = self.WORKER_EFFICIENCY.get(project_type, self.WORKER_EFFICIENCY['commercial'])
        work_capacity = num_workers * planned_duration * efficiency['sqft_per_worker_per_day']
        optimal_workers = int(total_area / (planned_duration * efficiency['sqft_per_worker_per_day']))
        optimal_workers = max(optimal_workers, 5)  # Minimum 5 workers

        # Check for overstaffing (more than 20% over optimal)
        if num_workers > optimal_workers * 1.2:
            excess_workers = num_workers - optimal_workers
            labor_cost_percent = 0.35  # Labor is ~35% of total cost
            savings_per_worker = (predicted_cost * labor_cost_percent) / num_workers
            savings = savings_per_worker * excess_workers * 0.7  # 70% of excess worker cost

            optimizations.append(Optimization(
                id='reduce_workers',
                category='labor',
                title=f'Optimize workforce: Reduce from {num_workers} to {optimal_workers} workers',
                description=f'Current workforce appears oversized for {total_area:,} sqft over {planned_duration} days. Optimal team size is {optimal_workers} workers.',
                savings_amount=round(savings),
                savings_percent=round(savings / predicted_cost * 100, 1),
                impact='medium',
                trade_off='Requires better coordination and scheduling',
                applicable=True
            ))

        # Suggest skilled worker mix optimization
        if num_workers >= 10:
            savings = predicted_cost * 0.02  # 2% savings
            optimizations.append(Optimization(
                id='worker_mix',
                category='labor',
                title='Optimize skilled/unskilled worker ratio',
                description='Use 60% skilled and 40% unskilled workers. Deploy skilled workers only for specialized tasks.',
                savings_amount=round(savings),
                savings_percent=2.0,
                impact='low',
                trade_off='Requires task-based scheduling',
                applicable=True
            ))

        # Local labor suggestion
        location = input_data.get('location', '').lower()
        if 'rural' in location or 'village' in location or any(x in location for x in ['district', 'taluk']):
            savings = predicted_cost * 0.03  # 3% savings
            optimizations.append(Optimization(
                id='local_labor',
                category='labor',
                title='Hire local labor from nearby villages',
                description='Local workers reduce transportation and accommodation costs. Also eligible for MGNREGA benefits.',
                savings_amount=round(savings),
                savings_percent=3.0,
                impact='medium',
                trade_off='May need additional training for specialized work',
                applicable=True
            ))

        return optimizations

    def _analyze_scheduling(self, input_data: Dict, predicted_cost: float) -> List[Optimization]:
        """Analyze scheduling-related optimizations"""
        optimizations = []

        planned_duration = input_data.get('planned_duration_days', 0)
        weather_risk = input_data.get('weather_risk_zone', 'moderate')

        # Monsoon avoidance suggestion
        if weather_risk in ['moderate', 'high']:
            savings = predicted_cost * 0.05  # 5% savings from avoiding monsoon delays
            optimizations.append(Optimization(
                id='avoid_monsoon',
                category='scheduling',
                title='Schedule construction during October-May',
                description='Avoid monsoon season (June-September) to prevent weather delays, material damage, and productivity loss.',
                savings_amount=round(savings),
                savings_percent=5.0,
                impact='high',
                trade_off='May need to adjust project start date',
                applicable=True
            ))

        # Phased construction suggestion for large projects
        total_area = input_data.get('total_area_sqft', 0)
        if total_area > 10000 and planned_duration > 180:
            savings = predicted_cost * 0.03  # 3% savings
            optimizations.append(Optimization(
                id='phased_construction',
                category='scheduling',
                title='Implement phased construction approach',
                description='Break project into 2-3 phases. Complete and handover usable sections early to generate cash flow.',
                savings_amount=round(savings),
                savings_percent=3.0,
                impact='medium',
                trade_off='Requires detailed phase planning',
                applicable=True
            ))

        # Extended timeline suggestion (if very tight schedule)
        if planned_duration < 90 and total_area > 5000:
            savings = predicted_cost * 0.04  # 4% savings from avoiding overtime
            optimizations.append(Optimization(
                id='extend_timeline',
                category='scheduling',
                title='Consider extending timeline to avoid overtime costs',
                description='Tight schedules require overtime and rush orders. A 15-20% longer timeline can reduce costs.',
                savings_amount=round(savings),
                savings_percent=4.0,
                impact='medium',
                trade_off='Longer project duration',
                applicable=True
            ))

        return optimizations

    def _analyze_design(self, input_data: Dict, predicted_cost: float) -> List[Optimization]:
        """Analyze design-related optimizations"""
        optimizations = []

        complexity = input_data.get('complexity_level', 'medium')
        project_type = input_data.get('project_type', 'commercial')
        num_floors = input_data.get('num_floors', 1)
        has_basement = input_data.get('has_basement', False)

        # Simplify design for high complexity projects
        if complexity == 'high':
            savings = predicted_cost * 0.06  # 6% savings
            optimizations.append(Optimization(
                id='simplify_design',
                category='design',
                title='Simplify architectural design elements',
                description='Reduce ornamental features, use standard window sizes, and minimize custom millwork.',
                savings_amount=round(savings),
                savings_percent=6.0,
                impact='medium',
                trade_off='Less unique aesthetic features',
                applicable=True
            ))

        # Modular construction suggestion
        if project_type in ['residential', 'commercial'] and num_floors <= 4:
            savings = predicted_cost * 0.04  # 4% savings
            optimizations.append(Optimization(
                id='modular_design',
                category='design',
                title='Use modular/standardized room dimensions',
                description='Standard room sizes (10x12, 12x14 ft) reduce material waste and simplify construction.',
                savings_amount=round(savings),
                savings_percent=4.0,
                impact='low',
                trade_off='Less flexibility in room layouts',
                applicable=True
            ))

        # Basement optimization
        if has_basement:
            savings = predicted_cost * 0.02  # 2% savings
            optimizations.append(Optimization(
                id='basement_optimization',
                category='design',
                title='Optimize basement depth and waterproofing',
                description='Reduce basement depth by 0.5m if possible. Use integral waterproofing instead of membrane.',
                savings_amount=round(savings),
                savings_percent=2.0,
                impact='low',
                trade_off='Slightly less basement headroom',
                applicable=True
            ))

        return optimizations

    def _analyze_procurement(self, input_data: Dict, predicted_cost: float) -> List[Optimization]:
        """Analyze procurement-related optimizations"""
        optimizations = []

        total_area = input_data.get('total_area_sqft', 0)

        # Bulk purchasing suggestion
        if total_area > 3000:
            savings = predicted_cost * 0.04  # 4% savings
            optimizations.append(Optimization(
                id='bulk_purchase',
                category='procurement',
                title='Negotiate bulk purchase discounts',
                description='Order cement, steel, and bricks in bulk. Negotiate 8-12% discount with suppliers for large orders.',
                savings_amount=round(savings),
                savings_percent=4.0,
                impact='high',
                trade_off='Requires upfront capital and storage space',
                applicable=True
            ))

        # Direct manufacturer purchase
        if total_area > 5000:
            savings = predicted_cost * 0.03  # 3% savings
            optimizations.append(Optimization(
                id='direct_purchase',
                category='procurement',
                title='Purchase directly from manufacturers',
                description='Buy steel from TATA/SAIL dealers directly, cement from factory outlets to skip middlemen.',
                savings_amount=round(savings),
                savings_percent=3.0,
                impact='medium',
                trade_off='May have minimum order quantities',
                applicable=True
            ))

        # Rate contract suggestion
        savings = predicted_cost * 0.02  # 2% savings
        optimizations.append(Optimization(
            id='rate_contract',
            category='procurement',
            title='Establish rate contracts with suppliers',
            description='Lock in current prices with suppliers for project duration. Protects against price increases.',
            savings_amount=round(savings),
            savings_percent=2.0,
            impact='medium',
            trade_off='Commitment to specific suppliers',
            applicable=True
        ))

        # Local material sourcing
        location = input_data.get('location', '')
        if location:
            savings = predicted_cost * 0.025  # 2.5% savings
            optimizations.append(Optimization(
                id='local_materials',
                category='procurement',
                title='Source materials from local suppliers',
                description='Reduce transportation costs by 40-60% by sourcing aggregates, bricks, and sand locally.',
                savings_amount=round(savings),
                savings_percent=2.5,
                impact='medium',
                trade_off='Quality verification needed for local suppliers',
                applicable=True
            ))

        return optimizations

    def _generate_summary(self, optimizations: List[Optimization], total_savings: float, original_cost: float) -> str:
        """Generate a human-readable summary of optimizations"""
        if not optimizations:
            return "No significant optimizations identified for this project configuration."

        categories = {}
        for opt in optimizations:
            cat = opt.category
            if cat not in categories:
                categories[cat] = 0
            categories[cat] += opt.savings_amount

        summary_parts = []
        if 'material' in categories:
            summary_parts.append(f"material substitutions (Rs. {categories['material']:,.0f})")
        if 'labor' in categories:
            summary_parts.append(f"workforce optimization (Rs. {categories['labor']:,.0f})")
        if 'scheduling' in categories:
            summary_parts.append(f"scheduling improvements (Rs. {categories['scheduling']:,.0f})")
        if 'procurement' in categories:
            summary_parts.append(f"procurement strategies (Rs. {categories['procurement']:,.0f})")
        if 'design' in categories:
            summary_parts.append(f"design simplifications (Rs. {categories['design']:,.0f})")

        savings_percent = (total_savings / original_cost * 100) if original_cost > 0 else 0

        return f"Potential savings of Rs. {total_savings:,.0f} ({savings_percent:.1f}%) through {', '.join(summary_parts)}."


# Singleton instance
cost_optimizer = CostOptimizer()

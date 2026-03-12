// API Base URL
const API_BASE = '/api';

// Chart instances storage
let chartInstances = {};

// Indian States and Districts for Location Autocomplete
const indianLocations = [
    // Major Cities
    "Mumbai, Maharashtra", "Delhi, NCT", "Bangalore, Karnataka", "Hyderabad, Telangana",
    "Chennai, Tamil Nadu", "Kolkata, West Bengal", "Pune, Maharashtra", "Ahmedabad, Gujarat",
    "Jaipur, Rajasthan", "Lucknow, Uttar Pradesh", "Kanpur, Uttar Pradesh", "Nagpur, Maharashtra",
    "Indore, Madhya Pradesh", "Thane, Maharashtra", "Bhopal, Madhya Pradesh", "Visakhapatnam, Andhra Pradesh",
    "Patna, Bihar", "Vadodara, Gujarat", "Ghaziabad, Uttar Pradesh", "Ludhiana, Punjab",
    "Agra, Uttar Pradesh", "Nashik, Maharashtra", "Faridabad, Haryana", "Meerut, Uttar Pradesh",
    "Rajkot, Gujarat", "Varanasi, Uttar Pradesh", "Srinagar, Jammu & Kashmir", "Aurangabad, Maharashtra",
    "Dhanbad, Jharkhand", "Amritsar, Punjab", "Allahabad, Uttar Pradesh", "Ranchi, Jharkhand",
    "Howrah, West Bengal", "Coimbatore, Tamil Nadu", "Jabalpur, Madhya Pradesh", "Gwalior, Madhya Pradesh",
    "Vijayawada, Andhra Pradesh", "Jodhpur, Rajasthan", "Madurai, Tamil Nadu", "Raipur, Chhattisgarh",
    "Kota, Rajasthan", "Chandigarh, Punjab", "Guwahati, Assam", "Solapur, Maharashtra",
    "Hubli, Karnataka", "Tiruchirappalli, Tamil Nadu", "Bareilly, Uttar Pradesh", "Mysore, Karnataka",
    "Tiruppur, Tamil Nadu", "Gurgaon, Haryana", "Aligarh, Uttar Pradesh", "Jalandhar, Punjab",
    "Bhubaneswar, Odisha", "Salem, Tamil Nadu", "Warangal, Telangana", "Guntur, Andhra Pradesh",
    "Bhiwandi, Maharashtra", "Saharanpur, Uttar Pradesh", "Gorakhpur, Uttar Pradesh", "Bikaner, Rajasthan",
    "Amravati, Maharashtra", "Noida, Uttar Pradesh", "Jamshedpur, Jharkhand", "Bhilai, Chhattisgarh",
    "Cuttack, Odisha", "Firozabad, Uttar Pradesh", "Kochi, Kerala", "Nellore, Andhra Pradesh",
    "Bhavnagar, Gujarat", "Dehradun, Uttarakhand", "Durgapur, West Bengal", "Asansol, West Bengal",
    "Rourkela, Odisha", "Nanded, Maharashtra", "Kolhapur, Maharashtra", "Ajmer, Rajasthan",
    "Akola, Maharashtra", "Gulbarga, Karnataka", "Jamnagar, Gujarat", "Ujjain, Madhya Pradesh",
    "Loni, Uttar Pradesh", "Siliguri, West Bengal", "Jhansi, Uttar Pradesh", "Ulhasnagar, Maharashtra",
    "Jammu, Jammu & Kashmir", "Sangli, Maharashtra", "Mangalore, Karnataka", "Erode, Tamil Nadu",
    "Belgaum, Karnataka", "Ambattur, Tamil Nadu", "Tirunelveli, Tamil Nadu", "Malegaon, Maharashtra",
    "Gaya, Bihar", "Jalgaon, Maharashtra", "Udaipur, Rajasthan", "Maheshtala, West Bengal",
    // Districts and smaller cities
    "Thanjavur, Tamil Nadu", "Dindigul, Tamil Nadu", "Vellore, Tamil Nadu", "Rajahmundry, Andhra Pradesh",
    "Tirupati, Andhra Pradesh", "Kakinada, Andhra Pradesh", "Anantapur, Andhra Pradesh",
    "Kurnool, Andhra Pradesh", "Kadapa, Andhra Pradesh", "Tinsukia, Assam", "Dibrugarh, Assam",
    "Silchar, Assam", "Jorhat, Assam", "Muzaffarpur, Bihar", "Bhagalpur, Bihar", "Darbhanga, Bihar",
    "Arrah, Bihar", "Begusarai, Bihar", "Bilaspur, Chhattisgarh", "Korba, Chhattisgarh",
    "Durg, Chhattisgarh", "Rajnandgaon, Chhattisgarh", "Panaji, Goa", "Margao, Goa", "Vasco, Goa",
    "Surat, Gujarat", "Gandhinagar, Gujarat", "Junagadh, Gujarat", "Anand, Gujarat", "Navsari, Gujarat",
    "Morbi, Gujarat", "Nadiad, Gujarat", "Surendranagar, Gujarat", "Bharuch, Gujarat",
    "Rohtak, Haryana", "Hisar, Haryana", "Panipat, Haryana", "Karnal, Haryana", "Sonipat, Haryana",
    "Yamunanagar, Haryana", "Panchkula, Haryana", "Bhiwani, Haryana", "Sirsa, Haryana",
    "Shimla, Himachal Pradesh", "Mandi, Himachal Pradesh", "Dharamshala, Himachal Pradesh",
    "Solan, Himachal Pradesh", "Bokaro, Jharkhand", "Deoghar, Jharkhand", "Hazaribagh, Jharkhand",
    "Giridih, Jharkhand", "Belgavi, Karnataka", "Davangere, Karnataka", "Bellary, Karnataka",
    "Bijapur, Karnataka", "Shimoga, Karnataka", "Tumkur, Karnataka", "Raichur, Karnataka",
    "Bidar, Karnataka", "Hospet, Karnataka", "Thiruvananthapuram, Kerala", "Kozhikode, Kerala",
    "Thrissur, Kerala", "Kollam, Kerala", "Palakkad, Kerala", "Alappuzha, Kerala", "Kannur, Kerala",
    "Kottayam, Kerala", "Malappuram, Kerala", "Guna, Madhya Pradesh", "Sagar, Madhya Pradesh",
    "Dewas, Madhya Pradesh", "Satna, Madhya Pradesh", "Ratlam, Madhya Pradesh", "Rewa, Madhya Pradesh",
    "Murwara, Madhya Pradesh", "Singrauli, Madhya Pradesh", "Burhanpur, Madhya Pradesh",
    "Ahmednagar, Maharashtra", "Latur, Maharashtra", "Dhule, Maharashtra", "Ichalkaranji, Maharashtra",
    "Parbhani, Maharashtra", "Panvel, Maharashtra", "Satara, Maharashtra", "Beed, Maharashtra",
    "Yavatmal, Maharashtra", "Imphal, Manipur", "Shillong, Meghalaya", "Aizawl, Mizoram",
    "Kohima, Nagaland", "Dimapur, Nagaland", "Berhampur, Odisha", "Sambalpur, Odisha",
    "Balasore, Odisha", "Puri, Odisha", "Bathinda, Punjab", "Pathankot, Punjab", "Moga, Punjab",
    "Abohar, Punjab", "Malerkotla, Punjab", "Khanna, Punjab", "Phagwara, Punjab",
    "Alwar, Rajasthan", "Bharatpur, Rajasthan", "Sikar, Rajasthan", "Pali, Rajasthan",
    "Sri Ganganagar, Rajasthan", "Bhilwara, Rajasthan", "Kishangarh, Rajasthan", "Beawar, Rajasthan",
    "Hanumangarh, Rajasthan", "Gangtok, Sikkim", "Tiruvallur, Tamil Nadu", "Cuddalore, Tamil Nadu",
    "Kanchipuram, Tamil Nadu", "Nagercoil, Tamil Nadu", "Karaikudi, Tamil Nadu", "Neyveli, Tamil Nadu",
    "Kumbakonam, Tamil Nadu", "Karimnagar, Telangana", "Nizamabad, Telangana", "Khammam, Telangana",
    "Ramagundam, Telangana", "Mahbubnagar, Telangana", "Nalgonda, Telangana", "Adilabad, Telangana",
    "Agartala, Tripura", "Moradabad, Uttar Pradesh", "Mathura, Uttar Pradesh", "Shahjahanpur, Uttar Pradesh",
    "Rampur, Uttar Pradesh", "Muzaffarnagar, Uttar Pradesh", "Etawah, Uttar Pradesh", "Mirzapur, Uttar Pradesh",
    "Budaun, Uttar Pradesh", "Haridwar, Uttarakhand", "Haldwani, Uttarakhand", "Roorkee, Uttarakhand",
    "Rudrapur, Uttarakhand", "Kashipur, Uttarakhand", "Durgapur, West Bengal", "Bardhaman, West Bengal",
    "Kharagpur, West Bengal", "Haldia, West Bengal", "English Bazar, West Bengal", "Baharampur, West Bengal",
    "Habra, West Bengal", "Itanagar, Arunachal Pradesh", "Port Blair, Andaman & Nicobar",
    "Silvassa, Dadra & Nagar Haveli", "Daman, Daman & Diu", "Kavaratti, Lakshadweep", "Puducherry, Puducherry"
];

// Function to filter locations based on input
function filterLocations(input) {
    const searchTerm = input.toLowerCase().trim();
    if (searchTerm.length < 2) return [];

    return indianLocations.filter(location =>
        location.toLowerCase().includes(searchTerm)
    ).slice(0, 10); // Limit to 10 suggestions
}

// Location Autocomplete Setup
const locationInput = document.getElementById('location');
const locationSuggestions = document.getElementById('location-suggestions');
const selectedLocationDiv = document.getElementById('selected-location');
const locationText = document.getElementById('location-text');

if (locationInput && locationSuggestions) {
    locationInput.addEventListener('input', (e) => {
        const value = e.target.value;
        const matches = filterLocations(value);

        if (matches.length > 0 && value.length >= 2) {
            locationSuggestions.innerHTML = matches.map(loc =>
                `<div class="suggestion-item" data-value="${loc}">
                    <i class="fas fa-map-marker-alt"></i> ${loc}
                </div>`
            ).join('');
            locationSuggestions.classList.remove('hidden');
        } else {
            locationSuggestions.classList.add('hidden');
        }

        // Update display
        if (value.length > 0) {
            selectedLocationDiv.classList.remove('hidden');
            locationText.textContent = value;
        } else {
            selectedLocationDiv.classList.add('hidden');
        }
    });

    locationSuggestions.addEventListener('click', (e) => {
        const item = e.target.closest('.suggestion-item');
        if (item) {
            const value = item.dataset.value;
            locationInput.value = value;
            locationSuggestions.classList.add('hidden');
            selectedLocationDiv.classList.remove('hidden');
            locationText.textContent = value;
        }
    });

    // Hide suggestions when clicking outside
    document.addEventListener('click', (e) => {
        if (!e.target.closest('.location-group')) {
            locationSuggestions.classList.add('hidden');
        }
    });

    // Show suggestions on focus if there's input
    locationInput.addEventListener('focus', (e) => {
        if (e.target.value.length >= 2) {
            const matches = filterLocations(e.target.value);
            if (matches.length > 0) {
                locationSuggestions.innerHTML = matches.map(loc =>
                    `<div class="suggestion-item" data-value="${loc}">
                        <i class="fas fa-map-marker-alt"></i> ${loc}
                    </div>`
                ).join('');
                locationSuggestions.classList.remove('hidden');
            }
        }
    });
}

// Work Name Input Handler
const workNameInput = document.getElementById('work_name');
const workNameDisplay = document.getElementById('work-name-display');
const workNameText = document.getElementById('work-name-text');

if (workNameInput) {
    workNameInput.addEventListener('input', (e) => {
        const value = e.target.value.trim();
        if (value.length > 0) {
            workNameDisplay.classList.remove('hidden');
            workNameText.textContent = value;
        } else {
            workNameDisplay.classList.add('hidden');
        }
    });
}

// Smart Project Detection - Keywords mapping
const projectKeywords = {
    infrastructure: [
        'road', 'highway', 'bridge', 'flyover', 'metro', 'railway', 'station',
        'airport', 'port', 'dam', 'canal', 'pipeline', 'tunnel', 'expressway',
        'overpass', 'underpass', 'sewage', 'drainage', 'water supply', 'power plant',
        'substation', 'transmission', 'telecom tower', 'cograte', 'culvert', 'pavement',
        'footpath', 'sidewalk', 'street', 'lane', 'path', 'nala', 'drain'
    ],
    residential: [
        'house', 'home', 'apartment', 'flat', 'villa', 'bungalow', 'township',
        'bhk', '1bhk', '2bhk', '3bhk', '4bhk', 'duplex', 'penthouse', 'residential',
        'housing', 'colony', 'society', 'condo', 'condominium', 'row house', 'quarters',
        'hostel', 'dormitory', 'dwelling'
    ],
    commercial: [
        'mall', 'shopping', 'office', 'tower', 'complex', 'plaza', 'center',
        'centre', 'hotel', 'resort', 'restaurant', 'showroom', 'retail', 'store',
        'supermarket', 'hypermarket', 'multiplex', 'cinema', 'theater', 'bank',
        'hospital', 'clinic', 'school', 'college', 'university', 'institute',
        'building', 'bhawan', 'bhavan', 'community hall', 'auditorium', 'library'
    ],
    industrial: [
        'factory', 'plant', 'warehouse', 'godown', 'manufacturing', 'industry',
        'industrial', 'mill', 'refinery', 'steel', 'cement', 'textile', 'pharma',
        'chemical', 'automotive', 'assembly', 'processing', 'storage', 'logistics',
        'cold storage', 'sez', 'industrial park'
    ]
};

// Keywords that indicate NO floors needed (non-building infrastructure)
const noFloorsKeywords = [
    'road', 'highway', 'bridge', 'flyover', 'expressway', 'overpass', 'underpass',
    'tunnel', 'canal', 'pipeline', 'drain', 'drainage', 'sewage', 'nala', 'culvert',
    'pavement', 'footpath', 'sidewalk', 'street', 'lane', 'path', 'dam', 'embankment',
    'retaining wall', 'boundary wall', 'compound wall', 'fencing', 'water tank',
    'overhead tank', 'sump', 'borewell', 'tubewell', 'handpump', 'transmission line',
    'power line', 'telecom tower', 'signal', 'traffic'
];

// Function to check if floors field should be shown
function shouldShowFloorsField(projectName, projectType) {
    const name = projectName.toLowerCase();

    // Check if any no-floors keyword is present
    for (const keyword of noFloorsKeywords) {
        if (name.includes(keyword)) {
            return false;
        }
    }

    // If project type is infrastructure, check if it's a building type
    if (projectType === 'infrastructure') {
        // Some infrastructure can be buildings (like stations, airports terminals)
        const buildingInfraKeywords = ['station', 'terminal', 'airport', 'port', 'bus stand', 'depot'];
        for (const keyword of buildingInfraKeywords) {
            if (name.includes(keyword)) {
                return true;
            }
        }
        return false;
    }

    return true; // Show floors for residential, commercial, industrial by default
}

// Function to toggle floors field visibility
function toggleFloorsField(show) {
    const floorsGroup = document.getElementById('num_floors')?.closest('.form-group');
    if (floorsGroup) {
        if (show) {
            floorsGroup.style.display = '';
            floorsGroup.classList.remove('hidden');
        } else {
            floorsGroup.style.display = 'none';
            floorsGroup.classList.add('hidden');
            // Reset to 1 when hidden
            document.getElementById('num_floors').value = 1;
        }
    }
}

// Default parameters for each project type
const defaultParams = {
    infrastructure: {
        complexity_level: 'high',
        num_floors: 1,
        material_quality: 'standard',
        suggested_area: 5000,
        suggested_workers: 30,
        suggested_duration: 180
    },
    residential: {
        complexity_level: 'medium',
        num_floors: 2,
        material_quality: 'standard',
        suggested_area: 2500,
        suggested_workers: 15,
        suggested_duration: 120
    },
    commercial: {
        complexity_level: 'medium',
        num_floors: 3,
        material_quality: 'standard',
        suggested_area: 15000,
        suggested_workers: 40,
        suggested_duration: 240
    },
    industrial: {
        complexity_level: 'medium',
        num_floors: 1,
        material_quality: 'economy',
        suggested_area: 25000,
        suggested_workers: 35,
        suggested_duration: 180
    }
};

// Detect project type from name
function detectProjectType(projectName) {
    const name = projectName.toLowerCase();
    for (const [type, keywords] of Object.entries(projectKeywords)) {
        for (const keyword of keywords) {
            if (name.includes(keyword)) {
                return { type, matchedKeyword: keyword };
            }
        }
    }
    return null;
}

// Smart detection input handler
const projectNameInput = document.getElementById('project_name');
if (projectNameInput) {
    projectNameInput.addEventListener('input', (e) => {
        const name = e.target.value;
        const detectedInfo = document.getElementById('detected-info');
        const detectedType = document.getElementById('detected-type');
        const projectTypeSelect = document.getElementById('project_type');

        if (name.length < 3) {
            detectedInfo.classList.add('hidden');
            // Show floors by default when no detection
            toggleFloorsField(true);
            return;
        }

        const detection = detectProjectType(name);
        if (detection) {
            detectedInfo.classList.remove('hidden');
            detectedType.textContent = detection.type.charAt(0).toUpperCase() + detection.type.slice(1) +
                                       ` (matched: "${detection.matchedKeyword}")`;

            // Auto-fill form fields
            projectTypeSelect.value = detection.type;

            const params = defaultParams[detection.type];
            document.getElementById('complexity_level').value = params.complexity_level;
            document.getElementById('material_quality').value = params.material_quality;

            // Toggle floors field based on project type
            const showFloors = shouldShowFloorsField(name, detection.type);
            toggleFloorsField(showFloors);

            if (showFloors) {
                document.getElementById('num_floors').value = params.num_floors;
            }

            // Only update if values are default
            const areaInput = document.getElementById('total_area_sqft');
            const workersInput = document.getElementById('num_workers');
            const durationInput = document.getElementById('planned_duration_days');

            if (areaInput.value === '10000') areaInput.value = params.suggested_area;
            if (workersInput.value === '20') workersInput.value = params.suggested_workers;
            if (durationInput.value === '180') durationInput.value = params.suggested_duration;
        } else {
            detectedInfo.classList.add('hidden');
            // Check work name field as well for floors toggle
            const workName = document.getElementById('work_name')?.value || '';
            const currentType = projectTypeSelect.value;
            const showFloors = shouldShowFloorsField(name + ' ' + workName, currentType);
            toggleFloorsField(showFloors);
        }
    });
}

// Also check work name input for floors toggle
const workNameInputForFloors = document.getElementById('work_name');
if (workNameInputForFloors) {
    workNameInputForFloors.addEventListener('input', (e) => {
        const workName = e.target.value;
        const projectName = document.getElementById('project_name')?.value || '';
        const projectType = document.getElementById('project_type')?.value || 'commercial';
        const combinedName = workName + ' ' + projectName;

        const showFloors = shouldShowFloorsField(combinedName, projectType);
        toggleFloorsField(showFloors);
    });
}

// Also toggle on project type change
const projectTypeSelect = document.getElementById('project_type');
if (projectTypeSelect) {
    projectTypeSelect.addEventListener('change', (e) => {
        const projectType = e.target.value;
        const workName = document.getElementById('work_name')?.value || '';
        const projectName = document.getElementById('project_name')?.value || '';
        const combinedName = workName + ' ' + projectName;

        const showFloors = shouldShowFloorsField(combinedName, projectType);
        toggleFloorsField(showFloors);
    });
}

// DOM Elements
const tabButtons = document.querySelectorAll('.tab-btn');
const tabContents = document.querySelectorAll('.tab-content');

// Tab Navigation
tabButtons.forEach(btn => {
    btn.addEventListener('click', () => {
        const tabId = btn.dataset.tab;
        switchToTab(tabId);
    });
});

function switchToTab(tabId) {
    // Update active states
    tabButtons.forEach(b => b.classList.remove('active'));
    tabContents.forEach(c => c.classList.remove('active'));

    document.querySelector(`[data-tab="${tabId}"]`).classList.add('active');
    document.getElementById(tabId).classList.add('active');

    // Load data for the tab
    if (tabId === 'dashboard') loadDashboard();
    if (tabId === 'projects') loadProjects();
    if (tabId === 'history') loadHistory();
    if (tabId === 'analytics') loadAnalytics();
}

// Initialize Dashboard
async function loadDashboard() {
    try {
        const [statsResponse, historyResponse] = await Promise.all([
            fetch(`${API_BASE}/projects/stats`),
            fetch(`${API_BASE}/predictions/history`)
        ]);

        const stats = await statsResponse.json();
        const predictions = await historyResponse.json();

        // Update header stats
        document.getElementById('total-projects-stat').textContent = stats.total_projects || 0;
        document.getElementById('total-predictions-stat').textContent = stats.total_predictions || 0;
        document.getElementById('avg-risk-stat').textContent = Math.round(stats.average_risk_score || 0);

        // Update project type counts
        const distribution = stats.project_type_distribution || {};
        document.getElementById('residential-count').textContent = distribution.residential || 0;
        document.getElementById('commercial-count').textContent = distribution.commercial || 0;
        document.getElementById('industrial-count').textContent = distribution.industrial || 0;
        document.getElementById('infrastructure-count').textContent = distribution.infrastructure || 0;

        // Update recent predictions
        updateRecentPredictions(predictions.slice(0, 5));

        // Initialize charts
        initDashboardCharts(stats, predictions);

    } catch (error) {
        console.error('Error loading dashboard:', error);
    }
}

function updateRecentPredictions(predictions) {
    const container = document.getElementById('recent-predictions-list');

    if (!predictions || predictions.length === 0) {
        container.innerHTML = '<p class="empty-state">No predictions yet. Make your first prediction!</p>';
        return;
    }

    container.innerHTML = predictions.map(pred => `
        <div class="recent-item">
            <div class="info">
                <div class="type">${pred.input_data?.project_type || 'Unknown'}</div>
                <div class="date">${new Date(pred.created_at).toLocaleDateString()}</div>
            </div>
            <div class="cost">${formatCurrency(pred.predicted_cost)}</div>
        </div>
    `).join('');
}

function initDashboardCharts(stats, predictions) {
    // Destroy existing charts
    Object.values(chartInstances).forEach(chart => chart?.destroy());

    // Project Type Distribution Chart
    const distribution = stats.project_type_distribution || {};
    const typeCtx = document.getElementById('projectTypeChart')?.getContext('2d');
    if (typeCtx) {
        chartInstances.projectType = new Chart(typeCtx, {
            type: 'doughnut',
            data: {
                labels: ['Residential', 'Commercial', 'Industrial', 'Infrastructure'],
                datasets: [{
                    data: [
                        distribution.residential || 0,
                        distribution.commercial || 0,
                        distribution.industrial || 0,
                        distribution.infrastructure || 0
                    ],
                    backgroundColor: ['#4CAF50', '#2196F3', '#FF9800', '#9C27B0'],
                    borderWidth: 0
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'bottom'
                    }
                }
            }
        });
    }

    // Risk Distribution Chart
    const riskCtx = document.getElementById('riskDistributionChart')?.getContext('2d');
    if (riskCtx && predictions.length > 0) {
        const lowRisk = predictions.filter(p => p.risk_score < 40).length;
        const mediumRisk = predictions.filter(p => p.risk_score >= 40 && p.risk_score < 70).length;
        const highRisk = predictions.filter(p => p.risk_score >= 70).length;

        chartInstances.riskDist = new Chart(riskCtx, {
            type: 'doughnut',
            data: {
                labels: ['Low Risk', 'Medium Risk', 'High Risk'],
                datasets: [{
                    data: [lowRisk, mediumRisk, highRisk],
                    backgroundColor: ['#4CAF50', '#FFC107', '#F44336'],
                    borderWidth: 0
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'bottom'
                    }
                }
            }
        });
    }

    // Cost Trend Chart
    const trendCtx = document.getElementById('costTrendChart')?.getContext('2d');
    if (trendCtx && predictions.length > 0) {
        const recentPreds = predictions.slice(0, 10).reverse();
        chartInstances.costTrend = new Chart(trendCtx, {
            type: 'line',
            data: {
                labels: recentPreds.map((_, i) => `Prediction ${i + 1}`),
                datasets: [{
                    label: 'Predicted Cost (₹)',
                    data: recentPreds.map(p => p.predicted_cost),
                    borderColor: '#1e3a5f',
                    backgroundColor: 'rgba(30, 58, 95, 0.1)',
                    fill: true,
                    tension: 0.4
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: false
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        ticks: {
                            callback: value => formatCurrencyShort(value)
                        }
                    }
                }
            }
        });
    }
}

// Toggle infrastructure section based on project type
function toggleInfrastructureSection() {
    const projectType = document.getElementById('project_type')?.value;
    const workName = (document.getElementById('work_name')?.value || '').toLowerCase();
    const projectName = (document.getElementById('project_name')?.value || '').toLowerCase();
    const combinedName = workName + ' ' + projectName;

    const infraSection = document.getElementById('infrastructure-section');
    const buildingFeatures = document.getElementById('building-features-section');
    const areaGroup = document.getElementById('total_area_sqft')?.closest('.form-group');

    // Check if it's an infrastructure project
    const isInfra = projectType === 'infrastructure' ||
        ['road', 'highway', 'drain', 'nala', 'culvert', 'bridge', 'pavement', 'street', 'path'].some(kw => combinedName.includes(kw));

    if (isInfra && infraSection) {
        infraSection.style.display = 'block';
        if (buildingFeatures) buildingFeatures.style.display = 'none';
        if (areaGroup) areaGroup.style.display = 'none';
    } else {
        if (infraSection) infraSection.style.display = 'none';
        if (buildingFeatures) buildingFeatures.style.display = 'block';
        if (areaGroup) areaGroup.style.display = '';
    }
}

// Toggle road/drain specific fields
function toggleInfraFields() {
    const workType = document.getElementById('work_type')?.value;
    const roadFields = document.querySelectorAll('.road-field');
    const drainFields = document.querySelectorAll('.drain-field');

    if (workType === 'drain') {
        drainFields.forEach(f => f.style.display = '');
        document.querySelector('[for="road_length_m"]').textContent = 'Drain Length (meters) *';
        document.querySelector('[for="road_width_m"]').textContent = 'Drain Width (meters) *';
    } else {
        drainFields.forEach(f => f.style.display = 'none');
        document.querySelector('[for="road_length_m"]').textContent = 'Road Length (meters) *';
        document.querySelector('[for="road_width_m"]').textContent = 'Road Width (meters) *';
    }
}

// Add event listeners for infrastructure toggle
document.getElementById('project_type')?.addEventListener('change', toggleInfrastructureSection);
document.getElementById('work_name')?.addEventListener('input', toggleInfrastructureSection);
document.getElementById('work_type')?.addEventListener('change', toggleInfraFields);

// Estimation type toggle
const estimationTypeRadios = document.querySelectorAll('input[name="estimation_type"]');
estimationTypeRadios.forEach(radio => {
    radio.addEventListener('change', (e) => {
        const btn = document.getElementById('generate-estimate-btn');
        if (e.target.value === 'boq') {
            btn.innerHTML = '<i class="fas fa-file-invoice-dollar"></i> Generate SOR-Based Estimate';
        } else {
            btn.innerHTML = '<i class="fas fa-brain"></i> Get AI/ML Prediction';
        }
    });
});

// Prediction Form Handler
const predictionForm = document.getElementById('prediction-form');
if (predictionForm) {
    predictionForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const formData = new FormData(predictionForm);

        // Get work name (required for government contractors)
        const workName = formData.get('work_name') || '';
        if (!workName.trim()) {
            alert('Please enter the Work Name / Project Title');
            document.getElementById('work_name').focus();
            return;
        }

        // Get estimation type
        const estimationType = formData.get('estimation_type') || 'boq';

        const data = {
            // Government-specific fields
            work_name: workName,
            tender_number: formData.get('tender_number') || '',
            department: formData.get('department') || '',
            scheme_name: formData.get('scheme_name') || '',
            contractor_class: formData.get('contractor_class') || 'Class_B',
            // Original fields
            project_name: formData.get('project_name') || workName,
            project_type: formData.get('project_type'),
            location: formData.get('location') || 'Unknown',
            total_area_sqft: parseFloat(formData.get('total_area_sqft')) || 1000,
            num_floors: parseInt(formData.get('num_floors')) || 1,
            num_workers: parseInt(formData.get('num_workers')),
            planned_duration_days: parseInt(formData.get('planned_duration_days')),
            material_quality: formData.get('material_quality'),
            complexity_level: formData.get('complexity_level'),
            has_basement: document.getElementById('has_basement')?.checked || false,
            weather_risk_zone: formData.get('weather_risk_zone'),
            contractor_experience_years: parseInt(formData.get('contractor_experience_years')) || 5,
            // Additional fields
            design_type: formData.get('design_type') || 'standard',
            green_building: formData.get('green_building') || 'none',
            soil_type: formData.get('soil_type') || 'normal',
            seismic_zone: formData.get('seismic_zone') || 'zone3',
            site_accessibility: formData.get('site_accessibility') || 'easy',
            permit_status: formData.get('permit_status') || 'pending',
            has_parking: document.getElementById('has_parking')?.checked || false,
            has_elevator: document.getElementById('has_elevator')?.checked || false,
            has_swimming_pool: document.getElementById('has_swimming_pool')?.checked || false,
            has_hvac: document.getElementById('has_hvac')?.checked || false,
            has_fire_system: document.getElementById('has_fire_system')?.checked || false,
            has_smart_systems: document.getElementById('has_smart_systems')?.checked || false,
            requires_demolition: document.getElementById('requires_demolition')?.checked || false,
            // Infrastructure fields
            work_type: formData.get('work_type') || 'building',
            road_length_m: parseFloat(formData.get('road_length_m')) || 500,
            road_width_m: parseFloat(formData.get('road_width_m')) || 5,
            road_type: formData.get('road_type') || 'bituminous',
            drain_length_m: parseFloat(formData.get('road_length_m')) || 500,
            drain_width_m: parseFloat(formData.get('road_width_m')) || 1,
            drain_depth_m: parseFloat(formData.get('drain_depth_m')) || 0.6,
            drain_type: formData.get('drain_type') || 'open',
            // Contract value for profit calculation
            contract_value: parseFloat(formData.get('contract_value')) || 0,
            bid_type: formData.get('bid_type') || 'at_par',
            bid_percentage: parseFloat(formData.get('bid_percentage')) || 0
        };

        try {
            let apiEndpoint = estimationType === 'boq'
                ? `${API_BASE}/predictions/govt-estimate`
                : `${API_BASE}/predictions/predict`;

            const response = await fetch(apiEndpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });

            if (!response.ok) throw new Error('Estimation failed');

            const result = await response.json();
            // Include government-specific fields in result
            result.work_name = data.work_name;
            result.tender_number = data.tender_number;
            result.department = data.department;
            result.scheme_name = data.scheme_name;
            result.contractor_class = data.contractor_class;
            result.project_name = data.project_name;
            result.project_type = data.project_type;
            result.location = data.location;
            result.total_area_sqft = data.total_area_sqft;
            result.planned_duration_days = data.planned_duration_days;
            result.estimation_type = estimationType;
            // Contract value for profit calculation
            result.contract_value = data.contract_value;
            result.bid_type = data.bid_type;
            result.bid_percentage = data.bid_percentage;

            if (estimationType === 'boq') {
                displayBOQResult(result);
            } else {
                displayPredictionResult(result);
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Failed to get estimate. Please try again.');
        }
    });
}

// Display BOQ Result
function displayBOQResult(result) {
    const resultContainer = document.getElementById('prediction-result');
    resultContainer.classList.remove('hidden');

    // Show BOQ section, hide ML results
    const boqSection = document.getElementById('boq-section');
    const mlResultsGrid = document.getElementById('ml-results-grid');

    boqSection.classList.remove('hidden');
    if (mlResultsGrid) mlResultsGrid.style.display = 'none';

    // Hide other ML-specific sections
    document.querySelector('.breakdown-section')?.classList.add('hidden');
    document.querySelector('.timeline-section')?.classList.add('hidden');
    document.querySelector('.risk-factors-section')?.classList.add('hidden');
    document.querySelector('.recommendations-section')?.classList.add('hidden');
    document.querySelector('.optimization-section')?.classList.add('hidden');

    // Display project header
    const projectHeader = document.getElementById('result-project-name');
    const projectTitle = document.getElementById('result-project-title');
    const projectTypeBadge = document.getElementById('result-project-type-badge');

    const displayName = result.work_name || result.project_name;
    if (displayName) {
        projectHeader.classList.remove('hidden');
        projectTitle.textContent = displayName;
        projectTypeBadge.textContent = result.work_type || result.project_type || 'Project';

        // Add government info
        let govtInfo = '';
        if (result.department) {
            govtInfo += `<span class="govt-badge dept">${result.department}</span>`;
        }
        if (result.tender_number) {
            govtInfo += `<span class="govt-badge tender">Tender: ${result.tender_number}</span>`;
        }
        if (result.location && result.location !== 'Unknown') {
            govtInfo += `<span class="govt-badge location"><i class="fas fa-map-marker-alt"></i> ${result.location}</span>`;
        }

        let govtInfoDiv = document.getElementById('result-govt-info');
        if (!govtInfoDiv && govtInfo) {
            govtInfoDiv = document.createElement('div');
            govtInfoDiv.id = 'result-govt-info';
            govtInfoDiv.className = 'result-govt-info';
            projectHeader.appendChild(govtInfoDiv);
        }
        if (govtInfoDiv) {
            govtInfoDiv.innerHTML = govtInfo;
        }
    }

    // Update factors
    document.getElementById('boq-location-factor').textContent = result.location_factor?.toFixed(2) || '1.00';
    document.getElementById('boq-quality-factor').textContent = result.quality_factor?.toFixed(2) || '1.00';

    // Populate BOQ table
    const tbody = document.getElementById('boq-tbody');
    tbody.innerHTML = '';

    if (result.boq && result.boq.length > 0) {
        result.boq.forEach(item => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${item.sno}</td>
                <td><strong>${item.item}</strong></td>
                <td>${item.description}</td>
                <td>${item.unit}</td>
                <td>${item.quantity.toLocaleString('en-IN')}</td>
                <td>${formatCurrency(item.rate)}</td>
                <td><strong>${formatCurrency(item.amount)}</strong></td>
            `;
            tbody.appendChild(row);
        });
    }

    // Update summary
    document.getElementById('boq-subtotal').textContent = formatCurrency(result.subtotal);
    document.getElementById('boq-profit').textContent = formatCurrency(result.contractor_profit);
    document.getElementById('boq-overhead').textContent = formatCurrency(result.overhead_charges);
    document.getElementById('boq-contingency').textContent = formatCurrency(result.contingency);
    document.getElementById('boq-before-gst').textContent = formatCurrency(result.amount_before_gst);
    document.getElementById('boq-gst-rate').textContent = result.gst_rate || 12;
    document.getElementById('boq-gst').textContent = formatCurrency(result.gst);
    document.getElementById('boq-cess').textContent = formatCurrency(result.labour_cess);
    document.getElementById('boq-grand-total').textContent = formatCurrency(result.grand_total);

    // Cost per unit
    if (result.cost_per_sqft) {
        document.getElementById('cost-per-unit-label').textContent = 'Cost per Sq.Ft.';
        document.getElementById('boq-cost-per-unit').textContent = formatCurrency(result.cost_per_sqft);
    } else if (result.cost_per_km) {
        document.getElementById('cost-per-unit-label').textContent = 'Cost per Km';
        document.getElementById('boq-cost-per-unit').textContent = formatCurrency(result.cost_per_km);
    } else if (result.cost_per_rm) {
        document.getElementById('cost-per-unit-label').textContent = 'Cost per R.M.';
        document.getElementById('boq-cost-per-unit').textContent = formatCurrency(result.cost_per_rm);
    }

    // Store result for export
    window.lastPredictionResult = result;
    window.lastBOQResult = result;

    // Calculate and display profit analysis
    displayProfitAnalysis(result);

    // Scroll to results
    resultContainer.scrollIntoView({ behavior: 'smooth' });
}

// Display Profit Analysis for Contractors
function displayProfitAnalysis(result) {
    const profitSection = document.getElementById('profit-analysis-section');
    if (!profitSection) return;

    const contractValue = result.contract_value || 0;
    const constructionCost = result.grand_total || result.predicted_cost || 0;

    // Show/hide section based on contract value
    if (contractValue <= 0) {
        profitSection.style.display = 'block';
        document.getElementById('profit-contract-value').textContent = 'Not Entered';
        document.getElementById('profit-construction-cost').textContent = formatCurrency(constructionCost);
        document.getElementById('profit-amount').textContent = '--';
        document.getElementById('profit-margin-label').textContent = 'Enter contract value above';

        const viabilityIndicator = document.getElementById('viability-indicator');
        viabilityIndicator.className = 'viability-indicator neutral';
        viabilityIndicator.innerHTML = '<i class="fas fa-info-circle"></i> <span id="viability-text">Enter Contract Value above to see your profit/loss analysis</span>';
        document.getElementById('viability-recommendation').textContent = 'The contract value is the amount the government will pay you for this work as per tender/agreement.';

        // Hide breakdown
        document.getElementById('profit-breakdown').style.display = 'none';
        return;
    }

    // Calculate profit
    const profit = contractValue - constructionCost;
    const profitMargin = (profit / contractValue) * 100;
    const isProfit = profit >= 0;

    // Update cards
    document.getElementById('profit-contract-value').textContent = formatCurrency(contractValue);
    document.getElementById('profit-construction-cost').textContent = formatCurrency(constructionCost);
    document.getElementById('profit-amount').textContent = (isProfit ? '+' : '') + formatCurrency(profit);
    document.getElementById('profit-margin-label').textContent = profitMargin.toFixed(1) + '% Margin';

    // Update profit card styling
    const profitAmountCard = document.getElementById('profit-amount-card');
    if (isProfit) {
        profitAmountCard.classList.remove('loss');
    } else {
        profitAmountCard.classList.add('loss');
    }

    // Update viability indicator
    const viabilityIndicator = document.getElementById('viability-indicator');
    const viabilityRecommendation = document.getElementById('viability-recommendation');
    let viabilityClass, viabilityIcon, viabilityText, recommendation;

    if (profitMargin >= 15) {
        viabilityClass = 'profitable';
        viabilityIcon = 'fa-check-circle';
        viabilityText = 'HIGHLY PROFITABLE - Excellent contract to take!';
        recommendation = 'This contract offers excellent profit margins. You can comfortably execute this project with good returns. Consider allocating quality resources to ensure timely completion.';
    } else if (profitMargin >= 8) {
        viabilityClass = 'profitable';
        viabilityIcon = 'fa-thumbs-up';
        viabilityText = 'PROFITABLE - Good contract, proceed with confidence';
        recommendation = 'This contract offers reasonable profit margins. Ensure tight cost control during execution. Monitor material prices and labor efficiency closely.';
    } else if (profitMargin >= 3) {
        viabilityClass = 'marginal';
        viabilityIcon = 'fa-exclamation-triangle';
        viabilityText = 'MARGINAL PROFIT - Proceed with caution';
        recommendation = 'This contract has thin margins. Any cost overrun or delay could eat into profits. Consider negotiating better terms or optimizing your execution plan. Strict project management is essential.';
    } else if (profitMargin >= 0) {
        viabilityClass = 'marginal';
        viabilityIcon = 'fa-exclamation-circle';
        viabilityText = 'BREAK-EVEN - Very risky, reconsider';
        recommendation = 'You are barely breaking even on this contract. Unless there are strategic reasons (future work, relationship building), this contract is risky. Any unexpected cost will result in loss.';
    } else if (profitMargin >= -10) {
        viabilityClass = 'loss';
        viabilityIcon = 'fa-times-circle';
        viabilityText = 'LOSS EXPECTED - Not recommended';
        recommendation = 'This contract will result in a loss based on current estimates. Review your bid calculation. Consider renegotiating terms, reducing scope, or declining the contract unless strategically necessary.';
    } else {
        viabilityClass = 'loss';
        viabilityIcon = 'fa-ban';
        viabilityText = 'SIGNIFICANT LOSS - DO NOT PROCEED';
        recommendation = 'This contract will result in significant financial loss. Either the contract value is too low or the scope is underestimated. Strongly recommend NOT taking this contract or completely renegotiating terms.';
    }

    viabilityIndicator.className = 'viability-indicator ' + viabilityClass;
    viabilityIndicator.innerHTML = `<i class="fas ${viabilityIcon}"></i> <span id="viability-text">${viabilityText}</span>`;
    viabilityRecommendation.textContent = recommendation;

    // Update breakdown table
    document.getElementById('profit-breakdown').style.display = 'block';
    document.getElementById('pb-contract-value').textContent = formatCurrency(contractValue);

    // Calculate breakdown from BOQ result
    const materialLaborCost = result.subtotal || (constructionCost * 0.75);
    const overheadCost = (result.overhead_charges || 0) + (result.contingency || 0) + (result.contractor_profit || 0);
    const gstCost = result.gst || (constructionCost * 0.12);
    const cessCost = result.labour_cess || (constructionCost * 0.01);

    document.getElementById('pb-material-cost').textContent = formatCurrency(materialLaborCost);
    document.getElementById('pb-overhead-cost').textContent = formatCurrency(overheadCost);
    document.getElementById('pb-gst-cost').textContent = formatCurrency(gstCost);
    document.getElementById('pb-cess-cost').textContent = formatCurrency(cessCost);
    document.getElementById('pb-net-profit').textContent = (isProfit ? '+' : '') + formatCurrency(profit);
    document.getElementById('pb-profit-margin').textContent = profitMargin.toFixed(1) + '%';

    // Update profit row styling
    const profitRow = document.getElementById('pb-profit-row');
    if (isProfit) {
        profitRow.classList.remove('loss');
    } else {
        profitRow.classList.add('loss');
    }

    profitSection.style.display = 'block';
}

// Display Prediction Results
function displayPredictionResult(result) {
    const resultContainer = document.getElementById('prediction-result');
    resultContainer.classList.remove('hidden');

    // Display work name prominently (for government contractors)
    const projectHeader = document.getElementById('result-project-name');
    const projectTitle = document.getElementById('result-project-title');
    const projectTypeBadge = document.getElementById('result-project-type-badge');

    // Use work_name as the primary title for government contractors
    const displayName = result.work_name || result.project_name;

    if (displayName && displayName.trim()) {
        projectHeader.classList.remove('hidden');
        projectTitle.textContent = displayName;
        projectTypeBadge.textContent = result.project_type || 'Project';

        // Add government details if available
        let govtInfo = '';
        if (result.department) {
            govtInfo += `<span class="govt-badge dept">${result.department}</span>`;
        }
        if (result.tender_number) {
            govtInfo += `<span class="govt-badge tender">Tender: ${result.tender_number}</span>`;
        }
        if (result.location && result.location !== 'Unknown') {
            govtInfo += `<span class="govt-badge location"><i class="fas fa-map-marker-alt"></i> ${result.location}</span>`;
        }

        // Create or update government info display
        let govtInfoDiv = document.getElementById('result-govt-info');
        if (!govtInfoDiv && govtInfo) {
            govtInfoDiv = document.createElement('div');
            govtInfoDiv.id = 'result-govt-info';
            govtInfoDiv.className = 'result-govt-info';
            projectHeader.appendChild(govtInfoDiv);
        }
        if (govtInfoDiv) {
            govtInfoDiv.innerHTML = govtInfo;
        }
    } else {
        projectHeader.classList.add('hidden');
    }

    // Update cost
    document.getElementById('predicted-cost').textContent = formatCurrency(result.predicted_cost);
    document.getElementById('cost-range').textContent =
        `Range: ${formatCurrency(result.cost_lower_bound)} - ${formatCurrency(result.cost_upper_bound)}`;

    // Cost per sqft
    const costPerSqft = result.total_area_sqft ? result.predicted_cost / result.total_area_sqft : 0;
    document.getElementById('cost-per-sqft').textContent = `${formatCurrency(costPerSqft)} per sq ft`;

    // Update delay
    document.getElementById('predicted-delay').textContent = `${result.predicted_delay_days} days`;
    document.getElementById('delay-range').textContent =
        `Range: ${result.delay_lower_bound} - ${result.delay_upper_bound} days`;

    // Completion date
    const plannedDays = result.planned_duration_days || 180;
    const totalDays = plannedDays + result.predicted_delay_days;
    const completionDate = new Date();
    completionDate.setDate(completionDate.getDate() + totalDays);
    document.getElementById('completion-date').textContent =
        `Est. completion: ${completionDate.toLocaleDateString('en-IN', { month: 'short', year: 'numeric' })}`;

    // Update probability
    const probability = (result.delay_probability * 100).toFixed(1);
    document.getElementById('delay-probability').textContent = `${probability}%`;
    document.getElementById('probability-fill').style.width = `${probability}%`;

    // Update risk score
    document.getElementById('risk-score').textContent = result.risk_score.toFixed(0);
    document.getElementById('risk-fill').style.width = `${result.risk_score}%`;

    // Risk label
    let riskLabel = 'Low Risk';
    let riskColor = '#4caf50';
    if (result.risk_score > 70) {
        riskLabel = 'High Risk';
        riskColor = '#f44336';
    } else if (result.risk_score > 40) {
        riskLabel = 'Medium Risk';
        riskColor = '#ff9800';
    }
    document.getElementById('risk-label').textContent = riskLabel;
    document.getElementById('risk-label').style.color = riskColor;

    // Cost Breakdown
    displayCostBreakdown(result.predicted_cost, result.project_type);

    // Timeline
    displayTimeline(result.planned_duration_days || 180, result.predicted_delay_days);

    // Risk factors
    displayRiskFactors(result.risk_factors || []);

    // Recommendations
    const recommendationsList = document.getElementById('recommendations-list');
    recommendationsList.innerHTML = '';
    if (result.recommendations && result.recommendations.length > 0) {
        result.recommendations.forEach(rec => {
            recommendationsList.innerHTML += `<li><i class="fas fa-check-circle"></i> ${rec}</li>`;
        });
    }

    // Optimization suggestions
    displayOptimizationSuggestions(result);

    // Store result for export
    window.lastPredictionResult = result;

    // Calculate and display profit analysis (for ML predictions too)
    displayProfitAnalysis(result);

    // Scroll to results
    resultContainer.scrollIntoView({ behavior: 'smooth' });
}

function displayCostBreakdown(totalCost, projectType) {
    // Cost breakdown percentages vary by project type
    const breakdowns = {
        residential: { materials: 45, labor: 30, equipment: 10, overhead: 10, contingency: 5 },
        commercial: { materials: 40, labor: 28, equipment: 15, overhead: 12, contingency: 5 },
        industrial: { materials: 50, labor: 22, equipment: 18, overhead: 5, contingency: 5 },
        infrastructure: { materials: 35, labor: 25, equipment: 25, overhead: 10, contingency: 5 }
    };

    const breakdown = breakdowns[projectType] || breakdowns.commercial;

    // Update breakdown values
    const categories = ['materials', 'labor', 'equipment', 'overhead', 'contingency'];
    categories.forEach(cat => {
        const cost = totalCost * (breakdown[cat] / 100);
        document.getElementById(`${cat}-cost`).textContent = formatCurrency(cost);
        document.getElementById(`${cat}-percent`).textContent = `${breakdown[cat]}%`;
    });

    // Create/Update chart
    const ctx = document.getElementById('costBreakdownChart')?.getContext('2d');
    if (ctx) {
        if (chartInstances.costBreakdown) chartInstances.costBreakdown.destroy();

        chartInstances.costBreakdown = new Chart(ctx, {
            type: 'pie',
            data: {
                labels: ['Materials', 'Labor', 'Equipment', 'Overhead', 'Contingency'],
                datasets: [{
                    data: categories.map(cat => breakdown[cat]),
                    backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF'],
                    borderWidth: 2,
                    borderColor: '#fff'
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: false
                    }
                }
            }
        });
    }
}

function displayTimeline(plannedDays, delayDays) {
    const timeline = document.getElementById('project-timeline');
    const totalDays = plannedDays + delayDays;

    // Define project phases
    const phases = [
        { name: 'Site Preparation', description: 'Land clearing, leveling, and basic setup', percent: 10 },
        { name: 'Foundation Work', description: 'Excavation, foundation laying, and curing', percent: 15 },
        { name: 'Structure Construction', description: 'Column, beam, and slab construction', percent: 30 },
        { name: 'MEP Installation', description: 'Mechanical, electrical, and plumbing work', percent: 20 },
        { name: 'Finishing Work', description: 'Plastering, painting, and final touches', percent: 20 },
        { name: 'Handover', description: 'Final inspection and project completion', percent: 5 }
    ];

    let cumulativeDays = 0;
    timeline.innerHTML = phases.map((phase, i) => {
        const phaseDays = Math.round(totalDays * (phase.percent / 100));
        cumulativeDays += phaseDays;
        const endDate = new Date();
        endDate.setDate(endDate.getDate() + cumulativeDays);

        return `
            <div class="timeline-item">
                <div class="timeline-content">
                    <h4>${phase.name}</h4>
                    <p>${phase.description}</p>
                    <div class="timeline-duration">
                        <i class="fas fa-calendar"></i> ${phaseDays} days
                        <span style="margin-left: 15px;"><i class="fas fa-flag-checkered"></i> ${endDate.toLocaleDateString('en-IN', { day: 'numeric', month: 'short' })}</span>
                    </div>
                </div>
            </div>
        `;
    }).join('');
}

function displayRiskFactors(riskFactors) {
    const container = document.getElementById('risk-factors-list');

    if (!riskFactors || riskFactors.length === 0) {
        container.innerHTML = '<p class="empty-state">No significant risk factors identified.</p>';
        return;
    }

    container.innerHTML = riskFactors.map(rf => `
        <div class="risk-factor">
            <span class="severity ${rf.severity}">${rf.severity}</span>
            <div class="details">
                <div class="factor-name">${rf.factor}</div>
                <div class="factor-impact">${rf.impact}</div>
            </div>
        </div>
    `).join('');

    // Risk factors radar chart
    const ctx = document.getElementById('riskFactorsChart')?.getContext('2d');
    if (ctx && riskFactors.length > 0) {
        if (chartInstances.riskFactors) chartInstances.riskFactors.destroy();

        const severityValues = { high: 3, medium: 2, low: 1 };
        chartInstances.riskFactors = new Chart(ctx, {
            type: 'radar',
            data: {
                labels: riskFactors.slice(0, 6).map(rf => rf.factor.substring(0, 15)),
                datasets: [{
                    label: 'Risk Level',
                    data: riskFactors.slice(0, 6).map(rf => severityValues[rf.severity] || 1),
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderWidth: 2,
                    pointBackgroundColor: 'rgba(255, 99, 132, 1)'
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    r: {
                        beginAtZero: true,
                        max: 3,
                        ticks: {
                            stepSize: 1,
                            display: false
                        }
                    }
                },
                plugins: {
                    legend: {
                        display: false
                    }
                }
            }
        });
    }
}

function displayOptimizationSuggestions(result) {
    const container = document.getElementById('optimization-cards');
    const suggestions = [];

    // Generate suggestions based on the result
    if (result.risk_score > 50) {
        suggestions.push({
            title: 'Reduce Risk Score',
            icon: 'fa-shield-alt',
            description: 'Consider hiring more experienced contractors or adding additional oversight.',
            positive: 'Risk -15%',
            negative: 'Cost +5%'
        });
    }

    if (result.predicted_delay_days > 10) {
        suggestions.push({
            title: 'Accelerate Timeline',
            icon: 'fa-rocket',
            description: 'Increasing workforce by 20% could reduce delays significantly.',
            positive: 'Delay -30%',
            negative: 'Cost +8%'
        });
    }

    suggestions.push({
        title: 'Material Optimization',
        icon: 'fa-cubes',
        description: 'Bulk purchasing of materials can reduce costs without affecting quality.',
        positive: 'Cost -5%',
        negative: ''
    });

    suggestions.push({
        title: 'Weather Planning',
        icon: 'fa-cloud-sun',
        description: 'Starting construction in dry season can minimize weather-related delays.',
        positive: 'Delay -20%',
        negative: ''
    });

    container.innerHTML = suggestions.map(s => `
        <div class="optimization-card">
            <h4><i class="fas ${s.icon}"></i> ${s.title}</h4>
            <p>${s.description}</p>
            <div class="optimization-impact">
                ${s.positive ? `<span class="impact-item positive">${s.positive}</span>` : ''}
                ${s.negative ? `<span class="impact-item negative">${s.negative}</span>` : ''}
            </div>
        </div>
    `).join('');
}

// Format currency in Indian Rupees
function formatCurrency(amount) {
    return new Intl.NumberFormat('en-IN', {
        style: 'currency',
        currency: 'INR',
        minimumFractionDigits: 0,
        maximumFractionDigits: 0
    }).format(amount);
}

function formatCurrencyShort(amount) {
    if (amount >= 10000000) return `₹${(amount / 10000000).toFixed(1)}Cr`;
    if (amount >= 100000) return `₹${(amount / 100000).toFixed(1)}L`;
    return formatCurrency(amount);
}

// Projects Management
const newProjectBtn = document.getElementById('new-project-btn');
const newProjectForm = document.getElementById('new-project-form');
const cancelProjectBtn = document.getElementById('cancel-project-btn');
const createProjectForm = document.getElementById('create-project-form');

if (newProjectBtn) {
    newProjectBtn.addEventListener('click', () => {
        newProjectForm.classList.toggle('hidden');
    });
}

if (cancelProjectBtn) {
    cancelProjectBtn.addEventListener('click', () => {
        newProjectForm.classList.add('hidden');
        createProjectForm.reset();
    });
}

if (createProjectForm) {
    createProjectForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const formData = new FormData(createProjectForm);
        const data = {
            name: formData.get('name'),
            project_type: formData.get('project_type'),
            location: formData.get('location') || 'Unknown',
            total_area_sqft: parseFloat(formData.get('total_area_sqft')),
            num_workers: parseInt(formData.get('num_workers')),
            planned_duration_days: parseInt(formData.get('planned_duration_days'))
        };

        try {
            const response = await fetch(`${API_BASE}/projects`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });

            if (!response.ok) throw new Error('Failed to create project');

            newProjectForm.classList.add('hidden');
            createProjectForm.reset();
            loadProjects();
        } catch (error) {
            console.error('Error:', error);
            alert('Failed to create project. Please try again.');
        }
    });
}

// Load Projects
async function loadProjects() {
    try {
        const response = await fetch(`${API_BASE}/projects`);
        const projects = await response.json();

        const projectsList = document.getElementById('projects-list');
        projectsList.innerHTML = '';

        if (projects.length === 0) {
            projectsList.innerHTML = '<p class="empty-state">No projects yet. Create your first project!</p>';
            return;
        }

        projects.forEach(project => {
            projectsList.innerHTML += `
                <div class="project-card">
                    <h3>${project.name}</h3>
                    <span class="project-type">${project.project_type}</span>
                    <div class="project-details">
                        <span><i class="fas fa-ruler-combined"></i> <strong>Area:</strong> ${project.total_area_sqft.toLocaleString()} sqft</span>
                        <span><i class="fas fa-users"></i> <strong>Workers:</strong> ${project.num_workers}</span>
                        <span><i class="fas fa-calendar-alt"></i> <strong>Duration:</strong> ${project.planned_duration_days} days</span>
                        <span><i class="fas fa-map-marker-alt"></i> <strong>Location:</strong> ${project.location || 'Not specified'}</span>
                        <span><i class="fas fa-clock"></i> <strong>Created:</strong> ${new Date(project.created_at).toLocaleDateString()}</span>
                    </div>
                    <div class="project-actions">
                        <button class="btn btn-primary btn-sm" onclick="predictForProject(${project.id})">
                            <i class="fas fa-calculator"></i> Predict
                        </button>
                        <button class="btn btn-secondary btn-sm" onclick="deleteProject(${project.id})">
                            <i class="fas fa-trash"></i> Delete
                        </button>
                    </div>
                </div>
            `;
        });
    } catch (error) {
        console.error('Error loading projects:', error);
    }
}

// Predict for existing project
async function predictForProject(projectId) {
    try {
        const response = await fetch(`${API_BASE}/projects/${projectId}`);
        const project = await response.json();

        // Switch to predict tab and fill form
        switchToTab('predict');

        document.getElementById('project_name').value = project.name || '';
        document.getElementById('project_type').value = project.project_type;
        document.getElementById('location').value = project.location || '';
        document.getElementById('total_area_sqft').value = project.total_area_sqft;
        document.getElementById('num_floors').value = project.num_floors || 1;
        document.getElementById('num_workers').value = project.num_workers;
        document.getElementById('planned_duration_days').value = project.planned_duration_days;
        document.getElementById('material_quality').value = project.material_quality || 'standard';
        document.getElementById('complexity_level').value = project.complexity_level || 'medium';
        document.getElementById('weather_risk_zone').value = project.weather_risk_zone || 'moderate';
        document.getElementById('contractor_experience_years').value = project.contractor_experience_years || 5;
        document.getElementById('has_basement').checked = project.has_basement || false;

    } catch (error) {
        console.error('Error:', error);
        alert('Failed to load project data.');
    }
}

// Delete project
async function deleteProject(projectId) {
    if (!confirm('Are you sure you want to delete this project?')) return;

    try {
        const response = await fetch(`${API_BASE}/projects/${projectId}`, {
            method: 'DELETE'
        });

        if (!response.ok) throw new Error('Failed to delete project');

        loadProjects();
    } catch (error) {
        console.error('Error:', error);
        alert('Failed to delete project.');
    }
}

// Load History
async function loadHistory() {
    try {
        const response = await fetch(`${API_BASE}/predictions/history`);
        const predictions = await response.json();

        const tbody = document.getElementById('history-tbody');
        tbody.innerHTML = '';

        if (predictions.length === 0) {
            tbody.innerHTML = '<tr><td colspan="8" style="text-align: center;">No predictions yet.</td></tr>';
            return;
        }

        predictions.forEach(pred => {
            const date = new Date(pred.created_at).toLocaleDateString();
            const inputData = pred.input_data || {};
            const costPerSqft = inputData.total_area_sqft ? pred.predicted_cost / inputData.total_area_sqft : 0;

            tbody.innerHTML += `
                <tr>
                    <td>${date}</td>
                    <td><span class="project-type" style="padding: 3px 10px; font-size: 0.8rem;">${inputData.project_type || 'N/A'}</span></td>
                    <td>${(inputData.total_area_sqft || 0).toLocaleString()}</td>
                    <td>${formatCurrency(pred.predicted_cost)}</td>
                    <td>${formatCurrency(costPerSqft)}</td>
                    <td>${pred.predicted_delay_days} days</td>
                    <td><span style="color: ${pred.risk_score > 70 ? '#f44336' : pred.risk_score > 40 ? '#ff9800' : '#4caf50'}; font-weight: 600;">${pred.risk_score.toFixed(0)}</span></td>
                    <td>
                        <button class="btn btn-sm btn-secondary" onclick="viewPredictionDetails(${pred.id})">
                            <i class="fas fa-eye"></i>
                        </button>
                    </td>
                </tr>
            `;
        });
    } catch (error) {
        console.error('Error loading history:', error);
    }
}

function viewPredictionDetails(predictionId) {
    // Could open a modal or navigate to details
    alert('Prediction details view coming soon!');
}

// Compare Scenarios
const compareBtnElement = document.getElementById('compare-btn');
if (compareBtnElement) {
    compareBtnElement.addEventListener('click', async () => {
        const scenarioCards = document.querySelectorAll('.scenario-card');
        const scenarios = [];

        scenarioCards.forEach((card, index) => {
            const nameInput = card.querySelector('.scenario-name');
            const data = {
                name: nameInput?.value || `Scenario ${index + 1}`,
                project_type: card.querySelector('[name="project_type"]').value,
                total_area_sqft: parseFloat(card.querySelector('[name="total_area_sqft"]').value),
                num_workers: parseInt(card.querySelector('[name="num_workers"]').value),
                planned_duration_days: parseInt(card.querySelector('[name="planned_duration_days"]').value),
                complexity_level: card.querySelector('[name="complexity_level"]').value,
                material_quality: card.querySelector('[name="material_quality"]').value
            };
            scenarios.push(data);
        });

        try {
            const response = await fetch(`${API_BASE}/predictions/compare`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ scenarios })
            });

            if (!response.ok) throw new Error('Comparison failed');

            const result = await response.json();
            displayComparisonResult(result);
        } catch (error) {
            console.error('Error:', error);
            alert('Failed to compare scenarios. Please try again.');
        }
    });
}

function displayComparisonResult(result) {
    const comparisonResult = document.getElementById('comparison-result');
    comparisonResult.classList.remove('hidden');

    // Summary
    const summary = document.getElementById('comparison-summary');
    summary.innerHTML = `
        <div class="summary-item">
            <div class="label">Lowest Cost</div>
            <div class="value">${result.summary.lowest_cost_scenario}</div>
        </div>
        <div class="summary-item">
            <div class="label">Lowest Delay</div>
            <div class="value">${result.summary.lowest_delay_scenario}</div>
        </div>
        <div class="summary-item">
            <div class="label">Lowest Risk</div>
            <div class="value">${result.summary.lowest_risk_scenario}</div>
        </div>
        <div class="summary-item">
            <div class="label">Cost Range</div>
            <div class="value">${formatCurrencyShort(result.summary.cost_range.min)} - ${formatCurrencyShort(result.summary.cost_range.max)}</div>
        </div>
    `;

    // Comparison Charts
    const costCtx = document.getElementById('comparisonCostChart')?.getContext('2d');
    if (costCtx) {
        if (chartInstances.comparisonCost) chartInstances.comparisonCost.destroy();
        chartInstances.comparisonCost = new Chart(costCtx, {
            type: 'bar',
            data: {
                labels: result.scenarios.map(s => s.scenario_name),
                datasets: [{
                    label: 'Predicted Cost',
                    data: result.scenarios.map(s => s.predicted_cost),
                    backgroundColor: result.scenarios.map((s, i) =>
                        s.predicted_cost === result.summary.cost_range.min ? '#4CAF50' : '#2196F3'
                    )
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    title: {
                        display: true,
                        text: 'Cost Comparison'
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        ticks: {
                            callback: value => formatCurrencyShort(value)
                        }
                    }
                }
            }
        });
    }

    const riskCtx = document.getElementById('comparisonRiskChart')?.getContext('2d');
    if (riskCtx) {
        if (chartInstances.comparisonRisk) chartInstances.comparisonRisk.destroy();
        chartInstances.comparisonRisk = new Chart(riskCtx, {
            type: 'bar',
            data: {
                labels: result.scenarios.map(s => s.scenario_name),
                datasets: [{
                    label: 'Risk Score',
                    data: result.scenarios.map(s => s.risk_score),
                    backgroundColor: result.scenarios.map(s =>
                        s.risk_score < 40 ? '#4CAF50' : s.risk_score < 70 ? '#FFC107' : '#F44336'
                    )
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    title: {
                        display: true,
                        text: 'Risk Comparison'
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        max: 100
                    }
                }
            }
        });
    }

    // Details
    const details = document.getElementById('comparison-details');
    const lowestCost = Math.min(...result.scenarios.map(s => s.predicted_cost));
    const lowestDelay = Math.min(...result.scenarios.map(s => s.predicted_delay_days));
    const lowestRisk = Math.min(...result.scenarios.map(s => s.risk_score));

    details.innerHTML = result.scenarios.map(scenario => {
        const isBestCost = scenario.predicted_cost === lowestCost;
        const isBestDelay = scenario.predicted_delay_days === lowestDelay;
        const isBestRisk = scenario.risk_score === lowestRisk;

        return `
            <div class="scenario-result">
                <h4><i class="fas fa-file-alt"></i> ${scenario.scenario_name}</h4>
                <div class="metric">
                    <span class="label">Predicted Cost</span>
                    <span class="value ${isBestCost ? 'best' : ''}">${formatCurrency(scenario.predicted_cost)} ${isBestCost ? '✓' : ''}</span>
                </div>
                <div class="metric">
                    <span class="label">Predicted Delay</span>
                    <span class="value ${isBestDelay ? 'best' : ''}">${scenario.predicted_delay_days} days ${isBestDelay ? '✓' : ''}</span>
                </div>
                <div class="metric">
                    <span class="label">Delay Probability</span>
                    <span class="value">${(scenario.delay_probability * 100).toFixed(1)}%</span>
                </div>
                <div class="metric">
                    <span class="label">Risk Score</span>
                    <span class="value ${isBestRisk ? 'best' : ''}">${scenario.risk_score.toFixed(0)} ${isBestRisk ? '✓' : ''}</span>
                </div>
            </div>
        `;
    }).join('');

    // AI Recommendation
    const recommendation = document.getElementById('comparison-ai-recommendation');
    const bestOverall = result.scenarios.reduce((best, current) => {
        const bestScore = best.predicted_cost / 1000000 + best.risk_score + best.predicted_delay_days;
        const currentScore = current.predicted_cost / 1000000 + current.risk_score + current.predicted_delay_days;
        return currentScore < bestScore ? current : best;
    });
    recommendation.textContent = `Based on a balanced analysis of cost, risk, and timeline, "${bestOverall.scenario_name}" offers the best overall value proposition. ` +
        `It provides a good balance between project cost (${formatCurrency(bestOverall.predicted_cost)}) and risk management (score: ${bestOverall.risk_score.toFixed(0)}).`;

    comparisonResult.scrollIntoView({ behavior: 'smooth' });
}

// Add Scenario
const addScenarioBtn = document.getElementById('add-scenario-btn');
if (addScenarioBtn) {
    addScenarioBtn.addEventListener('click', () => {
        const container = document.getElementById('scenarios-container');
        const scenarioCount = container.querySelectorAll('.scenario-card').length;

        const newCard = document.createElement('div');
        newCard.className = 'scenario-card';
        newCard.dataset.scenario = scenarioCount;
        newCard.innerHTML = `
            <div class="scenario-header">
                <h3><i class="fas fa-file-alt"></i> Scenario ${scenarioCount + 1}</h3>
                <input type="text" class="scenario-name" placeholder="Name this scenario" value="Scenario ${scenarioCount + 1}">
                <button class="remove-scenario-btn" onclick="removeScenario(${scenarioCount})"><i class="fas fa-times"></i></button>
            </div>
            <div class="form-grid">
                <div class="form-group">
                    <label>Project Type</label>
                    <select name="project_type">
                        <option value="residential">Residential</option>
                        <option value="commercial" selected>Commercial</option>
                        <option value="industrial">Industrial</option>
                        <option value="infrastructure">Infrastructure</option>
                    </select>
                </div>
                <div class="form-group">
                    <label>Area (sqft)</label>
                    <input type="number" name="total_area_sqft" value="10000" min="100">
                </div>
                <div class="form-group">
                    <label>Workers</label>
                    <input type="number" name="num_workers" value="20" min="1">
                </div>
                <div class="form-group">
                    <label>Duration (days)</label>
                    <input type="number" name="planned_duration_days" value="180" min="1">
                </div>
                <div class="form-group">
                    <label>Complexity</label>
                    <select name="complexity_level">
                        <option value="low">Low</option>
                        <option value="medium" selected>Medium</option>
                        <option value="high">High</option>
                    </select>
                </div>
                <div class="form-group">
                    <label>Material Quality</label>
                    <select name="material_quality">
                        <option value="economy">Economy</option>
                        <option value="standard" selected>Standard</option>
                        <option value="premium">Premium</option>
                    </select>
                </div>
            </div>
        `;

        container.appendChild(newCard);
    });
}

function removeScenario(index) {
    const container = document.getElementById('scenarios-container');
    const cards = container.querySelectorAll('.scenario-card');
    if (cards.length > 2) {
        cards[index]?.remove();
    } else {
        alert('At least 2 scenarios are required for comparison.');
    }
}

function resetScenarios() {
    location.reload();
}

// Analytics
async function loadAnalytics() {
    try {
        const [statsResponse, historyResponse] = await Promise.all([
            fetch(`${API_BASE}/projects/stats`),
            fetch(`${API_BASE}/predictions/history`)
        ]);

        const stats = await statsResponse.json();
        const predictions = await historyResponse.json();

        // Update metrics
        if (predictions.length > 0) {
            const avgCostPerSqft = predictions.reduce((sum, p) => {
                const area = p.input_data?.total_area_sqft || 1;
                return sum + (p.predicted_cost / area);
            }, 0) / predictions.length;

            const avgDelay = predictions.reduce((sum, p) => sum + p.predicted_delay_days, 0) / predictions.length;
            const highRiskCount = predictions.filter(p => p.risk_score >= 70).length;

            document.getElementById('avg-cost-sqft').textContent = formatCurrency(avgCostPerSqft);
            document.getElementById('avg-delay').textContent = `${avgDelay.toFixed(1)} days`;
            document.getElementById('high-risk-count').textContent = highRiskCount;

            const distribution = stats.project_type_distribution || {};
            const mostCommon = Object.entries(distribution).reduce((a, b) => a[1] > b[1] ? a : b, ['', 0]);
            document.getElementById('common-type').textContent = mostCommon[0] ? mostCommon[0].charAt(0).toUpperCase() + mostCommon[0].slice(1) : '-';
        }

        // Initialize analytics charts
        initAnalyticsCharts(stats, predictions);

    } catch (error) {
        console.error('Error loading analytics:', error);
    }
}

function initAnalyticsCharts(stats, predictions) {
    // Cost by Type Chart
    const costByTypeCtx = document.getElementById('costByTypeChart')?.getContext('2d');
    if (costByTypeCtx && predictions.length > 0) {
        if (chartInstances.costByType) chartInstances.costByType.destroy();

        const typeData = {};
        predictions.forEach(p => {
            const type = p.input_data?.project_type || 'unknown';
            if (!typeData[type]) typeData[type] = [];
            typeData[type].push(p.predicted_cost);
        });

        const types = Object.keys(typeData);
        const avgCosts = types.map(t => typeData[t].reduce((a, b) => a + b, 0) / typeData[t].length);

        chartInstances.costByType = new Chart(costByTypeCtx, {
            type: 'bar',
            data: {
                labels: types.map(t => t.charAt(0).toUpperCase() + t.slice(1)),
                datasets: [{
                    label: 'Average Cost',
                    data: avgCosts,
                    backgroundColor: ['#4CAF50', '#2196F3', '#FF9800', '#9C27B0']
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: {
                        beginAtZero: true,
                        ticks: {
                            callback: value => formatCurrencyShort(value)
                        }
                    }
                }
            }
        });
    }

    // Delay Patterns Chart
    const delayCtx = document.getElementById('delayPatternsChart')?.getContext('2d');
    if (delayCtx && predictions.length > 0) {
        if (chartInstances.delayPatterns) chartInstances.delayPatterns.destroy();

        chartInstances.delayPatterns = new Chart(delayCtx, {
            type: 'scatter',
            data: {
                datasets: [{
                    label: 'Delay vs Risk',
                    data: predictions.map(p => ({
                        x: p.risk_score,
                        y: p.predicted_delay_days
                    })),
                    backgroundColor: 'rgba(30, 58, 95, 0.6)'
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    x: { title: { display: true, text: 'Risk Score' } },
                    y: { title: { display: true, text: 'Delay (days)' } }
                }
            }
        });
    }

    // Cost Distribution Chart
    const costDistCtx = document.getElementById('costDistributionChart')?.getContext('2d');
    if (costDistCtx && predictions.length > 0) {
        if (chartInstances.costDist) chartInstances.costDist.destroy();

        const costs = predictions.map(p => p.predicted_cost);
        const ranges = ['< 10L', '10-50L', '50L-1Cr', '1-5Cr', '> 5Cr'];
        const rangeCounts = [
            costs.filter(c => c < 1000000).length,
            costs.filter(c => c >= 1000000 && c < 5000000).length,
            costs.filter(c => c >= 5000000 && c < 10000000).length,
            costs.filter(c => c >= 10000000 && c < 50000000).length,
            costs.filter(c => c >= 50000000).length
        ];

        chartInstances.costDist = new Chart(costDistCtx, {
            type: 'bar',
            data: {
                labels: ranges,
                datasets: [{
                    label: 'Number of Projects',
                    data: rangeCounts,
                    backgroundColor: '#1e3a5f'
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false
            }
        });
    }

    // Risk Trends Chart
    const riskTrendCtx = document.getElementById('riskTrendsChart')?.getContext('2d');
    if (riskTrendCtx && predictions.length > 0) {
        if (chartInstances.riskTrends) chartInstances.riskTrends.destroy();

        const recentPreds = predictions.slice(0, 20).reverse();
        chartInstances.riskTrends = new Chart(riskTrendCtx, {
            type: 'line',
            data: {
                labels: recentPreds.map((_, i) => i + 1),
                datasets: [{
                    label: 'Risk Score',
                    data: recentPreds.map(p => p.risk_score),
                    borderColor: '#e91e63',
                    backgroundColor: 'rgba(233, 30, 99, 0.1)',
                    fill: true,
                    tension: 0.4
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: { beginAtZero: true, max: 100 }
                }
            }
        });
    }
}

// Export Functions
function exportToPDF() {
    if (!window.lastPredictionResult || !window.lastPredictionResult.prediction_id) {
        alert('No prediction data to export. Please make a prediction first.');
        return;
    }

    // Show the branding modal
    const modal = document.getElementById('pdf-branding-modal');
    if (modal) {
        modal.classList.remove('hidden');
    }
}

function closePdfBrandingModal() {
    const modal = document.getElementById('pdf-branding-modal');
    if (modal) {
        modal.classList.add('hidden');
    }
}

function generatePdfReport() {
    if (!window.lastPredictionResult || !window.lastPredictionResult.prediction_id) {
        alert('No prediction data available.');
        closePdfBrandingModal();
        return;
    }

    const predictionId = window.lastPredictionResult.prediction_id;
    const companyName = document.getElementById('pdf-company-name')?.value || '';
    const contactInfo = document.getElementById('pdf-contact-info')?.value || '';

    // Build URL with query parameters
    let url = `${API_BASE}/predictions/${predictionId}/export/pdf`;
    const params = new URLSearchParams();
    if (companyName) params.append('company_name', companyName);
    if (contactInfo) params.append('contact_info', contactInfo);

    if (params.toString()) {
        url += '?' + params.toString();
    }

    // Show loading state
    const generateBtn = document.getElementById('pdf-generate-btn');
    if (generateBtn) {
        generateBtn.disabled = true;
        generateBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Generating...';
    }

    // Fetch PDF and trigger download
    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to generate PDF');
            }
            return response.blob();
        })
        .then(blob => {
            const downloadUrl = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = downloadUrl;
            a.download = `cost_estimate_report_${predictionId}.pdf`;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            window.URL.revokeObjectURL(downloadUrl);

            // Close modal and reset button
            closePdfBrandingModal();
        })
        .catch(error => {
            console.error('Error generating PDF:', error);
            alert('Failed to generate PDF report. Please try again.');
        })
        .finally(() => {
            // Reset button state
            if (generateBtn) {
                generateBtn.disabled = false;
                generateBtn.innerHTML = '<i class="fas fa-file-pdf"></i> Generate PDF';
            }
        });
}

function exportToExcel() {
    if (!window.lastPredictionResult) {
        alert('No prediction data to export.');
        return;
    }

    const result = window.lastPredictionResult;
    const csvContent = [
        ['Construction Cost Prediction Report'],
        [''],
        ['Project Name', result.project_name || 'N/A'],
        ['Project Type', result.project_type],
        [''],
        ['Predictions'],
        ['Total Cost', result.predicted_cost],
        ['Cost Lower Bound', result.cost_lower_bound],
        ['Cost Upper Bound', result.cost_upper_bound],
        ['Predicted Delay (days)', result.predicted_delay_days],
        ['Delay Probability', result.delay_probability * 100 + '%'],
        ['Risk Score', result.risk_score],
        [''],
        ['Generated on', new Date().toLocaleString()]
    ].map(row => row.join(',')).join('\n');

    const blob = new Blob([csvContent], { type: 'text/csv' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `prediction_${new Date().toISOString().split('T')[0]}.csv`;
    a.click();
}

function printResult() {
    window.print();
}

// AI Cost Optimizer Functions
function runCostOptimizer() {
    if (!window.lastPredictionResult || !window.lastPredictionResult.prediction_id) {
        alert('No prediction data available. Please make a prediction first.');
        return;
    }

    const predictionId = window.lastPredictionResult.prediction_id;

    // Show loading state
    const loadingEl = document.getElementById('optimizer-loading');
    const resultsEl = document.getElementById('optimizer-results');
    const runBtn = document.getElementById('run-optimizer-btn');

    if (loadingEl) loadingEl.classList.remove('hidden');
    if (resultsEl) resultsEl.classList.add('hidden');
    if (runBtn) {
        runBtn.disabled = true;
        runBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Analyzing...';
    }

    // Call the optimizer API
    fetch(`${API_BASE}/predictions/${predictionId}/optimize`)
        .then(response => {
            if (!response.ok) throw new Error('Optimization failed');
            return response.json();
        })
        .then(data => {
            displayOptimizerResults(data);
        })
        .catch(error => {
            console.error('Optimizer error:', error);
            alert('Failed to analyze optimizations. Please try again.');
        })
        .finally(() => {
            if (loadingEl) loadingEl.classList.add('hidden');
            if (runBtn) {
                runBtn.disabled = false;
                runBtn.innerHTML = '<i class="fas fa-bolt"></i> Analyze & Optimize';
            }
        });
}

function displayOptimizerResults(data) {
    const resultsEl = document.getElementById('optimizer-results');
    if (!resultsEl) return;

    // Update summary values
    document.getElementById('optimizer-original-cost').textContent = formatCurrency(data.original_cost);
    document.getElementById('optimizer-optimized-cost').textContent = formatCurrency(data.optimized_cost);
    document.getElementById('optimizer-total-savings').textContent = formatCurrency(data.total_savings);
    document.getElementById('optimizer-savings-percent').textContent = `(${data.total_savings_percent}%)`;

    // Update summary text
    const summaryText = document.getElementById('optimizer-summary-text');
    if (summaryText) {
        summaryText.innerHTML = `<i class="fas fa-info-circle"></i> ${data.summary}`;
    }

    // Display optimization suggestions
    const suggestionsEl = document.getElementById('optimizer-suggestions');
    if (suggestionsEl && data.optimizations) {
        suggestionsEl.innerHTML = data.optimizations.map((opt, index) => `
            <div class="optimization-card" data-id="${opt.id}">
                <div class="opt-header">
                    <label class="opt-checkbox">
                        <input type="checkbox" checked data-savings="${opt.savings_amount}">
                        <span class="checkmark"></span>
                    </label>
                    <div class="opt-category ${opt.category}">
                        <i class="fas ${getCategoryIcon(opt.category)}"></i>
                        ${opt.category.charAt(0).toUpperCase() + opt.category.slice(1)}
                    </div>
                    <div class="opt-impact impact-${opt.impact}">${opt.impact.toUpperCase()}</div>
                </div>
                <div class="opt-content">
                    <h4 class="opt-title">${opt.title}</h4>
                    <p class="opt-description">${opt.description}</p>
                    <div class="opt-trade-off">
                        <i class="fas fa-exclamation-circle"></i>
                        <span>Trade-off: ${opt.trade_off}</span>
                    </div>
                </div>
                <div class="opt-savings">
                    <span class="savings-label">Potential Savings</span>
                    <span class="savings-value">${formatCurrency(opt.savings_amount)}</span>
                    <span class="savings-percent">(${opt.savings_percent}%)</span>
                </div>
            </div>
        `).join('');

        // Add event listeners for checkboxes
        suggestionsEl.querySelectorAll('input[type="checkbox"]').forEach(checkbox => {
            checkbox.addEventListener('change', updateSelectedSavings);
        });
    }

    // Show results
    resultsEl.classList.remove('hidden');

    // Scroll to optimizer section
    document.getElementById('ai-optimizer-section')?.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

function getCategoryIcon(category) {
    const icons = {
        'material': 'fa-cubes',
        'labor': 'fa-users',
        'scheduling': 'fa-calendar-alt',
        'design': 'fa-drafting-compass',
        'procurement': 'fa-shopping-cart'
    };
    return icons[category] || 'fa-lightbulb';
}

function updateSelectedSavings() {
    const checkboxes = document.querySelectorAll('#optimizer-suggestions input[type="checkbox"]');
    let totalSelected = 0;

    checkboxes.forEach(cb => {
        if (cb.checked) {
            totalSelected += parseFloat(cb.dataset.savings) || 0;
        }
    });

    const originalCost = window.lastPredictionResult?.predicted_cost || 0;
    const optimizedCost = originalCost - totalSelected;
    const savingsPercent = originalCost > 0 ? (totalSelected / originalCost * 100).toFixed(1) : 0;

    document.getElementById('optimizer-optimized-cost').textContent = formatCurrency(optimizedCost);
    document.getElementById('optimizer-total-savings').textContent = formatCurrency(totalSelected);
    document.getElementById('optimizer-savings-percent').textContent = `(${savingsPercent}%)`;
}

function hideOptimizer() {
    const resultsEl = document.getElementById('optimizer-results');
    if (resultsEl) resultsEl.classList.add('hidden');
}

function applyOptimizations() {
    const checkboxes = document.querySelectorAll('#optimizer-suggestions input[type="checkbox"]:checked');
    const selectedOptimizations = [];

    checkboxes.forEach(cb => {
        const card = cb.closest('.optimization-card');
        if (card) {
            selectedOptimizations.push(card.dataset.id);
        }
    });

    if (selectedOptimizations.length === 0) {
        alert('Please select at least one optimization to apply.');
        return;
    }

    // Update the displayed cost with optimized value
    const optimizedCost = document.getElementById('optimizer-optimized-cost').textContent;
    const predictedCostEl = document.getElementById('predicted-cost');
    if (predictedCostEl) {
        predictedCostEl.innerHTML = `${optimizedCost} <span class="optimized-badge">Optimized</span>`;
    }

    // Show success message
    alert(`${selectedOptimizations.length} optimization(s) applied! The estimated cost has been updated.`);

    // Hide the optimizer results
    hideOptimizer();
}

function saveAsProject() {
    if (!window.lastPredictionResult) {
        alert('No prediction data to save.');
        return;
    }
    switchToTab('projects');
    document.getElementById('new-project-btn').click();
}

function exportHistory() {
    alert('Exporting history to CSV...');
    fetch(`${API_BASE}/predictions/history`)
        .then(r => r.json())
        .then(predictions => {
            const csvContent = [
                ['Date', 'Project Type', 'Area', 'Cost', 'Delay', 'Risk Score'],
                ...predictions.map(p => [
                    new Date(p.created_at).toLocaleDateString(),
                    p.input_data?.project_type || 'N/A',
                    p.input_data?.total_area_sqft || 0,
                    p.predicted_cost,
                    p.predicted_delay_days,
                    p.risk_score
                ])
            ].map(row => row.join(',')).join('\n');

            const blob = new Blob([csvContent], { type: 'text/csv' });
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = `prediction_history_${new Date().toISOString().split('T')[0]}.csv`;
            a.click();
        });
}

function clearHistory() {
    alert('Clear history feature requires backend implementation.');
}

function exportAllData() {
    exportHistory();
}

function applyHistoryFilters() {
    alert('Filtering feature coming soon!');
}

// =====================================================
// LIVE MATERIAL RATES FUNCTIONALITY
// =====================================================

let currentRatesData = null;
let ratesTrendCharts = {};
let isLoadingRates = false;

// Load rates for selected region - NOW USING LIVE PRICES API
async function loadRatesForRegion(forceRefresh = false) {
    if (isLoadingRates) return;

    const region = document.getElementById('rate-region')?.value || 'west';
    const refreshBtn = document.getElementById('refresh-rates-btn');
    const liveIndicator = document.getElementById('live-indicator');

    // Show loading state
    isLoadingRates = true;
    if (refreshBtn) {
        refreshBtn.disabled = true;
        refreshBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Fetching...';
    }
    if (liveIndicator) {
        liveIndicator.classList.add('loading');
    }

    try {
        // Use live prices API
        const response = await fetch(`${API_BASE}/rates/live?region=${region}&refresh=${forceRefresh}`);
        const data = await response.json();

        if (data.success) {
            currentRatesData = data;
            updateLiveRatesDisplay(data);
            updateLiveMaterialsTable(data);
            updateLaborTableFromLive(data);
            updateLivePriceAlerts();

            // Update live indicator
            if (liveIndicator) {
                liveIndicator.classList.remove('loading');
                liveIndicator.classList.add('live');
                liveIndicator.title = data.from_cache ? 'Cached data' : 'Live data';
            }

            // Update last updated time
            const lastUpdated = document.getElementById('rates-last-updated');
            if (lastUpdated && data.last_updated) {
                const updateTime = new Date(data.last_updated);
                const now = new Date();
                const diffMinutes = Math.round((now - updateTime) / 60000);

                if (diffMinutes < 1) {
                    lastUpdated.textContent = 'Just now';
                } else if (diffMinutes < 60) {
                    lastUpdated.textContent = `${diffMinutes} min ago`;
                } else {
                    lastUpdated.textContent = updateTime.toLocaleTimeString();
                }
            }

            // Initialize trend charts
            initRatesTrendCharts(region);
        } else {
            // Fallback to static rates
            const fallbackResponse = await fetch(`${API_BASE}/rates/summary?region=${region}`);
            const fallbackData = await fallbackResponse.json();
            currentRatesData = fallbackData;
            updateRatesDisplay(fallbackData);
            updateMaterialsTable(fallbackData);
            updateLaborTable(fallbackData);

            if (liveIndicator) {
                liveIndicator.classList.remove('loading', 'live');
            }
        }

    } catch (error) {
        console.error('Error loading live rates:', error);
        // Fallback to static rates
        try {
            const fallbackResponse = await fetch(`${API_BASE}/rates/summary?region=${region}`);
            const fallbackData = await fallbackResponse.json();
            currentRatesData = fallbackData;
            updateRatesDisplay(fallbackData);
            updateMaterialsTable(fallbackData);
            updateLaborTable(fallbackData);
        } catch (e) {
            console.error('Fallback also failed:', e);
        }
    } finally {
        isLoadingRates = false;
        if (refreshBtn) {
            refreshBtn.disabled = false;
            refreshBtn.innerHTML = '<i class="fas fa-sync-alt"></i> Refresh';
        }
    }
}

// Force refresh live prices
function refreshLivePrices() {
    loadRatesForRegion(true);
}

// Update display with live prices data
function updateLiveRatesDisplay(data) {
    // Last updated
    const lastUpdated = document.getElementById('rates-last-updated');
    if (lastUpdated && data.last_updated) {
        const time = new Date(data.last_updated);
        lastUpdated.textContent = time.toLocaleTimeString();
    }

    // Cement
    const cement = data.materials?.cement_opc_43;
    if (cement) {
        document.getElementById('cement-rate').textContent = `Rs. ${cement.price}`;
        updateLiveTrendDisplay('cement-trend', cement.trend, cement.change_percent);
    }

    // Steel
    const steel = data.materials?.steel_tmt_fe500;
    if (steel) {
        document.getElementById('steel-rate').textContent = `Rs. ${steel.price}`;
        updateLiveTrendDisplay('steel-trend', steel.trend, steel.change_percent);
    }

    // Sand
    const sand = data.materials?.river_sand;
    if (sand) {
        document.getElementById('sand-rate').textContent = `Rs. ${sand.price.toLocaleString('en-IN')}`;
        updateLiveTrendDisplay('sand-trend', sand.trend, sand.change_percent);
    }

    // Aggregate
    const aggregate = data.materials?.aggregate_20mm;
    if (aggregate) {
        document.getElementById('aggregate-rate').textContent = `Rs. ${aggregate.price.toLocaleString('en-IN')}`;
        updateLiveTrendDisplay('aggregate-trend', aggregate.trend, aggregate.change_percent);
    }

    // Bricks
    const brick = data.materials?.brick_first_class;
    if (brick) {
        document.getElementById('brick-rate').textContent = `Rs. ${brick.price.toLocaleString('en-IN')}`;
        updateLiveTrendDisplay('brick-trend', brick.trend, brick.change_percent);
    }

    // Mason (from labor data if available)
    const mason = data.labor?.mason;
    if (mason) {
        document.getElementById('mason-rate').textContent = `Rs. ${mason.rate || mason.price}`;
        updateLiveTrendDisplay('mason-trend', mason.trend, mason.change_percent);
    }

    // Update brand rates if available
    if (data.brands) {
        updateBrandRates(data.brands);
    }
}

// Update trend display for live data
function updateLiveTrendDisplay(elementId, trend, changePercent) {
    const element = document.getElementById(elementId);
    if (!element) return;

    let icon, text, className;
    if (trend === 'up') {
        icon = 'fa-arrow-up';
        text = `+${Math.abs(changePercent).toFixed(1)}%`;
        className = 'trend-up';
    } else if (trend === 'down') {
        icon = 'fa-arrow-down';
        text = `${changePercent.toFixed(1)}%`;
        className = 'trend-down';
    } else {
        icon = 'fa-minus';
        text = 'Stable';
        className = 'trend-stable';
    }

    element.innerHTML = `<i class="fas ${icon}"></i> <span>${text}</span>`;
    element.className = `rate-trend ${className}`;
}

// Update brand rates display
function updateBrandRates(brands) {
    // Update cement brand rates in card footer
    if (brands.cement) {
        const cementCard = document.querySelector('.rate-card.cement .brand-rates small');
        if (cementCard) {
            const brandText = Object.entries(brands.cement)
                .filter(([brand]) => brand !== 'Average')
                .slice(0, 3)
                .map(([brand, price]) => `${brand}: Rs.${price}`)
                .join(' | ');
            cementCard.textContent = brandText;
        }
    }

    // Update steel brand rates
    if (brands.steel) {
        const steelCard = document.querySelector('.rate-card.steel .brand-rates small');
        if (steelCard) {
            const brandText = Object.entries(brands.steel)
                .filter(([brand]) => brand !== 'Average')
                .slice(0, 3)
                .map(([brand, price]) => `${brand}: Rs.${price}`)
                .join(' | ');
            steelCard.textContent = brandText;
        }
    }
}

// Update materials table with live data
function updateLiveMaterialsTable(data) {
    const tbody = document.getElementById('materials-tbody');
    if (!tbody) return;

    tbody.innerHTML = '';

    Object.entries(data.materials || {}).forEach(([id, material]) => {
        const trendIcon = material.trend === 'up' ? 'fa-arrow-up trend-up' :
                         material.trend === 'down' ? 'fa-arrow-down trend-down' : 'fa-minus trend-stable';

        const changeClass = material.change_percent > 0 ? 'positive' :
                           material.change_percent < 0 ? 'negative' : '';

        const row = document.createElement('tr');
        row.dataset.category = material.category;
        row.dataset.name = material.name.toLowerCase();
        row.innerHTML = `
            <td>
                <strong>${material.name}</strong>
                <span class="source-badge" title="Source: ${material.source}">${material.source}</span>
            </td>
            <td><span class="category-badge ${material.category}">${material.category}</span></td>
            <td>${material.unit}</td>
            <td class="rate-value">Rs. ${material.price.toLocaleString('en-IN')}</td>
            <td><i class="fas ${trendIcon}"></i></td>
            <td class="${changeClass}">${material.change_percent > 0 ? '+' : ''}${material.change_percent.toFixed(1)}%</td>
            <td><button class="btn btn-sm btn-secondary" onclick="openUpdateModal('${id}', '${material.name}', ${material.price})"><i class="fas fa-edit"></i></button></td>
        `;
        tbody.appendChild(row);
    });
}

// Update labor table with live data
function updateLaborTableFromLive(data) {
    // Use static labor rates since live API focuses on materials
    // Fetch static labor rates
    fetch(`${API_BASE}/rates/labor`)
        .then(r => r.json())
        .then(laborData => {
            updateLaborTable({ labor: laborData });
        })
        .catch(() => {});
}

// Update live price alerts
function updateLivePriceAlerts() {
    fetch(`${API_BASE}/rates/live/alerts?threshold=3`)
        .then(r => r.json())
        .then(data => {
            const alertsList = document.getElementById('alerts-list');
            const alertBadge = document.getElementById('rates-alert-badge');
            const alertCount = document.getElementById('alert-count');

            if (!alertsList) return;

            if (data.alerts && data.alerts.length > 0) {
                alertsList.innerHTML = data.alerts.map(alert => `
                    <div class="alert-item ${alert.alert_type}">
                        <div class="alert-icon">
                            <i class="fas ${alert.trend === 'up' ? 'fa-arrow-up' : 'fa-arrow-down'}"></i>
                        </div>
                        <div class="alert-content">
                            <strong>${alert.material_name || alert.material_id}</strong>
                            <span class="${alert.change_percent > 0 ? 'positive' : 'negative'}">
                                ${alert.change_percent > 0 ? '+' : ''}${alert.change_percent.toFixed(1)}%
                            </span>
                        </div>
                        <div class="alert-price">Rs. ${alert.current_price.toLocaleString('en-IN')}</div>
                    </div>
                `).join('');

                if (alertBadge) {
                    alertBadge.classList.remove('hidden');
                    alertBadge.textContent = data.count;
                }
                if (alertCount) {
                    alertCount.textContent = data.count;
                }
            } else {
                alertsList.innerHTML = '<div class="no-alerts">No significant price changes</div>';
                if (alertBadge) alertBadge.classList.add('hidden');
                if (alertCount) alertCount.textContent = '0';
            }
        })
        .catch(error => {
            console.error('Error loading price alerts:', error);
        });
}

// Update key rates display cards
function updateRatesDisplay(data) {
    // Last updated
    document.getElementById('rates-last-updated').textContent = data.last_updated || 'Today';

    // Cement
    const cement = data.materials?.cement_opc_43;
    if (cement) {
        document.getElementById('cement-rate').textContent = `Rs. ${cement.rate}`;
        updateTrendDisplay('cement-trend', cement.trend, cement.change_percent);
    }

    // Steel
    const steel = data.materials?.steel_tmt_fe500;
    if (steel) {
        document.getElementById('steel-rate').textContent = `Rs. ${steel.rate}`;
        updateTrendDisplay('steel-trend', steel.trend, steel.change_percent);
    }

    // Sand
    const sand = data.materials?.river_sand;
    if (sand) {
        document.getElementById('sand-rate').textContent = `Rs. ${sand.rate.toLocaleString('en-IN')}`;
        updateTrendDisplay('sand-trend', sand.trend, sand.change_percent);
    }

    // Aggregate
    const aggregate = data.materials?.aggregate_20mm;
    if (aggregate) {
        document.getElementById('aggregate-rate').textContent = `Rs. ${aggregate.rate.toLocaleString('en-IN')}`;
        updateTrendDisplay('aggregate-trend', aggregate.trend, aggregate.change_percent);
    }

    // Bricks
    const brick = data.materials?.brick_first_class;
    if (brick) {
        document.getElementById('brick-rate').textContent = `Rs. ${brick.rate.toLocaleString('en-IN')}`;
        updateTrendDisplay('brick-trend', brick.trend, brick.change_percent);
    }

    // Mason
    const mason = data.labor?.mason;
    if (mason) {
        document.getElementById('mason-rate').textContent = `Rs. ${mason.rate}`;
        updateTrendDisplay('mason-trend', mason.trend, mason.change_percent);
    }
}

// Update trend display
function updateTrendDisplay(elementId, trend, changePercent) {
    const element = document.getElementById(elementId);
    if (!element) return;

    let icon, text, className;
    if (trend === 'up') {
        icon = 'fa-arrow-up';
        text = `+${Math.abs(changePercent)}% this month`;
        className = 'trend-up';
    } else if (trend === 'down') {
        icon = 'fa-arrow-down';
        text = `${changePercent}% this month`;
        className = 'trend-down';
    } else {
        icon = 'fa-minus';
        text = 'Stable';
        className = 'trend-stable';
    }

    element.innerHTML = `<i class="fas ${icon}"></i> <span>${text}</span>`;
    element.className = `rate-trend ${className}`;
}

// Update materials table
function updateMaterialsTable(data) {
    const tbody = document.getElementById('materials-tbody');
    if (!tbody) return;

    tbody.innerHTML = '';

    Object.entries(data.materials || {}).forEach(([id, material]) => {
        const trendIcon = material.trend === 'up' ? 'fa-arrow-up trend-up' :
                         material.trend === 'down' ? 'fa-arrow-down trend-down' : 'fa-minus trend-stable';

        const row = document.createElement('tr');
        row.dataset.category = material.category;
        row.dataset.name = material.name.toLowerCase();
        row.innerHTML = `
            <td><strong>${material.name}</strong></td>
            <td><span class="category-badge ${material.category}">${material.category}</span></td>
            <td>${material.unit}</td>
            <td class="rate-value">Rs. ${material.rate.toLocaleString('en-IN')}</td>
            <td><i class="fas ${trendIcon}"></i></td>
            <td class="${material.change_percent > 0 ? 'positive' : material.change_percent < 0 ? 'negative' : ''}">${material.change_percent > 0 ? '+' : ''}${material.change_percent}%</td>
            <td><button class="btn btn-sm btn-secondary" onclick="openUpdateModal('${id}', '${material.name}', ${material.rate})"><i class="fas fa-edit"></i></button></td>
        `;
        tbody.appendChild(row);
    });
}

// Update labor table
function updateLaborTable(data) {
    const tbody = document.getElementById('labor-tbody');
    if (!tbody) return;

    tbody.innerHTML = '';

    const skillLevels = {
        'unskilled': 'Unskilled',
        'helper': 'Semi-skilled',
        'mason': 'Skilled',
        'carpenter': 'Skilled',
        'plumber': 'Skilled',
        'electrician': 'Skilled',
        'bar_bender': 'Skilled',
        'painter': 'Skilled',
        'welder': 'Highly Skilled'
    };

    Object.entries(data.labor || {}).forEach(([id, labor]) => {
        const trendIcon = labor.trend === 'up' ? 'fa-arrow-up trend-up' :
                         labor.trend === 'down' ? 'fa-arrow-down trend-down' : 'fa-minus trend-stable';

        const row = document.createElement('tr');
        row.innerHTML = `
            <td><strong>${labor.name}</strong></td>
            <td>${skillLevels[id] || 'Skilled'}</td>
            <td class="rate-value">Rs. ${labor.rate}/day</td>
            <td><i class="fas ${trendIcon}"></i></td>
            <td class="${labor.change_percent > 0 ? 'positive' : labor.change_percent < 0 ? 'negative' : ''}">${labor.change_percent > 0 ? '+' : ''}${labor.change_percent}%</td>
        `;
        tbody.appendChild(row);
    });
}

// Load price alerts
async function loadPriceAlerts() {
    try {
        const response = await fetch(`${API_BASE}/rates/alerts`);
        const alerts = await response.json();

        const alertsList = document.getElementById('alerts-list');
        const alertCount = document.getElementById('alert-count');
        const alertBadge = document.getElementById('rates-alert-badge');

        const unreadAlerts = alerts.filter(a => !a.read);
        alertCount.textContent = unreadAlerts.length;

        if (unreadAlerts.length > 0) {
            alertBadge?.classList.remove('hidden');
            alertBadge.textContent = unreadAlerts.length;
        } else {
            alertBadge?.classList.add('hidden');
        }

        if (alerts.length === 0) {
            alertsList.innerHTML = '<div class="no-alerts"><i class="fas fa-check-circle"></i> No price alerts at this time</div>';
            return;
        }

        alertsList.innerHTML = alerts.slice(0, 5).map(alert => `
            <div class="alert-item ${alert.read ? 'read' : 'unread'} ${alert.type}">
                <div class="alert-icon">
                    <i class="fas ${alert.type === 'price_increase' ? 'fa-arrow-up' : 'fa-arrow-down'}"></i>
                </div>
                <div class="alert-content">
                    <div class="alert-title">${alert.material_id.replace(/_/g, ' ').toUpperCase()}</div>
                    <div class="alert-message">
                        ${alert.type === 'price_increase' ? 'Price increased' : 'Price decreased'} by
                        <strong>${alert.change_percent}%</strong>
                        (Rs.${alert.old_rate} → Rs.${alert.new_rate})
                    </div>
                    <div class="alert-date">${alert.date}</div>
                </div>
                ${!alert.read ? `<button class="mark-read-btn" onclick="markAlertRead('${alert.id}')"><i class="fas fa-check"></i></button>` : ''}
            </div>
        `).join('');

    } catch (error) {
        console.error('Error loading alerts:', error);
    }
}

// Mark alert as read
async function markAlertRead(alertId) {
    try {
        await fetch(`${API_BASE}/rates/alerts/${alertId}/read`, { method: 'POST' });
        loadPriceAlerts();
    } catch (error) {
        console.error('Error marking alert read:', error);
    }
}

// Filter materials table
function filterMaterialsTable() {
    const category = document.getElementById('material-category-filter')?.value || 'all';
    const search = document.getElementById('material-search')?.value.toLowerCase() || '';

    const rows = document.querySelectorAll('#materials-tbody tr');
    rows.forEach(row => {
        const rowCategory = row.dataset.category;
        const rowName = row.dataset.name;

        const categoryMatch = category === 'all' || rowCategory === category;
        const searchMatch = !search || rowName.includes(search);

        row.style.display = categoryMatch && searchMatch ? '' : 'none';
    });
}

// Initialize trend charts
async function initRatesTrendCharts(region) {
    // Cement trend chart
    const cementCtx = document.getElementById('cementTrendChart')?.getContext('2d');
    if (cementCtx) {
        try {
            const response = await fetch(`${API_BASE}/rates/materials/cement_opc_43?region=${region}`);
            const data = await response.json();

            if (ratesTrendCharts.cement) ratesTrendCharts.cement.destroy();

            const history = data.history || [];
            ratesTrendCharts.cement = new Chart(cementCtx, {
                type: 'line',
                data: {
                    labels: history.map(h => h.date.substring(5)),
                    datasets: [{
                        label: 'Cement Price (Rs/bag)',
                        data: history.map(h => h.rate),
                        borderColor: '#FF6384',
                        backgroundColor: 'rgba(255, 99, 132, 0.1)',
                        fill: true,
                        tension: 0.4
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: { legend: { display: false } },
                    scales: { y: { beginAtZero: false } }
                }
            });
        } catch (error) {
            console.error('Error loading cement trend:', error);
        }
    }

    // Steel trend chart
    const steelCtx = document.getElementById('steelTrendChart')?.getContext('2d');
    if (steelCtx) {
        try {
            const response = await fetch(`${API_BASE}/rates/materials/steel_tmt_fe500?region=${region}`);
            const data = await response.json();

            if (ratesTrendCharts.steel) ratesTrendCharts.steel.destroy();

            const history = data.history || [];
            ratesTrendCharts.steel = new Chart(steelCtx, {
                type: 'line',
                data: {
                    labels: history.map(h => h.date.substring(5)),
                    datasets: [{
                        label: 'Steel Price (Rs/kg)',
                        data: history.map(h => h.rate),
                        borderColor: '#36A2EB',
                        backgroundColor: 'rgba(54, 162, 235, 0.1)',
                        fill: true,
                        tension: 0.4
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: { legend: { display: false } },
                    scales: { y: { beginAtZero: false } }
                }
            });
        } catch (error) {
            console.error('Error loading steel trend:', error);
        }
    }
}

// Update rate modal
let currentUpdateMaterial = null;

function openUpdateModal(materialId, materialName, currentRate) {
    currentUpdateMaterial = materialId;
    document.getElementById('update-material-name').textContent = materialName;
    document.getElementById('update-current-rate').textContent = `Rs. ${currentRate}`;
    document.getElementById('new-rate').value = currentRate;
    document.getElementById('update-rate-modal').classList.remove('hidden');
}

function closeUpdateModal() {
    document.getElementById('update-rate-modal').classList.add('hidden');
    currentUpdateMaterial = null;
}

async function saveNewRate() {
    if (!currentUpdateMaterial) return;

    const newRate = parseFloat(document.getElementById('new-rate').value);
    if (isNaN(newRate) || newRate <= 0) {
        alert('Please enter a valid rate');
        return;
    }

    try {
        const response = await fetch(`${API_BASE}/rates/materials/${currentUpdateMaterial}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ rate: newRate })
        });

        const result = await response.json();

        if (result.success) {
            closeUpdateModal();
            loadRatesForRegion();

            if (result.alert) {
                alert(`Price Alert: Rate changed by ${result.alert.change_percent}%`);
            }
        } else {
            alert('Failed to update rate');
        }
    } catch (error) {
        console.error('Error updating rate:', error);
        alert('Failed to update rate');
    }
}

// =====================================================
// CROWDSOURCED PRICE REPORTING
// =====================================================

function openReportPriceModal() {
    const modal = document.getElementById('report-price-modal');
    if (modal) {
        modal.style.display = 'flex';
        document.getElementById('report-price-form').style.display = 'block';
        document.getElementById('rp-success-msg').style.display = 'none';
        document.getElementById('report-price-form').reset();
    }
}

function closeReportPriceModal() {
    const modal = document.getElementById('report-price-modal');
    if (modal) {
        modal.style.display = 'none';
    }
}

async function submitPriceReport(event) {
    event.preventDefault();
    const btn = document.getElementById('rp-submit-btn');
    btn.disabled = true;
    btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Submitting...';

    const data = {
        material_category: document.getElementById('rp-category').value,
        material_name: document.getElementById('rp-name').value,
        price: parseFloat(document.getElementById('rp-price').value),
        city: document.getElementById('rp-city').value,
        brand: document.getElementById('rp-brand').value,
        reporter_type: document.getElementById('rp-reporter-type').value,
        reporter_name: document.getElementById('rp-reporter-name').value,
        notes: document.getElementById('rp-notes').value,
    };

    try {
        const response = await fetch(`${API_BASE}/rates/crowdsourced/report`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        const result = await response.json();

        if (result.success) {
            document.getElementById('report-price-form').style.display = 'none';
            document.getElementById('rp-success-msg').style.display = 'block';
            loadCrowdsourcedPrices();
        } else {
            alert('Error: ' + (result.error || 'Failed to submit'));
        }
    } catch (error) {
        alert('Network error. Please try again.');
    } finally {
        btn.disabled = false;
        btn.innerHTML = '<i class="fas fa-paper-plane"></i> Submit Price Report';
    }
}

async function loadCrowdsourcedPrices() {
    try {
        const [pricesRes, recentRes, statsRes] = await Promise.all([
            fetch(`${API_BASE}/rates/crowdsourced/prices`),
            fetch(`${API_BASE}/rates/crowdsourced/recent?limit=10`),
            fetch(`${API_BASE}/rates/crowdsourced/stats`)
        ]);

        const pricesData = await pricesRes.json();
        const recentData = await recentRes.json();
        const statsData = await statsRes.json();

        // Update total reports badge
        const totalBadge = document.getElementById('crowd-total-reports');
        if (totalBadge && statsData.success) {
            totalBadge.textContent = `${statsData.total_reports} reports | ${statsData.cities_covered} cities`;
        }

        // Update prices grid
        const grid = document.getElementById('crowdsourced-prices-grid');
        if (grid && pricesData.success && pricesData.materials.length > 0) {
            grid.innerHTML = pricesData.materials.map(m => `
                <div style="background:white; border-radius:10px; padding:14px; border:1px solid #e0e0e0; box-shadow:0 2px 4px rgba(0,0,0,0.05);">
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                        <strong style="color:#333; text-transform:capitalize;">${m.material_category}</strong>
                        <span style="font-size:12px; background:#e8f5e9; color:#2e7d32; padding:2px 8px; border-radius:10px;">${m.report_count} reports</span>
                    </div>
                    <div style="font-size:22px; font-weight:700; color:#155724;">Rs. ${m.avg_price.toLocaleString()}</div>
                    <div style="font-size:12px; color:#888; margin-top:2px;">${m.unit}</div>
                    <div style="font-size:12px; color:#666; margin-top:6px;">
                        Range: Rs.${m.min_price.toLocaleString()} - Rs.${m.max_price.toLocaleString()}
                    </div>
                    <div style="font-size:11px; color:#999; margin-top:4px;">
                        Cities: ${m.cities_covered.slice(0, 3).join(', ')}${m.cities_covered.length > 3 ? '...' : ''}
                    </div>
                </div>
            `).join('');
        } else if (grid) {
            grid.innerHTML = '<div style="text-align:center; padding:20px; color:#666; grid-column:1/-1;"><i class="fas fa-info-circle"></i> No community reports yet. Be the first to report local prices!</div>';
        }

        // Update recent reports
        const recentList = document.getElementById('recent-reports-list');
        if (recentList && recentData.success && recentData.reports.length > 0) {
            recentList.innerHTML = recentData.reports.map(r => {
                const date = new Date(r.created_at);
                const timeAgo = getTimeAgo(date);
                return `
                    <div style="display:flex; justify-content:space-between; align-items:center; padding:8px 12px; border-bottom:1px solid #eee; font-size:13px;">
                        <div>
                            <strong>${r.material_name}</strong>
                            <span style="color:#666;"> - ${r.city}</span>
                            ${r.brand ? `<span style="color:#999;"> (${r.brand})</span>` : ''}
                        </div>
                        <div style="text-align:right;">
                            <strong style="color:#155724;">Rs. ${r.price.toLocaleString()}</strong>
                            <div style="font-size:11px; color:#999;">${timeAgo}</div>
                        </div>
                    </div>
                `;
            }).join('');
        } else if (recentList) {
            recentList.innerHTML = '<div style="text-align:center; padding:16px; color:#999; font-size:13px;">No reports yet</div>';
        }

    } catch (error) {
        console.error('Error loading crowdsourced prices:', error);
    }
}

function getTimeAgo(date) {
    const now = new Date();
    const diffMs = now - date;
    const diffMins = Math.floor(diffMs / 60000);
    const diffHours = Math.floor(diffMs / 3600000);
    const diffDays = Math.floor(diffMs / 86400000);

    if (diffMins < 1) return 'Just now';
    if (diffMins < 60) return `${diffMins}m ago`;
    if (diffHours < 24) return `${diffHours}h ago`;
    if (diffDays < 7) return `${diffDays}d ago`;
    return date.toLocaleDateString();
}

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    // Load dashboard on start
    loadDashboard();

    // Load rates when tab is clicked
    const ratesTab = document.querySelector('[data-tab="live-rates"]');
    if (ratesTab) {
        ratesTab.addEventListener('click', () => {
            setTimeout(() => {
                loadRatesForRegion();
                loadCrowdsourcedPrices();
            }, 100);
        });
    }

    // Close modal on outside click
    const modal = document.getElementById('report-price-modal');
    if (modal) {
        modal.addEventListener('click', (e) => {
            if (e.target === modal) closeReportPriceModal();
        });
    }
});

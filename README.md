# Smart Analytics Dashboard for Police "Good Work Done" (PS-3)

AI-powered dashboard to analyze, visualize, and rank district-level police "Good Work" data from CCTNS.

This project is a high-performance, role-based web application designed for senior police officers (DGP, SP) to transform raw CCTNS "Good Work Done" module data into actionable intelligence. It automates data processing, provides AI-driven insights, and creates a data-driven system for performance evaluation and recognition, as specified in the official PS-3 Problem Statement.

---

## 1. The Problem

Based on the official CCTNS Problem Statement (PS-3), police districts manually record data for special drives (NBW, narcotics, firearms, etc.), convictions, and detections. This manual process is inefficient, prone to errors, and makes it difficult to:

- *Visualize Trends:* Performance data is trapped in static reports, making state-wide visualization impossible.
- *Identify Top Performers:* It is difficult to compare and rank districts on key "Good Work" metrics.
- *Recognize Good Work:* There is no efficient, transparent system for recognizing exceptional performance.
- *Handle Diverse Formats:* Data is submitted in a mix of manual forms, Excel sheets, CSVs, and PDFs, creating a data-entry bottleneck.

---

## 2. Our Solution: A Two-Stage Strategic Dashboard

A secure, role-based web application that provides a unique dashboard for each level of the police hierarchy.

### I. The "State View" (DGP Dashboard)

*For:* Director General of Police (DGP) — strategic oversight, trend analysis, and resource allocation.

*Key Features:*
- *AI-Generated Monthly Summary:* NLG-based summary identifying top districts for convictions, NBW execution, and narcotics seizures.
- *AI-Powered Performance Forecast:* ML model predicts potential underperforming districts next month.
- *Live Geo-Analytics Map:* Choropleth heatmap of Odisha visualizing metrics like conviction rate and narcotics seizures.
- *Gamified Leaderboards:* Dynamic bar charts ranking districts on "Special Drive" metrics.
- *Automated Report Generation:* One-click export to PDF/CSV for official use.

### II. The "District View" (SP Dashboard)

*For:* Superintendent of Police (SP) — operational management and data reporting.

*Key Features:*
- *AI-Powered Smart Upload:* Uploads PDF/Excel reports; backend AI extracts and pre-fills digital forms.
- *CCTNS "Good Work Done" Forms:* Complete digital interface for manual entry.
- *Report Submission & Export:* Submit to DGP or export to PDF/Excel/CSV.
- *District KPI Widgets:* Real-time charts for pendency, NBW funnel, and missing persons.

---

## 3. The AI/ML Innovation

| AI/ML Model | Feature | Role & Purpose |
|--------------|----------|----------------|
| *Natural Language Generation (NLG)* | AI Monthly Summary | AI as Analyst — synthesizes 7 tables into English summary. |
| *Machine Learning (Forecasting)* | AI Performance Forecast | AI as Strategist — predicts future underperforming districts. |
| *NLP / Regex Parsing* | Smart Report Upload | AI as Clerk — parses unstructured PDFs and extracts data. |

---

## 4. Tech Stack

| Layer | Technologies |
|--------|---------------|
| *Frontend (UI)* | React 18, React Leaflet, Recharts, Axios, jsPDF, jsPDF-AutoTable |
| *Backend (Server)* | Node.js, Express.js, JWT, Multer, fs, path |
| *AI/ML & Data* | pdf-parse, xlsx, csv-parser, JavaScript-based NLG & ML |

---

## 5. Getting Started

### Prerequisites
- Node.js (v18.x or higher)
- npm (v9.x or higher)

### Backend Setup
bash
cd backend
npm install
npm start

Server starts at http://localhost:8000.

### Frontend Setup
bash
cd frontend
npm install
npm start

App runs at http://localhost:5173.

---

## 6. Login Credentials

| Role | Username | Password |
|------|-----------|-----------|
| DGP (State) | dgp_odisha | dgp123 |
| SP (Khordha) | sp_khordha | sp123 |
| SP (Cuttack) | sp_cctack | sp123 |
| SP (Ganjam) | sp_ganjam | sp123 |

---

## 7. API Endpoints

### Authentication
| Method | Endpoint | Description |
|--------|-----------|-------------|
| POST | /api/auth/login | Authenticate and get JWT |

### DGP APIs
| Method | Endpoint | Description |
|--------|-----------|-------------|
| GET | /api/ai/monthly_summary | AI NLG summary |
| GET | /api/ai/performance_forecast | ML-based performance forecast |
| GET | /api/drives/leaderboard/:metric | District ranking by metric |
| GET | /api/analytics/conviction_rates | Ranked conviction rates |
| GET | /api/analytics/map_data | Geo-analytics data |

### SP APIs
| Method | Endpoint | Description |
|--------|-----------|-------------|
| GET | /api/district_data/:district/:month | Get district data |
| POST | /api/cctns/report | Submit Good Work report |
| POST | /api/cctns/upload/nbw | Upload and parse report (AI) |

---

## 8. Data Schema

| Filename | PS-3 Part | Key Metrics |
|-----------|------------|-------------|
| cctns_nbw.json | 1a | pending_start_of_month, executed_total, etc. |
| cctns_firearms.json | 1b | cases_registered, persons_arrested, etc. |
| cctns_sand_mining.json | 1c | cases_registered, vehicle_seized, etc. |
| cctns_missing_persons.json | 1d | boy_missing_start, boy_traced, etc. |
| cctns_pendency.json | 1f | pendency_over_30_days, pendency_percentage, etc. |
| cctns_preventive_drives.json | 1g | preventive_nbw_executed, narcotics_seizure_ganja_kg, etc. |
| cctns_convictions.json | 2 | ipc_bns_trial_completed, ipc_bns_conviction, etc. |

---

Feature: Automated Report Generation
The dashboard allows high-level officers to instantly export comprehensive "Good Work Done" reports in multiple formats, satisfying a key requirement from the Problem Statement.

The "Export Report" button is prominently placed on the DGP Dashboard.

Users can select which specific widgets to include in the final report.

The system supports exporting as a structured PDF or a raw data CSV/Excel file.
<img width="350" height="125" alt="image" src="https://github.com/user-attachments/assets/789f8558-0649-40b5-a5f7-51883932670b" />
<img width="2625" height="1280" alt="image" src="https://github.com/user-attachments/assets/5a239a59-f64b-4840-a5bf-2800cc3dd9a3" />

Feature: High-Level KPI Statistics
The DGP Dashboard provides an immediate, at-a-glance summary of the most critical state-wide metrics. These cards are fully data-driven by the backend API, aggregating performance across all districts for the current month.

Live KPI cards show State Conviction Rate, Active AI Alerts, NBWs Executed, and Firearms Seized.
<img width="2591" height="442" alt="image" src="https://github.com/user-attachments/assets/990d519c-f5eb-4c05-84ec-ec3830e9e939" />


Feature Spotlight: AI Performance Forecast ("Districts to Watch")
The AI Performance Forecast widget, which uses ML to predict future pendency.

1.⁠ ⁠What is this Feature?
This widget is the direct implementation of the PS-3 requirement to "Predict potential underperforming districts or areas needing attention."

It is a machine learning model that runs on our time-series data (from cctns_pendency.json). Instead of just reporting last month's case pendency, this tool forecasts what the pendency percentage for every district will be next month.

2.⁠ ⁠How it Works (The AI/ML Logic)
Data Source: The backend GET /api/ai/performance_forecast endpoint is called.

Data Input: The server loads cctns_pendency.json, which has pendency data for all 30 districts for both Month 8 (August) and Month 9 (September).

ML Model: The getPerformanceForecast function in ai/analysis.js runs a simple linear regression (a core ML algorithm) for each district. It uses the two data points (Aug % and Sep %) to calculate a trend line (the slope).

Prediction: The model then projects this trend line forward one step (to Month 10) to get a projectedNextValue.

Analysis: It compares this future value to the last known value to find the projected % change.

Output: The backend sends this full analysis (the alerts, diagnostics, and summary objects) to your frontend.

3.⁠ ⁠Why This Feature is So Important (Your "Winning Edge")
This single widget demonstrates the entire value of your project. It's the difference between reactive reporting and proactive intelligence.

A "Dumb" Dashboard (The Competitors): Shows a chart that says, "Kalahandi's pendency was 40% last month." This is history. It's too late for the DGP to do anything but ask, "What happened?"

Our "Smart" Dashboard (Your Project): This widget tells the DGP, "Kalahandi's pendency is on a bad trend and is forecast to rise to 45% next month."

This is Actionable Intelligence. The DGP can now:

Act Proactively: The DGP doesn't have to wait for the problem. They can call the SP of Kalahandi today and ask, "What is happening with your case pendency? You are on a negative trend. What resources do you need to fix this?"

Identify "Districts to Watch": As your screenshot shows, the dashboard automatically does the analysis. The "Top 5 Rising" chart is a pre-built "Districts to Watch" list for the DGP.

Identify "Best Practices": The "Top 5 Falling" chart is equally important. The DGP can see that Angul's pendency is decreasing (-5.11%). They can now call the SP of Angul, learn what they are doing right (e.g., a new case review process), and apply those "best practices" to the underperforming districts.

This feature proves your dashboard is not just a data visualizer; it's a decision-making tool for high-level police leadership.
<img width="2029" height="1458" alt="image" src="https://github.com/user-attachments/assets/4192d302-c44b-4b26-9520-1beae1a96a96" />


Feature Spotlight: Geo-Analytics (GIS) Dashboard
The interactive GeoJSON map, colored by a selected metric. Here, it shows 'Conviction' rates, with darker green indicating better performance.

1.⁠ ⁠What is this Feature?
This widget directly satisfies the "Integration with GIS for location-based visualization" and "visualize trends" requirements from the Problem Statement (PS-3).

It's an interactive Choropleth Map (a data-heatmap) of Odisha. It allows the DGP to instantly see complex, state-wide performance data not as a boring table, but as a geographic, color-coded map.

2.⁠ ⁠How it Works (The AI/ML & Data Logic)
Data Source: The frontend calls the GET /api/analytics/map_data endpoint.

Data Fusion (Backend): This API is a powerful feature in itself. It performs a "data fusion" by combining data from four different CCTNS files (cctns_convictions.json, cctns_nbw.json, cctns_preventive_drives.json, cctns_firearms.json) into a single, clean JSON object for all 30 districts.

Interactivity (Frontend): The DGP can click the "Conviction," "NBW," or "Ganja" buttons. This changes a React state variable (mapMetric).

Dynamic Styling: The geoStyle function in the component reads this mapMetric state. It looks up the correct value for each district (e.g., conviction_rate: 44.4) and applies a specific color based on its performance (e.g., dark green for high conviction, dark red for high ganja seizure). The key={mapMetric} prop on the <GeoJSON /> component forces the map to re-render instantly when the metric changes.

On-Hover Detail: As seen in your screenshots, hovering over any district (like Dhenkanal) instantly brings up a popup with its exact statistics.

3.⁠ ⁠Why This Feature is So Important (Your "Winning Edge")
This map turns data into intelligence. It answers the DGP's biggest questions in a single glance.

It Identifies "Hotspots" (Problem Areas): Look at your screenshot image_94d402.png. A DGP can select "Ganja" and instantly see the entire southern part of the state light up bright red. They don't need to read a 50-page report to know they have a major narcotics corridor in Koraput, Malkangiri, and Ganjam. This is actionable intelligence for allocating a special task force.

It Identifies "Best Practices" (Top Performers): Look at your screenshot image_94d707.png. The DGP selects "Conviction" and sees Dhenkanal is dark green (high performance) while a neighboring district is light green (low performance). The DGP can now ask, "What is the SP in Dhenkanal doing right that the others aren't?" This directly helps identify and share best practices.

It Provides a Holistic View: The popup (image image_94d707.png) is critical. It shows that Dhenkanal has a good conviction rate but high Ganja seizures. This tells a complex story. It means the police are not just ignoring the problem; they are actively fighting it and winning in court.

This single feature is the core of "data-driven decision-making." It replaces thousands of rows of spreadsheet data with one intuitive, powerful, and actionable visual.
<img width="1283" height="960" alt="image" src="https://github.com/user-attachments/assets/7ad26dd3-8e9d-4199-958c-3040cc7b97c0" />
<img width="1241" height="943" alt="image" src="https://github.com/user-attachments/assets/c0bd9ee1-ecaf-4320-8463-259a47724a09" />
<img width="1256" height="946" alt="image" src="https://github.com/user-attachments/assets/506d2e9a-2d8a-4e80-9964-c977d4d94534" />

Feature Spotlight: AI Monthly Summary (NLG)
The AI/NLG widget that provides a plain-English summary of state performance.

1.⁠ ⁠What is this Feature?
This widget directly satisfies the key PS-3 requirement to: "Use natural language summaries (‘This month, Ganjam led in narcotics enforcement...’)"

This is an NLG (Natural Language Generation) feature. It acts as an AI data analyst that automatically writes a concise, human-readable report summary for the DGP. It answers the question, "What do I need to know right now?"

2.⁠ ⁠How it Works (The AI/ML Logic)
Data Source: The frontend calls the GET /api/ai/monthly_summary endpoint.

Data Fusion (Backend): This is a powerful AI feature. The backend API instantly queries all 7 CCTNS data files (convictionsDb, nbwDb, preventiveDb, etc.) for the latest month's data.

Find Top Performers: It runs an analysis to find the "winner" for each key "Good Work" metric:

Finds the district with the max(ipc_bns_conviction_rate). (In your screenshot, this is Cuttack at 64.5%).

Finds the district with the max(executed_total) NBWs. (In your screenshot, Ganjam with 280).

Finds the district with the max(narcotics_seizure_ganja_kg). (In your screenshot, Malkangiri with 5200 kg).

NLG Model: It passes this structured JSON ({conviction: "Cuttack", nbw: "Ganjam", narcotics: "Malkangiri"}) to our generateAISummary function in ai/analysis.js.

Output: That function uses a text template to build the final English sentence, which is then sent to the frontend.

3.⁠ ⁠Why This Feature is So Important (Your "Winning Edge")
This feature is the definition of a "Smart Dashboard."

It Saves the DGP's Time: A Director General of Police is one of the busiest officials in the state. They do not have time to read 30 separate district reports or manually compare 10 different charts. This AI does the work of an entire team of data analysts in less than a second.

It Provides Instant Recognition: The feature's primary purpose is "Good Work Recognition." It immediately identifies and praises the top-performing districts by name. This is a massive morale booster and directly implements the project's main goal.

It Sets the Agenda: This widget is the first thing the DGP sees. It sets the agenda for their day. They instantly know:

Who to praise (Cuttack, Ganjam, Malkangiri).

Which metrics are most important this month (Convictions, NBWs, Narcotics).

It's the "Wow" Factor: This is a true AI feature. It demonstrates that your dashboard doesn't just show data; it understands data. It takes thousands of rows of complex CCTNS data and translates it into simple, actionable, human-readable language.
<img width="906" height="865" alt="image" src="https://github.com/user-attachments/assets/fe336354-1c80-49ea-be81-89e2ffae8326" />

Feature Spotlight: "Special Drive" Leaderboard
The dynamic leaderboard widget, showing rankings for Firearms seized.

1.⁠ ⁠What is this Feature?
This is a dynamic and interactive "Top 10" leaderboard for the DGP. It directly addresses the need to "highlight top-performing districts" and "promote healthy competition" (gamification).

Instead of one static chart, this widget allows the DGP to instantly switch between different "Special Drive" metrics to see who is winning in each category.

2.⁠ ⁠How it Works (The Data & API Logic)
Data Source: This widget is powered by multiple CCTNS data files (cctns_firearms.json, cctns_preventive_drives.json, cctns_nbw.json, etc.).

Frontend Interaction: The DGP clicks on a metric button (e.g., "Firearms," "Sand Mining," "NBW Executed"). This updates a React state variable (metric).

Dynamic API (Backend): This metric state is passed to a single, powerful backend endpoint: GET /api/drives/leaderboard/:metric.

If the user clicks "Firearms," the frontend calls .../leaderboard/firearms_seized.

If the user clicks "NBW Executed," the frontend calls .../leaderboard/nbw_executed.

Backend Logic: The server's API logic is smart. It receives the metric parameter, selects the correct data file (e.g., firearmsDb for firearms, preventiveDb for narcotics), calculates the total value for each district, sorts the list, and sends back the Top 10.

Visualization: The React component re-renders the BarChart with the new data, showing the rankings for that specific drive.

3.⁠ ⁠Why This Feature is So Important (Your "Winning Edge")
This feature is a brilliant example of "Good Work Recognition" and "Gamification."

It Drives Competition: This is the "gamified leaderboard" from the problem statement. An SP in Jajpur (Rank #7 for Firearms) can see exactly how far they are behind Ganjam (Rank #1). This creates a powerful, data-driven incentive to improve performance in a specific area.

It's an "At-a-Glance" Briefing: The DGP can get a 30-second overview of the entire state's "Good Work" performance just by clicking the 5 tabs.

Click "NBW": "Ganjam is #1." (Image image_94df81.png)

Click "Firearms": "Ganjam is still #1." (Image image_94dee3.png)

Click "Sand Mining": "Ganjam is #1 again." (Image image_94df64.png)

It's Actionable: The DGP can instantly see that Ganjam, Khordha, and Cuttack are consistently the top 3 performers across multiple categories. This allows the DGP to recognize their SPs for outstanding work and investigate what they are doing right.
<img width="2667" height="1094" alt="image" src="https://github.com/user-attachments/assets/ceda4117-cb83-4974-a19a-ea90cb73953a" />
<img width="2673" height="1064" alt="image" src="https://github.com/user-attachments/assets/10b7f4fe-92c3-4d4f-80ac-b7f95aca961d" />

Feature Spotlight: Trend Analysis (Month-wise / Drive-wise)
The dynamic, multi-district trend analysis widget.

1.⁠ ⁠What is this Feature?
This is a dynamic, multi-series line chart that allows the DGP to compare the performance of the top districts over time for any "Good Work Done" metric.

As shown in your screenshot, the DGP can use the dropdowns to ask complex questions like, "Show me the Top 5 districts for 'NBW Executed' over the 'Last 6 months'." The dashboard instantly answers this by fetching the data and rendering the chart.

2.⁠ ⁠How it Works (The AI/ML & Data Logic)
Frontend Interaction: The DGP uses the three dropdowns to select a metric (e.g., 'nbw_executed'), a time range months (e.g., 6), and a number of districts topN (e.g., 5).

Dynamic API Call: This triggers a call to one of your most powerful backend endpoints: GET /api/trends/:metric?months=6&top=5.

Backend Logic (The Engine):

The server.js file receives this request.

It uses the buildMonthsList helper to get the last 6 month keys (e.g., ['2025-04', ... '2025-09']).

It selects the correct database (e.g., nbwDb for 'nbw_executed').

It iterates through all 30 districts and builds a time-series (an array of 6 values) for each one.

It calculates the total for each district over that period.

It sorts all districts by this total and filters for the topN (Top 5).

It returns a single, clean JSON object: { months: [...], series: [...] }.

Frontend Rendering: The React component receives this data and formats it for the Recharts line chart, creating a separate, color-coded <Line> for each of the 5 districts in the series array.

3.⁠ ⁠Why This Feature is So Important (Your "Winning Edge")
This single widget is more powerful than an entire static report.

It Fulfills a Core Requirement: This is the literal, and most powerful, implementation of "Trend analysis over time (month-wise, drive-wise)."

It Provides Deep, Comparative Insight: A simple leaderboard (which we also have) just shows who is #1 today. This chart shows how they got there. The DGP can see if Ganjam's top performance in NBWs is a recent spike or a long-term, consistent effort.

It Shows "Momentum": The list on the right, with "vs prev month" change, is a brilliant addition. The DGP can see that even though Ganjam is #1, their momentum is negative (-6.7%), while Khordha is #2 and also has negative momentum (-8.0%). This is a critical insight, suggesting a potential state-wide slowdown.

It's a "Six-in-One" Tool: This one widget can analyze all your key metrics (Narcotics, Firearms, Sand Mining, etc.). It's an incredibly versatile and data-dense tool that allows the DGP to explore the data themselves, satisfying the "interactive analytics" requirement.
<img width="1823" height="1045" alt="image" src="https://github.com/user-attachments/assets/16a40c71-4f67-43f7-b8cc-d29fabde7037" />

This screenshot (image_94eac2.png) shows your "Top Performing Districts (Trend Summary)" widget. This is a brilliant component that works as a perfect companion to the "Trend Analysis" line chart.

Here is the detailed breakdown of this feature.

Feature Spotlight: Top Performing Districts (Trend Summary)
The "Top Performing Districts" widget, showing a ranked list of total Ganja seizures over the last 6 months.

1.⁠ ⁠What is this Feature?
This widget is a powerful analytics tool that directly addresses the PS-3 requirement to "highlight top-performing districts" and support "trend analysis over time."

While the line chart (from your previous screenshot) shows the momentum and month-to-month changes, this widget shows the cumulative magnitude. It answers the simple, critical question: "Over the last 6 months, which district performed the best overall?"

As shown in your screenshot, the DGP can select "Ganja (kg)" and "6m" and instantly see that Malkangiri is the #1 performer, having seized a total of 10,200 kg in that period.

2.⁠ ⁠How it Works (The Data & API Logic)
This widget is powered by the exact same API endpoint as your "Trend Analysis" line chart: GET /api/trends/:metric.

Frontend Interaction: The DGP selects a metric (e.g., 'narcotics_ganja_kg') and a months (e.g., 6) from the dropdowns.

Dynamic API Call: The component calls GET /api/trends/narcotics_ganja_kg?months=6&top=5.

Backend Logic: The server.js file calculates the time-series data for every district for the last 6 months. It calculates the total for each district, sorts the list, and sends back the Top 5.

Frontend Rendering: This React component receives the series array from the API. Instead of plotting the individual monthly values (like the line chart does), it simply renders the district name and the pre-calculated total value in a clean, ranked list.

3.⁠ ⁠Why This Feature is So Important (Your "Winning Edge")
This component is the perfect summary of the more complex line chart.

It Provides Clear, Unambiguous Rankings: A line chart can be complex (e.g., "Khordha is #2 now, but Ganjam was #1 for 3 months"). This widget removes all ambiguity. It tells the DGP, "Based on the 6-month total, Malkangiri is your #1 performer in Ganja seizure. Full stop."

It's a Key "Recognition" Tool: This is the definition of "Good Work Recognition." It provides a clear, data-driven, and time-based metric to praise the SP of Malkangiri, Koraput, and Rayagada.

It's a Powerful "Gamification" Feature: By showing the "Top 5," it creates a clear target for all the other districts to aim for. It directly promotes healthy competition, as requested in the Problem Statement.

It's Highly Flexible: By pairing these dropdowns with a simple list, you have created a tool that can instantly generate a "Top 5" list for any metric (Firearms, NBWs, etc.) over any time period. This is a highly flexible and reusable analytics feature.
<img width="927" height="992" alt="image" src="https://github.com/user-attachments/assets/1a1c6b65-85c1-4384-a420-4dd23468ee80" />
<img width="945" height="994" alt="image" src="https://github.com/user-attachments/assets/784d199f-a261-4a80-a901-b0032af9a7f9" />

Feature Spotlight: District Performance Spotlight
The "Spotlight" widget, showing the Top 3 and Bottom 3 districts for key metrics.

1.⁠ ⁠What is this Feature?
This widget is a high-level summary that acts as a "call to action" for the DGP. It directly satisfies the PS-3 requirement to "highlight top-performing districts" and "identify areas needing attention."

It boils down all the complex data from the other charts into a simple, actionable list:

Who to Praise: "Top 3 (Conviction Rate)"

Who to Help: "Areas for Focus (Bottom 3 Conviction)"

Who is Overworked: "Top 3 (Highest Workload)" (This is part of your code, even if not in this specific screenshot)

2.⁠ ⁠How it Works (The Data & API Logic)
Data Source: This widget is a "Data Fusion" component. It gets its data from two separate, pre-calculated API endpoints that the DGPDashboard fetches:

GET /api/analytics/conviction_rates (for the Top/Bottom 3)

GET /api/analytics/workload (for the "Highest Workload" list)

Frontend Logic: The DistrictSpotlightWidget component in your React code receives this data as props.

Sorting & Slicing: It performs a simple, fast sort on these arrays.

It sorts the convictionRates data in descending order and uses .slice(0, 3) to get the Top 3.

It then sorts the same convictionRates data in ascending order and uses .slice(0, 3) to get the Bottom 3 ("Areas for Focus").

It sorts the workload data in descending order to find the districts with the highest "Case-to-Officer" ratio.

Visualization: It displays these as three simple, clean lists, using green for positive (Top 3) and orange/red for areas of concern.

3.⁠ ⁠Why This Feature is So Important (Your "Winning Edge")
This widget is the "So What?" of the entire dashboard.

It's the Ultimate Summary: If the DGP only has 10 seconds, this one widget tells them everything they need to know about state performance: who is succeeding, who is struggling, and who is overworked.

It Drives Accountability: This is the core of "Good Work Recognition." Being publicly listed as #1 (like Cuttack) is a powerful, non-financial reward for that SP. Conversely, no SP wants to be on the "Areas for Focus" list (like Kalahandi). It creates clear, data-driven accountability.

It Directs Management: This widget provides the DGP's meeting agenda.

"Call the SP of Cuttack and congratulate them. Find out what they're doing right."

"Call the SP of Kalahandi and ask what resources they need to fix their conviction rate."

"Look at the Highest Workload list and see if it correlates with the 'Areas for Focus' to see if a lack of resources is the root cause."

This single widget connects all your data (convictions, HR, crime) and transforms it into a simple, powerful management tool.
<img width="2806" height="810" alt="image" src="https://github.com/user-attachments/assets/a65f3599-66e9-4bc8-a88d-42c382502f2a" />

Feature Spotlight: Auto-Report for Exceptional Performance
The auto-generated report that ranks all districts by a final "Good Work Score".

1.⁠ ⁠What is this Feature?
This table is the final output of our entire AI system. It's a "Good Work Done" report that algorithmically ranks all 30 districts based on their overall performance. It fuses multiple key metrics (like Conviction Rate and Firearms Seizures) into a single, unified "Good Work Score," providing a clear, transparent, and data-driven basis for recognition.

2.⁠ ⁠How it Works (The AI/ML Logic)
This feature is a powerful example of a data fusion and scoring model, which is a key AI/ML technique.

Data Source: This widget is powered by a new, dedicated backend endpoint that you've created: GET /api/reports/good-work-done.

Data Fusion (Backend): This endpoint is a "summary of summaries." It fetches the latest data from multiple CCTNS files, just like our other widgets:

It gets ipc_bns_conviction_rate from cctns_convictions.json.

It calculates TotalFirearmSeized from cctns_firearms.json.

(It can be expanded to include NBW, Narcotics, etc.)

AI Scoring Model (Backend):

The API's real "AI" is that it solves the "apples and oranges" problem. How do you compare 10 firearms seizures to a 50% conviction rate?

It does this by normalizing the data (scaling all metrics from 0 to 1).

It then applies a weighted model to calculate the final "Score". For example: Score = (Normalized_Conviction_Rate * 0.6) + (Normalized_Firearms_Seized * 0.4)

Ranking: The backend sorts all 30 districts by this final "Good Work Score" and sends the complete, ranked list to the frontend.

Visualization: The frontend simply renders this list as a clean, easy-to-read table, highlighting the top performers (like Khordha and Ganjam) in yellow.

3.⁠ ⁠Why This Feature is So Important (Your "Winning Edge")
This single table is the ultimate "Good Work Recognition" tool and the perfect summary of your project's value.

It's the "Recognition" button: This table is the answer to the PS-3 goal. The DGP doesn't need to do any work. The report is auto-generated, instantly showing that Khordha and Ganjam deserve recognition.

It's Transparent: It's not a "black box." The table clearly shows why Khordha is #1. It's not just their high "Score" (77.5%), but their high "Conv. Rate" (62.2%) and "Firearms" (29) seizures. It makes the ranking defensible and fair.

It's the Foundation for Reporting: This table is the core data used by your "Export Report" feature. When the DGP clicks "Export PDF" or "CSV," they are exporting this ranked list, fulfilling the "generate auto-reports... in official formats" requirement.

It Gamifies Performance: This table is the ultimate leaderboard. It creates a powerful incentive for the SP of Cuttack (#3) to analyze their performance and find ways to beat Ganjam and Khordha next month.
<img width="2401" height="1344" alt="image" src="https://github.com/user-attachments/assets/558cb7f3-8760-46fb-8533-706bbff57ef7" />


<img width="2546" height="169" alt="image" src="https://github.com/user-attachments/assets/70bb9b24-6f1f-4f9c-a53d-705e683a62ed" />

This section provides a detailed analysis of the District KPI Widgets (Feature 1), the primary operational view for the Superintendent of Police (SP).The key importance of this row of widgets is Tactical Management: it allows the SP to identify bottlenecks and resource gaps before they escalate to a state-level issue.Feature Spotlight: District Operational KPIs (SP Dashboard)This row of widgets transforms complex statistical tables into immediate, visual performance snapshots, giving the SP full control over their district's operational health.WidgetFeature DescriptionOperational ImportanceCase Pendency GaugeDisplays the percentage of cognizable cases pending for over 30 days (from cctns_pendency.json).Core Efficiency Metric. Gives the SP an immediate, single metric to gauge investigative and judicial efficiency. A high percentage (Red Zone) signals an urgent need for case review and intervention.NBW Drive FunnelVisualizes the flow of Non-Bailable Warrants from Total Issued → Total Disposed → Total Executed (from cctns_nbw.json).Resource Optimization & Throughput. Allows the SP to quickly identify where the bottleneck lies in the warrant process: are warrants piling up, or is the execution rate low? Tracks the actual performance of the Warrant Drive.Missing Persons DriveA comparative bar chart showing the count of persons currently Missing vs. Traced (broken down by age/gender).Success Rate & Accountability. Directly measures the success of tracing efforts. This metric holds staff accountable for closing high-priority missing person cases and is a key measure of community response.
<img width="2546" height="964" alt="image" src="https://github.com/user-attachments/assets/a0885b1b-fb3c-46c6-81be-e2bf1da302f5" />

Feature Spotlight: CCTNS Report Submission Module (SP Dashboard)This feature is the primary tool for the SP to manage and submit their monthly "Good Work Done" data.1. Digital Forms (Data Entry)This interface is the digital version of the CCTNS Annexure tables. It breaks down the submission process into clear, manageable sections (Part 1a: NBW Drive, Part 1b: Firearms Drive, etc.), ensuring data standardization at the source.Importance: It replaces messy, error-prone spreadsheets and paper documents with a unified digital form, solving the "Manual Forms" requirement and improving data quality before submission.2. Submit / Export Menu (The Action Center)The Submit / Export Report button provides the SP with all necessary actions in one menu:ActionPurposeOperational ImportanceSubmit to DGPFinalizes the data and sends the complete report to the central server.Compliance & Accountability. This is the core 'write' function, providing proof that the district has compiled and submitted its performance data.Download as PDF/Excel/CSVAllows the SP to instantly generate and download a clean, formatted copy of the submitted data.Local Auditing & Record-Keeping. Ensures the SP has a verifiable local record of the report for internal files or for quick reference, fulfilling the "Allow export in official formats" requirement at the district level.This combined module is the foundation for the entire project, ensuring that the necessary data is collected efficiently before it is fed to the DGP's AI analytics dashboard.
<img width="2306" height="1216" alt="image" src="https://github.com/user-attachments/assets/99242341-e941-4551-85cf-e9f34c35772f" />
<img width="458" height="443" alt="image" src="https://github.com/user-attachments/assets/ceade406-33b6-4c40-8024-03b4e0050443" />


This section provides a detailed analysis of the AI-Powered Smart Report Upload module, the single most critical feature for implementing the "Automated Data Processing" requirement of PS-3.

Feature Spotlight: Smart Report Upload (AI)
The Smart Report Upload widget, ready to process a file and automatically pre-fill the form.

1.⁠ ⁠What is this Feature?
This is the central feature of the Automated Data Processing requirement. It allows the SP's staff to bypass manual data entry by uploading their existing digital reports (PDF or Excel).

Importance: It directly solves the "Handle diverse formats (Excel, CSV, PDF uploads)" requirement. It transforms a time-consuming, error-prone administrative task into an instant, AI-driven process, allowing officers to focus on field work instead of bureaucracy.

2.⁠ ⁠How it Works (The AI/NLP Logic)
This process is a prime example of turning unstructured data into structured intelligence:

Frontend Action: The user selects the report type (e.g., "Part 1a: NBW Drive") and uploads a file (PDF/XLSX).

API Call: The file is sent via POST /api/cctns/upload/nbw.

Backend AI (NLP): If the file is a PDF, the backend:

Reads the raw text from the document buffer (pdf-parse).

Feeds the text into the parseNbwPdfText AI function (located in ai/analysis.js).

This function uses specialized Regular Expressions (a form of NLP) to scan the raw text, locate keywords (like "Executed total" and "Pending as on"), and extract the corresponding numeric values.

Frontend Payoff: The structured JSON object ({executed_total: 250, pending_end_of_month: 420}) is sent back to the SPDashboard.jsx, which uses it to automatically fill every field of the CCTNS report form for the user to review and submit.

3.⁠ ⁠Why This Feature is Crucial
Accuracy: It drastically reduces human data entry error, ensuring the foundation of the DGP's strategic analysis is reliable.

Efficiency: It is a force multiplier, saving hours of time per district every month.

Practical AI: It's an excellent, practical demonstration of how AI/NLP can be used in police administration to automate rote compliance tasks.
<img width="2339" height="820" alt="image" src="https://github.com/user-attachments/assets/adb34aa0-c27c-4c89-8889-56b65a0f7a1f" />


```


Analytics Dashboard for Police (CCTNS Good Work Done)**  
AI + Data + Governance = Smarter Policing in Odisha

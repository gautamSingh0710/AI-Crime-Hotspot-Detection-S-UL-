import pandas as pd
import random

# -------------------------------
# 1. LOAD DATA
# -------------------------------
df = pd.read_csv("42_District_wise_crimes_committed_against_women_2001_2012.csv")
coords = pd.read_csv("district_state_lon_lat.csv")

# -------------------------------
# 2. CLEAN DATA
# -------------------------------
df['DISTRICT'] = df['DISTRICT'].str.lower().str.strip()
df['STATE/UT'] = df['STATE/UT'].str.lower().str.strip()

coords['city'] = coords['city'].str.lower().str.strip()

coords['city'] = coords['city'].str.replace(' district','', regex=False)
coords['city'] = coords['city'].str.replace(' city','', regex=False)

df['DISTRICT'] = df['DISTRICT'].replace({
    'cuddapah': 'kadapa',
    'bangalore': 'bengaluru',
    'puducherry': 'pondicherry'
})

# -------------------------------
# 3. TOTAL CRIME
# -------------------------------
df['Total_Crime'] = df.iloc[:,3:].sum(axis=1)

# -------------------------------
# 4. MERGE
# -------------------------------
merged = pd.merge(df, coords, left_on='DISTRICT', right_on='city', how='left')
cleaned = merged.dropna(subset=['lat','lon'])

print("\n📊 Data Ready:", len(cleaned), "rows")

# -------------------------------
# 5. CLUSTERING
# -------------------------------
from sklearn.cluster import KMeans

X = cleaned[['lat','lon']]
kmeans = KMeans(n_clusters=5, random_state=0)
cleaned['cluster'] = kmeans.fit_predict(X)

cluster_analysis = cleaned.groupby('cluster')['Total_Crime'].mean()
hotspot_cluster = cluster_analysis.idxmax()

print("\n🔥 Most Dangerous Cluster:", hotspot_cluster)

# -------------------------------
# 6. USER INPUT (STATE + DISTRICT 🔥)
# -------------------------------
user_input = input("\n🔍 Enter State or District Name: ").lower()

district_match = cleaned[cleaned['DISTRICT'].str.contains(user_input)]
state_match = cleaned[cleaned['STATE/UT'].str.contains(user_input)]

import folium

# -------------------------------
# STATE SEARCH (e.g. kerala)
# -------------------------------
if len(state_match) > 0:
    print("\n🌍 State Mode Activated")

    center_lat = state_match['lat'].mean()
    center_lon = state_match['lon'].mean()

    m = folium.Map(location=[center_lat, center_lon], zoom_start=7)

    for _, r in state_match.iterrows():
        color = 'red' if r['cluster'] == hotspot_cluster else 'blue'

        folium.CircleMarker(
            location=[r['lat'], r['lon']],
            radius=5,
            color=color,
            fill=True
        ).add_to(m)

    m.save("crime_hotspot_map.html")
    print("🗺️ State map ready (zoom & explore manually!)")

# -------------------------------
# DISTRICT SEARCH (e.g. ludhiana)
# -------------------------------
elif len(district_match) > 0:
    print("\n📍 Matching Districts:")
    print(district_match['DISTRICT'].unique())

    row = district_match.iloc[0]

    print("\n📊 Crime Summary:")
    print("District:", row['DISTRICT'])
    print("Total Crime:", row['Total_Crime'])

    if row['cluster'] == hotspot_cluster:
        print("🚨 HIGH RISK AREA")
    else:
        print("✅ Moderate / Low Risk")

    # Top crimes
    crimes = df[df['DISTRICT'] == row['DISTRICT']].iloc[:,3:-1]
    print("\n🔥 Top Crimes:")
    print(crimes.sum().sort_values(ascending=False).head(3))

    # -------------------------------
    # BLIND SPOT MAP 🔥
    # -------------------------------
    m = folium.Map(location=[row['lat'], row['lon']], zoom_start=10)

    district_data = cleaned[cleaned['DISTRICT'] == row['DISTRICT']]

    for _, r in district_data.iterrows():
        lat_offset = r['lat'] + random.uniform(-0.05, 0.05)
        lon_offset = r['lon'] + random.uniform(-0.05, 0.05)

        if r['Total_Crime'] > 400:
            color = 'darkred'
        elif r['Total_Crime'] > 250:
            color = 'red'
        elif r['Total_Crime'] > 150:
            color = 'orange'
        else:
            color = 'blue'

        folium.CircleMarker(
            location=[lat_offset, lon_offset],
            radius=6,
            color=color,
            fill=True,
            fill_opacity=0.7
        ).add_to(m)

    m.save("crime_hotspot_map.html")
    print("🗺️ District hotspot map ready!")

else:
    print("❌ No match found")

# -------------------------------
# 7. PREDICTION
# -------------------------------
new_location = pd.DataFrame([[28.61, 77.23]], columns=['lat','lon'])
pred_cluster = kmeans.predict(new_location)

print("\n🔮 Predicted Cluster:", pred_cluster[0])
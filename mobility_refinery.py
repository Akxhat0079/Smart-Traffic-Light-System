import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def refine():
    df = pd.read_csv("raw_traffic_pulses.csv")
    
    # Cleaning
    df = df[df['needs_cleaning'] == False]
    
    # Feature Scaling for Chapter 8
    scaler = StandardScaler()
    scaled = scaler.fit_transform(df[['current_speed', 'delay', 'confidence']])
    
    # Clustering
    km = KMeans(n_clusters=4, random_state=42)
    df['cluster_id'] = km.fit_predict(scaled)
    
    # Priority Scoring from Chapter 7.4
    # We use a 1-4 rank based on the delay quartile
    df['priority_rank'] = pd.qcut(df['delay'].rank(method='first'), 4, labels=[4, 3, 2, 1])
    
    df.to_csv("refined_mobility_data.csv", index=False)
    print("✨ Refinement complete. All 10+ columns ready.")

if __name__ == "__main__":
    refine()
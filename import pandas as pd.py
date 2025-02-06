import pandas as pd


data = {
    "Location": ["sreet london", "birrigham", "wester", "Residential A", "Intersection c"],
    "Time": ["Morning", "Afternoon", "Evening", "Night", "Morning"],
    "Weather": ["Clear", "Rainy", "Clear", "Snowy",],
    "Road_Condition": ["Dry", "Wet", "Dry", "Icy", "Wet"],
    "Vehicle_Type": ["Car",  "Motorcycle", "Bus", "Car"],
    "Injury_Severity": ["Minor", "Severe",  "Minor", "Severe"],
}

df = pd.read_csv(data)

import csv
from statistics import mean
def get_city_temperatures(filename, city_name):
    temperature_data = {}
    
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            # Check if this row matches our city
            if row['City'] == city_name:
                # Extract year-month from date (format: 1849-01-01 -> 1849-01)
                date_str = row['dt']
                year_month = date_str[:7]  # Take first 7 characters (YYYY-MM)
                
                # Get temperature, handle missing values
                temp_str = row['AverageTemperature']
                if temp_str and temp_str.strip():  # Check if not empty
                    try:
                        temperature = float(temp_str)
                        temperature_data[year_month] = temperature
                    except ValueError:
                        # Skip rows with invalid temperature data
                        continue
    
    return temperature_data
def get_available_cities(filename, limit=None):
    cities = set()
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            cities.add(row['City'])
            if limit and len(cities) >= limit:
                break
    return sorted(list(cities))

# =============================================================================
# ASSIGNMENT: Build a Temperature Data API
# =============================================================================
# Students should implement these 5 functions to create a complete API
import csv
def find_temperature_extremes(filename, city_name): #Initialize extremes with sentinel values for comparison
    extremes = {'hottest': {'date': '', 'temperature': float('-inf')}, 
                'coldest': {'date': '', 'temperature': float('inf')}}  
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['City'] == city_name: #Only processes rows that match the specified city.
                date_str = row['dt']  
                year_month = date_str[:7]# Extract the year-month portion of the date (YYYY-MM)
                try:
                    temp = float(row['AverageTemperature'])
                    if temp > extremes['hottest']['temperature']:
                        extremes['hottest'] = {'date': year_month, 'temperature': temp}# Update hottest month if this temp is higher
                    if temp < extremes['coldest']['temperature']:
                        extremes['coldest'] = {'date': year_month, 'temperature': temp}# Update coldest month if this temp is lower
                except ValueError:  # Skip if temperature data is missing
                    continue
    return extremes
def get_seasonal_averages(filename, city_name, season):
    season_months = {             #map seasons to the correspponding months
        'spring': ['03', '04', '05'],
        'summer': ['06', '07', '08'],
        'fall': ['09', '10', '11'],
        'winter': ['12', '01', '02']
    }
    if season not in season_months:   #validate season input
        raise ValueError("Invalid season. Choose from 'spring', 'summer', 'fall', or 'winter'.")
    total_temp = 0
    count = 0
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['City'] == city_name:  # Process only rows matching the target city
                date_str = row['dt']
                month = date_str[5:7]     # Extract month from date string (assumes YYYY-MM-DD format)
                try:
                    temp = float(row['AverageTemperature'])
                    if month in season_months[season]:   # Accumulate if month belongs to the specified season
                        total_temp += temp
                        count += 1
                except ValueError:
                    continue
    if count == 0:  # Return None if no data was found for that season
        return {'city': city_name, 'season': season, 'average_temperature': None}
    return {'city': city_name, 'season': season, 'average_temperature': total_temp / count}# Return computed average
#Compute average temperature and count for the specified decade.
def compare_decades(filename, city_name, decade1, decade2):
    def get_decade_avg_temp(decade):
        start_year = decade
        end_year = decade + 9
        total_temp = 0
        count = 0

        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['City'] == city_name:
                    year = int(row['dt'][:4])  # Assume date format is YYYY-MM-DD; extract year
                    if start_year <= year <= end_year:
                        try:
                            temp = float(row['AverageTemperature'])
                            total_temp += temp
                            count += 1
                        except ValueError:
                            continue

        if count == 0: #Returns (average_temp, count) or (None, 0) if no valid data.
            return None, 0
        return total_temp / count, count

    avg_temp1, count1 = get_decade_avg_temp(decade1)
    avg_temp2, count2 = get_decade_avg_temp(decade2)

    if avg_temp1 is None or avg_temp2 is None:
        return {'error': 'Insufficient data for one or both decades.'}

    difference = avg_temp2 - avg_temp1
    trend = 'warming' if difference > 0 else 'cooling' if difference < 0 else 'stable'

    return {
        'city': city_name,
        'decade1': {
            'period': f'{decade1}s',
            'avg_temp': avg_temp1,
            'data_points': count1
        },
        'decade2': {
            'period': f'{decade2}s',
            'avg_temp': avg_temp2,
            'data_points': count2
        },
        'difference': difference,
        'trend': trend
    }
#Parameters:
       # filename (str): Path to the CSV file containing city temperature data.
       # target_city (str): Name of the target city to compare temperatures.
       # tolerance (float): Maximum allowed difference in average temperatures to consider cities as similar.
def find_similar_cities(filename, target_city, tolerance=2.0):
    target_data = get_city_temperatures(filename, target_city)
    if not target_data:
        return {
            'target_city': target_city,
            'target_avg_temp': None,
            'similar_cities': [],
            'tolerance': tolerance
        }

    target_avg = mean(target_data.values())
    results = []

    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        city_data = {}
        for row in reader:
            city = row['City']      
            country = row['Country']
            temp_str = row['AverageTemperature']
            if temp_str and temp_str.strip():
                try:   # Convert temperature string to float and add to city_data dictionary
                    city_data.setdefault((city, country), []).append(float(temp_str))
                except ValueError:
                    continue

   # Compare each city's average temperature with the target city's average
    for (city, country), vals in city_data.items():
        if city == target_city:
            continue
        avg = mean(vals)   
        diff = abs(avg - target_avg)
        if diff <= tolerance:  # If difference is within tolerance, add to results
            results.append({  
                'city': city,
                'country': country,
                'avg_temp': avg,
                'difference': diff
            })

    return {
        'target_city': target_city,
        'target_avg_temp': target_avg,
        'similar_cities': results,
        'tolerance': tolerance
    }

def get_temperature_trends(filename, city_name, window_size=5):
   temps= get_city_temperatures(filename, city_name)
   if not temps:
      return {}
   annual={}
   for d, t in temps.items():
      y=int(d[:4])
      annual.setdefault(y, []).append(t)
      annual_avg = {y: mean(v) for y,v in annual.items()}
      years = sorted(annual_avg.keys())
   moving ={}
   for i in range(len(years)):
      if i+1 >= window_size:
         window_years = years[i+1-window_size:i+1]
         moving[years[i]]= mean([annual_avg[y] for y in window_years])
   n=len(years)
   x= list(range(n))
   y=[annual_avg[yr] for yr in years]
   x_mean, y_mean = mean(x), mean(y)
   num = sum((x[i]-x_mean)*(y[i]-y_mean) for i in range(n))
   den = sum((x[i]-x_mean)**2 for i in range(n))
   slope = num/den if den else 0
   return{
      'city': city_name,
      'raw_annual_data': annual_avg,
      'moving_averages': moving,
      'trend_analysis': {
         'overall_slope': slope,
         'warming_periods': [],
         'cooling_periods':[]
      }
    }   


# =============================================================================
# TESTING CODE 
# =============================================================================

def test_api_functions():
    filename = 'GlobalLandTemperaturesByMajorCity.csv'
    test_city = 'Madras'
    
    print("Testing Temperature Data API")
    print("=" * 40)
    
    # Test basic function
    temps = get_city_temperatures(filename, test_city)
    print(f"Basic function: Found {len(temps)} temperature records")
    
    # Test extremes
    extremes = find_temperature_extremes(filename, test_city)
    print(f"Extremes: Hottest = {extremes['hottest']['temperature']}°C")
    
    # Test seasonal averages
    summer_avg = get_seasonal_averages(filename, test_city, 'summer')
    print(f"Seasonal: Summer average = {summer_avg['average_temperature']:.1f}°C")
    
    # Test decade comparison
    comparison = compare_decades(filename, test_city, 1980, 2000)
    print(f"Decades: Temperature change = {comparison['difference']:.2f}°C")
    
    # Test similar cities
    similar = find_similar_cities(filename, test_city, tolerance=3.0)
    print(f"Similar cities: Found {len(similar['similar_cities'])} matches")
    
    trends = get_temperature_trends(filename, test_city)
    if trends:
        print(f"Trends: Overall slope = {trends['trend_analysis']['overall_slope']:.4f}°C/year")
    else:
        print("No temperature data available for trend analysis.")

# Implement the functions defined below to form a useful
if __name__ == "__main__":
    test_api_functions()

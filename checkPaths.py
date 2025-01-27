from datetime import datetime
from math import radians, sin, cos, sqrt, atan2
import os
from extractingMetadata import extract_metadata, process_photos


# Function to calculate Haversine distance between two points
def haversine(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(float, [lat1, lon1, lat2, lon2])
    R = 6371000  # Earth radius in meters
    phi1, phi2 = radians(lat1), radians(lat2)
    d_phi = radians(lat2 - lat1)
    d_lambda = radians(lon2 - lon1)
    a = sin(d_phi / 2) ** 2 + cos(phi1) * cos(phi2) * sin(d_lambda / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c

# Function to check crossing paths
def check_crossing_paths(metadata1, metadata2, time_threshold=15, distance_threshold=100):
    lat1, lon1 = metadata1.get('Latitude', 0), metadata1.get('Longitude', 0)
    lat2, lon2 = metadata2.get('Latitude', 0), metadata2.get('Longitude', 0)
    time1, time2 = metadata1.get('DateTime'), metadata2.get('DateTime')

    if None in [lat1, lon1, lat2, lon2, time1, time2]:
        return False, "Insufficient metadata to compare."

    distance = haversine(lat1, lon1, lat2, lon2)
    if distance > distance_threshold:
        return False, "Locations too far apart."

    fmt = "%Y:%m:%d %H:%M:%S"
    t1, t2 = datetime.strptime(time1, fmt), datetime.strptime(time2, fmt)
    time_diff = abs((t1 - t2).total_seconds() / 60)  # in minutes
    if time_diff > time_threshold:
        return False, "Times do not overlap."

    return True, f"Paths crossed! Distance: {distance:.2f} meters, Time difference: {time_diff:.2f} minutes."

# Function to process photos and check paths
def process_photos_and_check_paths(directory):
    metadata_list = process_photos(directory)
    # Compare each pair of photos
    for i in range(len(metadata_list)):
        for j in range(i + 1, len(metadata_list)):
            result, message = check_crossing_paths(metadata_list[i], metadata_list[j])
            print(f"Comparing {metadata_list[i]['Filename']} and {metadata_list[j]['Filename']}: {message}")

def main():
    photo_directory = "../photos"
    process_photos_and_check_paths(photo_directory)


if __name__ == "__main__":
    main()

from math import radians, sin, cos, sqrt, atan2
from datetime import datetime
from extractingMetadata import extract_metadata
import os


# Function to calculate Haversine distance between two points
def haversine(lat1, lon1, lat2, lon2):
    R = 6371000  # Earth radius in meters
    phi1, phi2 = radians(lat1), radians(lat2)
    d_phi = radians(lat2 - lat1)
    d_lambda = radians(lon2 - lon1)
    a = sin(d_phi / 2) ** 2 + cos(phi1) * cos(phi2) * sin(d_lambda / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c


# Function to check crossing paths
def check_crossing_paths(metadata1, metadata2, time_threshold=15, distance_threshold=100):
    lat1, lon1 = metadata1.get('Latitude'), metadata1.get('Longitude')
    lat2, lon2 = metadata2.get('Latitude'), metadata2.get('Longitude')
    time1 = metadata1.get('DateTime')
    time2 = metadata2.get('DateTime')

    if None in [lat1, lon1, lat2, lon2, time1, time2]:
        return False, "Insufficient metadata to compare."

    # Calculate distance
    distance = haversine(lat1, lon1, lat2, lon2)
    if distance > distance_threshold:
        return False, "Locations too far apart."

    # Calculate time difference
    fmt = "%Y:%m:%d %H:%M:%S"
    t1 = datetime.strptime(time1, fmt)
    t2 = datetime.strptime(time2, fmt)
    time_diff = abs((t1 - t2).total_seconds() / 60)  # in minutes
    if time_diff > time_threshold:
        return False, "Times do not overlap."

    return True, f"Paths crossed! Distance: {distance:.2f} meters, Time difference: {time_diff:.2f} minutes."


# Function to process photos and check paths
def process_photos_and_check_paths(directory):
    metadata_list = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('jpg', 'jpeg', 'png')):
                photo_path = os.path.join(root, file)
                metadata = extract_metadata(photo_path)
                metadata['Filename'] = file
                metadata_list.append(metadata)

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

from datetime import datetime
from math import radians, sin, cos, sqrt, atan2
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
    lat1, lon1 = metadata1.get('Latitude', None), metadata1.get('Longitude', None)
    lat2, lon2 = metadata2.get('Latitude', None), metadata2.get('Longitude', None)
    time1, time2 = metadata1.get('DateTime'), metadata2.get('DateTime')

    # If any critical metadata is missing, skip
    if None in [lat1, lon1, lat2, lon2, time1, time2]:
        return False, {
            "message": "Insufficient metadata to compare.",
            "lat1": None,
            "lon1": None,
            "lat2": None,
            "lon2": None
        }

    distance = haversine(lat1, lon1, lat2, lon2)
    if distance > distance_threshold:
        return False, {
            "message": "Locations too far apart.",
            "lat1": lat1,
            "lon1": lon1,
            "lat2": lat2,
            "lon2": lon2
        }

    fmt = "%Y:%m:%d %H:%M:%S"
    t1, t2 = datetime.strptime(time1, fmt), datetime.strptime(time2, fmt)
    time_diff = abs((t1 - t2).total_seconds() / 60.0)  # minutes

    if time_diff > time_threshold:
        return False, {
            "message": "Times do not overlap.",
            "lat1": lat1,
            "lon1": lon1,
            "lat2": lat2,
            "lon2": lon2
        }

    # If we made it here, it's a crossing
    return True, {
        "message": f"Paths crossed! Distance: {distance:.2f}m, Time diff: {time_diff:.2f} min.",
        "lat1": lat1,
        "lon1": lon1,
        "lat2": lat2,
        "lon2": lon2
    }


# Function to process photos and check paths in a single directory
def process_photos_and_check_paths(directory):
    metadata_list = process_photos(directory)
    # Compare each pair of photos
    for i in range(len(metadata_list)):
        for j in range(i + 1, len(metadata_list)):
            result, message_data = check_crossing_paths(metadata_list[i], metadata_list[j])
            print(f"Comparing {metadata_list[i]['Filename']} and {metadata_list[j]['Filename']}: {message_data['message']}")


# Function to process photos and check paths between two directories
def process_photos_and_check_paths_2directories(directory1, directory2):
    metadata_list1 = process_photos(directory1)
    metadata_list2 = process_photos(directory2)

    crossed_paths = []

    # Compare each pair of photos between two different directories
    for meta1 in metadata_list1:
        for meta2 in metadata_list2:
            result, message_data = check_crossing_paths(meta1, meta2)
            if result:
                crossed_paths.append({
                    'File1': meta1['Filename'],
                    'File2': meta2['Filename'],
                    'Message': message_data['message'],
                    'Lat1': message_data['lat1'],
                    'Lon1': message_data['lon1'],
                    'Lat2': message_data['lat2'],
                    'Lon2': message_data['lon2']
                })
                print(f"Comparing {meta1['Filename']} and {meta2['Filename']}: {message_data['message']}")

    return crossed_paths


def main():
    photo_directory = "../photos"
    process_photos_and_check_paths(photo_directory)


if __name__ == "__main__":
    main()

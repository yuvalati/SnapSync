from datetime import datetime
from math import radians, sin, cos, sqrt, atan2
# If you need geocoding, ensure we import from extractingMetadata
from extractingMetadata import process_photos, geocode_location


def haversine(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(float, [lat1, lon1, lat2, lon2])
    R = 6371000  # Earth radius in meters
    phi1, phi2 = radians(lat1), radians(lat2)
    d_phi = radians(lat2 - lat1)
    d_lambda = radians(lon2 - lon1)
    a = sin(d_phi / 2) ** 2 + cos(phi1) * cos(phi2) * sin(d_lambda / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c


def check_crossing_paths(metadata1, metadata2, time_threshold=15, distance_threshold=100):
    lat1, lon1 = metadata1.get('Latitude'), metadata1.get('Longitude')
    lat2, lon2 = metadata2.get('Latitude'), metadata2.get('Longitude')
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

    # EXIF time format is usually "YYYY:MM:DD HH:MM:SS"
    fmt = "%Y:%m:%d %H:%M:%S"
    t1 = datetime.strptime(time1, fmt)
    t2 = datetime.strptime(time2, fmt)
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
        "message": f"Distance: {distance:.2f}m.\nTime diff: {time_diff:.2f} min.",
        "lat1": lat1,
        "lon1": lon1,
        "lat2": lat2,
        "lon2": lon2
    }


def process_photos_and_check_paths(directory):
    metadata_list = process_photos(directory)
    # Compare each pair of photos within the same directory
    for i in range(len(metadata_list)):
        for j in range(i + 1, len(metadata_list)):
            result, message_data = check_crossing_paths(metadata_list[i], metadata_list[j])
            print(
                f"Comparing {metadata_list[i]['Filename']} and {metadata_list[j]['Filename']}: {message_data['message']}")


def process_photos_and_check_paths_2directories(directory1, directory2):
    metadata_list1 = process_photos(directory1)
    metadata_list2 = process_photos(directory2)

    crossed_paths = []

    for meta1 in metadata_list1:
        for meta2 in metadata_list2:
            result, message_data = check_crossing_paths(meta1, meta2)
            if result:
                # Optionally geocode using lat1/lon1 (current user):
                city, country = None, None
                if message_data['lat1'] is not None and message_data['lon1'] is not None:
                    city, country = geocode_location(message_data['lat1'], message_data['lon1'])

                # Reformat DateTime from the current user's photo (meta1) to dd-mm-yyyy HH:MM:SS
                original_dt = meta1.get('DateTime')  # or meta2, if you prefer
                date_to_show = "Unknown"
                if original_dt:
                    try:
                        dt_obj = datetime.strptime(original_dt, "%Y:%m:%d %H:%M:%S")
                        # Reformat
                        date_to_show = dt_obj.strftime("%d-%m-%Y %H:%M:%S")
                    except Exception as e:
                        print(f"Error parsing or formatting DateTime '{original_dt}': {e}")

                crossed_paths.append({
                    # If you want to keep these old fields (File1, File2) just in JSON:
                    'File1': meta1.get('Filename', 'Unknown'),
                    'File2': meta2.get('Filename', 'Unknown'),

                    'Message': message_data['message'],
                    'Lat1': message_data['lat1'],
                    'Lon1': message_data['lon1'],
                    'Lat2': message_data['lat2'],
                    'Lon2': message_data['lon2'],

                    # New/updated fields:
                    'City': city,
                    'Country': country,
                    'DateTime': date_to_show
                })

                print(f"Comparing {meta1['Filename']} and {meta2['Filename']}: {message_data['message']}")

    return crossed_paths


def main():
    photo_directory = "../photos"
    process_photos_and_check_paths(photo_directory)


if __name__ == "__main__":
    main()

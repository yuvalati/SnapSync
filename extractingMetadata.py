import os
import exifread
import requests


# Convert GPS data to degrees from the exifread tags format
def convert_to_degrees(value):
    # Expecting value in the format of a list of exifread.utils.Ratio objects
    d = float(value[0].num) / float(value[0].den)
    m = float(value[1].num) / float(value[1].den)
    s = float(value[2].num) / float(value[2].den)
    return d + (m / 60.0) + (s / 3600.0)


# Get latitude from EXIF tag
def get_latitude(tags):
    lat = tags.get('GPS GPSLatitude')
    lat_ref = tags.get('GPS GPSLatitudeRef')
    if lat and lat_ref:
        lat = convert_to_degrees(lat.values)
        if lat_ref.values != 'N':
            lat = -lat
    else:
        lat = None
    return lat


# Get longitude from EXIF tag
def get_longitude(tags):
    lon = tags.get('GPS GPSLongitude')
    lon_ref = tags.get('GPS GPSLongitudeRef')
    if lon and lon_ref:
        lon = convert_to_degrees(lon.values)
        if lon_ref.values != 'E':
            lon = -lon
    else:
        lon = None
    return lon


def geocode_location(lat, lon):
    # This is a placeholder function. You'll need an actual API key and use a real geocoding service.
    response = requests.get(f"https://api.opencagedata.com/geocode/v1/json?q={lat}+{lon}&"
                            f"key=6fb9eb926a384d2980a9a488fa9fd626")
    data = response.json()
    if data['results']:
        city = data['results'][0]['components']['city']
        country = data['results'][0]['components']['country']
        return city, country
    return None, None


# Extract metadata from a photo
def extract_metadata(photo_path):
    metadata = {}
    try:
        with open(photo_path, 'rb') as f:
            tags = exifread.process_file(f, details=False)
            metadata['Latitude'] = get_latitude(tags)
            metadata['Longitude'] = get_longitude(tags)
            datetime = tags.get('Image DateTime')
            if datetime:
                metadata['DateTime'] = str(datetime)
    except Exception as e:
        print(f"Error reading metadata from {photo_path}: {e}")
    return metadata


# Main function to process a directory of photos
def process_photos(directory):
    all_metadata = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('jpg', 'jpeg', 'png')):
                photo_path = os.path.join(root, file)
                metadata = extract_metadata(photo_path)
                metadata['Filename'] = file
                all_metadata.append(metadata)
    return all_metadata


def main():
    photo_directory = "../photos"
    metadata_list = process_photos(photo_directory)
    for metadata in metadata_list:
        print("\nPhoto Metadata:")
        print(f"Filename: {metadata['Filename']}")
        print(f"Latitude: {metadata.get('Latitude')}")
        print(f"Longitude: {metadata.get('Longitude')}")
        print(f"Date and Time: {metadata.get('DateTime')}")


if __name__ == "__main__":
    main()

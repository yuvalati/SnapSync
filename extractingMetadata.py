import os
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import datetime


# Function to extract metadata from a photo
def extract_metadata(photo_path):
    metadata = {}
    try:
        with Image.open(photo_path) as img:
            exif_data = img._getexif()
            if exif_data:
                for tag, value in exif_data.items():
                    tag_name = TAGS.get(tag, tag)

                    if tag_name == 'GPSInfo':
                        gps_data = {}
                        for gps_tag in value:
                            sub_tag = GPSTAGS.get(gps_tag, gps_tag)
                            gps_data[sub_tag] = value[gps_tag]
                        metadata['GPSInfo'] = gps_data
                    else:
                        metadata[tag_name] = value

                # Extracting specific metadata
                gps_info = metadata.get('GPSInfo', {})
                if gps_info:
                    lat = get_latitude(gps_info)
                    lon = get_longitude(gps_info)
                    metadata['Latitude'] = lat
                    metadata['Longitude'] = lon

                if 'DateTime' in metadata:
                    metadata['DateTime'] = metadata['DateTime']

    except Exception as e:
        print(f"Error reading {photo_path}: {e}")

    return metadata

# Helper function to convert GPS data to degrees
def convert_to_degrees(value):
    d, m, s = value
    return d + (m / 60.0) + (s / 3600.0)

# Function to get latitude

def get_latitude(gps_info):
    lat = gps_info.get('GPSLatitude')
    lat_ref = gps_info.get('GPSLatitudeRef')
    if lat and lat_ref:
        lat = convert_to_degrees(lat)
        if lat_ref != 'N':
            lat = -lat
    return lat

# Function to get longitude
def get_longitude(gps_info):
    lon = gps_info.get('GPSLongitude')
    lon_ref = gps_info.get('GPSLongitudeRef')
    if lon and lon_ref:
        lon = convert_to_degrees(lon)
        if lon_ref != 'E':
            lon = -lon
    return lon

# Main function to extract metadata from a directory of photos
def process_photos(directory):
    all_metadata = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('jpg', 'jpeg', 'png')):
                photo_path = os.path.join(root, file)
                metadata = extract_metadata(photo_path)
                metadata['Filename'] = file
                all_metadata.append(metadata)
    return all_metadata

# Example usage
def main():
    photo_directory = "../photos"
    metadata_list = process_photos(photo_directory)

    # Print extracted metadata
    for metadata in metadata_list:
        print("\nPhoto Metadata:")
        # print(metadata)
        print(f"Filename: {metadata['Filename']}")
        print(f"Latitude: {metadata.get('Latitude')}")
        print(f"Longitude: {metadata.get('Longitude')}")
        print(f"Date and Time: {metadata.get('DateTime')}")

if __name__ == "__main__":
    main()

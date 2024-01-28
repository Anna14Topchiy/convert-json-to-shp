import geopandas as gpd

def convert_geojson_to_shp(geojson_path, shp_path):
    # Read GeoJSON file
    gdf = gpd.read_file(geojson_path)

    # Truncate column names to 10 characters
    gdf.columns = [col[:10] for col in gdf.columns]

    # Write to Shapefile
    gdf.to_file(shp_path, driver='ESRI Shapefile')

if __name__ == "__main__":
    # Replace 'input.geojson' with your GeoJSON file path
    geojson_file = r'C:\Users\annat\OneDrive\kasko\source_preparation_for_each_country\NL\scripts_for_api_mapillary\tl_mapillary\merged_tl.geojson'

    # Replace 'output.shp' with your desired Shapefile output path
    shp_file = r'C:\Users\annat\OneDrive\kasko\source_preparation_for_each_country\NL\scrip_snap_points_to_line\json_to_shp\merged_tl.shp'

    convert_geojson_to_shp(geojson_file, shp_file)

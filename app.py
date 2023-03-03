import os
import math
import pandas as pd
from PIL import Image
import streamlit as st

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Load the data sheets
compatibility_data = pd.read_excel(os.path.join(script_dir, 'Service BI Analyst - Home Assignment.xlsx'), sheet_name='Table 1', index_col=0)
inventory_data = pd.read_excel(os.path.join(script_dir, 'Service BI Analyst - Home Assignment.xlsx'), sheet_name='Table 2', index_col=0)
components_data = pd.read_excel(os.path.join(script_dir, 'Service BI Analyst - Home Assignment.xlsx'), sheet_name='Components', squeeze="columns")

# Define power_keys as a global variable
global power_keys
power_keys = {} # Dictionary to save the power keys
components = components_data.tolist()   # List of components
regions = inventory_data.columns.tolist()   # Extract the regions from inventory sheet


# List the compatible powers for each power key
def extract_compatible_power():
    # Loop through each column until reaching the header "Y1300" (defect data/assymetric)
    j=0
    for j, col_name in enumerate(compatibility_data.columns):
        if col_name == "Y1300":
            break
        power_keys[col_name] = []   #dictionary of lists [power key -> compatible powers]
        for i, value in compatibility_data[col_name].items():
            if value == 'ü':
                power_keys[col_name].append(i)

    # Loop through each row starting from index j (Y1300)
    for i, row in compatibility_data.iloc[j:].iterrows():
        # List comprehension to extract the compatible power keys for this row
        power_keys[i] = [col_name for col_name in compatibility_data.columns if (col_name < "Y1300" and row[col_name] == 'ü') or (col_name >= "Y1300" and compatibility_data.loc[i, col_name] == 'ü')]


# Find the maximum capacity for a given power list and region
def get_max_power_info(power_list, region):
    # Filter the dataframe to only include rows with a key in the input power list
    power_df = inventory_data.loc[power_list]

    # Check if the power_df DataFrame is empty
    if power_df.empty:
        return None

    # Find the value for the specified region
    max_power = power_df[region].max()

    # Find the key(s) with the maximum value for the specified region
    max_power_keys = power_df[power_df[region] == max_power].index.tolist()

    return max_power, max_power_keys


# Get the compatible powers for a given component
def get_compatible_power(component):
    # Extract the power key from the component name
    power_key = component.split('-')[0]
    if power_key in power_keys:
        return power_keys[power_key]
    else:
        return []


# Define the Streamlit app
def app():
    extract_compatible_power()
    img = Image.open(os.path.join(script_dir,'solaredge.png'))
    st.image(img, width=200)
    st.title("Component Power Search")
    st.write("This app allows you to search for compatible power for different components in different regions.")

    # Create dropdown menus for selecting component and region
    component_selected = st.selectbox("Select component", components)
    regions_selected = st.multiselect("Select region(s)", regions)
    st.markdown(f"<p style='color: white; font-weight:bold; font-size:20px;'>\n\nHighest compatible power:", unsafe_allow_html=True)

    # Check if a component and regions are selected
    if component_selected and regions_selected:
        # Loop through each selected region
        for region_selected in regions_selected:
            # Extract the compatible power for the selected component
            compatible_power = get_compatible_power(component_selected)

            # Check if any compatible power is found
            if compatible_power:
                # Get the maximum capacity for the compatible powers in the selected region
                max_power, max_power_keys = get_max_power_info(compatible_power, region_selected)
                
                if max_power > 0:
                    st.markdown(f"<p style='color: #0BDA51; font-weight:standard; font-size:22px;'>{region_selected}: {', '.join(max_power_keys)}  ({math.floor(max_power)}pcs)", unsafe_allow_html=True)

                else:
                    # Display a warning message for no capacity
                    st.error(f"No capacity found in {region_selected} for {component_selected}!")
            else:
                st.warning(f"No compatible power found for {component_selected} in {region_selected}!")
    else:
        st.warning("Please select component and region(s).")

# Run the app
if __name__ == '__main__':
    app()

import os
import time
import numpy as np
import pandas as pd
from PIL import Image
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go


# Get the directory of the current file
script_dir = os.path.dirname(os.path.abspath(__file__))

# Load the data sheets
compatibility_data = pd.read_excel(os.path.join(script_dir, 'Service BI Analyst - Home Assignment.xlsx'), sheet_name='Table 1', index_col=0)
inventory_data = pd.read_excel(os.path.join(script_dir, 'Service BI Analyst - Home Assignment.xlsx'), sheet_name='Table 2', index_col=0)
components_data = pd.read_excel(os.path.join(script_dir, 'Service BI Analyst - Home Assignment.xlsx'), sheet_name='Components', squeeze="columns")


global power_keys   
power_keys = {}     # Dictionary to save the power keys (A100, B150...)
components = components_data.tolist()   # Extract components from components sheet
regions = inventory_data.columns.tolist()   # Extract the regions from inventory sheet


# List the compatible powers for each power key
def extract_compatible_power():
    # Loop through each column until reaching the header "Y1300" (defect data/assymetric)
    j=0
    for j, col_name in enumerate(compatibility_data.columns):
        if col_name == "Y1300":
            break
        power_keys[col_name] = []   # dictionary of lists [power key -> compatible powers]
        for i, value in compatibility_data[col_name].items():
            if value == 'ü':
                power_keys[col_name].append(i)

    # Loop through each row starting from index j (Y1300)
    for i, row in compatibility_data.iloc[j:].iterrows():
        # List comprehension to extract the compatible power keys for this row
        power_keys[i] = [col_name for col_name in compatibility_data.columns if (col_name < "Y1300" and row[col_name] == 'ü') or (col_name >= "Y1300" and compatibility_data.loc[i, col_name] == 'ü')]


# Find the maximum amount for a given power list and region
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


# Get the compatible powers for a given component (AJ1850-we455-d5d5  ->  AJ1850)
def get_compatible_power(component):
    # Extract the power key from the component name
    power_key = component.split('-')[0]
    if power_key in power_keys:
        return power_keys[power_key]
    else:
        return []


def create_inventory_dashboard():
    # Create a new DataFrame that summarizes inventory levels for each power and region
    inventory_summary = inventory_data.stack().reset_index(name='Inventory')
    inventory_summary = inventory_summary.rename(columns={'level_0': 'Power', 'level_1': 'Region'})

    # Create a new column to indicate color based on inventory levels
    colors = pd.cut(inventory_summary['Inventory'], bins=[-1, 0, 10, np.inf], labels=['red', 'yellow', 'green'])
    inventory_summary['Color'] = colors

    # Create a slider to filter inventory levels
    inventory_filter = st.select_slider('Filter inventory quantity:', options=list(range(102)) + [999], value=(0, 101),
                                           format_func=lambda value: f'100+' if value == 101 else str(value))

    # Modify the selected options to replace 101 with 999
    if 101 in inventory_filter:
        inventory_filter = (inventory_filter[0], 999) if inventory_filter[1] == 101 else (999, inventory_filter[1])

    # Filter the inventory_summary DataFrame based on the slider values
    filtered_inventory_summary = inventory_summary[(inventory_summary['Inventory'] >= inventory_filter[0]) &
                                                    (inventory_summary['Inventory'] <= inventory_filter[1])]

    # Create a heatmap of inventory levels, with color-coded cells based on inventory levels
    fig = go.Figure(go.Heatmap(x=filtered_inventory_summary['Region'], y=filtered_inventory_summary['Power'],
                               z=filtered_inventory_summary['Inventory'], colorscale='RdYlGn',
                               zmin=0, zmax=100, showscale=True,
                               hovertemplate='Power: %{y}<br>Region: %{x}<br>Inventory: %{z}<br>Color: %{customdata}',
                               customdata=filtered_inventory_summary['Color']))

    # Add labels and title to the plot
    fig.update_layout(title='Inventory quantity by Power and Region', xaxis_title='Region', yaxis_title='Power')

    # Reverse the order of the y-axis (A-Z up down)
    fig.update_layout(yaxis=dict(autorange="reversed"))

    # Create a container for the plot
    with st.container():
        fig.update_layout(width=600, height=800)

        # Set the style of the plot
        st.plotly_chart(fig, style={'height': '100px', 'width': '100%'})


def compatible_power_chart(selected_component, selected_regions):
    # Get the compatible power keys for the selected component
    compatible_power = get_compatible_power(selected_component)
    if not compatible_power:
        st.warning(f"No compatible powers found for {selected_component}")
        return

    # Filter the inventory_data DataFrame to only include the selected regions and compatible power keys
    inventory = inventory_data.loc[compatible_power, selected_regions]

    # Sort the inventory qty desc of power
    inventory = inventory.sort_values(ascending=False)

    # Create a bar chart of the inventory quantity
    fig = px.bar(inventory, x=inventory.index, y=inventory.values, labels={'x': 'Power', 'y': 'Inventory'},
                 color=inventory.values, color_continuous_scale='RdYlGn', height=265)

    # Add title and axis labels to the plot
    fig.update_layout(title={
            'text': f"{selected_regions}",
            'font': {'size': 20}
        },
    xaxis_title='Power',
    yaxis_title='Inventory')
    # Create a container for the plot
    with st.container():
        st.plotly_chart(fig, use_container_width=True)



def app():
    extract_compatible_power()
    st.set_page_config(page_title="My Streamlit App", page_icon=":guardsman:", layout="wide")
    
    # Out of inventory report
    def report_issue(reg):
        st.success(f"No compatible Power reported successfully")

    # Confirm button and timer message 
    def confirm_issue(reg):
        cancel_pressed = False
        with col_cancel:
            cancel_button = st.button(label="Cancel", key=f"Cancel{reg}")
        if cancel_button:
            cancel_pressed = True
        for i in range(5, 0, -1):
            if cancel_pressed:
                break
            timer_message = st.info(f"{max_power_keys[0]} from {reg} confirmed within {i}...")
            time.sleep(1)
            timer_message.empty()    
        st.success(f"{max_power_keys[0]} from {reg} confirmed succefully")
        return cancel_pressed

    # Logo img
    img = Image.open(os.path.join(script_dir,'solaredge.png'))
    # Divide screen by cols
    col1, empty_col, col2, empty_col = st.columns([6, 3, 7, 2])
    with st.container():
        with col1:
            st.image(img, width=300)
            st.title("Component Power Search")
            st.write("Search for compatible power for different components in different regions.")
            st.write("<br>", unsafe_allow_html=True)

            # Selecting component and region
            component_selected = st.selectbox("Select component", components)
            all_selected_regions = st.multiselect("Select region(s)", regions)
            st.markdown(f"<p style='color: white; font-weight:bold; font-size:20px;'>\n\nHighest compatible power:", unsafe_allow_html=True)

            if component_selected and all_selected_regions:
                # Loop through each selected region
                for region_selected in all_selected_regions:
                    # Extract the compatible power for the selected component
                    compatible_power = get_compatible_power(component_selected)
                    # Check if any compatible power is found
                    if compatible_power:
                        # Get the maximum quantity for the compatible powers in the selected region
                        max_power, max_power_keys = get_max_power_info(compatible_power, region_selected)

                        if max_power > 0:
                            col_data, col_confirm, col_cancel,  = st.columns([3.5 ,1 , 1])
                            with col_data:
                                st.markdown(f"<p style='color: #0BDA51; font-weight: standard; font-size:22px;'>{region_selected}: <span style='text-decoration: underline; font-weight: bold;'>{', '.join(max_power_keys)}", unsafe_allow_html=True)
                                with col_confirm:
                                    confirm_button = st.button(label=f"Confirm", key=f"Confirm{max_power}{region_selected}")
                                    if confirm_button:
                                        with col_data:
                                            confirm_issue(region_selected)
                        # Out of inventory                     
                        else:
                            col_data, col_confirm, col_cancel,  = st.columns([3.5 ,1 , 1])
                            with col_data:
                            # Display a message for no quantity
                                st.markdown(f"<p style='color: red; font-weight: standard; font-size:22px;'>{region_selected}: No compatible Power", unsafe_allow_html=True)
                            with col_confirm:
                                report_button = st.button(label=f"Report", key=f"report_button")
                            with col_data:
                                if report_button:
                                    report_issue(region_selected)
                    # No compatible power found
                    else:
                        st.warning(f"No compatible power found for {component_selected} in {region_selected}!")
            else:
                    st.warning("Please select component and region(s).")

        with col2:
            tab1, tab2 = st.tabs(["Compatible power", "Inventory"])
            with tab1:
                st.markdown(f"<p style='color: white; font-weight:none; font-size:20px;'>Compatible Power for <u style='color:white; font-weight: bold;'>{component_selected}</u></p>", unsafe_allow_html=True)
                # Create a button to trigger the creation of the bar chart
                if component_selected and all_selected_regions:
                    for region in all_selected_regions:
                        compatible_power_chart(component_selected, region)
            with tab2:
                create_inventory_dashboard()

if __name__ == '__main__':
    app()

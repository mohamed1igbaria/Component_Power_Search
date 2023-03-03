# Component Power Search

##### With this application, you can find the best power match for different components across various regions by utilizing the provided data. The app searches through all available compatible inventory options and selects the option with the highest capacity/maximum amount.
-------------
## Getting Started
### Installation
1. ###### Install Python 3, You can download Python from the official website: https://www.python.org/downloads/
2. ###### Install the required Python packages by running the following commands in your terminal:
```
pip install pandas
```
```
pip install streamlit
```
```
pip install pillow
```
-------------
### Running the App
1. ###### Clone this repository to your local machine:
```
git clone https://github.com/your-username/your-repo.git
```

2. ###### In your terminal Navigate to the project directory by changing the 'path':
```
cd/"path"
```

3. ###### Download the data file 'Service BI Analyst - Home Assignment.xlsx' and save it in the project directory.

4. ###### Run the app using the following command in your terminal:
```
streamlit run app.py
```

5. ###### The app will open in a new browser window at http://localhost:8501.
-------------
### Using the App
1. ###### Select a component from the dropdown menu.
<img width="789" alt="Screenshot 2023-03-03 at 14 36 41" src="https://user-images.githubusercontent.com/92742400/222730830-5728a60c-95ab-45ea-bdb0-4f50378297c1.png">

2. ###### Select one or more regions from the multiselect menu.
<img width="788" alt="Screenshot 2023-03-03 at 14 37 20" src="https://user-images.githubusercontent.com/92742400/222730972-f221c8d3-7f83-45a7-b510-975dc868d374.png">
<img width="789" alt="Screenshot 2023-03-03 at 14 46 01" src="https://user-images.githubusercontent.com/92742400/222730981-4b6e63cf-d41e-4ec5-a388-850dfbd1e3a9.png">

3. ###### The app will display the highest compatible power for the selected component in each selected region.
<img width="788" alt="Screenshot 2023-03-03 at 14 46 17" src="https://user-images.githubusercontent.com/92742400/222731033-b0555884-8181-435f-885c-e553cbc38f3c.png">

-------------
### Troubleshooting 
- If you get an error message that the required packages are not installed (**'ModuleNotFoundError'**), make sure you have installed the prerequisites as described above.
- If you get an error message that the input file could not be found (**'FileNotFoundError'**), make sure you have changed the file path in the code to match the location of the input file on your machine.

-------------
### Suggested features 
##### Future iterations of the project could include some of the following improvements:
1. ###### Delete power item: Allow the agent to delete a power from the compatibility or inventory list.
2. ###### Agents should be able to enter the quantity of the new inventory and the region where it is available.
3. ###### Allow the agent to add a new component to the components list, with its compatible powers, and inventory.
4. ###### Connect two powers as compatibles: Allow the agent to connect two powers as compatible with each other.
6. ###### If the power or region is not already in the inventory list, the tool should prompt the agent to create a new entry.
7. ###### Inventory Overview Dashboard: This dashboard would display an overview of inventory levels for each power and region, highlighting any low inventory levels that need attention.
8. ###### Component Compatibility Dashboard: This dashboard would display a visual representation of component compatibility between different powers, making it easier for agents to quickly identify compatible replacement options.
9. ###### Historical Data Dashboard: This dashboard would display historical data on call volume, inventory levels, and component usage over time. This could help managers make data-driven decisions and plan for future inventory needs.



&copy; SolarEdge

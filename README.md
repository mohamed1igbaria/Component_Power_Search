<img width="468" alt="solaredge" src="https://user-images.githubusercontent.com/92742400/222926917-0cc3e26c-89d5-4731-a4b9-9b5b9acf4067.png">

# Component Power Search

##### Using the provided data this application enables you to identify the optimal power pairing for diverse components in various regions. 
##### By exploring all feasible inventory alternatives, the app selects the option with the maximum quantity. 
##### Additionally, the app visualizes the inventory power to identify low quantity, providing you with a comprehensive understanding of available power options.

- Note 1: The "Table 1" sheet in the data file (xlsx) contains an asymmetric table. To address this, I assumed that the table should be symmetric, I ran the function "extract_compatible_power" on the columns up to "Y1300". After that, I ran the same function by rows.

- Note 2: The "Confirm" and "Report" buttons are non-functional and are used only to display relevant messages.

-------------
## Getting Started
### Installation
1. ###### Install Python 3, You can download Python from the official website: https://www.python.org/downloads/
2. ###### Install the required packages by running the following command in your terminal (make sure that you are running this command in the correct environment):
```
pip install -r requirements.txt
```
-------------
### Running the App
1. ###### Clone this repository to your local machine:
```
git clone https://github.com/mohamed1igbaria/Component_Power_Search.git
```

2. ###### In your terminal Navigate to the project directory by changing the <path>:
```
cd <path>/Component_Power_Search
```

3. ###### Run the app using the following command in your terminal:
```
streamlit run pwr_search.py
```

4. ###### The app will open in a new browser window at http://localhost:8501.
-------------
### Using the App
1. ###### Select a component from the dropdown menu.
<img width="1586" alt="Screenshot 2023-03-04 at 21 49 15" src="https://user-images.githubusercontent.com/92742400/222927274-524f5fec-5e89-4fec-8d21-2f3e0eaa5f72.png">

2. ###### Select one or more regions from the multiselect menu.
<img width="1563" alt="Screenshot 2023-03-04 at 22 29 20" src="https://user-images.githubusercontent.com/92742400/222927425-1d9565d6-4fac-4632-b9a1-bf935ef8ca22.png">
<img width="1587" alt="Screenshot 2023-03-04 at 21 49 45" src="https://user-images.githubusercontent.com/92742400/222927471-24c344be-935a-429f-a592-1c753b23f8ee.png">

3. ###### The maximum quantity of compatible power will be displayed on the screen, with bar charts showing the quantity of each power option for the selected component in each chosen region. The bar charts will be sorted in descending order, and will include all available compatible power options..
<img width="1518" alt="Screenshot 2023-03-04 at 20 34 50" src="https://user-images.githubusercontent.com/92742400/222927835-f9e86e88-1730-4968-a41f-12d92fe8057c.png">

4. ###### To verify the Power token, click the "Confirm" button. If you accidentally confirm the token, you have 5 seconds to undo the action by clicking the "Cancel" button.
<img width="1588" alt="Screenshot 2023-03-04 at 21 50 03" src="https://user-images.githubusercontent.com/92742400/222930205-cc9b1531-17da-4bf6-8a2d-53289b520e3b.png">
<img width="1588" alt="Screenshot 2023-03-04 at 21 50 12" src="https://user-images.githubusercontent.com/92742400/222928701-8d4ac4ad-2774-4e02-9afe-c088d628dc5d.png">

5. ###### If there are no compatible power quantity available, the agent can notify the relevant personnel about the issue by pressing "Report" button.
<img width="1587" alt="Screenshot 2023-03-04 at 21 50 26" src="https://user-images.githubusercontent.com/92742400/222928864-5d2a561e-f434-4dc2-86a2-a4328f8197f6.png">

6. ###### In the "Inventory" tab, regardless of the selected component the stock personnel can easily visualize the inventory to identify any empty power sources at a glance, enabling efficient inventory management and timely restocking as required. Additionally, a slider is provided to display the relevant power of the chosen diverse quantity, organized by regions.
<img width="1586" alt="Screenshot 2023-03-04 at 21 51 04" src="https://user-images.githubusercontent.com/92742400/222929240-bd217f4d-3a26-4085-a639-67328e859d08.png">
<img width="1590" alt="Screenshot 2023-03-04 at 21 52 56" src="https://user-images.githubusercontent.com/92742400/222929262-db387cc0-53b9-4f65-866b-b206b4de9bc0.png">


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
5. ###### If the power or region is not already in the inventory list, the tool should prompt the agent to create a new entry.
6. ###### Historical Data Dashboard: This dashboard would display historical data on call volume, inventory levels, and component usage over time. This could help managers make data-driven decisions and plan for future inventory needs.



&copy; SolarEdge

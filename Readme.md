# Rice Yield Predictor Web App
This project is a web application that predicts agricultural yield based on various input parameters such as energy use, water use, fertilizer use, pesticide use, rural population, and pesticide imports.

## Step-by-Step Installation  

### Clone the Repository  

1. Open your terminal or Git Bash.  

2. Navigate to the folder where you want to store the project

3. Clone the repository:  
   ```bash  
   git clone https://github.com/ltfrosty/webapp.git  
   ```  

### Navigate to the Project Directory  
1. Navigate to where you git cloned the repository

2. Go into the folder for this project:  
   - Windows:  
     ```bash  
     cd webapp  
     ```  
   - Unix/MacOS:  
     ```bash  
     cd webapp 
     ```  

### Set Up a Virtual Environment  

1. Ensure **pipenv** is installed:  
   ```bash  
   pip install --user pipenv  
   ```  
2. Install project dependencies:  
   ```bash  
   pipenv install  
   ```  
3. Activate the virtual environment:  
   ```bash  
   pipenv shell  
   ```  

### Run the Web App  

1. Navigate to the project folder:  
   ```bash  
   cd webapp 
   ```  
2. Start the Flask application:  
   ```bash  
   flask run  
   ```  
3. Open a browser and go to `http://127.0.0.1:5000/` to access the app. 

## Usage

1. Navigate to the web application.
2. Input the required parameters such as energy use, water use, fertilizer use, pesticide use, rural population, and pesticide imports.
3. Click the "Predict" button to get the predicted rice yield.

## License

This project is licensed under the MIT License.
    

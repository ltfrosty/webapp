# Rice Yield Predictor Web App
This project is a web application that predicts agricultural yield based on various input parameters such as energy use, water use, fertilizer use, pesticide use, rural population, and pesticide imports.

# Project Structure
__pycache__/
.ebextensions/
    miniproject1.config
.ebignore
.flaskenv
.gitignore
app/
    __init__.py
    __pycache__/
    middleware.py
    routes.py
    static/
        __target__/
            copy.js
            library.js
            library.project
            math.js
            org.transcrypt.__runtime__.js
            random.js
        library.py
    templates/
        index.html
application.py
DeployEB.md
Pipfile
Pipfile.lock
runflaskvoc.sh

# Step-by-Step Installation  

## Clone the Repository  

1. Open your terminal or Git Bash.  
2. Navigate to the folder where you want to store the project:  
   ```bash  
   cd Downloads  
   ```  
3. Clone the repository:  
   ```bash  
   git clone https://github.com/Data-Driven-World/d2w_mini_projects  
   ```  

## Navigate to the Project Directory  

1. Go to the folder for this project:  
   - Windows:  
     ```bash  
     cd d2w_mini_projects\mp_sort  
     ```  
   - Unix/MacOS:  
     ```bash  
     cd d2w_mini_projects/mp_sort  
     ```  

## Set Up a Virtual Environment  

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

## Run the Web App  

1. Navigate to the root folder:  
   ```bash  
   cd ~/Downloads/d2w_mini_projects/mp_sort  
   ```  
2. Start the Flask application:  
   ```bash  
   flask run  
   ```  
3. Open a browser and go to `http://127.0.0.1:5000/` to access the app. 

# Usage

1. Navigate to the web application.
2. Input the required parameters such as energy use, water use, fertilizer use, pesticide use, rural population, and pesticide imports.
3. Click the "Predict" button to get the predicted rice yield.

# License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
    
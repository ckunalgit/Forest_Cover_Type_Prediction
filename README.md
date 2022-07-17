# Forest_Cover_Type_Prediction
This model is helpful in noticing the changes occurred due to heavy floods or any other calamities which affected the forest land

# Creating virtual env for project
conda create -p venv_ffcp python=3.7 -y

# Activating conda env
conda activate E:\ineuron\vs\projects\Forest_Cover_Type_Prediction\venv_ffcp

# Install required libraries {Before running this, created setup.py file, else this step will fail as we have a '.e' in our requirements file}
pip install -r requirements.txt

# To remove env folder from git
git rm --cached -r venv_ffcp
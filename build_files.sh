# Print a message indicating the build process is starting
echo " BUILD START"

# Install the required Python packages specified in the requirements.txt file using pip
# The -m option runs the pip module as a script using Python 3.9
python3.9 -m pip install -r requirements.txt

# Collect all the static files in the Django project
# The --noinput option runs the command without prompting for user input
# The --clear option deletes the existing static files before collecting the new ones
python3.9 manage.py collectstatic --noinput --clear

# Print a message indicating the build process has ended
echo " BUILD END" 

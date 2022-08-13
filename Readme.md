#Team96 - Anima_lib

## Relevant Links

- #### [Database Schema](https://www.figma.com/file/dbuMWTtl6UgEcVcvtI97Np/Untitled?node-id=0%3A1)
- #### [Figma](https://www.figma.com/file/gFDREjDvch3LiCT3x1jmRN/Team-96_Anima-lib?node-id=1734%3A7634)
- #### [First Presentation](https://drive.google.com/file/d/17mP2BijevHPgeVjKOV6op29VJttYO148/view?usp=sharing)

### **_Fork and Clone Repository_**

1. Visit the Repository to the Project on Github Website: https://github.com/zuri-training/Team96_Anima-lib
2. Click the "Fork" button on the upper right corner of the Repo page.
3. Clone the forked repository to your local machine (computer)

   - Click on the "Code" button on the Repo page
   - Copy the URL for the forked Repo. Something like - https://github.com/github_username/Team96_Anima-lib
   - Create a Folder on your Local machine / Computer for the project Workspace
   - Open Command prompt / Terminal in the same folder location
   - In your Terminal, type:
     `git clone https://github.com/github_username/Team96_Anima-lib`
   - Ensure that "github_username" in the link is your username!

### **_Add Remote to Upstream_**

4. Add git Remote to Upstream:
   - In your terminal, type:
     `git remote add upstream https://github.com/zuri-training/Team96_Anima-lib`

### **_Pull from Upstream_**

5. Pull from upstream to download all changes in the project using `git pull upstream main`

### **_Create and checkout a new branch_**

6. - In your terminal, type:
     `git checkout -b new-branch-name`
     The "new-branch-name" can be anything you want to name the branch with.

### **_Finish assigned Task / Issue_**

7. Enter the project folder/file and complete your assigned task / feature on your local machine as you would normally do.

8. When you are ready to add and push your feature or task to the Repo
   You can confirm if you are in the right branch with: `git branch`

   - Add your changes using:
     `git add file_name `
   - Commit your changes to the branch with a message using
     `git commit -m "Commit message"`

     Note: If you only fixed a bug, make your commit message start with "fixed a bug:" then whatever bug you fixed.
     Something like this: `git commit -m "fixed a bug: I corrected the nav bar of the homepage"`

### **_Push New Branch to "Origin" Repository_**

9. Push your commit to your branch
   `git push origin new-branch-name`

### **_Create Pull Request_**

11. Once you push the changes to your repo/branch, the **_`Compare & pull request`_** button will appear in GitHub page of your repo.
12. Click the button and make your request. Leave a comment in your request.
13. Click Create pull request to open a new pull request.


## **_Working with the Django project_**

### You'll have to install your own virtual environment and install the dependencies. Follow these steps.

1. Step 1: Go to your terminal and type --> pip install virtualenv
2. Step 2: Create your own virtual environment --> virtualenv "whatever name you choose for your virtual environment"
3. Step 3: Activate your virtual environment --> cd (name of virtual environment from step 2)
4. Step 4: Write this (scripts/activate) into the terminal
5. Step 5: Install dependencies --> pip install -r requirements.txt (This might not be necessary though)
6. Step 6: Write (python manage.py createsuperuser) into the terminal
7. Step 7: python manage.py makemigrations
8. Step 8: python manage.py migrate
9. Step 7: Write (python manage.py runserver) into the terminal
10. Step 8: Do your thing.

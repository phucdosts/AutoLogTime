# Auto Log Time

## Installation instruction
1. Download the source code from the git repository https://github.com/phucdosts/AutoLogTime, 
   or you can download the .zip file + unzip it
   ![img.png](introduction-img/git-repo.png)
   
2. Fill your username - password to login the insider portal and other data such as activity and project etc. in the 
   quote mark 
![img.png](introduction-img/fil-data.png)

1. Download and install python from https://www.python.org/downloads/release/python-395/ or any version of python, 
  download the `Windows installer`
   
- Install python by clicking the option `Install Now`, remember to enable the checkbox `Add Python x.x to PATH`
![img.png](introduction-img/python-installer.png)
  

2. Open the environment variables and make sure that you have the `Python Path` in the settings, 
  the path may be different due to your installation configuration 
  (check the installation path in the `Install Now` option to see the `Python Path`)
![img_1.png](introduction-img/search-environment-variable.png)
![img.png](introduction-img/advance-tab.png)
![img.png](introduction-img/environment-path.png)
![img.png](introduction-img/python-path.png)
  
3. Open the cmd and check for Python and install `Selenium`
![img.png](introduction-img/cmd.png)

- Check if we install Python correctly by the command `python --version` and `pip --version`
- Install the selenium library with the command `pip install -U selenium`, 
  you can see the installed packages with the command `pip list`, it's required to have these 4 packages below
![img.png](introduction-img/selenium-installation.png)
  
4. Set up window task scheduler
- Open the `Task scheduler`
![img.png](introduction-img/task-scheduler.png)
- Create new task and give it a name
![img.png](introduction-img/task-scheduler-general.png)
- Set a schedule
![img.png](introduction-img/task-scheduler-trigger.png)
- Set up the action
- `Program/script` is the `Python path`, Eg: `C:\Users\phuc.do\AppData\Local\Programs\Python\Python39\python.exe`
- `Add arguments` is the `script name`, Eg: `main.py`
- `Start in` is the `AutoLogTime directory path`, Eg: `C:\Users\phuc.do\PycharmProjects\autolog`
![img.png](introduction-img/task-scheduler-action.png)
![img.png](introduction-img/python-exe-path.png)
![img.png](introduction-img/autolog-path.png)
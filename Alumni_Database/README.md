# Steps to run Nexus Consulting application

1.	Install MySQL onto your Windows machine. Keep admin password as ‘root’.
  - a.	To download MySQL installer, go to the following link http://dev.mysql.com/downloads/installer/.
  - b.	To install MySQL using the MySQL installer, double-click on the MySQL installer file and follow the steps below:
    1)	 Windows configures MySQL Installer

    ![Image1](https://github.com/ankity09/learn/blob/master/Alumni_Database/images/image1.png)
    
    2)	 Welcome Screen: A welcome screen provides several options. Choose the first option: Install MySQL Products
    
    ![Image2](https://github.com/ankity09/learn/blob/master/Alumni_Database/images/image2.png)
    
    3) Download the latest MySQL products: MySQL installer checks and downloads the latest MySQL products including MySQL server, MySQL Workbench, etc.
    
    ![Image3](https://github.com/ankity09/learn/blob/master/Alumni_Database/images/image3.png)
    
    4)	Click Next button to continue
    
    ![Image4](https://github.com/ankity09/learn/blob/master/Alumni_Database/images/image4.png)
    
    5)	Choosing a Setup Type: there are several setup types available. Choose the Full option to install all MySQL products and features.
    
    ![Image5](https://github.com/ankity09/learn/blob/master/Alumni_Database/images/image5.png)
    
    6)	MySQL Server Configuration: choose Config Type and MySQL port (3006 by default) and click Next button to continue.
    
    ![Image6](https://github.com/ankity09/learn/blob/master/Alumni_Database/images/image6.png)
    
    7)	MySQL Server Configuration: choose a password (‘root’) for the root account. 
    
    ![Image7](https://github.com/ankity09/learn/blob/master/Alumni_Database/images/image7.png)
    
    8) Follow the next steps, and complete the installation.

2.	Use the Provided .sql query files in the folder named ‘SQL Queries’ to create and populate database on MySQL.

3.	Install WAMP server onto your Windows machine. Instructions to install can be found here https://websiteforstudents.com/getting-apache2-mysql-php-windows-10/

4.	Run WAMP server, and run Apache Web Server and MySQL Server from the WAMP Server control panel.
Change the Apache Server listening port to 8080.

5.	Paste the two .php files provided to C:\wamp64\www\HTML.

6.	Open Chrome, and type ‘http://localhost:8080/HTML/Project0503-02_nexus.php’

7.	Within the application, select the tab you are interested in getting information about, apply the filters as desired, and press Submit.


## Application Screenshots

### Alumni Based out of Chicago

![UI1](https://github.com/ankity09/learn/blob/master/Alumni_Database/images/UI1.png)

![Result1](https://github.com/ankity09/learn/blob/master/Alumni_Database/images/Result1.png)

### Alumni Graduated before 2014 with a CGPA above 3.5

![UI2](https://github.com/ankity09/learn/blob/master/Alumni_Database/images/UI2.png)

![Result2](https://github.com/ankity09/learn/blob/master/Alumni_Database/images/Result2.png)


## ERD Diagram 

![Project0503-02_ERD](https://github.com/ankity09/learn/blob/master/Alumni_Database/images/Project0503-02_ERD.png)

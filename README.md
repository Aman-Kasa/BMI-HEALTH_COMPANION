![BMI Health Companion](https://th.bing.com/th/id/R.1889d0320aa1b0d11adbfebde1cac649?rik=qziqfqARWRUzyg&pid=ImgRaw&r=0)
BMI Health Companion
Welcome to the BMI Health Companion, an application designed to help users calculate their Body Mass Index (BMI) based on their height and weight. The app utilizes an external API to fetch accurate BMI calculations and provide valuable insights into your health status.

  # Features
1) Calculate BMI: Input your weight and height, and the app will compute your BMI.

2) Category Classification: The app classifies your BMI into categories (Underweight, Normal weight, Overweight, and Obesity).

3) Health Insights: Based on your BMI, the app provides useful health tips and guidelines for maintaining a healthy lifestyle.

4) Technology Stack
   a) Frontend: HTML, CSS, JavaScript
   b) Backend: The application utilizes the BMI Calculator API from RapidAPI to compute BMI.
   c) python(flask)

5) API Used
This project uses the Body Mass Index (BMI) Calculator API provided by Principal APIs to perform the BMI calculation. This API allows the application to calculate BMI efficiently by taking height and weight inputs and classifying the result accordingly.

 # API Documentation:
Base URL: https://rapidapi.com/principalapis/api/body-mass-index-bmi-calculator

Endpoint: /calculate

Method: POST

API Key: Make sure to sign up at RapidAPI to obtain your API key.

  # How to Use
1) Clone this repository to your local machine:
   git clone https://github.com/Aman-Kasa/BMI-health_companion.git

2) Navigate to the project directory:
    cd BMI-health_companion

3) Open the index.html file in your browser to launch the application.

4) Input your weight and height in the respective fields and click Calculate to get your BMI and health status.

   
   # Here’s a list of file types and directories in a .gitignore file:

1) Environment files: .env, .env.template

2) Virtual environments: venv/, myenv/

3) Node dependencies: node_modules/

4) OS-generated files: .DS_Store (macOS), Thumbs.db (Windows)

5) Compiled code: .pyc, .pyo, __pycache__/

6) Logs: *.log
    Secrets: *.key, *.pem
   

   # Deployment

1) The application is deployed on a web server and can be accessed through the provided URL.
        (6262-web-01 ubuntu	54.196.180.228) (6262-web-02 ubuntu	23.22.186.247)  (6262-lb-01	ubuntu 3.90.2.171)

2) Make sure you configure the API key properly to avoid unauthorized access.

3) To deploy this on your server, follow the necessary steps for web hosting or use services like GitHub Pages or any hosting provider of your choice.



   # Credits
API: BMI Calculator API by Principal APIs

   # DEMO Link
https://youtu.be/TwAQJqNOBGY?feature=shared







# Online-Foodie
Foodie is an online food delivery platform designed to offer a seamless experience for users to browse local restaurants, order their favorite meals, and get them delivered swiftly to their doorstep. 
Project Name: Online Food Delivery Website with Payment Integration
Description:
This project is a fully functional Online Food Delivery Website that allows customers to browse various food items, add them to their cart, and securely process payments through Stripe's API. It offers a seamless and secure ordering experience with a focus on user convenience and security.

The website is built using Django as the backend framework and integrates with Stripe for handling credit card payments. The frontend is developed using HTML5, CSS3, and JavaScript, creating a modern and responsive interface optimized for both desktop and mobile devices.

Features:
Food Menu Display: Users can browse through different food items with descriptions and images.
Shopping Cart: Add, and update food items in the cart before proceeding to checkout.
Secure Payment Integration: Uses Stripe API to ensure secure and reliable credit card payments.
Real-Time Payment Validation: Instant feedback on payment information with Stripe Elements to ensure all details are correctly entered.
Order Summary: Displays the total amount before proceeding to payment.
Responsive Design: The website is fully responsive, ensuring a smooth experience across various screen sizes.
Error Handling: Provides error messages for invalid card information and failed transactions.

Tech Stack:
Backend: Django 4.0 (Python)
Frontend: HTML5, CSS3, JavaScript
Payment Integration: Stripe API
Database: SQLite (or any Django-compatible database)
Version Control: Git
Deployment: Ready for deployment on platforms that support Django

Installation and Setup:

1.Clone the Repository:
git clone https://github.com/your-username/online-food-delivery-site.git

2.Navigate to the project directory:
cd online-food-delivery-site

3.Install Dependencies: Ensure you have Python and pip installed. Run the following command to install the required packages:
pip install -r requirements.txt

4.Configure Stripe API Keys: Update your Stripe API keys in the settings.py file:
STRIPE_PUBLISHABLE_KEY = 'your-publishable-key'
STRIPE_SECRET_KEY = 'your-secret-key'

5.Run Database Migrations: Set up the database with:
python manage.py migrate

6.Run the Development Server: Start the Django development server with:
python manage.py runserver

7.Access the Website: Open your browser and visit http://127.0.0.1:8000 to start browsing and ordering food.

If you'd like to contribute to the project:

Fork the repository
Create a new branch for your feature (git checkout -b feature/new-feature)
Commit your changes (git commit -m 'Add new feature')
Push to your branch (git push origin feature/new-feature)
Open a Pull Request


License:
This project is open-source and licensed under the MIT License.

Future Enhancements:
User Profiles: Implement user login and profiles to save past orders and preferences.
Discount and Offers: Integrate a discount system for promotions and coupon codes.


ScreenShots:
![Foodie01](https://github.com/user-attachments/assets/446dcd02-b76c-41dd-bcfc-2b35f03ea4ec)
![Foodie02](https://github.com/user-attachments/assets/b16eb9ca-b3e5-4c76-931f-584035c3a702)
![Foodie03](https://github.com/user-attachments/assets/6706f298-3fe7-4f65-80f7-3b64a9546eea)
![Foodie04](https://github.com/user-attachments/assets/b00959ae-e643-4660-b850-94d700b6afe3)
![Foodie06](https://github.com/user-attachments/assets/47586748-5c82-41d6-86a4-2dbec5d953ee)

Administration:
![food bk](https://github.com/user-attachments/assets/4bf35984-fccb-4dc3-ad1d-57e951971e57)
![food bk01](https://github.com/user-attachments/assets/269ce1c7-80b8-42ef-badf-cd0dd32467c5)



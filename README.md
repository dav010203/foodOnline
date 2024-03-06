# Multi-Vendor Restaurant Marketplace

## Introduction
Welcome to the Multi-Vendor Restaurant Marketplace project, built with Django! This platform allows multiple restaurants to list their menus and manage orders while providing customers with a variety of culinary options from different vendors.

## Features
- Multi-vendor support: Different restaurants can register and showcase their menus.
- Product management: Vendors can add, update, and delete their menu items.
- Order management: Customers can place orders, and vendors can manage these orders.
- User authentication: Support for customer and vendor sign-up/sign-in.
- Location based search and filtering: Customers can search for dishes or nearby restaurants and filter by categories.

## Getting Started

### Prerequisites
Dependencies listed in `requirements.txt`

### Installation
1. Clone the repository to your local machine:
git clone https://github.com/dav010203/foodOnline.git
2. Navigate to the project directory:
cd foodOnline
3. Install the required dependencies:
pip install -r requirements.txt
4. Set up the database:
python manage.py migrate
5. Create a superuser:
python manage.py createsuperuser
6. Run the server:
python manage.py runserver
7. Visit `http://127.0.0.1:8000/` in your browser.

## Usage
- As a vendor, you can register your restaurant, add menu items, and manage orders.
- As a customer, you can browse different restaurants, view menus, and place orders.

## Contributing
Contributions are welcome! Please feel free to fork the repository, make changes, and submit pull requests.
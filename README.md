# Food Delivery Backend API

This is a backend API for a food delivery service built using Django and Django Rest Framework. The API allows restaurant owners to manage their restaurants, categories, menu items, modifiers, and customers to place orders.

## Features

- **User Roles**: Supports owners and employees for each restaurant.
- **Menu Management**: Restaurant owners and employees can manage menus, categories, menu items, and modifiers.
- **Order Management**: Customers can place orders and pay via card or cash.
- **Authentication**: Custom user authentication using Django's built-in authentication system with token-based authentication.

## Getting Started

### Prerequisites

Before you begin, make sure you have Python 3.8 or later installed on your machine.

### Installation

1. Clone the repository:

   ## bash ##
   git clone https://github.com/RumelNHORS/food_delivery.git
   cd food_delivery

2. Set up a virtual environment:
    python -m venv env
    ## Linux ##
    source env/bin/activate 
    ## Windows ##
    source env\Scripts\activate

3. Install the dependencies:
    pip install -r requirements.txt

4. Apply database migrations:
    python manage.py makemigrations
    python manage.py migrate

5. Create a superuser to access the Django admin panel:
    python manage.py createsuperuser

6. Run the development server:
    python manage.py runserver



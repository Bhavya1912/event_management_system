# Event Management System

This is a Django web application for a fictional event management system. The application provides REST APIs for managing events, registrations, venues, and users. It supports two types of user roles: Admin and Participants.

## Tech Stack

- Django (with Django Rest Framework)
- PostgreSQL / SQLite / MySQL (choose the appropriate database for your setup)

## Setup Instructions

1. Clone the repository:
```
git clone git@github.com:Bhavya1912/event_management_system.git
```
2. Navigate to the project directory:
```
cd event-management-system
```

3. Create and activate a virtual environment (optional but recommended):
```
python -m venv venv
source venv/bin/activate
```


4. Install the dependencies:
```
pip install -r requirements.txt
```

5. Configure the database:
- Open the `settings.py` file in the `event_management_system` directory.
- Update the database settings according to your setup (e.g., database engine, name, user, password).
- Save the file.

6. Apply database migrations:
```
python manage.py migrate
```

7. Start the development server:
```
python manage.py runserver
```


8. The application should now be running at `http://localhost:8000/`. You can access the APIs using an API testing tool like Postman.

## API Documentation

For detailed API documentation and examples, please refer to the [API Documentation](api_documentation.md) file.

## Testing

The APIs have been tested using Postman. You can find the Postman collection in the [Postman Collection](postman_collection.json) file.

## Deployment

This application can be deployed to a hosting provider of your choice. Ensure that you configure the appropriate environment variables, such as database credentials and secret keys.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

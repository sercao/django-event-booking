# Django Event Booking

A simple Django application for booking events. Users can create events, make reservations, and add comments.

## Features

- User authentication
- Event creation, editing, and deletion
- Reservation management
- Email notifications for reservations
- Commenting on events

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/sercao/django-event-booking.git
    cd django-event-booking
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up the database:
    ```sh
    python manage.py migrate
    ```

5. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```sh
    python manage.py runserver
    ```

7. Open your browser and go to `http://127.0.0.1:8000`.

## Usage

- Register a new user or log in with an existing account.
- Create, edit, or delete events.
- Make reservations for events.
- View and manage your reservations.
- Add comments to events.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request.

## License

This project is licensed under the MIT License.

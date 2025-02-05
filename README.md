# EvalEasy MS Test

This microservice is designed to manage and generate tests for educational purposes. It allows instructors to create subjects, question pools, questions with answers, and generate tests with multiple variants. The generated tests can be downloaded as Word documents.

## Features
- Create subjects, question pools, and questions with answers.
- Generate tests with multiple variants.
- Download generated tests as Word documents.
- Regenerate test files.

## Endpoints
### Subjects
- `POST /api/subjects/` - Create a new subject.

### Questions
- `POST /api/questions/` - Create a new question with nested answers.

### Question Pools
- `POST /api/question-pools/` - Create a new question pool.

### Tests
- `POST /api/generate-test/` - Generate a new test with multiple variants.
- `POST /api/regenerate-test/<int:test_id>/` - Regenerate the Word file for an existing test.
- `GET /api/download-word/<int:test_id>/` - Download the generated Word file for a test.
- `GET /api/tests/<str:assessment_id>/correct_answers/` - Get the correct answers for a test.

## Requirements
- Python 3.8+
- Django 5.1.5
- Django REST framework 3.14.0
- psycopg2-binary 2.9.3
- python-docx 0.8.11
- PostgreSQL

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/1javid/evaleasy-ms-test.git
    cd evaleasy-ms-test/ms_test
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## PostgreSQL Setup
1. Install PostgreSQL and create a new database:
    ```sh
    sudo -u postgres psql
    CREATE DATABASE ms_test;
    CREATE USER postgres WITH PASSWORD '1234';
    ALTER ROLE postgres SET client_encoding TO 'utf8';
    ALTER ROLE postgres SET default_transaction_isolation TO 'read committed';
    ALTER ROLE postgres SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE ms_test TO postgres;
    \q
    ```

2. Apply the migrations:
    ```sh
    python manage.py migrate
    ```

## Usage
1. Run the development server:
    ```sh
    python manage.py runserver 8001
    ```

2. Access the API at [http://127.0.0.1:8001/api/](http://_vscodecontentref_/1)

3. Use the provided endpoints to create subjects, question pools, questions, and generate tests.

4. Download the generated test files using the provided download endpoint.
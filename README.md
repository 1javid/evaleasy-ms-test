# EvalEasy MS Test

This microservice is designed to manage and generate tests for educational purposes. It allows instructors to create subjects, question pools, questions with answers, and generate tests with multiple variants. The generated tests can be downloaded as Word documents.

## Features
- Create subjects, question pools, and questions with answers.
- Generate tests with multiple variants.
- Download generated tests as Word documents.
- Regenerate test files.

## Endpoints

### Subjects

- `POST /api/test/subjects/` - Create a new subject.
- `GET /api/test/subjects/list/` - List all subjects.
- `GET /api/test/subjects/<int:pk>/` - Retrieve a specific subject by ID.

### Questions

- `POST /api/test/questions/` - Create a new question with nested answers.
- `POST /api/test/questions/bulk/<int:question_pool_id>/` - Create many questions given a question pool ID.
- `GET /api/test/questions/question-pool/<int:question_pool_id>/` - List questions by question pool ID.
- `DELETE /api/test/questions/question-pool/<int:question_pool_id>/delete/<int:question_id>/` - Delete questions by question pool ID.

### Question Pools

- `POST /api/test/question-pools/` - Create a new question pool.
- `GET /api/test/question-pools/subject/<int:subject_id>/` - List question pools by subject ID.

### Tests

- `POST /api/test/generate-test/` - Generate a new test.
- `GET /api/test/tests/subject/<int:subject_id>/` - List tests by subject ID.
- `GET /api/test/tests/<str:assessment_id>/` - Retrieve a test by assessment ID.
- `GET /api/test/tests/<str:assessment_id>/questions/` - List test questions by assessment ID.
- `GET /api/test/tests/subject/<int:subject_id>/group-ids/` - List group IDs by subject ID.
- `GET /api/test/tests/group/<str:group_id>/` - List tests by group ID.
- `GET /api/test/tests/group/<str:group_id>/download-link/` - Download a zip file of all tests with the same group ID.
- `POST /api/test/regenerate-test/<int:test_id>/` - Regenerate a test file.
- `GET /api/test/download-word/<int:test_id>/` - Download the Word file for a specific test.
- `GET /api/test/tests/<str:assessment_id>/correct_answers/` - Get correct answers for a test by assessment ID.
- `GET /api/test/tests/<str:assessment_id>/questions/` - List test questions by assessment ID.
- `GET /api/test/tests/subject/<int:subject_id>/group-ids/` - List group IDs by subject ID.
- `GET /api/test/tests/group/<str:group_id>/` - List tests by group ID.
- `GET /api/test/tests/group/<str:group_id>/download-link/` - Download a zip file of all tests with the same group ID.
- `GET /api/test/tests/<str:assessment_id>/` - Retrieve a test by assessment ID (previously by `pk`).


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

2. Access the API at http://127.0.0.1:8002/api/

3. Use the provided endpoints to create subjects, question pools, questions, and generate tests.

4. Download the generated test files using the provided download endpoint.
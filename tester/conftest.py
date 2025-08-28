import os
import pytest
from selenium import webdriver
import psycopg2


# ---------- Selenium Driver Fixture ----------
@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # assumes chromedriver is in PATH (in Docker it's preinstalled)
    yield driver
    driver.quit()


# ---------- Database Connection Fixture ----------
@pytest.fixture(scope="session")
def db_conn():
    """
    Fixture to provide a PostgreSQL DB connection.
    Reads details from environment variables.
    """
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        database=os.getenv("DB_NAME", "testdb"),
        user=os.getenv("DB_USER", "testuser"),
        password=os.getenv("DB_PASSWORD", "testpass"),
        port=os.getenv("DB_PORT", "5432"),
    )
    yield conn
    conn.close()


@pytest.fixture(scope="function")
def db_cursor(db_conn):
    """
    Fixture to provide a cursor for DB operations.
    Rolls back changes after each test so tests are isolated.
    """
    cur = db_conn.cursor()
    yield cur
    db_conn.rollback()
    cur.close()

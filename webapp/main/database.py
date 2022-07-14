import os
from dataclasses import dataclass

import psycopg
from psycopg.rows import class_row


@dataclass
class Fruit:
    id: str
    name: str
    fruit_type: str
    is_deleted: bool


def get_conn():
    uri = os.getenv('POSTGRES_URL')
    return psycopg.connect(uri)


def find_fruits():
    with get_conn() as conn:
        with conn.cursor(row_factory=class_row(Fruit)) as cur:
            return cur.execute('SELECT * FROM fruits where is_deleted = false')\
                .fetchall()


def save_fruit(fruit):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                'INSERT INTO fruits (id, name, fruit_type) VALUES (%s, %s, %s)',
                (fruit.id, fruit.name, fruit.fruit_type))

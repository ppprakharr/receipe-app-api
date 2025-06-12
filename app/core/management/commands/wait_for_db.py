"""
Django command to wait for the database to be available
"""

from django.core.management.base import BaseCommand
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError
import time


class Command(BaseCommand):
    """
    Django command to wait for db
    """

    def handle(self, *args, **kwargs):
        """entrypoint for command"""
        self.stdout.write("Waiting for Database...")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write("Unable to connect to db waiting..")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database Available"))

from __future__ import absolute_import
from django.core.management.base import BaseCommand, CommandError
import os,sys

class Command(BaseCommand):
    help = 'crawls the website for products and categories'

    def add_arguments(self, parser):
        parser.add_argument('args', nargs='*')

    def run_from_argv(self, argv):
        self._argv = argv[:] 
        super(Command, self).run_from_argv(argv)

    def handle(self, *args, **options):
        os.environ['SCRAPY_SETTINGS_MODULE'] = args[0]
        from scrapy.cmdline import execute
        execute(list(args))
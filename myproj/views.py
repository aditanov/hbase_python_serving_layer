
import json
import logging
import random
import threading

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.generic import TemplateView


import happybase


logger = logging.getLogger(__name__)

N_KEYS = 10000

#
# Initialization
#
# Importing this module has side-effects; way to go Django. :s
#

pool = happybase.ConnectionPool(
    size=3,
    host='172.30.0.173')


def index(request):
#HBASE_TABLE = 'program_prioritas_berita_perhari'

    start = 'row-key-%d' % random.randint(0, N_KEYS)
    with pool.connection() as connection:
        table = connection.table(settings.HBASE_TABLE)
        scan = table.scan(limit=4)
        output = list(scan)

#    if 'use-after-return' in request.GET:
        # XXX: It is an error to use the connection after it was
        # returned to the pool. The next line introduces a race
        # condition and may cause random errors when used in
        # a multi-threaded environment!
 #       connection.tables()

  #  logger.debug('Request from thread %s', threading.current_thread().name)

    return HttpResponse(json.dumps(output))
  
  #return HttpResponse(connection.tables())
        



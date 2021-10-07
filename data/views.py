import ast
import csv
import json
from decimal import Decimal

from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection, connections
import pandas as pd
from .config import data_to_cols


def my_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)

    return str(obj)


def homepage(request):
    return render(request, 'data/index.html')


def datapage(request):
    tables = connection.introspection.table_names()
    # print()
    return render(request, 'data/datas.html', context={'tables': tables})


def detail(request, table_name):
    if request.method == 'POST':
        print('vot tuta')
        print(request.POST)
        columns = ast.literal_eval(str(request.POST.getlist('column')))
        cols_as_list = ', '.join(columns)
        print(cols_as_list)
        cursor = connections['default'].cursor()
        print(cursor)
        # data = pd.read_sql("select {cols_list} from {table_name}".format(cols_list=cols_as_list, table_name=table_name),
        #                    connections['default'])
        # data =
        cursor.execute("select {cols_list} from {table_name}".format(cols_list=cols_as_list, table_name=table_name))
        query = cursor.fetchall()
        result_data = []
        for result in query:
            result_data.append(dict(zip(columns, result)))

        json_data = json.dumps(result_data, ensure_ascii=False, default=my_default)
        pd_data = pd.read_json(json_data)
        print(pd_data)
        request.session['json_data'] = json_data
        # print(json_data)
        # for q in query:
        #     print(q)
        return render(request, 'data/detail.html',
                      context={'json_data': json_data, 'table_name': table_name, 'column_names': columns})
    print(request.POST)
    print(table_name)
    cursor = connections['default'].cursor()
    print(cursor)
    cursor.execute("select * from {} limit 0".format(table_name))
    colnames = [desc[0] for desc in cursor.description]
    print(cursor.description)
    print(colnames)
    col_namedesc = data_to_cols[table_name]
    return render(request, 'data/detail.html', context={'table_name': table_name, 'col_namedesc': col_namedesc})


def export(request, table_name):
    # print('SALAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAM')
    # if request.method == 'POST':
    #     print(table_name)
    #     print('SALAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAM')
    #     print(request.POST)
    # return None
    json_data = request.session.get('json_data')
    pd_data = pd.read_json(json_data)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{table_name}.csv"'

    writer = csv.writer(response)
    writer.writerow(list(pd_data.columns))
    writer.writerows(list(pd_data.itertuples(index=False)))
    return response

import ast
import csv
import json
from decimal import Decimal

from django.http import HttpResponse
from django.shortcuts import render, redirect
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
    if request.method == 'POST':
        print(request.POST.get('freq'))
        table_name = 'data_' + '_'.join(request.POST.get(s) for s in ['freq', 'topic'])
        print(table_name)
        # cursor = connections['default'].cursor()
        # cursor.execute("select * from {} limit 0".format(table_name))
        # colnames = [desc[0] for desc in cursor.description]
        # print(cursor.description)
        # print(colnames)
        # col_namedesc = data_to_cols[table_name]
        return redirect('/datapage/' + table_name)
        # return render(request, 'data/detail.html', context={'table_name': table_name, 'col_namedesc': col_namedesc})
        # return render(request, 'data/datas.html')

    return render(request, 'data/datas.html')
    # tables = connection.introspection.table_names()
    # print()
    # return render(request, 'data/datas.html', context={'tables': tables})


def detail(request, table_name):
    if request.method == 'POST':
        print('vot tuta')
        print(request.POST)
        columns = ast.literal_eval(str(request.POST.getlist('column')))
        # cols_as_list = ', '.join(columns)
        cols_as_seq = ''
        for col in columns:
            cols_as_seq += '"{}"'.format(col)
            cols_as_seq += ','
        print(cols_as_seq)
        # print(columns)
        # query_str = '('
        # for c in columns:
        #     query_str += c
        # print(cols_as_list)
        cursor = connections['default'].cursor()
        print(cursor)
        # data = pd.read_sql("select {cols_list} from {table_name}".format(cols_list=cols_as_list, table_name=table_name),
        #                    connections['default'])
        # data =
        # cursor.execute("select {cols_list} from {table_name}".format(cols_list=cols_as_list, table_name=table_name))
        # cursor.execute(
        #     "select * from dict_variable where desc_en_vr in {cols_list}".format(cols_list=tuple(cols_as_list)))

        # cursor.execute(f'''
        # with temp as (
        # select distinct tarix
        # from {table_name}
        # )
        # ''')
        #
        # print()
        cursor.execute('''
        CREATE TEMP TABLE tabletemp
        (
        tarix timestamp
        );
        insert into tabletemp
        select distinct tarix from {table_name} order by tarix;
        '''.format(table_name=table_name))

        for col in tuple(columns):
            col.replace("'", "")
            query1 = '''
            ALTER TABLE tabletemp ADD COLUMN "{col_name}" numeric(38,10)
            '''.format(col_name=col)
            cursor.execute(query1)

            query2 = '''
            UPDATE tabletemp t SET "{col_name}" = t1.values FROM
            (SELECT d.tarix, d.values FROM data_m_macro d
             JOIN tabletemp t 
             ON d.tarix = t.tarix
             where id_vr = (select id_vr from dict_variable where desc_en_vr = '{col_name}')) t1
             where t1.tarix = t.tarix
            '''.format(col_name=col)
            cursor.execute(query2)

        # query = '''select * from {table_name} where id_vr in
        #     (select id_vr from dict_variable where desc_en_vr in {cols_list})'''.format(
        #     table_name=table_name, cols_list=tuple(columns))
        # TODO - split varnames into cotations!!! - DONE
        # ('Nominal GDP', 'Non-oil GDP')
        # print(query)
        cursor.execute('''select {cols} from tabletemp'''.format(cols=cols_as_seq[:-1]))
        query = cursor.fetchall()
        print('tut query')
        print(query)
        result_data = []
        cursor.execute('''
        DROP TABLE tabletemp;
        ''')
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
    col_namedesc = []
    cursor.execute("SELECT DISTINCT desc_en_vr FROM data_m_macro JOIN dict_variable USING(id_vr)")
    col_namedesc = [item[0] for item in cursor.fetchall()]
    print(col_namedesc)
    # cursor.execute("select * from {} limit 0".format(table_name))
    # colnames = [desc[0] for desc in cursor.description]
    # print(cursor.description)
    # print(colnames)
    # col_namedesc = data_to_cols[table_name]
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

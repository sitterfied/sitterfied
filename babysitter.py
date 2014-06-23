#!/usr/bin/python
import psycopg2
import requests


def main():
    # conn_string = "host='sitterfied-alewisohn.azva.dotcloud.net' port='1631' dbname='sitterfied' user='root' password='5KwP90YVA1E9zGLl5pSj'"
    conn_string = "host='beta-alewisohn.azva.dotcloud.net' port='1278' dbname='sitterfied' user='root' password='ge4WmFz38zPLSciaNcDs'"

    # print the connection string we will use to connect
    print "Connecting to database\n	->%s" % (conn_string)

    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()

    # execute our Query
    cursor.execute("""SELECT
        up.first_name as first_name,
        up.last_name as last_name,
        up.email as email,
        count(t.sitter_id) as team_size,
        string_agg(us.first_name || ' ' || us.last_name, ', ') as sitter_name,
        string_agg(us.email, ',') as sitter_email,
        string_agg(us.avatar, ', ') as sitter_avatar
    FROM public.app_parent_sitter_teams t
    LEFT OUTER JOIN public.app_user up on up.id = t.parent_id
    LEFT OUTER JOIN public.app_user us on us.id = t.sitter_id
    GROUP BY t.parent_id, up.first_name, up.last_name, up.email
    ORDER BY t.parent_id
    """)

    # retrieve the records from the database
    records = cursor.fetchall()

    # print out the records using pretty print
    # note that the NAMES of the columns are not shown, instead just indexes.
    # for most people this isn't very useful so we'll show you how to return
    # columns as a dictionary (hash) in the next example.
    # pprint.pprint(records)

    json_parent = ""
    count = 0
    for record in records:
        count += 1
        json_parent += "{"
        json_parent += '"name" : "' + record[0].strip() + " " + record[1].strip() + '",'
        json_parent += '"email" : "' + record[2].strip() + '",'

        sitter_names = record[4].split(',')
        sitter_emails = record[5].split(',')
        sitter_images = record[6].split(',')

        json_sitter = ''
        for i in range(0, int(record[3])):
            json_sitter += '{'
            json_sitter += '"name" : "' + sitter_names[i].strip() + '",'
            json_sitter += '"email" : "' + sitter_emails[i].strip() + '",'
            json_sitter += '"image" : "' + sitter_images[i].strip() + '"'
            json_sitter += '}'

            if(i != int(record[3]) - 1):
                json_sitter += ','

        json_parent += '"data" : {'
        json_parent += '"sitters" : [' + json_sitter + ']'
        json_parent += '}}'

        if(count != len(records)):
            json_parent += ','

    json = '{"contacts": [' + json_parent + ']}'

    print "Request body\n	->%s" % (json)

    # headers = {'Authorization': 'Token  # token="4a866b43f5f0f148d62fb8fcdf668d6f"'}  # Test
    headers = {'Authorization': 'Token token="eeaf1c3b2d47247cc401a3e7dc9162b5"'}  # Production

    try:
        r = requests.post('http://www.knowtify.io/api/v1/contacts/upsert', data=json, headers=headers)
    except Exception as e:
        print "API error\n	->%s" % (e.message)

    print "API response\n      ->%s" % (r.content)


if __name__ == "__main__":
    main()

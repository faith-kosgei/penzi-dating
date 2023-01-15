import pymysql


def getDb():
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='lovemum2002',
                         database='PENZI DB')
    return db


# checks user
def user_exists(phone_number):
    with getDb().cursor() as cursor:
        sql = "SELECT * FROM `PENZI DB`.users WHERE msisdn = %s"
        cursor.execute(sql, (phone_number,))
        return len(cursor.fetchall()) > 0


def user_described(msisdn):
    with getDb().cursor() as cursor:
        sql = "SELECT complexity, personality, interests " \
              "FROM `PENZI DB`.description " \
              "WHERE msisdn = %s"
        cursor.execute(sql, (msisdn,))
        return cursor.fetchall()


# extract name and gender from table users
def user_name(msisdn):
    with getDb().cursor() as cursor:
        sql = "SELECT name, gender " \
              "FROM `PENZI DB`.users " \
              " WHERE msisdn = %s;"
        cursor.execute(sql, (msisdn,))
        return cursor.fetchall()


# extract details from users table
def get_user(msisdn):
    with getDb().cursor() as cursor:
        sql = "SELECT name, age, county, town, msisdn " \
              "FROM `PENZI DB`.users " \
              " WHERE msisdn = %s;"
        cursor.execute(sql, (msisdn,))
        return cursor.fetchall()


# get more details from details table
def get_details(msisdn):
    with getDb().cursor() as cursor:
        sql = "SELECT level_of_education, profession, marital_status, ethnicity " \
              "FROM `PENZI DB`.details " \
              " WHERE msisdn = %s;"
        cursor.execute(sql, (msisdn,))
        return cursor.fetchall()


# save user
def save_user(name, age, msisdn, gender, county, town):
    db = getDb()
    cursor = db.cursor()
    cursor.execute(f'INSERT INTO users(name, age, msisdn, gender, county, town) VALUES ("%s", %s, "%s", '
                   f'"%s", "%s", "%s")' %
                   (name, age, msisdn, gender, county, town))
    db.commit()
    cursor.close()
    db.close()


def get_user_from_db():
    with getDb().cursor() as cursor:
        sql = "SELECT * FROM users"
        cursor.execute(sql)
        return cursor.fetchall()


# user details
def save_details(level_of_education, profession, marital_status, religion, ethnicity, msisdn):
    db = getDb()
    cursor = db.cursor()
    cursor.execute(f'INSERT INTO details(level_of_education, profession, marital_status, religion, ethnicity, msisdn) '
                   f' VALUES ("%s", "%s", "%s", "%s", "%s", "%s")' %
                   (level_of_education, profession, marital_status, religion, ethnicity, msisdn))
    db.commit()
    cursor.close()
    db.close()


def get_details_from_db():
    with getDb().cursor() as cursor:
        sql = "SELECT * FROM details"
        cursor.execute(sql)
        return cursor.fetchall()


# user description
def save_description(msisdn, complexity, personality, interests):
    db = getDb()
    cursor = db.cursor()
    cursor.execute(f'INSERT INTO description(msisdn, complexity, personality, interests) '
                   f' VALUES ("%s", "%s", "%s", "%s")' %
                   (msisdn, complexity, personality, interests))
    db.commit()
    cursor.close()
    db.close()


def get_description_from_db():
    with getDb().cursor() as cursor:
        sql = "SELECT * FROM description"
        cursor.execute(sql)
        return cursor.fetchall()


# match


def save_partner(age, msisdn, town):
    db = getDb()
    cursor = db.cursor()
    cursor.execute(f'INSERT INTO partner(age, msisdn, town) VALUES (%s, "%s", "%s")' %
                   (age, msisdn, town))
    db.commit()
    cursor.close()
    db.close()


def get_partner(age1, age2, town):
    with getDb().cursor() as cursor:
        sql = "SELECT name, age,town, msisdn FROM users WHERE age BETWEEN %s AND %s AND town=%s;"
        cursor.execute(sql, (age1, age2, town))
        return cursor.fetchall()


def save_message(msg, to, msisdn):
    db = getDb()
    cursor = db.cursor()
    cursor.execute(f'INSERT INTO messages (message, `to`, `from`) VALUES ("%s", "%s", "%s")' %
                   (msg, to, msisdn))
    db.commit()
    cursor.close()
    db.close()


def save_response(msg, to, sender):
    db = getDb()
    cursor = db.cursor()
    cursor.execute(f'INSERT INTO messages (message, `to`, `from`) VALUES ("%s", "%s", "%s")' %
                   (msg, to,  sender))
    db.commit()
    cursor.close()
    db.close()

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from db import save_user, save_details, save_description, user_exists, user_described, user_name, get_user, \
    get_details, get_partner, save_message, save_response

app = Flask(__name__)


# first step
# @app.route('/start', methods=['POST'])
def start(request):
    msg = request.json['msg']
    msisdn = request.json['msisdn']

    # save_message(msg, to, msisdn)     

    if user_exists(msisdn):
        return ("You were registered for dating with your initial details."
                "To search for a MPENZI, SMS match#age#town to 22141 and meet the person of your dreams."
                "E.g., match#23-25#Nairobi")
    else:
        return ("Welcome to our dating service with 6000 potential dating partners!To register SMS "
                "start#name#age#gender#county#town to 22141.E.g., start#John Doe#26#Male#Nakuru#Naivasha")


# registration
# @app.route('/register-by-sms', methods=['POST'])
def registration(request):
    msg = request.get_json()['msg']
    msisdn = request.get_json()['msisdn']
    user_data = msg.split('#')
    name = user_data[1]
    age = user_data[2]
    gender = user_data[3]
    county = user_data[4]
    town = user_data[5]

    save_user(name, age, msisdn, gender, county, town)
    return ("Your profile has been created successfully "
            "details#levelOfEducation#profession#maritalStatus#religion#ethnicity to 22141.E.g. "
            "details#diploma#driver#single#christian#mijikenda")


# user details
# @app.route('/details', methods=['POST'])
def user_details(request):
    msg = request.get_json()['msg']
    msisdn = request.get_json()['msisdn']
    user_data = msg.split('#')
    level_of_education = user_data[1]
    profession = user_data[2]
    marital_status = user_data[3]
    religion = user_data[4]
    ethnicity = user_data[5]

    save_details(level_of_education, profession, marital_status, religion, ethnicity, msisdn)
    return ("This is the last stage of registration."
            "SMS a brief description of yourself to 22141 starting with the word MYSELF."
            "E.g., MYSELF chocolate, lovely, sexy etc.")


# details on user2
# @app.route('/details-using-msisdn', methods=['POST'])
def details(request):
    msg = request.json['msg']
    msisdn = request.json['msisdn']
    phone_number = msg

    user1 = get_user(phone_number)
    user2 = get_details(phone_number)
    ((name, age, county, town, msisdn),) = user1
    (detail,) = user2
    detail = ', '.join(detail)
    sentence = f'{name} aged {age} {county} county {town} town,has a {detail} send DESCRIBE {msisdn} to get more ' \
               f'details about {name} '

    return sentence


# User description
# @app.route('/description', methods=['POST'])
def user_description(request):
    msg = request.get_json()['msg']
    msisdn = request.get_json()['msisdn']
    user_data = msg.split(',')
    complexity = user_data[1]
    personality = user_data[2]
    interests = user_data[3]

    save_description(msisdn, complexity, personality, interests)
    return ("You are now registered for dating."
            "To search for a MPENZI, SMS match#age#town to 22141 and meet the person of your dreams."
            "E.g., match#23-25#Kisumu")


# describe user 2
# @app.route('/describe-using-msisdn', methods=['POST'])
def describe(request):
    msg = request.json['msg']
    msisdn = request.json['msisdn']
    user_data = msg.split('#')
    phone_number = user_data[1]

    user1 = user_name(phone_number)
    user2 = user_described(phone_number)
    ((name, gender),) = user1
    pronoun = 'herself' if gender == 'Female' else 'himself'
    (qualities,) = user2
    qualities = ', '.join(qualities)
    sentence = f'{name} describes {pronoun} as {qualities}'

    return sentence


# match

# @app.route('/match', methods=['POST'])
def match_user(request):
    msg = request.json['msg']
    msisdn = request.json['msisdn']
    user_data = msg.split('-')
    lower_limit = user_data[1]
    upper_limit = user_data[2]
    town = user_data[3]

    partner = get_partner(lower_limit, upper_limit, town)
    ((name, age, town, phone_number),) = partner

    sentence = f'We have someone who match your choice! We will send you details of them shortly.To get more details ' \
               f'about a person, SMS their number e.g., 0722010203 to 22141,' \
               f'{name},aged {age}, {phone_number},' \
               f'send NEXT to 22141 to receive details of the remaining people '

    return jsonify(sentence)


# @app.route('/save-message', methods=['POST'])
def save_sent(request):
    msg = request.json['msg']
    msisdn = request.json['msisdn']
    receiver = request.json['receiver']
    user = save_message(msg, receiver, msisdn)
    return jsonify(user)


@app.route('/save-response', methods=['POST'])
def save_received():
    msg = request.json['msg']
    sender = request.json['sender']
    to = request.json['to']

    user = save_response(msg, to, sender)
    return jsonify(user)


@app.route('/send', methods=['GET', 'POST'])
@cross_origin()
def main():
    msg = request.get_json()['msg']
    if msg.lower() == 'penzi':
        reply = start(request)

    elif msg.lower().startswith('start'):
        reply = registration(request)

    elif msg.lower().startswith('details'):
        reply = user_details(request)

    elif msg.lower().startswith('myself'):
        reply = user_description(request)

    elif msg.lower().startswith('describe'):
        reply = describe(request)

    elif msg.lower().startswith('match'):
        reply = match_user(request)

    elif msg.lower().startswith(''):
        reply = details(request)
    else:
        reply = None

    response = {
        'status': 'success' if reply else 'failed',
        'reply': reply
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)

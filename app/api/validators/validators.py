import re

class ValidateUser():
    def validate_email(self, email):
        if re.match(r"(^[a-zA-z0-9_.]+@[a-zA-z0-9-]+\.[a-z]+$)", email) is False:
            return make_response(jsonify({'error': 'Provide a valid email address'}), 400)
        else:
            return False

    def validate_pasword(self, password):
        if len(password) < 9:
            return {'error': 'Password must be at least 8 characters long!'}

        elif re.search('[0-9]', password) is None:
            return {'error': 'Password must have at least one number!'}

        elif re.search('[A-Z]', password) is None:
            return {'error': 'Password must have at least one capital letter!'}

        elif re.search('[a-z]', password) is None:
            return {'error': 'Password must have at least one alphabet letter!'}

        elif re.search('[!,#,$,%,&,*,+,-,<,=,>,?,@,^,_,{,|,},~,]', password) is None:
            return {'error': 'Password must have at least a special character!'}

        else:
            return False

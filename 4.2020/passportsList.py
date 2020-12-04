def get_passports_list():
    passports = []
    with open("passports.txt", "r") as file:
        passport = dict()
        for line in file:
            line = line.rstrip()
            if len(line) == 0:
                passports.append(passport)
                passport = dict()
            else:
                fields = line.split()
                for field in fields:
                    field = field.split(':')
                    passport[field[0]] = field[1]
        passports.append(passport)
    return passports


def get_valid_passwords_list():
    passports = get_passports_list()
    valid_passports = []
    for passport in passports:
        keys = passport.keys()
        if 'cid' in keys and len(keys) == 8:
            valid_passports.append(passport)
        if 'cid' not in keys and len(keys) == 7:
            valid_passports.append(passport)
    return valid_passports

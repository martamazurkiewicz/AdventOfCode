import re
from passportsList import get_valid_passwords_list


def byr_validation(byr):
    return 1920 <= int(byr) <= 2002


def iyr_validation(iyr):
    return 2010 <= int(iyr) <= 2020


def eyr_validation(eyr):
    return 2020 <= int(eyr) <= 2030


def hgt_validation(hgt):
    if re.match("[0-9]{3}cm$", hgt) and 150 <= int(hgt[0:3]) <= 193:
        return True
    if re.match("[0-9]{2}in$", hgt) and 59 <= int(hgt[0:2]) <= 76:
        return True
    return False


def hcl_validation(hcl):
    return re.match('^#[0-9|a-f]{6}', hcl)


def ecl_validation(ecl):
    ecl_list = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return ecl in ecl_list


def pid_validation(pid):
    return re.match("[0-9]{9}", pid)


def check_if_passport_valid(passport):
    func = {'byr': byr_validation(passport['byr']),
            'iyr': iyr_validation(passport['iyr']),
            'eyr': eyr_validation(passport['eyr']),
            'hgt': hgt_validation(passport['hgt']),
            'hcl': hcl_validation(passport['hcl']),
            'ecl': ecl_validation(passport['ecl']),
            'pid': pid_validation(passport['pid'])}
    for key in passport:
        if key != 'cid':
            if func[key] is False:
                return False
    return True


passports = get_valid_passwords_list()
valid = 0
for passport in passports:
    if check_if_passport_valid(passport):
        valid += 1

print(valid)

import json

input = open("input.txt", "r")
lines = input.read().split("\n\n")

fixed_lines = []
passports = []
for line in lines:
    passport = line.replace("\n", " ")
    fixed_lines.append(passport)
for passport in fixed_lines:
    x = passport.split()
    tempdict = {}
    for entry in x:
        entry = entry.split(":")
        key = entry[0]
        val = entry[1]
        tempdict.update({key:val})
    passports.append(tempdict)

def fld_check():
        if "byr" in entry and "iyr" in entry and "eyr" in entry and "hgt" in entry and "hcl" in entry and "ecl" in entry and "pid" in entry:
            return True

def byr_check(byr):
    if "byr" in entry:
        if 1920 <= int(byr) <= 2002:
            return True

def iyr_check(iyr):
    if "iyr" in entry:
        if 2010 <= int(iyr) <= 2020:
            return True

def eyr_check(eyr):
    if "eyr" in entry:
        if 2020 <= int(eyr) <= 2030:
            return True

def hgt_check(hgt):
    if "hgt" in entry:
        if entry.get('hgt')[-2:] == "cm":
            if 150 <= int(entry.get("hgt")[:-2]) <= 193:
                return True
        if entry.get('hgt')[-2:] == "in":
            if 59 <= int(entry.get("hgt")[:-2]) <= 76:
                return True

def hcl_check(hcl):
    if "hcl" in entry:
        valid_char = {"#", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"}
        if entry.get("hcl")[0] == "#" and valid_char.issuperset(entry.get("hcl")):
            return True

def ecl_check(ecl):
    if "ecl" in entry:
        valid_ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        if entry.get("ecl") in valid_ecl:
            return True

def pid_check(pid):
    if "pid" in entry:
        if len(entry.get("pid")) == 9:
            return True

valid_passwd = 0
for entry in passports:
    if (fld_check() is True and byr_check(entry.get("byr")) is True and iyr_check(entry.get("iyr")) is True and eyr_check(entry.get("eyr")) is True and hgt_check(entry.get("hgt")) is True and hcl_check(entry.get("hcl")) is True and ecl_check(entry.get("ecl")) is True and pid_check(entry.get("pid")) is True):
        valid_passwd = valid_passwd + 1

print(valid_passwd)
x = 0
for entry in passports:
    if pid_check(entry.get("pid")) is True:
        x = x + 1
print(x)


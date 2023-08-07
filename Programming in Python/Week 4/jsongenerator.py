import json
from employee import details, employee_name, age, title

def create_dict(name, age, title):
    employee_dict = {
        "first_name": str(name),
        "age": int(age),
        "title": str(title)
    }
    return employee_dict


def write_json_to_file(json_obj, output_file):
    newfile = open(output_file, "w")
    newfile.write(json_obj)
    newfile.close()


def main():
    details()

    employee_dict = create_dict(employee_name, age, title)

    print("employee_dict: " + str(employee_dict))

    json_object = json.dumps(employee_dict)
    print("json_object: " + str(json_object))

    write_json_to_file(json_object, "employee.json")

if __name__ == "__main__":
    main()
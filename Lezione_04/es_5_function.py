def describe_city(name:str,country:str = "Italy")->str:

    print(f"{name} is in {country}")

describe_city("Rome")
describe_city("London", "England")
describe_city("Tokyo", "Japan")
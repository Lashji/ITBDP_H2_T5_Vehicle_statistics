import csv


def create_charts(data):
    create_most_common_chart(data)
    create_car_km_chart(data)
    create_car_age_chart(data)
    create_car_co2_chart(data)


def read_data(filename):
    data = []
    with open(filename, mode='r') as f:
        csv_reader = csv.DictReader(f, delimiter=';')
        for row in csv_reader:
            if row["ajoneuvoluokka"] == "M1":
                data.append(row)
    return data


def main():
    data = read_data("Ajoneuvojen avoin data 5.3.csv")

    # for i in data[:5]:
    #     print(i)
    create_charts(data)


def create_most_common_chart(data):
    ""


def create_car_km_chart(data):
    ""


def create_car_age_chart(data):
    ""


def create_car_co2_chart(data):
    ""


main()

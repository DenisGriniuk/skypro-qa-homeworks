from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone 13", "+79216665554"))
catalog.append(Smartphone("Samsung", "Galaxy S22", "+79237623488"))
catalog.append(Smartphone("OUKITEL", "WP12 Pro", "+79987654321"))
catalog.append(Smartphone("Huawei", "Y5p", "+79354657684"))
catalog.append(Smartphone("Xiaomi", "Mi 11", "+79555662387"))

for smartphone in catalog:
    print(f"{smartphone.phone_brand} - {smartphone.phone_model}. {smartphone.subscriber_number}")

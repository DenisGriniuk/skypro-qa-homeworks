from smartphone import Smartphone

catalog = []

smartphone1 = Smartphone("Apple", "iPhone 13", "+79216665554")
smartphone2 = Smartphone("Samsung", "Galaxy S22", "+79237623488")
smartphone3 = Smartphone("OUKITEL", "WP12 Pro", "+79987654321")
smartphone4 = Smartphone("Huawei", "Y5p", "+79354657684")
smartphone5 = Smartphone("Xiaomi", "Mi 11", "+79555662387")

catalog.append(smartphone1)
catalog.append(smartphone2)
catalog.append(smartphone3)
catalog.append(smartphone4)
catalog.append(smartphone5)

for smartphone in catalog:
    print(f"{smartphone.phone_brand} - {smartphone.phone_model}. {smartphone.subscriber_number}")

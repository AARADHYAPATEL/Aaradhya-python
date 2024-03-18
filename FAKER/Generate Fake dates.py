from faker import Faker

# Create a Faker object
faker = Faker()

# Generate a fake date
fake_date = faker.date_of_birth()
print("Fake DOB:", fake_date)

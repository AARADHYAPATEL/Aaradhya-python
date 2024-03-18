from faker import Faker

# Create a Faker object
faker = Faker()

# Generate fake email-address
fake_email = faker.email()
print("Fake email address", fake_email)

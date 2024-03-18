from faker import Faker

# Create a Faker object
faker = Faker()

# Generate fake user profile
fake_profile = faker.profile()
print("Fake User Profile:", fake_profile)

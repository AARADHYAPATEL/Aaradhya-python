class DietApp:
    def __init__(self):
        self.meals = []
        self.calorie_goal = 2000

    def add_meal(self):
        meal_name = input("Enter the name of the meal: ")
        calories = int(input("Enter the number of calories in this meal: "))
        self.meals.append({"name": meal_name, "calories": calories})
        print(f"Added {meal_name} with {calories} calories.")

    def view_meals(self):
        if not self.meals:
            print("No meals added yet.")
            return
        print("\nLogged Meals:")
        for meal in self.meals:
            print(f"{meal['name']} - {meal['calories']} calories")
        total_calories = sum([meal['calories'] for meal in self.meals])
        print(f"Total caloric intake: {total_calories}/{self.calorie_goal} calories\n")

    def set_calorie_goal(self):
        self.calorie_goal = int(input("Enter your daily calorie goal: "))
        print(f"Daily calorie goal set to {self.calorie_goal} calories.")

    def meal_suggestions(self):
        print("Here are some healthier meals suggestions:")
        suggestions = [
            {"name": "Grilled Chicken Salad", "calories": 350},
            {"name": "Quinoa and Black beans", "calories": 400},
            {"name": "Vegetable Stir-fry", "calories": 300},
            {"name": "Greek Yogurt with Fruits", "calories": 200}
        ]
        for suggestion in suggestions:
            print(f"{suggestion['name']} - {suggestion['calories']} calories")

    def run(self):
        while True:
            print("\n--- Diet App Menu ---")
            print("1. Add a meal")
            print("2. View meals")
            print("3. Set daily calorie goal")
            print("4. Get meal suggestions")
            print("5. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_meal()
            elif choice == "2":
                self.view_meals()
            elif choice == "3":
                self.set_calorie_goal()
            elif choice == "4":
                self.meal_suggestions()
            elif choice == "5":
                print("Thank you for using the Diet App!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = DietApp()
    app.run()
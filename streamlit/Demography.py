import streamlit as st
import plotly.express as px


# Class for managing countries
class Country:
    def __init__(self, name, population, growth_rate, area):
        self.name = name
        self.population = population  # in millions
        self.growth_rate = growth_rate  # in percentage
        self.area = area  # in square kilometers

    def population_density(self):
        """Calculate the population density (people per square km)."""
        return self.population * 1_000_000 / self.area  # population in actual numbers

    def projected_population(self, years):
        """Calculate the projected population after a certain number of years based on growth rate."""
        return self.population * (1 + self.growth_rate / 100) ** years


def create_population_graph(country_data):
    """Generate a population growth graph using Plotly."""
    years = list(range(2024, 2034))  # For the next 10 years
    population_values = [
        country_data["population"] * (1 + country_data["growth_rate"] / 100) ** (year - 2024)
        for year in years
    ]

    # Create a Plotly line chart
    fig = px.line(
        x=years,
        y=population_values,
        labels={"x": "Year", "y": "Population (in millions)"},
        title=f"Population Growth for {country_data['name']}",
    )

    return fig


def show_data_visualization():
    """Display Data Visualization screen."""
    st.title("Demographic Data Visualization")

    countries = [
        Country("USA", 345, 0.53, 9833520),  # USA population in millions, growth rate, area in sq km
        Country("India", 1450, 0.92, 3287263),
        Country("China", 1419, -0.23, 9596961),
        Country("Brazil", 212, 0.56, 8515767),
        Country("Japan", 123, -0.54, 377975),  # Japan with negative growth rate
    ]

    # Display demographic data and graphs
    for country in countries:
        country_data = {
            'name': country.name,
            'population': country.population,
            'growth_rate': country.growth_rate,
            'area': country.area,
            'population_density': country.population_density(),
            'projected_population_10_years': country.projected_population(10)
        }

        st.subheader(country.name)
        st.write(f"**Growth Rate**: {country_data['growth_rate']}%")
        st.write(f"**Population**: {country_data['population']} million")
        st.write(f"**Population Density**: {country_data['population_density']:.2f} people per sq km")
        st.write(f"**Projected Population in 10 Years**: {country_data['projected_population_10_years']:.2f} million")

        # Display the population growth graph
        fig = create_population_graph(country_data)
        st.plotly_chart(fig)


def show_article():
    """Display SEEP Analysis Article screen."""
    st.title("SEEP Analysis Article")

    article_path = "article.md"  # Ensure the article.md file exists in the project directory
    try:
        with open(article_path, "r", encoding="utf-8") as file:
            article_content = file.read()
        st.markdown(article_content)
    except FileNotFoundError:
        st.error("The article.md file was not found! Please ensure it exists in the project directory.")


def main():
    """Main function to display the home page with navigation buttons."""
    st.title("Welcome to the Demographic Dashboard!")

    # Display navigation buttons
    st.subheader("Choose an option:")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Go to Data Visualization"):
            st.session_state.page = "data"

    with col2:
        if st.button("Read SEEP Analysis Article"):
            st.session_state.page = "article"

    # Check the current page state and redirect accordingly
    if "page" in st.session_state:
        if st.session_state.page == "data":
            show_data_visualization()
        elif st.session_state.page == "article":
            show_article()


if __name__ == "__main__":
    # Initialize session state for maintaining navigation
    if "page" not in st.session_state:
        st.session_state.page = "home"
    main()

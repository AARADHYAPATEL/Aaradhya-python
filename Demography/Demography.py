import streamlit as st
import plotly.express as px


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
    years = list(range(2024, 2034))  # For next 10 years
    population_values = [country_data["population"] * (1 + country_data["growth_rate"] / 100) ** (year - 2024) for year
                         in years]

    # Create a Plotly line chart
    fig = px.line(x=years, y=population_values, labels={'x': 'Year', 'y': 'Population (in millions)'},
                  title=f"Population Growth for {country_data['name']}")

    return fig


# Streamlit App
def main():
    st.title("Demographic Data Visualization")

    # Sample Data
    countries = [
        Country("USA", 331, 0.7, 9833520),  # USA population in millions, growth rate, area in sq km
        Country("India", 1391, 1.0, 3287263),
        Country("China", 1441, 0.5, 9596961),
        Country("Brazil", 213, 0.8, 8515767),
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

        # Display demographic info
        st.write(f"**Population**: {country_data['population']} million")
        st.write(f"**Growth Rate**: {country_data['growth_rate']}%")
        st.write(f"**Population Density**: {country_data['population_density']:.2f} people per sq km")
        st.write(f"**Projected Population in 10 Years**: {country_data['projected_population_10_years']:.2f} million")

        # Display the population growth graph
        fig = create_population_graph(country_data)
        st.plotly_chart(fig)


if __name__ == "__main__":
    main()

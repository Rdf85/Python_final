import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Loading the Airbnb dataset
file_path = "airbnb_listings.csv"  
airbnb_data = pd.read_csv("airbnb_listings.csv")
def top_rated_listings(data, nights, instant_bookable, top_n=10):
    """Get the top-rated listings based on specified criteria."""
    filtered_data = data[(data['minimum_nights'] >= nights) & (data['instant_bookable'] == instant_bookable)]
    top_listings = filtered_data.nlargest(top_n, 'review_scores_rating')
    return top_listings[['id', 'name', 'review_scores_rating', 'minimum_nights', 'instant_bookable']]
# Filtering listings based on specified criteria (minimum nights and instant bookability) and returning the top-rated listings.
def response_rate_vs_time(data):
    """Plot the host response rate against host response time."""
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='host_response_time', y='host_response_rate', data=data)
    plt.title('Host Response Rate vs Response Time')
    plt.xlabel('Host Response Time')
    plt.ylabel('Host Response Rate')
    plt.show()
# Creating a scatter plot to visualize the relationship between host response rate and response time
# Example usage
nights = 8
instant_bookable = True
top_n = 10

result_top_rated = top_rated_listings(airbnb_data, nights, instant_bookable, top_n)
print(result_top_rated)

response_rate_vs_time(airbnb_data)

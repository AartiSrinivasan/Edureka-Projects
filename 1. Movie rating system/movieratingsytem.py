def rate_movie():
    movie_ratings = {}  # Dictionary to store movie ratings and comments

    while True:
        print("Movie Ratings:")
        movie_name = input("Enter the movie name (or 'q' to quit): ")
        
        if movie_name.lower() == 'q':
            break  # Exit the loop if the user enters 'q'
        
        rating = float(input(f"Rate the movie '{movie_name}' on a scale from 1 to 5 (1=terrible, 5=excellent): "))
        comment = input("Add a comment (optional): ")

        if 1 <= rating <= 5:
            movie_ratings[movie_name] = {"Rating": rating, "Comment": comment}
            print(f"Thank you for rating the movie '{movie_name}' {rating} stars with the comment: '{comment}'")
        else:
            print("Please enter a valid rating between 1 and 5.")

    # Print the movie ratings and comments
    print("\nMovie Ratings:")
    for movie, info in movie_ratings.items():
        rating = info["Rating"]
        comment = info["Comment"]
        print(f"Movie: {movie}, Rating: {rating}, Comment: {comment if comment else 'No comment'}")

if __name__ == "__main__":
    rate_movie()


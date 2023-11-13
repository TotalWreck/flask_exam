def zip_names(first_name, last_name):
    combined_names = [f"{first} {last}" for first, last in zip(first_name, last_name)]
    return combined_names
# HostelFoodBot

[Live Link](<https://hostel-food-bot.vercel.app/>)

HostelFoodBot is a cooking chatbot designed to help users find recipes based on the ingredients they have. The bot provides a user-friendly interface where users can input their ingredients and receive recipe suggestions.

## Features

- **User Input**: Users can enter ingredients they have on hand.
- **Recipe Suggestions**: The bot provides recipes based on the input ingredients.
- **Dark Mode**: A toggle switch allows users to switch between light and dark themes for better visibility.
- **Loading Animation**: A loading animation indicates when the bot is processing the request.

## Technologies Used

- **HTML**: For the structure of the web application.
- **CSS**: For styling the application and making it responsive.
- **JavaScript**: For handling user interactions and fetching data from the backend.
- **Python**: The backend logic is implemented in Python using the Flask framework (or similar) to handle recipe requests.

## Setup Instructions

To set up the project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd HostelFoodBot
   ```

2. **Install Dependencies**:
   Make sure you have Python installed. Then, install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Variables**:
   Create a `.env` file in the root directory and add any necessary environment variables (if applicable).

4. **Run the Application**:
   Start the application using the following command:
   ```bash
   python HostelFoodBot.py
   ```

5. **Access the Application**:
   Open your web browser and go to `http://localhost:5000` (or the appropriate port).

## Usage

1. Enter the ingredients you have in the input box.
2. Press "Enter" to submit your ingredients or click the "Get Recipe" button.
3. The bot will respond with a recipe suggestion based on the ingredients provided.
4. You can toggle between light and dark mode using the switch at the top right.

## Deployment

This application can be deployed on platforms like Vercel. Ensure that your `vercel.json` is correctly configured to handle the routes and static files.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

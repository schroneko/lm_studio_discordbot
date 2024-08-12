# LM Studio Discord Bot

This Discord bot integrates with LM Studio to provide an AI-powered assistant for your Discord server. It uses locally hosted language models through LM Studio's API to generate responses to user queries.

## Features

- Connects to LM Studio's local API
- Responds to Discord slash commands
- Uses OpenAI-compatible API for language model interactions

## Prerequisites

- Python 3.7+
- LM Studio running locally
- Discord Bot Token

## Installation

1. Clone this repository:

   ```
   git clone https://github.com/your-username/lm-studio-discord-bot.git
   cd lm-studio-discord-bot
   ```

2. Install the required dependencies:

   ```
   python3 -m venv .venv && source .venv/bin/activate && pip install --upgrade pip
   pip install -r requirements.txt
   ```

3. Copy the `.env.example` file to `.env` and add your Discord Bot Token:
   ```
   cp .env.example .env
   ```
   Then edit the `.env` file and add your Discord Bot Token:
   ```
   DISCORD_BOT_TOKEN=your_discord_bot_token_here
   ```

## Usage

1. Ensure LM Studio is running and serving a model on `http://localhost:1234`.

2. Run the bot:

   ```
   python main.py
   ```

3. In Discord, use the `/ask` slash command followed by your question to interact with the bot.

## Configuration

- The bot automatically detects the model being served by LM Studio.
- You can modify the system message and other parameters in the `ask` function in `main.py`.

## Error Handling

- The bot checks for LM Studio connection on startup and will exit if it cannot connect.
- Errors during interactions are caught and reported back to the user in Discord.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Disclaimer

This bot interacts with AI models. Ensure you comply with the usage terms of LM Studio and any models you use.

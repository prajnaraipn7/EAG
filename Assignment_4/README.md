# Math Agent with Keynote Integration

This project implements a math agent that can perform calculations, visualize results in Keynote, and send results via email. It uses the MCP (Model Control Protocol) framework to create a client-server architecture for mathematical operations and presentation tasks.

## Features

- Mathematical operations (addition, subtraction, multiplication, division, etc.)
- Advanced calculations (factorial, logarithms, trigonometric functions)
- Fibonacci sequence generation
- Exponential sum calculations
- Keynote integration for visual presentation
- Automated email notifications with results

## Prerequisites

- Python 3.x
- Keynote (macOS)
- SMTP server access (for email functionality)
- Google Gemini API key

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-directory>
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file with the following variables:
```
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SENDER_EMAIL=your_email@gmail.com
SENDER_PASSWORD=your_app_password
GEMINI_API_KEY=your_gemini_api_key
```

## Project Structure

- `talk2mcp-client.py`: Client implementation that handles user interaction and coordinates operations
- `talk2mcp-server.py`: Server implementation that provides mathematical tools and Keynote integration

## Usage

1. Start the server:
```bash
python talk2mcp-server.py
```

2. Run the client:
```bash
python talk2mcp-client.py
```

The client will:
1. Calculate mathematical results
2. Open Keynote
3. Create a presentation
4. Draw a rectangle
5. Write the result in the rectangle
6. Send the result via email

## Available Mathematical Tools

- Basic operations: `add`, `subtract`, `multiply`, `divide`
- Advanced operations: `power`, `sqrt`, `cbrt`, `factorial`
- Trigonometric functions: `sin`, `cos`, `tan`
- Special functions: `fibonacci_numbers`, `int_list_to_exponential_sum`

## Keynote Integration

The system can:
- Open Keynote
- Create new slides
- Draw rectangles
- Add text to shapes
- Clear slides
- Manage presentation layout

## Email Integration

Results are automatically sent via email with:
- Sender and recipient information
- Subject line
- Formatted calculation results
- Additional context

## Development

To run in development mode:
```bash
python talk2mcp-server.py dev
```

To run tests:
```bash
python talk2mcp-server.py test
```

## Security Notes

- Never commit the `.env` file to version control
- Use app-specific passwords for email authentication
- Keep API keys secure

## License

[Add your license information here]

## Contributing

[Add contribution guidelines here] 
# Affiliate Management System (AMS)

A comprehensive affiliate tracking and management system built with FastAPI and React.

## Features

- **Dashboard**: Real-time metrics and performance tracking
- **Link Management**: Create, track, and optimize affiliate links
- **Applications**: Manage affiliate program applications
- **Earnings**: Track and analyze earnings across programs
- **Reports**: Generate detailed performance reports
- **AI Tools**: AI-powered content generation and optimization

## Tech Stack

- **Backend**: FastAPI, SQLAlchemy, Google AI
- **Frontend**: React, TailwindCSS
- **Database**: SQLite (configurable for other databases)
- **AI**: Google's Generative AI (Gemini Pro)

## Prerequisites

- Python 3.8+
- Node.js 14+
- Google AI API Key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/affiliate-track.git
cd affiliate-track
```

2. Install backend dependencies:
```bash
cd ams/backend
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configurations
```

4. Initialize the database:
```bash
python init_db.py
```

5. Start the backend server:
```bash
uvicorn main:app --reload
```

6. Start the frontend (in a new terminal):
```bash
cd ../frontend
npm install
npm start
```

## Environment Variables

Create a `.env` file with the following variables:

```env
DATABASE_URL=sqlite:///./ams.db
GOOGLE_AI_KEY=your_google_ai_key
SECRET_KEY=your_secret_key
```

## API Documentation

Once the server is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- FastAPI for the amazing web framework
- React for the frontend library
- Google AI for generative AI capabilities
- TailwindCSS for styling

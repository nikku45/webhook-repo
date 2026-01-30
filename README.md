# GitHub Activity Tracker

A lightweight Flask web application designed to track and display GitHub events in real-time using Webhooks and MongoDB.

## 🚀 Features

- **Real-time Tracking**: Automatically captures GitHub events using webhooks.
- **Event Support**:
  - `push`: Tracks commits to branches.
  - `pull_request`: Tracks when PRs are opened.
  - `merge`: Tracks when PRs are successfully merged.
- **Persistent Storage**: Uses MongoDB to store event history.
- **Modern UI**: A clean, responsive dashboard to view the latest activity.

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Database**: MongoDB
- **Frontend**: HTML5, Vanilla CSS
- **Tools**: ngrok (for local testing)

## 📋 Prerequisites

- **Python 3.x**
- **MongoDB** (Running locally at `localhost:27017`)
- **ngrok** (Optional, for exposing local server to GitHub)

## ⚙️ Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Set up a virtual environment** (Recommended):
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   source venv/bin/activate  # macOS/Linux
   ```

3. **Install dependencies**:
   ```bash
   pip install flask pymongo
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```
   The server will start on `http://localhost:5000`.

## 🌐 Configuring GitHub Webhooks

1. **Expose your local server**:
   Use ngrok to create a public URL for your local Flask app:
   ```bash
   ngrok http 5000
   ```
   Copy the `https` forwarding URL (e.g., `https://random-id.ngrok-free.app`).

2. **Add Webhook to GitHub**:
   - Go to your GitHub Repository -> **Settings** -> **Webhooks**.
   - Click **Add webhook**.
   - **Payload URL**: Append `/webhook` to your ngrok URL (e.g., `https://random-id.ngrok-free.app/webhook`).
   - **Content type**: `application/json`.
   - **Which events?**: Select `Let me select individual events` and choose `Pushes` and `Pull requests`.
   - Click **Add webhook**.

## 🖥️ Usage

- Open `http://localhost:5000` in your browser to view the dashboard.
- Whenever a push or pull request occurs in your repository, the dashboard will automatically update with the event details.

## 📂 Project Structure

```text
├── app.py              # Flask server and webhook logic
├── templates/          # Frontend HTML templates
│   └── index.html      # Main dashboard
├── README.md           # Project documentation
└── .gitignore          # Ignored files
```

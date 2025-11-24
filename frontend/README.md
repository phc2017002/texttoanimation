# VidSimplify Frontend

This is the Next.js frontend for the VidSimplify video generation platform.

## 🚀 Getting Started

1.  **Install Dependencies**:
    ```bash
    npm install
    ```

2.  **Run Development Server**:
    ```bash
    npm run dev
    ```

3.  **Open in Browser**:
    Navigate to [http://localhost:3000](http://localhost:3000).

## 🏗️ Architecture

-   **Framework**: Next.js 14 (App Router)
-   **Styling**: Tailwind CSS
-   **Icons**: Lucide React
-   **Animations**: Framer Motion
-   **API Client**: `src/lib/api.ts` connects to the Python backend at `http://localhost:8000`.

## 📄 Pages

-   `/` - Landing page with features and demo.
-   `/app` - Main application for generating videos.

## 🔧 Configuration

The API URL is configured in `src/lib/api.ts`. Default is `http://localhost:8000`.

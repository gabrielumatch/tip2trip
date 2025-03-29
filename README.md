# Tip2Trip - Social Network for Motorhome Owners & Digital Nomads

Tip2Trip is a social networking platform designed specifically for motorhome owners and digital nomads. It allows users to share their travel experiences, discover new places, plan routes, and connect with fellow travelers.

## Features

- **User Profiles**
  - Custom profiles with vehicle information
  - Follow other users
  - Premium subscription options

- **Places**
  - Discover RV-friendly locations
  - Read and write reviews
  - Track amenities and facilities
  - Share photos and experiences

- **Route Planning**
  - Create and share travel routes
  - Add multiple waypoints
  - Calculate distances and estimated travel times
  - Share route experiences

- **Social Feed**
  - Share posts with text, images, and videos
  - Tag locations and users
  - Like and comment on posts
  - Use hashtags for better discovery

## Technology Stack

- **Backend:**
  - Django
  - Django REST Framework
  - PostgreSQL
  - Cloudflare R2 (for media storage)

- **Frontend:**
  - React
  - Shadcn UI
  - Tailwind CSS

- **External Services:**
  - Google Maps Platform
  - Stripe (for payments)

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/tip2trip.git
   cd tip2trip
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Fill in your configuration values

5. Initialize the database:
   ```bash
   python manage.py migrate
   ```

6. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Environment Variables

The following environment variables are required:

```
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:3000

# External Services
STRIPE_SECRET_KEY=your-stripe-secret-key
STRIPE_PUBLISHABLE_KEY=your-stripe-publishable-key
GOOGLE_MAPS_API_KEY=your-google-maps-api-key

# Cloudflare R2
CLOUDFLARE_R2_ENDPOINT=your-r2-endpoint
CLOUDFLARE_R2_ACCESS_KEY_ID=your-r2-access-key
CLOUDFLARE_R2_SECRET_ACCESS_KEY=your-r2-secret-key
CLOUDFLARE_R2_BUCKET_NAME=your-bucket-name
```

## API Documentation

The API documentation is available at `/api/docs/` when running the development server.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 
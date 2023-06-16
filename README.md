# Development
```bash
# Frontend React 
cd frontend
npm install
npm start

# Backend FastAPI
cd backend
pipenv install
pipenv shell
pipenv run dev

```

# Production
```bash
cd frontend
npm install
npm build
cp -r  build/ ../backend/

cd ../backend
pipenv install
pipenv shell
pipenv run start

```
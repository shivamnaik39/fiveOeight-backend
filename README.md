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
npm run build
cp -r  build/ ../backend/

cd ../backend
pipenv install
pipenv shell
pipenv run start

```

# Docker
```bash
docker build . -t five_o_eight
docker run --name five_o_eight-app -p 8000:8000 five_o_eight

```
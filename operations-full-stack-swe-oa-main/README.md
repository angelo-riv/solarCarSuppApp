# McMaster Solar Car Operations Team - Development Challenge
A FastAPI application with a single POST endpoint that takes a list of numbers and returns them sorted. 

## How to Build
Ensure you have docker engine running before continuing with following steps. 

```bash

# Build the Docker image
docker build -t solar-car-api .

# Run the container
docker run -p 8000:8000 solar-car-api

# Test the API (On separate terminal)
# Linux/MAC
curl -X POST http://localhost:8000/sorted-numbers \
  -H "Content-Type: application/json" \
  -d '{"numbers": [45, 23, 78, 12, 91, 34, 67, 89, 56, 3]}'

# Windows
Invoke-RestMethod -Uri "http://127.0.0.1:8000/sorted-numbers" `
  -Method POST `
  -ContentType "application/json" `
  -Body '{"numbers":[2,5,8,24,2141,2512,21]}'

# Or open link FastAPI link given in terminal and type in "/docs" at the end of the website link. 
# An option to try out the api should be available

# End Docker
docker stop <container_id>
```

### Example Request:
```json
{
    "numbers": [45, 23, 78, 12, 91, 34, 67, 89, 56, 3]
}
```

### Response:
```json
{
    "original_numbers": [45, 23, 78, 12, 91, 34, 67, 89, 56, 3],
    "sorted_numbers": [3, 12, 23, 34, 45, 56, 67, 78, 89, 91]
}
```
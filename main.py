from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from pydantic import BaseModel
import requests
from routers import auth_router, data_curation_router, insight_analysis_router, visualization_router

app = FastAPI()

# Include the routers
app.include_router(auth_router.router)
app.include_router(data_curation_router.router)
app.include_router(insight_analysis_router.router)
app.include_router(visualization_router.router)

# Auth0 settings
AUTH0_DOMAIN = "dev-lweowtswfm2nqllq.eu.auth0.com"
API_AUDIENCE = "https://quantumconsciousai/api"
ALGORITHMS = ["RS256"]

# Auth0 OAuth2 Password Flow
oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"https://{AUTH0_DOMAIN}/oauth/token")

class TokenData(BaseModel):
    sub: str = None

def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        # Get the public key from Auth0
        jwks_url = f"https://{AUTH0_DOMAIN}/.well-known/jwks.json"
        jwks = requests.get(jwks_url).json()
        unverified_header = jwt.get_unverified_header(token)
        rsa_key = {}
        for key in jwks["keys"]:
            if key["kid"] == unverified_header["kid"]:
                rsa_key = {
                    "kty": key["kty"],
                    "kid": key["kid"],
                    "use": key["use"],
                    "n": key["n"],
                    "e": key["e"]
                }
        if rsa_key:
            payload = jwt.decode(token, rsa_key, algorithms=ALGORITHMS, audience=API_AUDIENCE)
            token_data = TokenData(sub=payload.get("sub"))
            return token_data
        else:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Could not validate credentials")
    except JWTError:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Could not validate credentials")

# Protect a route with Auth0
@app.get("/auth-protected")
def read_protected_data(token_data: TokenData = Depends(verify_token)):
    return {"message": f"Hello, {token_data.sub}"}

# Existing root route
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}

# Print routes and run the app
if __name__ == "__main__":
    import uvicorn
    from fastapi.routing import APIRoute

    # Print out all registered routes
    for route in app.routes:
        if isinstance(route, APIRoute):
            print(f"Route path: {route.path} | Methods: {route.methods}")

    # Start the FastAPI app
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)

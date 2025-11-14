from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from utils.integrations import get_env_var
from utils.io_functions import get_ip
from utils.my_math import some_function

# Create FastAPI app instance
app = FastAPI(
    title="Datadrivet Template API",
    description="A simple FastAPI application exposing utility functions!",
    version="0.1.0",
)


# Pydantic models for request/response
class MathRequest(BaseModel):
    x: int


class MathResponse(BaseModel):
    input: int
    result: int


class IPResponse(BaseModel):
    ip: str


class EnvVarRequest(BaseModel):
    var_name: str
    default: Optional[str] = None


class EnvVarResponse(BaseModel):
    var_name: str
    value: Optional[str]


# Routes
@app.get("/")
async def hello_world():
    """Hello World endpoint"""
    return {"message": "Hello from datadrivet-template FastAPI!"}


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "datadrivet-template"}


@app.post("/math", response_model=MathResponse)
async def do_math(request: MathRequest):
    """Perform math operation using some_function"""
    try:
        result = some_function(request.x)
        return MathResponse(input=request.x, result=result)
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Math operation failed: {str(e)}"
        ) from e


@app.get("/ip", response_model=IPResponse)
async def get_current_ip():
    """Get current public IP address"""
    try:
        ip = get_ip()
        return IPResponse(ip=ip)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to get IP: {str(e)}"
        ) from e


@app.post("/env", response_model=EnvVarResponse)
async def get_environment_variable(request: EnvVarRequest):
    """Get environment variable value"""
    try:
        value = get_env_var(request.var_name, request.default)
        return EnvVarResponse(var_name=request.var_name, value=value)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to get env var: {str(e)}"
        ) from e


@app.get("/demo")
async def demo_all_functions():
    """Demo endpoint that showcases all utility functions"""
    try:
        # Math operation
        math_result = some_function(1)

        # Get IP
        current_ip = get_ip()

        # Get environment variable (with fallback)
        secret_pw = get_env_var("SECRET_PASSWORD", "not_set")
        # Only show first 3 characters for security
        secret_preview = secret_pw[:3] + "..." if secret_pw != "not_set" else "not_set"

        return {
            "message": "Demo of all utility functions",
            "math_result": f"some_function(1) = {math_result}",
            "current_ip": current_ip,
            "secret_password_preview": secret_preview,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Demo failed: {str(e)}") from e


# Main function for backwards compatibility
def main():
    print("Hello from datadrivet-template!")
    print(f"Do math: {some_function(1)}")
    your_ip = get_ip()
    print(f"Your IP is: {your_ip}")
    pw = get_env_var("SECRET_PASSWORD")
    print(f"Secret password: {pw[:3]}...")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
